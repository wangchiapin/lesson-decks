# 生活情境教材每日排程 lesson-decks

> 每天自動產出兩套 pptx 教材：「生活情境短文」和「情境生存」，給說西班牙語的華語學習者

- **網址：** 無（純檔案 repo，沒有網頁；成品是 `decks/` 與 `survival/decks/` 裡的 pptx 和 zip）
- **Firebase 專案：** 不使用 Firebase
- **登入方式：** —
- **狀態：** 使用中（排程每天台灣時間 17:00 執行；目前計畫 2026-11-01 到 2026-11-13，另有 2026-10-21 的測試成品）
- **備註：** 兩套排程互相獨立，各改各的資料夾，不要混在一起動。

## 兩套教材

| 教材 | 資料夾 | 每天做什麼 | 排程手冊 |
|---|---|---|---|
| 生活情境短文 | `decks/`、`tools/`、`topics_plan.tsv`、`used_topics.txt` | 10 個主題（A2／B1／B2 共 130 個計畫主題，A2 50、B1 40、B2 40），每個主題一份 pptx，打包成 zip | `RUNBOOK.md` |
| 情境生存 | `survival/` | 5 個「情境生存」主題（像機場篇、飯店篇那一型，計畫檔共 70 列：第 0 組 5 個是 2026-10-21 的測試，其餘 13 天 65 個是正式排程），每個主題一份 pptx | `survival/RUNBOOK.md` |

## 資料夾

- `decks/YYYY-MM-DD_<等級>/`：當天的 pptx（`MMDD_01.pptx` …）、`index.txt`（檔名對應主題）、zip。
- `survival/decks/YYYY-MM-DD/`：情境生存的當天成品，另有 `prompts.md`（圖片提示）。
- `topics_plan.tsv`、`survival/plan.tsv`：每天要做的主題計畫（`status` 做完會改成 `done`）。
- `used_topics.txt`、`survival/used_topics.txt`：已做過的主題，不可重複。
- `tools/`：`build_deck.py`（產生 pptx）、`finalize_day.py`（檢查計畫、打包、更新紀錄）。
- `survival/tools/`：`survival_runner.py`、`package_day.py`、`survival_template.pptx`。
- `skill/`、`survival/skill/`：版型與規則說明（對應 Claude 的 skill `chinese-life-lesson-maker`、`chinese-scene-survival-deck`）。
- `examples/`、`survival/examples/`：主題資料檔的範例。

## 給 Claude

- 跟 Ben 說明時用白話繁體中文；推送前先問，Ben 說「推」才推（排程自動執行時照各自的 RUNBOOK）。
- 做之前先讀對應的 RUNBOOK；不要 force push，也不要 rebase。
