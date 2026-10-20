---
name: "chinese-life-lesson-maker"
description: "Ben 做「生活情境短文」教材時使用：給主題和關鍵詞，產出短文、單字、問答、補充、中西英翻譯、P2討論題，再轉簡體，並可直接輸出 pptx。"
---

# 生活情境短文教材製作

對象：Ben 的學生，都是說西班牙文的華語學習者（中初級）。教的是台灣華語。
使用時機：Ben 給一個主題（例如「落枕」），可能附幾個想教的詞或句型。

## 對 Ben 說話
用白話繁體中文，少用技術名詞。先交文字稿，讓 Ben 確認內容；Ben 說「做成 ppt」或說內容 OK 後，再輸出 pptx。
如果主題跟舊教材重複（目前已有 20 個：排隊、睡過頭、熬夜、小偷、衣服穿反、打翻、綁鞋帶、喝醉、照顧小孩厭世、惡夢、跌倒、沒空、延長線、曬衣服、講電話、落枕、伸懶腰、樓上樓下、淹水、濫好人），先提醒他。

## 一個主題 = 4 張投影片（內容各自獨立輸出）
1. 繁體 P1：短文（投影片文字）+ 備註（單字、問答、補充、翻譯）
2. 繁體 P2：同一張圖，右邊文字留空，備註放討論題
3. 簡體 P1：由 1 轉簡體，備註跟 1 相同
4. 簡體 P2：由 2 轉簡體，備註跟 2 相同

## 產出順序與規則

### 1. 短文
- 4～7 行，一行一個意思。**每行不超過 12 個字（含標點）**，因為投影片字級 40，超過會跨行。對話型字級縮到 32，每行可到 15 字。
- 第一人稱小故事，貼近日常；有笑點或反轉更好。
- 自然帶入 Ben 指定的詞和句型，並多用常見功能詞（……的時候、還好、所以、但是、最後）。
- 對話型主題（情緒、人際）可改成 A、B 對話，6～8 句。
- 一個主題只講一件事，不要塞太多新詞。

### 2. 單字（P1 備註第一段）
- 10～20 個詞，每行 3～4 個，詞與詞之間用「 //  」分隔。
- 格式：`中文：español / English`。西文可列 2 個近義說法。
- 容易混淆的詞，補一行區分，例如 levantarse → 正式的起床 // despertarse → 醒來。
- 只列短文裡出現的詞，加上必要的連帶詞。

### 3. 問答（圖片問答）
- 格式：`問答：問題1? // 問題2? // 問題3?`，全部是看圖和短文就能答的問題（誰、在哪、做什麼、為什麼、最後怎麼樣）。
- 5～7 題，由易到難。
- 有兩組時寫成「問答1」「問答2」，第二組問學生自己的經驗。

### 4. 補充用法
- 1～3 個重點，格式：`補充：重點1 // 重點2 // 重點3`。
- 每個重點給 2～3 個例子，需要時加西文解釋。
- 優先選：句型（要我+V、很+不adj、V到…、怎麼V都…）、容易搞錯的詞（掉 vs 倒）、搭配詞（V過頭：走過頭、坐過頭）、台灣口語。

### 5. 翻譯
- 西班牙文和英文各整篇翻一次，放 P1 備註最後。
- 西班牙文預設用拉丁美洲通用說法（例如 celular），避免只在西班牙使用的詞（móvil、ordenador）。若 Ben 另有指定再改。
- 翻譯要自然，不要逐字翻。

### 6. P2 討論題
- 10～13 題，每題一行，格式：`編號.中文問題? 西班牙文問題`。
- 另外一份英文版，編號相同，與中西版之間空一行。
- 順序：經驗（你常常…嗎？）→ 最近一次 → 原因 → 習慣細節 → 你們國家怎麼樣 → 延伸話題 → 看法與假設（如果…你會…？）。
- 至少 1 題問「在你的國家」，至少 1 題用「如果…」，讓學生用到補充用法。
- 問題要能讓學生說很多，不要只能回答是或不是。

## 簡體版
- 預設只轉字形，保留台灣用詞（例如「捷運」不改成「地鐵」），因為教的是台灣華語。Ben 要求時才改成大陸用語。
- 簡體文字稿只重新輸出投影片上的中文（短文、P2 中文問題），備註裡的西文和英文共用。
- 繁簡結果必須逐行對應，行數、標點完全一致。

## 文字稿輸出格式
```
【主題編號與名稱】

▍繁體 P1 投影片文字
（短文）

▍P1 備註
（單字）

問答：...
補充：...

西班牙文：...
英文：...

▍繁體 P2 備註
（中文問題 + 西文，英文另一份）

▍簡體 P1 投影片文字
（短文）

▍簡體 P2
（中文問題簡體版）
```

## 輸出 pptx

Ben 要 ppt 時，用 python-pptx 直接產生 4 張投影片（不需要 Ben 的舊檔）。每個主題一個檔，檔名「主題名_教材.pptx」。完成後用 SendUserFile 寄給 Ben。

版面規格（量自舊教材，16:9，寬 12192000、高 6858000 EMU，空白版面）：
- 右邊主文字框：x=4036741, y=147106, 寬 8053659, 高 6588974。淺藍底 #DAE3F3，深綠框 #375623，框線 1.5pt，文字黑色、置中、垂直置中、行距 150%、字級 40pt。不自動縮字。
- 左下單字框：x=217798, y=2823882, 寬 3718582, 高 3912197。淺綠底 #E2F0D9，同樣綠框。內容留空（上課時老師自己寫）。
- 左上圖片區：x=217798, y=147106, 寬 3718582, 高 2600000。先放灰色虛線框寫「（在這裡放圖片）」，Ben 自己換圖。
- P2 的右邊文字框保留，但內容留空。
- 字體全部用「澳聲通拼音庫楷-繁」，簡體頁也用同一個（latin、ea、cs 三個 typeface 都設）。繁體 lang=zh-TW，簡體 lang=zh-CN。雲端沒有這個字體，預覽會用備用字，在 Ben 自己的電腦才會正確顯示，要先告訴他。
- 備註：P1 和簡體 P1 放「單字、問答、補充、西文、英文」；P2 和簡體 P2 放「中西問題 + 空行 + 英文問題」。

建立這個檔的 python 結構：
```python
from pptx import Presentation
from pptx.util import Emu, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn
from lxml import etree

FONT = "澳聲通拼音庫楷-繁"
BLUE, GREEN, BORDER = RGBColor(0xDA,0xE3,0xF3), RGBColor(0xE2,0xF0,0xD9), RGBColor(0x37,0x56,0x23)
prs = Presentation(); prs.slide_width = Emu(12192000); prs.slide_height = Emu(6858000)

def box(slide, x, y, w, h, fill, lines=None, lang="zh-TW"):
    sh = slide.shapes.add_textbox(Emu(x), Emu(y), Emu(w), Emu(h))
    sh.fill.solid(); sh.fill.fore_color.rgb = fill
    sh.line.color.rgb = BORDER; sh.line.width = Emu(19050)
    tf = sh.text_frame; tf.word_wrap = True; tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    bp = tf._txBody.find(qn('a:bodyPr'))
    for c in list(bp): bp.remove(c)
    etree.SubElement(bp, qn('a:noAutofit'))
    for i, t in enumerate(lines or [""]):
        para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        para.alignment = PP_ALIGN.CENTER; para.line_spacing = 1.5
        if t:
            r = para.add_run(); r.text = t; r.font.size = Pt(40); r.font.color.rgb = RGBColor(0,0,0)
            rPr = r._r.get_or_add_rPr(); rPr.set('lang', lang)
            for tag in ('a:latin','a:ea','a:cs'):
                etree.SubElement(rPr, qn(tag)).set('typeface', FONT)

def make_slide(lines, notes, lang):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    box(s, 4036741, 147106, 8053659, 6588974, BLUE, lines, lang)
    box(s, 217798, 2823882, 3718582, 3912197, GREEN)
    ph = s.shapes.add_shape(1, Emu(217798), Emu(147106), Emu(3718582), Emu(2600000))
    ph.fill.solid(); ph.fill.fore_color.rgb = RGBColor(0xF2,0xF2,0xF2)
    ph.line.color.rgb = RGBColor(0xA6,0xA6,0xA6); ph.line.dash_style = 4
    ph.text_frame.text = "（在這裡放圖片）"
    s.notes_slide.notes_text_frame.text = notes

# 順序：繁 P1、繁 P2（lines=None）、簡 P1、簡 P2（lines=None）
```
輸出前用程式檢查不要有 U+E0100～U+E01EF 的異體字選擇符號，並用 soffice 轉 PDF 再看圖確認每行沒有跨行。

## 完成前檢查（務必做）
1. 單字都有出現在短文裡，短文的重點詞都有在單字裡。
2. 問答問題，看短文就能答。
3. P2 每題的中文、西文、英文互相對得上，編號連續、沒有多打或少打（舊教材曾有編號 113、西文與中文錯位的狀況）。
4. 繁簡逐行對應，沒有漏轉的字（舊教材曾有「來」沒轉成「来」）。
5. 不要夾入看不見的異體字選擇符號，輸出前用純文字確認。
6. 句子是台灣常用說法，不是翻譯腔。
7. 短文每行不超過 12 字，pptx 渲染後沒有折行。

## 若 Ben 沒給關鍵詞
先提出 3～5 個建議的詞或句型，再寫短文；他要的話才直接寫。