# Agents.md

## 快速開始

```bash
npm run dev      # 本地開發伺服器，位於 localhost:4321
npm run build    # 建置到 dist/
npm run preview  # 預覽 production 建置結果
```

- **Node** >=22.12.0 必要。
- 專案無測試、lint、格式化或型別檢查腳本。

## 專案結構

- `src/pages/` — 頁面路由（`index`、`about`、`blog`）+ `posts/` 內的 Markdown 文章
- `src/layouts/` — `BaseLayout.astro`（主外殼）、`MarkdownPostLayout.astro`（文章包裝層）
- `src/components/` — `Header`、`Footer`、`Navigation`、`Menu`、`Social`、`Welcome`
- `src/styles/global.css` — 全域樣式
- `src/scripts/menu.js` — 漢堡選單切換（客戶端 JS）
- 純 Astro 6.x，無額外框架或整合。

## 內容與部落格

- 文章位於 `src/pages/posts/` 目錄，使用 `.md` 檔案並附 frontmatter。
- Frontmatter 必須包含：`layout`、`title`、`pubDate`、`author`、`description`、`image`（含 `url` + `alt`）、`tags`。
- 頂層文章使用 `../../layouts/MarkdownPostLayout.astro` 作為 `layout`，子目錄內的文章使用 `../../../layouts/...`。
- 部落格列表使用 `import.meta.glob('./posts/**/*.md', { eager: true })`，會遞迴匹配所有巢狀子目錄的文章，並以目錄名稱（年份）分組顯示。

## 已知問題

- `src/pages/about.astro:32` — `var(--frontWeith)` 為筆誤，應為 `var(--fontWeight)`；CSS 變數名稱不符。

## 語言

- 網站語言為**繁體中文**。頁面內容、UI 標籤及導覽皆使用中文。

## 編輯器

- VSCode：推薦擴充功能為 `astro-build.astro-vscode`。Launch config 可啟動 `astro dev`。
