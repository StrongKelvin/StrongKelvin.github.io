## Why

每篇文章閱讀完後，目前沒有引導讀者探索更多相關內容的機制，降低了站內閱讀連貫性與內容發現率。加入時間軸風格的文章列表，能讓讀者在文章底部直覺地瀏覽近期文章，提升互動與停留時間。

## What Changes

- 新增 `PostTimelineList` 可複用元件，以垂直年分時間軸視覺風格呈現文章列表
- 在 `MarkdownPostLayout` 底部插入近期文章時間軸（排除當前文章，依日期降序，顯示 5 篇）
- 將時間軸元件同步整合至 `/blog` 與 `/@blog` 頁面
- 設計定稿參考 `preview-timeline.html`，採用 **實點+自發光 (tl-needle-glow)** 樣式：年份群組可摺疊，年份文字自帶光暈

## Capabilities

### New Capabilities
- `post-timeline-list`: 可複用的垂直時間軸文章列表元件，支援年份群組、可摺疊、實點自發光視覺效果

### Modified Capabilities

（無既有 spec 需修改）

## Impact

- `src/components/PostTimelineList.astro` — 新元件（含可摺疊年群 accordion 邏輯）
- `src/layouts/MarkdownPostLayout.astro` — 底部新增時間軸區塊
- `src/pages/blog.astro`、`src/pages/@blog.astro` — 整合時間軸取代卡片清單
- CSS 新增時間軸視覺樣式（垂直線、實心圓點、自發光光暈、可摺疊動畫、暗黑模式支援）
