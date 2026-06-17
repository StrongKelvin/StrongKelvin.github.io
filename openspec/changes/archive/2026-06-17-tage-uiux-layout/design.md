## Context

`src/pages/tags/[tag].astro` 目前是網站中唯一未遵循 `.main` 雙欄 grid 佈局的內容頁面。它直接使用 `<p>` 和 `<ul>` 搭配最簡陋的 `<BlogPost>` 元件（僅產出 `<li><a>`），沒有 Profile hero、沒有 Sidebar、沒有卡片式文章列表。

網站其他內容頁面（`index.astro`、`blog.astro`、`MarkdownPostLayout.astro`）都遵循統一的佈局模式：

1. `<Profile>` hero banner
2. `<div class="main">` 雙欄 grid（1fr content + 280px sidebar）
3. 文章以 `.post-card` 卡片樣式呈現
4. `<Sidebar>` 顯示分類、標籤雲、近期文章

CSS 變數系統（OKLCH）已支援淺色／深色模式，現有 tags 頁面未使用。

## Goals / Non-Goals

**Goals:**
- `[tag].astro` 頁面與其他內容頁面視覺一致
- `BlogPost` 元件升級為完整卡片（含日期、描述、標籤）
- 現有功能完全保留，僅改變視覺呈現

**Non-Goals:**
- 不修改 `tags/index.astro`（該頁面另案處理）
- 不新增外部相依套件
- 不改變路由結構

## Decisions

### 1. 升級 BlogPost 元件而非內嵌卡片 markup

選擇升級 `BlogPost.astro` 並擴充其 props（`date`、`description`、`tags`）而非在 `[tag].astro` 中直接撰寫卡片 HTML。理由：元件化有利維護，若未來其他頁面也需卡片列表可復用。

### 2. 保留 `<ul>` 語意結構，但套用卡片樣式

卡片容器使用 `<li class="post-card">` 搭配 `list-style: none`，保留無障礙語意的同時取得視覺一致性。

### 3. 統計資訊使用 `.section-title` 風格

在頁面標題處顯示「標籤：{tag}（共 {n} 篇文章）」，採用 `.section-title` 的樣式（small uppercase、border-bottom），與其他頁面 section 標題一致。

## Risks / Trade-offs

- **BlogPost props 增加** → 現有其他使用處（目前僅一處）需一併更新 props，但這是預期行為且範圍很小
- **無漸進增強** → 卡片樣式依賴 CSS variables，若變數未定義會 fallback 但外觀不佳；網站已全局定義，風險低
