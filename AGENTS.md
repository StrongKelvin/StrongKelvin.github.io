# AGENTS.md

## 開發指令

```bash
npm run dev      # 本機 dev server -> localhost:4321
npm run build    # 靜態輸出至 dist/
npm run preview  # 預覽 production build
```

- Node >=22.12.0
- 無測試、lint、格式化、型別檢查腳本
- `astro check` 可經由 `npx astro check` 執行（需手動安裝 `@astrojs/check`）

## 架構重點

| 路徑 | 說明 |
|---|---|
| `src/pages/` | 路由頁面（index, blog, about, tags/, posts/\[...slug\]） |
| `src/layouts/` | `BaseLayout.astro`（主外殼）、`MarkdownPostLayout.astro`（文章包裝） |
| `src/components/` | Header, Footer, Sidebar, Profile, Giscus, BlogPost, Navigation, Menu, Social, Welcome, Greeting.jsx (Preact), ThemeIcon |
| `src/content.config.ts` | Astro content collections 定義（`glob` 載入器讀取 `src/blog/**/[^_]*.md`） |
| `src/blog/` | 所有 Markdown 文章依年份分目錄存放（2019 ~ 2026） |

整合：`@astrojs/preact` + `astro-icon`。JSX 使用 Preact（`tsconfig.json` 設定）。

## 部落格須知

- **文章前端資料**須包含：`layout`、`title`、`pubDate`、`author`、`description`、`image`（`url` + `alt`）、`tags`。
- `layout` 路徑取決於文章深度：`src/blog/2025/foo.md` 用 `../../layouts/...`，`src/blog/2025/sub/bar.md` 用 `../../../layouts/...`。
- 文章路由為 `/posts/{id}`（由 `src/content.config.ts` 中的檔案相對路徑決定 id）。
- 所有頁面透過 `getCollection('blog')` 讀取內容；**唯獨 `src/pages/tags/index.astro` 尚未遷移**，仍使用舊的 `import.meta.glob`（參考 `src/pages/tags/[tag].astro` 的新寫法）。
- Giscus 評論元件掛在 `MarkdownPostLayout` 中。

## CI/CD

- GitHub Actions（`.github/workflows/deploy.yml`）：push 到 `main` 分支時自動建置並部署到 GitHub Pages。

## 語言

- 全站使用**繁體中文**。

## VSCode

- 推薦擴充：`astro-build.astro-vscode`
- Launch config 可直接啟動 `astro dev`
