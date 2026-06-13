## Context

Header 目前使用 `oklch(100% 0 0 / 0.82)` 背景（全白 + 0.82 不透明度）搭配 `backdrop-filter: blur(12px)`，在淺色模式下視覺上與瀏覽器網址列融為一體。ThemeIcon.astro 已存在但未被任何佈局引入，其 `dark` class 切換機制也缺少對應的 CSS 變數定義，導致深色模式實際上無效。

## Goals / Non-Goals

**Goals:**
- Header 背景從全白改為 `var(--color-surface)`，加上較深邊框，使其與頁面內容有明確層次
- 將 ThemeIcon 整合進 Header 右側，與搜尋按鈕並列
- 在 `global.css` 補上 `html.dark` 的 CSS 變數覆寫（參考 `preview-timeline.html` 的色值）
- 確保 header 在 dark 模式下也有對應的樣式

**Non-Goals:**
- 不改動 Footer、Sidebar 等其他元件的佈局
- 不新增外部相依套件（維持現有 Astro + Preact 架構）
- 不改變 Giscus 的主題連動邏輯

## Decisions

1. **保持 class-based 主題切換（`.dark`）而非 attr-based（`[data-theme]`）**
   - ThemeIcon.astro 與 Giscus.astro 均已使用 `classList.contains('dark')`，統一沿用可避免重構
   - CSS 選擇器使用 `html.dark` 即可對應

2. **Header 背景採用 `var(--color-surface)` 而非硬編碼色值**
   - 讓 Header 背景隨主題自動切換（淺色時偏白，深色時偏暗）
   - 維持 `backdrop-filter: blur(12px)` 半透明效果，以保留模糊遮透的現代感

3. **ThemeIcon 直接嵌入 Header.astro，而非透過 slot 或 islands**
   - 因為 ThemeIcon 已經是 Astro 元件（非 Preact），直接引用最簡潔
   - 不需要 client-side hydration 的互動邏輯（ThemeIcon 的 script 是 `is:inline`）

4. **深色主題色值直接引用 preview-timeline.html 的定義**
   - 那組色值是已審定過的設計色調，維持一致性

## Risks / Trade-offs

- [Header 背景加深可能影響可讀性] → 對比色維持原來比例，只改變背景層級
- [ThemeIcon 的 `is:inline` script 在 Header 內部可能重複執行] → Header 只被 BaseLayout 引用一次，無重複問題
- [`.dark` class 在 Astro 的 SSR 階段無法偵測] → 主題初始化已在 ThemeIcon 的 inline script 中處理，透過 `localStorage` 和 `matchMedia` 在 client 端決定
