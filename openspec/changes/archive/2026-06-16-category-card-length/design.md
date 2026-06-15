## Context

Sidebar 的分類卡片目前以靜態方式列出所有 tag，僅支援按照文章數量降冪（同名按字母升冪）排序。隨著 tags 數量已超過 20 筆，卡片高度不斷增長，在視覺上與操作上都不理想。

專案已整合 `@astrojs/preact`，可用 Preact component 處理 client-side 互動。

## Goals / Non-Goals

**Goals:**
- 分類卡片最大可視高度限制為 title + 10 筆資料
- 超出 10 筆時顯示垂直捲軸
- 在 title 右側新增排序切換按鈕，支援「依名稱」與「依熱門度」兩種模式
- 預設排序：依熱門度降冪 → 同名時依名稱字母升冪

**Non-Goals:**
- 不影響「標籤」與「社群」卡片
- 不改變路由或文章資料結構
- 不做動畫或過渡效果（除非輕量）

## Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| 互動方案 | 使用 Preact component + `client:load` | 專案已整合 Preact，無需額外相依；`client:load` 確保 SSG 頁面上 hydrate 後即可互動 |
| 排序狀態管理 | 單一 `useState` 存 `"name"` 或 `"count"` | 簡單、無需外部 state 管理 |
| Component 拆分 | 將分類卡片抽成獨立 Preact component `CategoryCard` | 避免 Sidebar.astro 過度膨脹，邏輯與樣式隔離 |
| CSS 捲軸 | `.cat-list` 加上 `max-height` + `overflow-y: auto` | 純 CSS，零 JS 開銷 |

## Risks / Trade-offs

- **Risks**: 少於 10 筆時仍顯示 scrollbar track → 可加 `overflow-y: auto` 只在需要時顯示捲軸
- **Trade-off**: 抽成 Preact component 增加一個檔案，但 Sidebar.astro 保持簡潔
