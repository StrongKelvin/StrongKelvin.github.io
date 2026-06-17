## ADDED Requirements

### Requirement: Search overlay toggle
Header 中的搜尋按鈕 SHALL 點擊後展開搜尋 overlay。再次點擊或按下 ESC 鍵 SHALL 關閉 overlay。

#### Scenario: Open search overlay
- **WHEN** 使用者點擊 Header 中的搜尋按鈕
- **THEN** 顯示 Pagefind 搜尋 overlay，且搜尋輸入框自動取得焦點

#### Scenario: Close search overlay via ESC
- **WHEN** 使用者按下 ESC 鍵
- **THEN** 搜尋 overlay 關閉

#### Scenario: Close search overlay via backdrop click
- **WHEN** 使用者點擊 overlay 背景（非結果區域）
- **THEN** 搜尋 overlay 關閉

### Requirement: Real-time search
系統 SHALL 在使用者輸入關鍵字時即時透過 Pagefind 比對文章標題與內文，並顯示比對結果。當輸入為空時 SHALL 顯示提示文字而非結果列表。

#### Scenario: Search with matching results
- **WHEN** 使用者輸入關鍵字且存在至少一篇標題或內文包含該關鍵字的文章
- **THEN** 系統顯示匹配的文章列表，每篇包含標題、高亮片段、發佈日期

#### Scenario: Search with no results
- **WHEN** 使用者輸入關鍵字且沒有任何文章符合
- **THEN** 系統顯示「無符合結果」提示

#### Scenario: Empty input
- **WHEN** 使用者清空搜尋輸入框
- **THEN** 系統隱藏結果列表，顯示搜尋提示

### Requirement: Search result navigation
每筆搜尋結果 SHALL 是可點擊的連結，點擊後導向該文章的頁面。

#### Scenario: Click search result
- **WHEN** 使用者點擊某筆搜尋結果
- **THEN** 瀏覽器導向該文章頁面，且搜尋 overlay 關閉

### Requirement: Search index auto-generation
建置階段 SHALL 自動執行 Pagefind 索引生成，無需手動介入。

#### Scenario: Build generates Pagefind index
- **WHEN** 執行 `npm run build`
- **THEN** `dist/pagefind/` 目錄產生存放搜尋索引的檔案
