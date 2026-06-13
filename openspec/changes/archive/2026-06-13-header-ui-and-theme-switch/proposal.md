## Why

目前的 Header 採用白色半透明背景（`oklch(100% 0 0 / 0.82)`），在淺色模式下容易與瀏覽器網址列視覺混淆，缺乏層次感。此外，深色佈景主題的基礎設施（class 切換、localStorage 持久化）雖已存在，但缺少對應的 CSS 變數定義，導致切換主題後頁面外觀無實際變化，也缺少 Header 內的主題切換按鈕。

## What Changes

- **Header 背景加深**：將 Header 背景色從全白改為帶有表面色的背景（如 `var(--color-surface)` 搭配較明顯的邊框），使其與瀏覽器網址列有清楚區隔
- **Header 新增主題切換按鈕**：將現有 `ThemeIcon.astro` 整合進 Header 最右側，取代或並列於搜尋按鈕旁
- **補完深色主題 CSS 變數**：在 `global.css` 中補上 `html.dark` 的 CSS 變數覆寫，使用 `preview-timeline.html` 中定義的 oklch 色值
- **移除非使用的主題切換機制**：ThemeIcon.astro 現行未被任何頁面引用，整合至 Header 後正式啟用

## Capabilities

### New Capabilities
- `theme-switch`: Header 內建淺色／深色佈景主題切換功能。包含切換按鈕 UI、主題狀態持久化、以及全域深色樣式定義

### Modified Capabilities
- （無既有 spec 需要修改）

## Impact

- `src/components/Header.astro`：背景色變更、新增 ThemeIcon 元件引用
- `src/components/ThemeIcon.astro`：保留核心邏輯，若需要可配合 Header 調整樣式
- `src/layouts/BaseLayout.astro`：無需改動（Header 整合後自動生效）
- `src/styles/global.css`：新增 `html.dark` 的 CSS 變數區塊
