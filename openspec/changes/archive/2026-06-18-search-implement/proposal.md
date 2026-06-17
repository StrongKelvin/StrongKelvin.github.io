## Why

目前網站導覽列的搜尋按鈕僅為視覺裝飾，指向 `/blog` 頁面，沒有真正的搜尋功能。隨著部落格文章數量增加，訪客無法快速找到特定內容，需要一個全文搜尋解決方案。選擇 Pagefind 而非手動維護 fuse.js 索引，是為了降低長期維護成本。

## What Changes

- 將 Header 中的搜尋按鈕改為可展開的搜尋列，輸入關鍵字後即時顯示 Pagefind 搜尋結果
- 搜尋範圍涵蓋所有部落格文章的**標題**與**內文**
- 結果顯示匹配的文章列表，包含標題、摘要高亮片段與發佈日期
- 使用 Pagefind 自動建置搜尋索引，無需手動維護索引生成程式

## Capabilities

### New Capabilities
- `search`: 全站部落格文章搜尋功能，使用 Pagefind 實現零維護全文搜尋

### Modified Capabilities

（無既有 spec 需要修改）

## Impact

- `src/components/Header.astro`：搜尋按鈕改為觸發 Pagefind 搜尋 overlay
- 新增 `src/components/SearchOverlay.jsx`：封裝 Pagefind UI 的 Preact 元件
- 依賴新增：`pagefind`（devDependency，僅建置時需要）
- CI/CD（`.github/workflows/deploy.yml`）：建置流程需加入 Pagefind 索引生成步驟
- 所有頁面的 Header 都會受影響（搜尋功能全域可用）
