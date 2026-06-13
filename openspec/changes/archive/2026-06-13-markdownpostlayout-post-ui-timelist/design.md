## Context

現有部落格頁面（`blog.astro`、`@blog.astro`、首頁）皆使用卡片式文章列表，缺乏時間軸視覺元素。`MarkdownPostLayout` 在文章底部完全沒有後續閱讀引導。標籤頁面 `/tags/[tag]` 僅顯示純文字連結，體驗較粗糙。

已產出設計原稿 `preview-timeline.html`，內含四種時間軸變體，經評估後定稿採用 **tl-needle-glow（實點+自發光）** 作為最終樣式。

## Goals / Non-Goals

**Goals:**
- 建立可複用的 `PostTimelineList` Astro 元件，嚴格遵循 `preview-timeline.html` 中 `tl-needle-glow` 變體的視覺規範
- 在 `MarkdownPostLayout` 文章內容底部嵌入時間軸區塊，顯示近期文章（排除當前文章，預設 5 篇）
- 整合至 `/blog` 與 `/@blog` 頁面，取代既有卡片清單
- 支援暗黑模式（`data-theme="dark"`），時間軸顏色自動切換
- 元件含客戶端 accordion 行為：點擊年份標題切換展開/收合，同一時間僅展開一年

**Non-Goals:**
- 不修改 content collection schema
- 不更動現有路由結構
- 不引入外部相依套件
- 不保留卡片/時間軸切換 toggle（未來可擴充）
- 不修改 `tag/index.astro`（尚未遷移至 content collections）
- 不在 `MarkdownPostLayout` 中實作可摺疊功能（近期文章區塊固定展開，不需 accordion）

## Decisions

1. **設計規範錨定**：以 `preview-timeline.html` 作為實作參考，選擇 `tl-needle-glow` 變體：
   - 垂直線：1.5px `var(--color-border)`，左側定位
   - 實心圓點：9x9px，開啟時放大 1.4x，加上多層 `box-shadow` 光暈
   - 年份自發光：`.year-header` 在 `is-open` 時加上 `background` + `box-shadow` 光暈效果
   - 摺疊動畫：`.post-list` 使用 `max-height` + `opacity` transition

2. **accordion 行為（僅用於 `/blog` 與 `/@blog`）**：同一時間僅展開一年群組，點擊另一年時自動收合當前展開者。`MarkdownPostLayout` 底部近期文章固定展開，不需 accordion。

3. **純 Astro + 少量客戶端 JS**：時間軸渲染由 Astro SSR 完成，accordion 切換行為透過 `<script>` 內嵌 JS 處理。

4. **顏色值**：
   - 圓點光暈：`oklch(78% 0.10 230 / 0.35)` 向外遞減
   - 年份光暈背景：`oklch(78% 0.10 230 / 0.15)` + `box-shadow` 三層
   - 所有顏色透過 CSS 變數隨 `data-theme` 切換

5. **props 設計**：
   - `posts` - 文章陣列（必要）
   - `excludeSlug` - 排除指定文章 slug（選填）
   - `limit` - 筆數上限，預設 5（選填）
   - `groupByYear` - 是否依年份分組，預設 true（選填）
   - `accordion` - 是否啟用可摺疊 accordion 行為，預設 true（選填）

## Risks / Trade-offs

- [JS 依賴] Accordion 行為依賴客戶端 JS，若使用者停用 JS 則所有年群同時展開（degradation 合理）
- [CSS 體積] 時間軸樣式約 120-150 行 CSS（含 glow 效果與動畫），可接受
- [顏色系統] `oklch()` 使用特定色相角度（230），若未來主題色改變需一併更新
