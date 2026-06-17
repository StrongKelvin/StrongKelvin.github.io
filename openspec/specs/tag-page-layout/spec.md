# tag-page-layout 規格書

## 目的
待定——由封存 tage-uiux-layout 變更所建立。封存後請更新目的。

## 需求
### 需求：標籤頁面跟隨主佈局網格

標籤頁面的 `<div class="main">` SHALL 與其他內容頁面使用相同的雙欄網格佈局：`grid-template-columns: 1fr 280px`，搭配 `gap: var(--space-xl)`，並在 `max-width: 768px` 時摺疊為單欄。

#### 情境：標籤頁面在桌面版呈現雙欄佈局
- **WHEN** 視窗寬度大於 768px
- **THEN** 頁面內容 SHALL 以雙欄網格顯示，左側為內容、右側為側邊欄

#### 情境：標籤頁面在手機版摺疊為單欄
- **WHEN** 視窗寬度為 768px 或更小
- **THEN** 頁面 SHALL 以單欄垂直堆疊顯示內容與側邊欄

### 需求：標籤頁面包含 Profile 英雄區

標籤頁面 SHALL 在頁面內容區域頂部渲染 `<Profile>` 元件，與 `index.astro` 和 `blog.astro` 的引入方式相同。

#### 情境：Profile 英雄區出現在內容頂部
- **WHEN** 標籤頁面載入
- **THEN** Profile 英雄區 SHALL 顯示在主內容網格上方，包含頭像、名稱、副標題、自我介紹與技術標籤

### 需求：標籤頁面包含 Sidebar

標籤頁面 SHALL 在網格右欄渲染 `<Sidebar>` 元件，並接收 `allPosts` 與 `allTags` 作為 props。

#### 情境：Sidebar 在桌面版顯示於右欄
- **WHEN** 標籤頁面在桌面視埠上渲染
- **THEN** Sidebar SHALL 在 `.main` 網格的右欄中可見

#### 情境：Sidebar 在手機版顯示於內容下方
- **WHEN** 標籤頁面在手機視埠（768px 或更小）上渲染
- **THEN** Sidebar SHALL 以單欄形式顯示在主內容下方

### 需求：標籤頁面以卡片形式顯示篩選後的文章

經選取標籤篩選後的文章 SHALL 使用 `.post-card` 卡片樣式顯示，搭配 `--color-surface` 背景、`--radius-md` 圓角、`--color-border` 邊框，以及懸停效果。

#### 情境：篩選後的文章以樣式化卡片顯示
- **WHEN** 標籤頁面渲染篩選後的文章
- **THEN** 每篇文章 SHALL 以卡片形式呈現，包含標題、發布日期、描述與標籤膠囊

#### 情境：文章卡片具備懸停效果
- **WHEN** 使用者將游標懸停在文章卡片上
- **THEN** 卡片邊框 SHALL 變為 `--color-accent-muted` 並顯示輕微的 box-shadow

### 需求：標籤頁面顯示含文章數量的區段標題

頁面 SHALL 以 `.section-title` 樣式（小型大寫、`--color-text-secondary`、底部邊框）顯示區段標題，內容包含標籤名稱與文章數量。

#### 情境：區段標題顯示標籤名稱與數量
- **WHEN** 標籤頁面渲染標籤 "astro" 與 5 篇文章
- **THEN** 區段標題 SHALL 顯示如 "標籤：astro（共 5 篇文章）" 的文字

### 需求：BlogPost 元件渲染為完整卡片

`<BlogPost>` 元件 SHALL 接受 `title`、`url`、`date`、`description` 與 `tags` 等 props，並渲染完整的 `.post-card` 元素及所有文章後設資料。

#### 情境：BlogPost 渲染包含所有後設資料的卡片
- **WHEN** BlogPost 接收到 title、url、date、description 與 tags 等 props
- **THEN** 它 SHALL 渲染一張卡片，包含作為連結的標題、格式化日期、描述文字與標籤膠囊

#### 情境：BlogPost 在缺少選用 props 時渲染最小卡片
- **WHEN** BlogPost 僅接收到 title 與 url 等 props（無 date、description、tags）
- **THEN** 它 SHALL 渲染僅包含標題作為連結的卡片，並優雅降級

