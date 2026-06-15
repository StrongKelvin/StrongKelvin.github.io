## 1. 定義深色主題 CSS 變數

- [x] 1.1 在 `src/styles/global.css` 新增 `html.dark` 區塊，補上所有顏色變數覆寫（參考 `preview-timeline.html` 的 oklch 色值）
- [x] 1.2 確認 `html` 加上 `transition` 讓主題切換有平滑動畫

## 2. 調整 Header 背景樣式

- [x] 2.1 將 Header 的 `background` 從 `oklch(100% 0 0 / 0.82)` 改為 `var(--color-surface)` 搭配既有 `backdrop-filter`
- [x] 2.2 確認 Header 在 light/dark 兩種主題下均有正確的背景與邊框顏色

## 3. 將 ThemeIcon 整合至 Header

- [x] 3.1 在 `Header.astro` 中 import `ThemeIcon` 元件
- [x] 3.2 在 Header 右側（搜尋按鈕旁）加入 `<ThemeIcon />`
- [x] 3.3 調整 `.nav-search` 與 ThemeIcon 之間的間距，確保右側元件排列整齊

## 4. 驗證與清理

- [x] 4.1 啟動 dev server 確認切換主題時 Header 與全頁面顏色正確變換
- [x] 4.2 確認 `localStorage` 主題偏好跨頁面持久化
- [x] 4.3 確認無 flicker 問題（dark 主題應在首次 paint 前已套用）
- [x] 4.4 確認行動版 Header 在 RWD 斷點下正常顯示
