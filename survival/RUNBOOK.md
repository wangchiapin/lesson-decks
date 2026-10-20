# 情境生存簡報每日排程手冊（survival/）

對象：Ben 的西語學生。每天台灣時間 17:00 做 5 個「情境生存」主題（跟機場篇、飯店篇同一型）的 pptx，打包後推到本 repo。不分程度。
注意：repo 其他資料夾（RUNBOOK.md、topics_plan.tsv、decks/）是另一個「生活情境短文」排程，**不要動**。本流程只改 `survival/` 底下的檔案。

## 檔案
- `plan.tsv`：每天 5 個主題與 6 個小場景提示（date=0 那組是測試）
- `used_topics.txt`：已做過的 13 個主題（不得重複）
- `tools/survival_runner.py` + `tools/survival_template.pptx`：用主題資料檔產生 pptx
- `tools/package_day.py`：打包 zip
- `examples/example_topic.py`：主題資料檔範例（完整格式）
- `skill/chinese-scene-survival-deck_SKILL.md`：版型規格（Skill `chinese-scene-survival-deck` 不可用時讀這份）

## 步驟
1. 取台灣日期（Asia/Taipei）。從 `plan.tsv` 找該日 5 列（status=planned）。不在計畫內或年份不是 2026 就停止。測試模式見最後。
2. 確認這 5 個主題不在 `used_topics.txt`、也不與 plan.tsv 其他列重複。
3. 每個主題寫一個資料檔 `work/<seq>_<name>.py`（放在 survival/work/，不要 commit），格式同 `examples/example_topic.py`：
   - `FILE`（中文篇名，例「牙醫篇」）、`OPEN`
   - `SCENES`：6 個情境，每個 3～4 句（中, 西, 英）、5～7 個生詞（中, 西短釋, 英）、圖片提示。依 plan.tsv 的 6 個場景提示各做一頁。
   - `FILL`：2 組填空對話（6～7 行，挖空用 `[詞]`，詞必須出現在前面生詞表）
   - `SORT`：3 組排序對話（6、6、8 行）
   - `REVIEW`：3 句核心問句＋3 個角色提示詞
   - 句子要是真的會在現場說的話；西語用拉美學生熟悉的說法，注意重音與標點；台灣情境（悠遊卡、健保、發票等）。
   - 中文一律寫繁體（程式會轉簡體放投影片）。不要加任何特殊讀音選擇符。
4. 執行 `python3 tools/survival_runner.py work/<file>.py out/<MMDD>/`，直到最後印出 `PROBLEMS: none` 且沒有 `MISSING vocab`。
5. 目視檢查：把 pptx 複製一份移除所有投影片的 `show` 屬性，用 soffice 轉 pdf（`soffice --headless --convert-to pdf`），pdftoppm 轉圖，看生詞框是否超過 7 行、對話是否蓋到黃色小框。環境沒有拼音字型，字寬僅供參考。有問題就縮短西語釋義或句子再重跑。
6. 輸出到 `survival/decks/YYYY-MM-DD/`（測試用 `survival/decks/test_YYYY-MM-DD/`）：
   - `MMDD_01.pptx` … `MMDD_05.pptx`（檔名只用 ASCII）
   - `index.txt`（UTF-8）：`MMDD_01.pptx = 篇名`
   - `prompts.md`：每個主題 6 張情境圖的生圖提示詞（用資料檔的圖片提示擴寫：同一位墨西哥男旅客、格子襯衫、背包，台灣場景，無印風）
   - 壓縮檔：`python3 tools/package_day.py <資料夾> <資料夾>/YYYY-MM-DD.zip`（每天一個 zip，內含 5 個 pptx＋index.txt＋prompts.md）
7. 更新 `plan.tsv` 當天 5 列 status 為 done，把主題加進 `used_topics.txt`（測試模式不要改這兩個檔）。
8. `git pull --rebase origin main` 後 commit、`git push origin main`（只 add `survival/`）。push 被拒就再 pull --rebase 重試，最多 3 次。訊息：`survival 2026-11-01: 5 decks`。
9. 某主題做不出來：換一個不重複的相近細部主題，在 index.txt 註明。

## 測試模式
排程提示說「測試」時：用 plan.tsv 中 day=0 的 5 個主題；輸出資料夾 `survival/decks/test_2026-10-21/`，檔名 `T_01.pptx`…；不改 plan.tsv、used_topics.txt；commit 訊息 `survival test run: 5 decks`。完成後回報每一步是否順利（clone、skill、建檔、檢查、push）、問題與耗時。
