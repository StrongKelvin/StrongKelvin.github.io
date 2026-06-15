## 1. Preact Component — CategoryCard

- [x] 1.1 建立 `src/components/CategoryCard.jsx`，接收 `categories`（`{name, count}[]`）作為 prop
- [x] 1.2 實作 `useState` 管理排序模式（`"count"` | `"name"`），預設為 `"count"`
- [x] 1.3 根據排序模式對 `categories` 進行排序：`"count"` 按 count 降冪（同名依 name 升冪），`"name"` 按 name 升冪
- [x] 1.4 渲染 title「分類」右側的排序切換按鈕，清楚標示當前模式
- [x] 1.5 渲染分類列表，每個項目包含名稱與計數徽章，連結至 `/tags/{name}`
- [x] 1.6 加入 CSS：`.cat-list` 設 `max-height` 為 10 筆資料高度，`overflow-y: auto`，僅超出時顯示捲軸

## 2. 整合至 Sidebar.astro

- [x] 2.1 在 `Sidebar.astro` 中匯入 `CategoryCard` 並以 `client:load` 掛載
- [x] 2.2 將現有分類邏輯的計算結果（`categories` 陣列）傳給 `CategoryCard`
- [x] 2.3 移除 Sidebar.astro 中舊的分類卡片標記與樣式

## 3. 驗證

- [x] 3.1 執行 `npm run build` 確認無編譯錯誤
- [x] 3.2 執行 `npm run preview` 確認分類卡片顯示正確、排序切換運作正常、超出 10 筆出現捲軸
