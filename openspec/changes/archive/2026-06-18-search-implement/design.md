## Context

目前 Header 的搜尋按鈕是一個無功能的 `<a>` 連結指向 `/blog`。網站使用 Astro v6 靜態生成，透過 GitHub Pages 部署。文章數量目前約 18 篇，預計會持續增長。需要使用 Pagefind 作為搜尋引擎以降低長期維護成本。

Pagefind 是由 Astro 團隊維護的靜態搜尋工具，建置時自動掃描 HTML 生成搜尋索引，內建中文分詞與模糊搜尋，產出結果包含高亮片段。

## Goals / Non-Goals

**Goals:**
- 在 Header 中提供可展開的搜尋 overlay，輸入關鍵字即時比對
- 搜尋範圍涵蓋所有文章的標題與內文
- 結果顯示文章標題、內文高亮片段與發佈日期
- 使用 Pagefind 自動建置索引，零手動維護
- CI/CD 流程中自動執行 Pagefind 索引生成

**Non-Goals:**
- 搜尋標籤（標籤已有獨立頁面）
- 伺服器端搜尋（網站為靜態部署，無後端）
- 自訂分詞邏輯（Pagefind 內建處理）

## Decisions

| 決策 | 選擇 | 替代方案 | 理由 |
|---|---|---|---|
| 搜尋引擎 | Pagefind | fuse.js, lunr, MiniSearch | 自動索引、內建中文分詞、零維護、Astro 生態相容 |
| UI 模式 | Pagefind 內建 UI + Preact 封裝 | 自訂 overlay | 直接使用 Pagefind 的 search.js 輸出，包裝為 Preact 元件以符合專案慣例 |
| 索引觸發 | `npx pagefind` 在 build 後執行 | Astro 整合套件 | 整合套件可能版本滯後，直接 CLI 最穩定 |
| 元件框架 | Preact (client:load) | Vanilla JS | 專案已有 Preact 整合，hydrate 成本低 |

## Risks / Trade-offs

- [Pagefind 依賴] 需額外建置步驟 → 在 CI/CD 與本機 dev script 中加入 `npx pagefind`
- [Pagefind 索引範圍] 預設掃描 `dist/` 所有 HTML → 可透過 `--glob` 限制範圍避免多餘索引
- [中文分詞品質] Pagefind 使用 char-based n-gram，對中文效果良好但非完美 → 已通過多數靜態部落格驗證
