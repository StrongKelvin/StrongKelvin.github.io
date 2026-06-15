## Context

Sidebar.astro 目前使用硬編碼的 `categories` 陣列與文章實際 tags 脫節。Sidebar 已收到 `allPosts`（內容 collection）與 `allTags`（去重後標籤列表）作為 props。

## Goals / Non-Goals

**Goals:**
- 從 `allPosts` 中提取所有出現過的 tags 作為分類來源
- 統計每個 tag 出現的文章數量作為計數
- 排序方式：按文章數量降冪排列，數量相同則依 tag 名稱字母排序
- 維持 `/tags/{tag}` 的 URL 路徑不變

**Non-Goals:**
- 不變更標籤雲區塊（`allTags`）的呈現方式
- 不變更 Sidebar 的 prop 介面
- 不新增 UI 樣式變更

## Decisions

- **動態推導分類**：使用 `allPosts` 迭代收集所有 tags 並計數，取代硬編碼。無需額外依賴或資料結構。
- **slug 即 tag**：不再需要 slug 欄位，直接使用原始 tag 字串作為路徑。
- **排序策略**：依計數降冪 + 名稱字母升冪，讓熱門分類優先顯示。

## Risks / Trade-offs

- **標籤名稱雜亂**：若文章 tags 未標準化（大小寫不一致），可能產生重複分類 → 由內容維護者確保 tags 一致性，實作時不做自動正規化以維持與 `/tags` 頁面行為一致。
