#!/usr/bin/env python3
"""生活情境短文排程輔助工具（取代手動改名、index、zip、更新計畫）。

用法:
  python3 tools/finalize_day.py plan [YYYY-MM-DD]
      印出該日（預設 Asia/Taipei 今天）的 10 個主題與程度，並檢查是否與 used_topics / 計畫內其他列重複。
      不在計畫內 → 印 NOT_IN_PLAN 並以 exit 3 結束（排程請就此停止）。
  python3 tools/finalize_day.py pack <YYYY-MM-DD> <topics檔.py> <build輸出資料夾> [--test PREFIX] [--dry-run]
      把 build_deck.py 的輸出（主題名_教材.pptx）依 topics 檔順序改名為 MMDD_01.pptx…，
      放進 decks/YYYY-MM-DD_<level>/，寫 index.txt 與 YYYY-MM-DD_<level>.zip，
      並把計畫當天 10 列 status 改 done、主題加進 used_topics.txt。
      --test PREFIX: 測試模式，檔名用 PREFIX_01…，資料夾 decks/test_<date>_<level>/，不改計畫與 used_topics。
      --dry-run: 只印出會做什麼，不寫任何檔案。
"""
import sys, os, csv, io, zipfile, shutil, importlib.util
from datetime import datetime
from zoneinfo import ZoneInfo

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLAN = os.path.join(ROOT, "topics_plan.tsv")
USED = os.path.join(ROOT, "used_topics.txt")


def today_taipei():
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d")


def load_plan():
    with open(PLAN, encoding="utf-8", newline="") as f:
        rd = csv.reader(f, delimiter="\t")
        header = next(rd)
        rows = [r for r in rd if r]
    return header, rows


def used_list():
    with open(USED, encoding="utf-8") as f:
        return [l.strip() for l in f if l.strip()]


def day_rows(rows, header, date):
    di, li, ti = header.index("date"), header.index("level"), header.index("topic")
    return [r for r in rows if r[di] == date], di, li, ti


def cmd_plan(date):
    header, rows = load_plan()
    mine, di, li, ti = day_rows(rows, header, date)
    if not mine:
        print(f"NOT_IN_PLAN {date}")
        sys.exit(3)
    used = set(used_list())
    others = [r[ti] for r in rows if r[di] != date]
    levels = {r[li] for r in mine}
    print(f"DATE {date}  LEVEL {','.join(sorted(levels))}  COUNT {len(mine)}")
    bad = False
    for i, r in enumerate(mine, 1):
        flag = ""
        if r[ti] in used: flag = "  <-- 已在 used_topics"; bad = True
        if r[ti] in others: flag = "  <-- 與計畫其他天重複"; bad = True
        print(f"{i:02d}\t{r[li]}\t{r[ti]}{flag}")
    if len(mine) != 10: print("WARN: 不是 10 列"); bad = True
    print("CHECK", "PROBLEMS" if bad else "ok")


def cmd_pack(date, topics_file, build_dir, test_prefix=None, dry=False):
    header, rows = load_plan()
    mine, di, li, ti = day_rows(rows, header, date)
    if not mine:
        print(f"NOT_IN_PLAN {date}"); sys.exit(3)
    level = mine[0][li]
    spec = importlib.util.spec_from_file_location("topics_mod", topics_file)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    names = [t["name"] for t in mod.T]
    if len(names) != 10:
        print(f"ERROR: topics 檔有 {len(names)} 個主題，需要 10 個"); sys.exit(2)
    mmdd = date[5:].replace("-", "")
    prefix = test_prefix or mmdd
    folder = f"{'test_' if test_prefix else ''}{date}_{level}"
    out = os.path.join(ROOT, "decks", folder)
    plan_topics = [r[ti] for r in mine]
    replaced = [n for n in names if n not in plan_topics]
    missing_in_build = [n for n in names if not os.path.exists(os.path.join(build_dir, f"{n}_教材.pptx"))]
    if missing_in_build:
        print("ERROR: build 資料夾缺少:", missing_in_build); sys.exit(2)
    index_lines = []
    for i, n in enumerate(names, 1):
        note = "（替換主題，非計畫原主題）" if n in replaced else ""
        index_lines.append(f"{prefix}_{i:02d}.pptx = {n}{note}")
    print("OUT", out)
    print("\n".join(index_lines))
    if replaced: print("REPLACED", replaced)
    if dry:
        print("DRY-RUN: 未寫入任何檔案"); return
    os.makedirs(out, exist_ok=True)
    for i, n in enumerate(names, 1):
        shutil.copyfile(os.path.join(build_dir, f"{n}_教材.pptx"), os.path.join(out, f"{prefix}_{i:02d}.pptx"))
    with open(os.path.join(out, "index.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(index_lines) + "\n")
    zname = f"{folder.replace('test_', 'test_', 1)}.zip" if test_prefix else f"{date}_{level}.zip"
    with zipfile.ZipFile(os.path.join(out, zname), "w", zipfile.ZIP_DEFLATED) as z:
        for i in range(1, 11):
            z.write(os.path.join(out, f"{prefix}_{i:02d}.pptx"), f"{prefix}_{i:02d}.pptx")
        z.write(os.path.join(out, "index.txt"), "index.txt")
    print("ZIP", os.path.join(out, zname))
    if test_prefix:
        print("TEST: 未更新 topics_plan.tsv / used_topics.txt"); return
    # 更新計畫：該日 10 列 status=done；被替換的主題改成實際做的主題
    si = header.index("status")
    repl_iter = iter([n for n in names if n not in plan_topics])
    for r in mine:
        r[si] = "done"
    for r in mine:
        if r[ti] not in names:
            r[ti] = next(repl_iter, r[ti])
    buf = io.StringIO(newline="")
    w = csv.writer(buf, delimiter="\t", lineterminator="\n")
    w.writerow(header); w.writerows(rows)
    with open(PLAN, "w", encoding="utf-8", newline="") as f:
        f.write(buf.getvalue())
    used = used_list()
    with open(USED, "a", encoding="utf-8") as f:
        for n in names:
            if n not in used: f.write(n + "\n")
    print("UPDATED topics_plan.tsv (done) and used_topics.txt")


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a: print(__doc__); sys.exit(1)
    if a[0] == "plan":
        cmd_plan(a[1] if len(a) > 1 else today_taipei())
    elif a[0] == "pack":
        test = None; dry = "--dry-run" in a
        if "--test" in a: test = a[a.index("--test") + 1]
        pos = [x for i, x in enumerate(a[1:], 1) if not x.startswith("--") and not (test and a[i - 1] == "--test")]
        cmd_pack(pos[0], pos[1], pos[2], test, dry)
    else:
        print(__doc__); sys.exit(1)
