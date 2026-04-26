# PetPack Intel - 寵物經濟 + 包裝產業供應鏈情報追蹤

## 專案狀態：建置中

### 系統架構

| 模組 | 說明 | 狀態 |
|------|------|------|
| **股價抓取** | 20 檔股票，Yahoo Finance | 待建置 |
| **新聞爬蟲** | 涵蓋 20 家公司 | 待建置 |
| **規則引擎** | 關鍵字匹配、情緒分析、重要性評分、異常偵測 | 待客製化 |
| **報告生成** | 每日報告、7 日報告 | 待建置 |
| **前端** | D3.js Dashboard、供應鏈圖、事件時間軸 | 待建置 |
| **CI/CD** | daily-ingest.yml + deploy-pages.yml | 待建置 |

---

## 追蹤範圍

### 寵物經濟 (8 家)

**上游 - 寵物鮮食** (1 家)
- Freshpet 鮮寵 (FRPT NASDAQ)

**中游 - 醫藥/用品** (4 家)
- Zoetis 碩騰 (ZTS NYSE) - 動物醫藥
- IDEXX 愛德士 (IDXX NASDAQ) - 寵物診斷
- Central Garden & Pet (CENT NASDAQ) - 寵物用品
- Elanco 禮來動保 (ELAN NYSE) - 動物保健

**下游 - 零售/服務** (3 家)
- Chewy 寵物電商 (CHWY NYSE)
- Trupanion 寵物保險 (TRUP NASDAQ)
- Petco (WOOF NASDAQ) - 寵物零售

### 包裝產業 (12 家)

**上游 - 原料** (1 家)
- International Paper 國際紙業 (IP NYSE)

**中游 - 包裝製造** (11 家)
- Ball 波爾 (BALL NYSE) - 金屬容器
- Amcor 安姆科 (AMCR NYSE) - 軟性包裝
- Sealed Air 希悅爾 (SEE NYSE) - 保護性包裝
- Smurfit Westrock 斯莫菲特 (SW NYSE) - 瓦楞紙箱
- Packaging Corp. 美國包裝 (PKG NYSE) - 瓦楞紙箱
- 正隆 (1904.TW TWSE) - 紙業/包裝
- 榮成紙業 (1909.TW TWSE) - 紙業/包裝
- Crown Holdings 皇冠 (CCK NYSE) - 金屬容器
- Graphic Packaging (GPK NYSE) - 消費品包裝
- Berry Global 貝瑞 (BERY NYSE) - 塑膠包裝
- Sonoco (SON NYSE) - 工業包裝

### 主題 (configs/topics.yml)

**寵物經濟主題**
- 寵物食品 (pet_food)
- 獸醫支出 (vet_spending)
- 寵物保險 (pet_insurance)

**包裝產業主題**
- 包裝價格 (packaging_price)
- 永續包裝 (sustainable_packaging)
- 紙價 (paper_price)

**共通主題**
- 財報 / 展望

---

## 標準流程

```
fetch_news → enrich_event → generate_metrics → detect_anomalies →
generate_daily → generate_7d_report → update_baselines → deploy
```

## 資料夾結構

```
petpack-intel/
├── lib/                        # 規則引擎
├── scripts/                    # 執行腳本
├── configs/                    # 設定檔
│   ├── companies.yml           # 20 家公司 + 上下游關係
│   ├── topics.yml              # 主題 + 關鍵字
│   ├── sentiment_rules.yml     # 情緒詞典
│   ├── importance_rules.yml    # 重要性規則
│   └── anomaly_rules.yml       # 異常偵測規則
├── fetchers/                   # 公司新聞爬蟲
├── data/
│   ├── raw/                    # 原始抓取資料
│   ├── events/                 # 標準格式事件 (JSONL)
│   ├── metrics/                # 每日指標
│   ├── baselines/              # 歷史基準線
│   ├── normalized/             # 股價資料
│   ├── financials/             # 財務資料
│   ├── holders/                # 持股資料
│   └── fund_flow/              # 資金流向
├── reports/
│   ├── daily/                  # 每日報告
│   └── 7d/                     # 7 日報告
├── site/
│   ├── index.html              # D3.js Dashboard
│   └── data/                   # 前端資料
└── CLAUDE.md
```

---

## 產出報告（Claude CLI）

當用戶說「產出報告」時，執行以下流程：

### 1. 拉取最新資料
```bash
git pull origin main
```

### 2. 讀取事件資料
- 讀取近 7 天的 `data/events/{date}.jsonl`
- 識別重要事件、主題趨勢、供應鏈動態

### 3. 產出分析並寫入 JSON
讀取現有的 Actions 報告 JSON，追加 `llm_analysis` 和 `financials` 欄位。

### 4. Commit 並 Push
```bash
git add site/data/reports/
git commit -m "Weekly report: {date}"
git push
```

---

## 快速啟動

```bash
cd repos/petpack-intel
source .venv/bin/activate

# 啟動本地伺服器
python3 -m http.server 6232 -d site

# 瀏覽器開啟
open http://localhost:6232
```


---

## 每日例行（進入此 repo 時自動提醒）

當你讀取此 CLAUDE.md 時，主動執行以下檢查並提醒用戶：

### 自動檢查清單

1. **同步最新** — `git pull origin main`
2. **今日 Actions 狀態** — `gh run list --limit 1`
3. **今日事件數** — `wc -l data/events/$(date +%Y-%m-%d).jsonl`
4. **關鍵字審計** — 讀取 `site/data/reports/daily/$(date +%Y-%m-%d).json` 的 `filter_audit` 欄位

### 提醒格式

```
📋 每日狀態
- Actions: ✅/❌
- 今日事件: N 筆
- 關鍵字審計: ✅ 通過 / ⚠️ gate2 擋住率 XX%，建議檢視
```

若 `filter_audit.alert` 為 true 或 `gate2_block_rate > 30%`，提醒用戶：「有關鍵字需要調整，要執行關鍵字審計嗎？」

### 關鍵字審計流程（用戶確認後執行）

1. 檢視 `filter_audit.gate2_samples` 中被擋住的文章標題
2. 判斷每篇是否與本追蹤產業相關
3. 相關的文章 → 找出缺少的關鍵字，建議新增到 `configs/topics.yml`
4. 呈現結果：

```
## 關鍵字審計結果

通過率：XX% | Gate 2 擋住率：XX%

### 被擋住但應通過的文章
| 標題 | 缺少的關鍵字 | 建議加入的主題 |
|------|-------------|--------------|

### 建議新增關鍵字
topics.yml → {topic_id} → keywords 新增：
- keyword1
- keyword2
```

5. 用戶確認後更新 `configs/topics.yml`，commit + push

