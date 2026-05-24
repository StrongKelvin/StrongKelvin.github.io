---
name: git-commit
description: >
  協助使用者產生結構化的 Git commit message，採用雙語並陳格式（英文 Conventional Commits 標題 + 繁體中文說明）。
  當使用者提到「提交」、「commit」、「寫 commit」、「commit message」、「git 提交」等關鍵字時，請務必使用這個 skill。
  即使使用者只說「存一下」、「記錄變更」、「做完這個功能了」等模糊表述，只要語境涉及版本控制提交，就應觸發此 skill。
---

# Git Commit 技能

## 核心原則

這個 skill 的目的是幫使用者寫出**結構清晰、便於日後查閱**的 commit message。好的 commit message 能讓專案協作更順暢，也讓 `git log` 和 `git bisect` 真正發揮價值。

使用者的專案使用繁體中文，但業界慣例是 commit 標題用英文。所以這個 skill 採用**雙語並陳**：標題用英文 Conventional Commits 格式，正文用繁體中文詳細說明變更內容與原因。

## 工作流程

當使用者表達提交意圖時（「幫我 commit」、「寫個 commit message」、「提交一下」等），依序執行以下步驟：

### 步驟 1：了解當前狀態

```bash
git status
git diff --staged --stat   # 暫存區檔案概覽
git diff --staged          # 暫存區詳細變更
```

如果暫存區是空的但工作目錄有變更，詢問使用者是否要將所有變更加入暫存區。

### 步驟 2：分析變更

閱讀 diff 內容，理解：
- **變更的類型**：新功能、修正、重構、文件、樣式等
- **變更的範圍**：影響了哪些模組或元件
- **變更的目的**：為什麼要做這個變更

不要只看檔案名稱，要真正理解 diff 的內容。

### 步驟 3：向使用者報告並討論

用繁體中文向使用者簡要說明你看到的變更內容，例如：

```
我注意到你修改了這些檔案：
- src/components/Header.astro（導覽列連結更新）
- src/pages/about.astro（關於頁面內容擴充）

變更摘要：更新了導覽列的連結結構，並在關於頁面新增了團隊介紹區塊。

你希望 commit 訊息的重點放在哪裡？還是直接產生？
```

這讓使用者有機會修正你的理解，也避免 commit message 偏離意圖。

### 步驟 4：產生 commit message

根據使用者的回饋，產生雙語 commit message。

## Commit Message 格式

### 標題（英文）

使用 Conventional Commits 格式：

```
type(scope): short description
```

**type 類型**：
- `feat` — 新功能
- `fix` — 錯誤修正
- `docs` — 文件變更
- `refactor` — 重構（不屬於 feat 或 fix）
- `style` — 程式碼格式（空白、逗號等，不影響邏輯）
- `perf` — 效能優化
- `test` — 測試相關
- `chore` — 建置、CI、依賴等維護工作

**scope（選擇性）**：受影響的模組或元件名稱，如 `header`、`blog`、`layout`。

**short description**：
- 祈使句，現在式
- 首字母小寫
- 結尾無句號
- 50 字元以內

### 正文（繁體中文）

標題下方空一行後寫入正文。正文應包含：

1. **做了什麼**：簡述變更內容
2. **為什麼做**：變更的原因或目的
3. **注意事項**（選擇性）：需要留意的地方，如破壞性變更、相依性更新等

正文每行不超過 72 字元，無需結尾句號。

### 完整範例

```
feat(header): add navigation links for blog and about pages

在導覽列新增部落格與關於頁面的連結
更新選單項目的 active 狀態判斷邏輯
移除已廢棄的首頁連結
```

```
fix(blog): correct date sorting on post list

修正文章列表的日期排序錯誤
原本使用字串比對導致 2026/01 排在 2025/12 之前
改為 Date 物件比對後排序正常
```

```
refactor(pages): extract repeated layout logic into BaseLayout

將頁面中重複的佈局邏輯萃取到 BaseLayout 元件
- 統一管理 meta title 和 description
- 簡化各頁面的 frontmatter 結構
- 無功能變更
```

## 提交方式

產生 commit message 後，用以下方式讓使用者確認：

1. 顯示完整的 commit message
2. 詢問使用者：「這個 commit message 可以嗎？要直接提交還是需要修改？」
3. 如果使用者同意，執行：

```bash
git commit -m "title" -m "body"
```

4. 如果使用者想修改，根據回饋調整後重新顯示確認

## 邊界情況處理

- **暫存區為空**：告知使用者並詢問是否要 `git add .` 或指定檔案
- **大量的變更（>10 個檔案）**：建議拆分為多個 commit，並詢問是否要分批處理
- **合併衝突**：不產生 commit message，先引導使用者解決衝突
- **merge commit**：使用預設的 merge commit message，不需要特別處理
- **WIP / 暫時性提交**：如果使用者明確表示只是暫存，可使用 `chore(wip): save progress` 並在正文說明

## 語言風格指引

與使用者溝通時使用繁體中文，語氣專業但親切。不要直接幫使用者執行 commit，一定要經過確認步驟。使用者對這個專案的理解一定比你深，你的角色是協助而非主導。
