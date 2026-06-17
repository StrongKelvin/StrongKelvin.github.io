## 1. 安裝與設定 Pagefind

- [x] 1.1 安裝 Pagefind：`npm install -D pagefind`
- [x] 1.2 更新 `package.json` 的 build script：`"build": "astro build && npx pagefind --source dist"`

## 2. CI/CD 整合

- [x] 2.1 在 `.github/workflows/deploy.yml` 的 build 步驟中，Astro build 完成後加入 `npx pagefind --source dist`

## 3. Preact 搜尋覆蓋層元件

- [x] 3.1 建立 `src/components/SearchOverlay.jsx`，實作 overlay 開關狀態與鍵盤事件（ESC 關閉）
- [x] 3.2 使用動態 `import('/pagefind/pagefind.js')` 載入 Pagefind 客戶端
- [x] 3.3 實作輸入框 onChange 事件，呼叫 `pagefind.search(term)` 即時搜尋
- [x] 3.4 渲染搜尋結果（標題、高亮片段、發佈日期），支援鍵盤 ↑↓ 選擇與 Enter 確認

## 4. 修改 Header.astro

- [x] 4.1 將搜尋 `<a>` 改為 `<button>`，移除 `href="/blog"`
- [x] 4.2 引入 SearchOverlay 元件並以 `client:load` 掛載

## 5. 覆蓋層樣式

- [x] 5.1 在 SearchOverlay 中撰寫 overlay 佈局、進出動畫與響應式樣式，與網站主題變數一致