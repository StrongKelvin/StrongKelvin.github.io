## 1. Sidebar 分類動態化

- [x] 1.1 移除 `Sidebar.astro` 中硬編碼的 `categories` 陣列
- [x] 1.2 實作自 `allPosts` 動態推導分類的邏輯（迭代 tags、計數、排序）
- [x] 1.3 更新模板中分類 URL 使用 tag 原始字串（不再需要 slug）

## 2. 驗證

- [x] 2.1 執行 `npm run dev` 確認 sidebar 分類區塊正確顯示實際 tag 與計數
- [x] 2.2 確認點擊分類連結可正確導向 `/tags/{tag}` 頁面
