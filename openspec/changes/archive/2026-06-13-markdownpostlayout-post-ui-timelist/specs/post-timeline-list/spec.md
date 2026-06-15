## 新增需求

### 需求：時間軸文章列表元件
系統 SHALL 提供一個 `PostTimelineList.astro` 元件，以垂直時間軸佈局呈現文章列表，包含年份分組、可折疊年份區段（手風琴），以及與 `preview-timeline.html` tl-needle-glow 變體一致的光暈視覺效果。

#### 情境：預設時間軸渲染
- **WHEN** 元件收到跨多個年份的文章陣列
- **THEN** 它 SHALL 將每個年份渲染為可折疊區段，包含年份標頭（年份標籤、文章數量徽章、箭頭指示器），以及垂直排列的文章項目（含時間軸線段與圓點標記）

#### 情境：依年份分組
- **WHEN** 文章跨多個年份（例如 2025 和 2026）
- **THEN** 元件 SHALL 將每個年份渲染為獨立區段，各年份內文章依日期降冪排序，年份以最新優先排列

#### 情境：遵守 limit 屬性
- **WHEN** `limit` 屬性設為 `5`
- **THEN** 元件 SHALL 在所有年份中最多渲染 5 篇文章，以最新優先

#### 情境：排除特定文章
- **WHEN** `excludeSlug` 屬性設為 `"2025/2025-1"`
- **THEN** 元件 SHALL 在套用 limit 之前，從渲染列表中排除該 ID 的文章

#### 情境：收到空文章陣列
- **WHEN** `posts` 屬性為空陣列
- **THEN** 元件 SHALL 不渲染任何內容（無時間軸容器）

### 需求：可折疊年份區段（手風琴）
年份區段 SHALL 可透過點擊互動折疊，且一次僅開啟一個年份。

#### 情境：點擊切換年份
- **WHEN** 使用者點擊年份標頭
- **THEN** 若該年份已關閉，則開啟它並關閉其他所有年份；若該年份已開啟，則關閉它

#### 情境：預設開啟第一個年份
- **WHEN** 元件渲染
- **THEN** 第一個（最新）年份群組 SHALL 預設開啟，其餘關閉

#### 情境：透過屬性停用手風琴
- **WHEN** `accordion` 屬性設為 `false`
- **THEN** 所有年份群組 SHALL 以展開且不可折疊的方式渲染

### 需求：元件 API 介面
元件 SHALL 接受型別化的屬性以利彈性整合。

#### 情境：接受所有定義屬性
- **WHEN** 元件以 `posts`、`excludeSlug`、`limit`、`groupByYear` 和 `accordion` 呼叫
- **THEN** 它 SHALL 正確套用所有屬性，無 TypeScript 錯誤

### 需求：時間軸視覺樣式（tl-needle-glow）
視覺樣式 SHALL 與 `preview-timeline.html` tl-needle-glow 變體完全相同，使用網站的設計 token。

#### 情境：顯示垂直時間軸線段
- **WHEN** 元件渲染
- **THEN** 左側 SHALL 出現一條垂直線段（1.5px、`var(--color-border)`），貫穿時間軸完整高度

#### 情境：活躍年份的實心圓點與光暈
- **WHEN** 年份群組開啟
- **THEN** 其圓點標記 SHALL 為 9x9px 實心 `var(--color-accent)`，縮放 1.4 倍，並具有分層 box-shadow 光暈：4px 柔軟強調色環、14px 更寬柔環、32px 擴散外光暈

#### 情境：年份標頭自體發光
- **WHEN** 年份群組開啟
- **THEN** 年份標頭 SHALL 顯示圓角背景（`oklch(78% 0.10 230 / 0.15)`）與三層 box-shadow 光暈效果

#### 情境：年份標頭顯示中繼資料
- **WHEN** 元件渲染
- **THEN** 每個年份標頭 SHALL 顯示：大號年份標籤（1.6rem、粗體）、文章數量徽章（等寬字型、圓角藥丸）、以及區段開啟時旋轉 90° 的箭頭指示器（▶）

#### 情境：文章項目顯示日期、標題、標籤
- **WHEN** 元件渲染
- **THEN** 每個文章項目 SHALL 顯示：等寬字型日期（MM-DD）、可點擊的標題連結、以及右側的內聯標籤徽章

#### 情境：文章項目懸停效果
- **WHEN** 使用者懸停於文章項目
- **THEN** 項目背景 SHALL 變為 `var(--color-accent-soft)`，標題連結 SHALL 變為 `var(--color-accent)`

### 需求：折疊動画
開啟與關閉年份區段 SHALL 有平滑動畫。

#### 情境：平滑開啟／關閉過渡
- **WHEN** 年份區段被打開或關閉
- **THEN** 文章列表 SHALL 以 `max-height` 過渡（0.4s cubic-bezier）和 `opacity` 過渡（0.3s ease）進行動畫

### 需求：深色模式支援
元件 SHALL 透過 `data-theme` 屬性遵循網站的深色模式。

#### 情境：適應深色主題
- **WHEN** `<html>` 設有 `data-theme="dark"`
- **THEN** 所有時間軸顏色 SHALL 透過 CSS 自訂屬性適應，光暈效果在深色背景上正確渲染

### 需求：響應式佈局
元件 SHALL 適應行動裝置視埠。

#### 情境：行動版單欄
- **WHEN** 視埠寬度為 768px 或以下
- **THEN** 時間軸左側內距 SHALL 從 `var(--space-xl)` 縮減為 `var(--space-lg)`，年份標籤字型 SHALL 縮小至 1.3rem，文章項目 SHALL 將標籤換行至標題下方

### 需求：整合至 MarkdownPostLayout
`MarkdownPostLayout.astro` SHALL 在文章底部包含一個「近期文章」時間軸區段。

#### 情境：文章底部的近期文章區段
- **WHEN** `MarkdownPostLayout.astro` 渲染
- **THEN** 它 SHALL 包含一個時間軸，顯示 5 篇最新文章（排除當前文章），位於 `<div class="post-content">` 區段之後，且手風琴停用（所有年份展開）

#### 情境：排除當前文章
- **WHEN** 渲染近期文章時間軸
- **THEN** 當前文章 SHALL 不出現在時間軸列表中

#### 情境：靜態展開檢視
- **WHEN** 在 `MarkdownPostLayout` 內部渲染
- **THEN** 時間軸 SHALL 顯示所有可用年份，完全展開且不可折疊

### 需求：整合至 /blog 與 /@blog 頁面
`/blog` 與 `/@blog` 頁面 SHALL 使用 `PostTimelineList` 並啟用手風琴行為。

#### 情境：/blog 使用時間軸
- **WHEN** `/blog.astro` 渲染
- **THEN** 它 SHALL 以時間軸格式渲染所有文章，啟用手風琴且 groupByYear=true

#### 情境：/@blog 使用時間軸
- **WHEN** `@blog.astro` 渲染
- **THEN** 它 SHALL 以時間軸格式渲染所有文章，啟用手風琴且 groupByYear=true
