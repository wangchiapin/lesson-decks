# 每日生活情境短文教材（排程執行手冊）

每天台灣時間 17:00 執行。目標：產出當天 10 個主題的 pptx，打包後推到本 repo。

## 步驟
0. 準備環境（每次都做，工作階段是全新的）：
   `pip install opencc-python-reimplemented python-pptx --break-system-packages -q`
   repo 若已在 /home/claude/lesson-decks 就直接用，不用重新 clone。
1. 執行 `python3 tools/finalize_day.py plan`（自動用 Asia/Taipei 今天的日期；也可加日期參數）。
   印出當天 10 列（level、topic）。若印出 `NOT_IN_PLAN`（exit 3）就停止、什麼都不做。
2. 同一個指令已檢查主題有沒有與 `used_topics.txt` 或計畫內其他天重複；結尾 `CHECK ok` 才繼續。若有重複，依步驟 9 處理。
3. 用 skill `chinese-life-lesson-maker` 的規則（若 skill 不可用，改讀 `skill/chinese-life-lesson-maker_SKILL.md`，內容相同），為每個主題產生教材資料，程度用該列的 level（A2／B1／B2）。資料格式與範例見 `examples/topics_sample_B2.py`（`add(...)`），主題檔放在 /tmp 或 repo 外，不要 commit；`add` 的第一個參數（主題名）要與計畫一致，順序也一致。A2 的句子更短更簡單，B2 可較長。
4. 執行 `python3 tools/build_deck.py <topics檔> <build資料夾>`（build 資料夾放在 repo 外，例如 /tmp/build），修到 PROBLEMS 顯示 none（每行 ≤12 字、單字都出現在短文中、P2 為 10–13 題）。
5. 轉圖片目視檢查不換行（soffice → pdf → pdftoppm），有問題就改。
6. 執行 `python3 tools/finalize_day.py pack <YYYY-MM-DD> <topics檔> <build資料夾>`。它會：
   - 把 pptx 改名為 `MMDD_01.pptx` … `MMDD_10.pptx`（順序同 topics 檔）、放進 `decks/YYYY-MM-DD_<level>/`
   - 寫 `index.txt`（UTF-8）：`MMDD_01.pptx = 主題中文名`
   - 建 `YYYY-MM-DD_<level>.zip`（內含檔名皆為 ASCII）
   - 步驟 7 也一併做完（見下）。可先加 `--dry-run` 看會做什麼。
7. （由 pack 自動完成）`topics_plan.tsv` 當天 10 列 status 改 `done`，當天主題加進 `used_topics.txt`。執行後用 `git diff --stat` 確認只動了這兩個檔和 decks/。
8. commit 並 push 到 main，只 add `decks/`、`topics_plan.tsv`、`used_topics.txt`。commit 訊息例：`2026-11-01 A2: 10 decks`。
   push 被拒絕（另一個排程也在推 main）時：`git pull --no-rebase origin main` 合併後再 push，最多重試 3 次；不要 force push、不要 rebase。若 topics_plan.tsv 或 used_topics.txt 有衝突，兩邊都保留（status 以 done 為準）。
9. 若某主題做不出來，換一個不重複的相近細部主題（topics 檔用新名字），pack 會在 index.txt 註明「替換主題」並更新計畫。
10. 若任何一步最後失敗（push 不成功、建檔檢查修不好、repo 讀不到），用 PushNotification 通知 Ben：哪一步、為什麼、卡在哪個日期。全部成功就不必通知。

## 規則
- 所有主題不得與 `used_topics.txt` 及計畫內其他主題重複，但可以更細部。
- 一律使用 Ben 要求的字型與版型（見 tools/build_deck.py）。
