# 每日生活情境短文教材（排程執行手冊）

每天台灣時間 17:00 執行。目標：產出當天 10 個主題的 pptx，打包後推到本 repo。

## 步驟
1. 讀 `topics_plan.tsv`，找出今天（Asia/Taipei 日期）的 10 列（date、level、topic）。若今天不在計畫內就停止。
2. 讀 `used_topics.txt` 與 `topics_plan.tsv`，確認今天主題沒有與其他天重複。
3. 用 skill `chinese-life-lesson-maker` 的規則，為每個主題產生教材資料，程度用該列的 level（A2／B1／B2）。資料格式與範例見 `examples/topics_sample_B2.py`（`add(...)`）；A2 的句子更短更簡單，B2 可較長。
4. 執行 `python3 tools/build_deck.py <topics檔> <輸出資料夾>`，修到 PROBLEMS 顯示 none（每行 ≤12 字、單字都出現在短文中、P2 為 10–13 題）。
5. 轉圖片目視檢查不換行（soffice → pdf → pdftoppm），有問題就改。
6. 輸出放在 `decks/YYYY-MM-DD_<level>/`：
   - pptx 檔名只用 ASCII：`MMDD_01.pptx` … `MMDD_10.pptx`
   - `index.txt`（UTF-8）：`MMDD_01.pptx = 主題中文名`
   - 同資料夾再放壓縮檔 `YYYY-MM-DD_<level>.zip`（用 Python zipfile 建立、內含檔名皆為 ASCII）
7. 把 `topics_plan.tsv` 當天 10 列 status 改成 `done`，把當天主題加進 `used_topics.txt`。
8. commit 並 push 到 main。commit 訊息例：`2026-11-01 A2: 10 decks`。
9. 若某主題做不出來，換一個不重複的相近細部主題，並在 index.txt 註明。

## 規則
- 所有主題不得與 `used_topics.txt` 及計畫內其他主題重複，但可以更細部。
- 一律使用 Ben 要求的字型與版型（見 tools/build_deck.py）。
