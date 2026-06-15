## 需求

### 需求：Sidebar 分類動態推導
系統 SHALL 在 Sidebar 中提供「分類」區塊，從所有文章的 tags 動態推導分類清單，取代硬編碼的假資料。

#### 情境：分類來自文章 tags
- **WHEN** Sidebar 渲染
- **THEN** 分類 SHALL 從 `allPosts` 中所有文章的 `tags` 陣列迭代收集，統計每個 tag 出現的文章數

#### 情境：排序依計數降冪 + 名稱字母升冪
- **WHEN** 分類清單渲染
- **THEN** 分類 SHALL 先依文章數量降冪排序；數量相同時，依 tag 名稱字母升冪排序

#### 情境：連結使用原始 tag 字串
- **WHEN** 使用者點擊分類連結
- **THEN** URL SHALL 為 `/tags/{tag}`，使用原始 tag 字串（不經 slug 轉換）

#### 情境：分類計數與實際文章數一致
- **WHEN** 分類計數顯示
- **THEN** 每個 tag 的計數 SHALL 等於擁有該 tag 的文章總數
