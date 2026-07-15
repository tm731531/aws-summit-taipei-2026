# 2026-07-15（三）AWS Summit Taipei 2026 — Day 1

> 場地：TICC 台北國際會議中心
> 議程來源：[我的推薦文](https://blog.tomting.com/2026/07/10/aws-summit-taipei-2026-enterprise-ai-sessions/)

**實際跑了 5 場**：Keynote / MOD01 / KIRO02 / KIRO05 / MOD03。MOD04 臨時有事沒去。

## 🔍 這份筆記怎麼來的、可信度如何

現場錄音 3.3 小時 → 本地 faster-whisper 轉錄（105,014 字）→ Cerebras 結構化摘要 → **逐字稿與 149 張現場投影片逐一交叉比對**。

**whisper 把技術名詞聽壞了很多**，一律以投影片為準。已修正的例子：

| 聽成 | 實際 |
|---|---|
| Hot Engineering | **Harness** Engineering |
| Bible Coding | **Vibe** Coding |
| Antarctic Cloud | **Anthropic** |
| NTT / SEAL | **MCP** / **Skill** |
| Stealing | **Steering** |
| Witfrog | **Wipro** |
| Face API | **FastAPI** |
| 一 K S | **EKS** |
| colorcontainer | **Kata Containers** |
| G-Ryzen | **gVisor** |

**每個事實都有可信度標記：**

- ✅ 投影片可查證（附張數）
- 🎤 僅講者口述，投影片無
- ⚠️ 聽不清或有疑義 → 進各節的「待查核」，**不寫進正文假裝是事實**

**可查證率跟該場拍了幾張投影片直接相關**：

| 場次 | 投影片 | ✅ 可查證 | ⚠️ 存疑 |
|---|---|---|---|
| Keynote | **只有 2 張** | 2 | **17** |
| MOD01 | 36 張 | 26 | 7 |
| KIRO02 | 39 張 | 44 | 1 |
| KIRO05 | 22 張 | 24 | 0 |
| MOD03 | 50 張 | 見獨立分析 | — |

> ⚠️ **Keynote 那節請當作殘缺品讀**：錄音從 10:33 才開始（前 33 分鐘沒錄到），現場只拍了 2 張投影片。大量產品名無從查證，全部進了待查核。**寧可少寫，不要寫錯。**

---

## 重點摘要

1. **AI 生產力悖論是今年的起手式**。MOD01 用 METR 的 RCT 研究（16 位開發者、246 個任務）打臉體感：**AI 讓資深開發者慢了 19%**，而所有人賽前都預測會快 20-40%。論點是：Coding 只是 SDLC 的一小段，不改流程，省下的時間會被其他環節吃回去。
2. **Kiro 是今年 AWS 推的主線**，兩場（KIRO02 方法論 + KIRO05 實作）都在講同一件事：把 AI 從「憑感覺」推上「可控、可追溯的工程交付」。三層心智模型 **Prompt → Context → Harness**。
3. **MOD03 是唯一一場「真的做出來了」的**：BitoGroup 在 EKS 上蓋多租戶 AI Agent 平台，受金管會監管、資料不能外流。**這場另有[獨立深度分析](MOD03-深度分析-多租戶AI平台.md)**。
4. **一個貫穿全天的張力**：所有場次都在講「怎麼讓 AI 可控」，沒有一場在講模型能力。今年的主題是**治理**，不是 AI。

---

---

## 10:00–11:00 KEY001: Day 1 大會主題演講  ｜ 📍 3F 大會堂

**角度**：定調 — 今年主軸

> ⚠️ **錄音從約 10:33 才開始**（前 33 分鐘沒錄到），且現場只拍了 2 張投影片。本節涵蓋範圍不完整。開場（大會主軸破題、講者介紹等）內容完全缺失。

### 一句話

AWS 這場 Keynote 的主軸是「把原本為人類設計的環境,改造成為 Agent 打造的環境」——透過安全（AWS Continuum）、代理執行基礎設施（Bedrock AgentCore）、記憶與知識層（新發表的 AWS Context）三個支柱,協助客戶（如客戶案例中的 AI-DLC 轉型公司、以及 OpenAI Codex 的委派模式）在企業裡持續累積 AI 帶來的「動能」（momentum）。

### 新產品發表

- ✅ **001｜AWS Context**（NEW, COMING SOON）
  投影片完整文字見下方「投影片抄錄」。要點：context intelligence for all your data and agents at scale；self-learning knowledge graph；Iceberg-native metadata；shared agent skills；structured and unstructured data；整合 Glue Data Catalog 與 SageMaker Unified Studio。
  逐字稿中對應段落（14:xx–19:xx 附近）講者多次講到「AWC」「打造知識座鋪」「用 Iceberg 格式來去儲存」等,語音上聽起來像是把 **AWS Context** 講成「AWC」。⚠️ 這段逐字稿內把產品名聽成「AWC」出現兩次（見待查核表 #7、#8）,其中一次疑似其實是在講別的主體（下一位來賓）,而非這個產品本身,已分開列入待查核。

- ✅ **002｜Codex expands what AWS customers can delegate**（OpenAI）
  投影片完整文字見下方「投影片抄錄」。左欄 Software teams：plan, build, review and deploy／modernize applications and infrastructure／run long-lived, parallel workflows。右欄 Knowledge workers：analyze data and build spreadsheets／create presentations, documents and research／coordinate projects and everyday work。投影片下方還有一行藍字（疑似 tagline）連同中文字幕疊在一起,翻拍角度導致**模糊到無法可靠抄錄**,故不列入逐字抄錄,僅列入待查核。

- 🎤 **AWS Continuum**（僅口述,投影片無）— 講者描述為「一個全面的產品組合,可以保護工作負載」的安全 Agent 產品家族。去年 12 月已推出 PenTesting、Code Review 作為 AWS Security Agent 的一部分,現在歸入 Continuum 家族。這次新增：
  - 「威脅建模」（threat modeling）能力：從編碼 Agent 直接產生威脅模型,映射到應用程式架構、原始碼與設計文件,對應 6 個 STRIDE 類別（逐字稿聽成「Stripe 類別」,⚠️ 待查核,STRIDE 是威脅建模常見框架名稱,但此處為聽譯推測,未經投影片證實,不採用,原樣列入待查核）。
  - 一個「針對○○漏洞的 Continuum」子產品：逐字稿聽成「城市馬漏洞」,明顯是聽譯錯誤,完全無法辨識原名 → ⚠️ 待查核。功能描述：擷取現有積壓/待辦清單,自動掃描環境找出漏洞與關鍵攻擊路徑,用某種評分機制排序、驗證漏洞（含誤判判斷）,並主動提出緩解措施；有「學習模式」與「Enforcement 強制模式」（可自動修復）兩階段。

- 🎤 **Amazon Bedrock AgentCore**（逐字稿聽成「Amazon Backrock Agent Core」,⚠️ 待查核）— 描述為讓 Agent 在生產環境「大規模、安全地建置、連接、優化」的平台,提供內建對話記憶、工具/API 與資料來源的安全認證,宣稱適用任何框架與模型。舉例客戶：Axel（⚠️ 客戶名存疑）生產力提升 3–5 倍；PGA 賽事報導快 10 倍；Workday 每月為客戶減少 100 小時財務規劃工時。
  - 其中一個子元件逐字稿聽成「Agent Core Hardness」(⚠️ 待查核,可能是 "harness" 但未經投影片證實) — 描述為用 3 個 API 呼叫、幾分鐘內啟動 Agent,運作在隔離的 Micro VM 環境,與 Agent 邏輯解耦(可換模型不用改邏輯)。
  - 另一個子元件逐字稿聽成「Mirror 背景」(⚠️ 待查核,懷疑是 "Memory"，但未經投影片證實) — 描述為讓 Agent 的決策隨使用次數變好（例：第 14 次決策比第一次好），靠累積的背景資訊達成。

- 🎤 **網路搜尋 grounding**：可讓 Amazon 內部 Agent 產品「Quick」「Kiro」「Alexa Plus」使用即時網路搜尋資訊,且原生運作在 AWS 環境內。⚠️「Quick」疑似為 Amazon Q 的聽譯錯誤,但未經投影片證實,待查核。Kiro、Alexa+ 為既有公開產品名,聽譯合理性較高。

- 🎤 **管理型知識庫（Managed Knowledge Base）**：逐字稿聽成「Answer BlackRock 的這個管理的知識庫」(⚠️ 待查核,疑似仍是 Amazon Bedrock Knowledge Bases 的新功能，但名稱不確定) — 宣稱可跨知識庫查詢、串連不同文件間相關概念做 re-ranking，而非只做向量最近匹配；並提到已有客戶（含 OpenAI）在用。

- 🎤 **GPT 模型於 Amazon Bedrock 上架**（OpenAI 講者提及）：2025 年 8 月起 GPT 模型已上架 Amazon Bedrock 與 SageMaker JumpStart；2025 年 11 月簽署多年技術架構協議；提到「GPT 5.4、5.5」及「最新的 5.6」模型現於 Bedrock 上可用。⚠️ **這些版本號一律待查核**（逐字稿一度聽成「GBD 5.3 還有 5.4」，另一段清楚聽到「GPT 5.4 還有 5.5」與「5.6」，數字前後不完全一致，且完全無投影片佐證）。5.6 模型下還提到兩個聽起來像代號的詞「Solitaire」「Luna」,⚠️ 高度存疑,不確定是模型代號還是聽譯錯誤。

### 客戶案例

逐字稿開頭（錄音起點,約對應原始 keynote 中段）即是一段客戶上台分享 **AI-DLC 導入歷程**,判斷屬於本場 Keynote 內容（由主持人在此之前介紹該公司代表上台,分享結束後主持人接續感謝並銜接安全主題）。

- 講者/公司名稱**聽譯不一致,待查核**：逐字稿一開始稱該公司代表為「金剛晃先生」，公司名為「ASKO」，經營「企業用電商平台 ASKO」及「個人用電商網站 ROHAGO」；但演講結束後主持人道謝時稱呼「吉岡先生」——前後人名不一致，⚠️ 全部待查核，不確定是同一人的兩種聽譯還是另有其人。
- 背景：該公司核心系統自 2020 年起部署在 AWS 上。去年 10 月 19 日遭受勒索軟體（逐字稿：額數軟體，⚠️ 疑似聽譯錯誤，原文推測應為「勒索軟體」但未經投影片證實）攻擊，一個月內損失 95% 營收，決定「從零開始重建事業與系統」，而非恢復原狀，改用 **AI-DLC**（AI 導入生命週期，逐字稿稱為 AI DLC：不只是把 AI 用在創造價值的改革工作上，而是從發現問題到最終決策的整個過程都善用 AI）。
- 導入方式：先透過**集訓（bootcamp）**，從小主題開始（例如 Mail Magazine 效率化），累積 AI-DLC 的成功體驗；接著讓業務端與工程師一起累積成功經驗，有把握後才挑戰更大的轉型。
- 案例一：電商平台商品快速上架 — 過去商品負責人要花大量時間跨工具協調溝通，導入 AI-DLC 整合業務流程後，開發時間減半、商品上架速度快一倍。做法是業務人員與工程師盯著同一螢幕，當場對 AI 提出反饋，減少等待與返工。
- 案例二：因應輕油（原油？⚠️ 存疑，逐字稿為「輕油危機」）供應不穩，用一個逐字稿稱為「**Keyroll**」的工具（⚠️ 待查核，聽譯不確定是否為既有產品 Kiro 或其他名稱）在短時間內完成需求預測與備料策略，決策流程從過去「兩週」縮短為「三小時」，最終順利拿到日本政府「醫療手套」（逐字稿：非有醫療手套，⚠️ 詞義不明，待查核）的獨家銷售權。
- 該公司總結 AI-DLC 成功的四個關鍵：
  1. 目標一致、下定決心（含決定淘汰長年使用的舊系統）
  2. 業務端與工程師站在同一陣線推動
  3. 把決策/執行權限下放給第一線（加快速度）
  4. 建立讓大家安心運用 AI 的環境（含安全性與相關投資）

### 值得帶走的

1. 本場 Keynote 的敘事骨幹是「幫 Agent 打造這個世界」：安全（Continuum）、代理執行基礎設施（Bedrock AgentCore）、記憶與知識層（新發表的 AWS Context）三層堆疊。
2. AWS Context（新發表，COMING SOON）主打用 Iceberg 格式統一儲存結構化/非結構化資料，做成 self-learning knowledge graph，並整合 Glue Data Catalog、SageMaker Unified Studio。
3. OpenAI 用 Codex 說明「委派」（delegation）概念的三階段演進：自動完成 → 與工程師協作 → 委派整批工作（原本估一週的工作，數小時或數分鐘內完成）；OpenAI 宣稱內部 100% 員工在用 Codex，PR 完成量翻倍。
4. 客戶案例（公司名待查核）示範 AI-DLC 落地路徑：先用小主題集訓建立信心，再挑戰大型轉型（商品上架、危機下的供應決策），並強調業務與工程「同一畫面」即時協作是關鍵做法之一。
5. Amazon Bedrock（逐字稿聽成 Backrock，待查核拼寫）第一季處理的 token 量已超越過去所有年度總和，反映 agentic 工作負載規模正快速擴張。

### ❓ 待查核

| # | 逐字稿位置 | 逐字稿原文 | 存疑原因 | 備註 |
|---|---|---|---|---|
| 1 | 00:12 | 「ASKO公司」「ROHAGO」 | 客戶公司/產品名，僅口述，無投影片 | 兩個名稱都可能是聽譯結果，需查原名 |
| 2 | 00:12 / 09:09 | 講者名「金剛晃先生」 vs 「吉岡先生」 | 同一場分享，主持人開場與結尾對講者的稱呼不一致 | 疑似聽譯前後不一致，需確認正確人名 |
| 3 | 01:29 | 「額數軟體的攻擊」 | 疑似「勒索軟體」的聽譯錯誤 | 未經投影片證實 |
| 4 | 02:20 | 「AI DLC」 | 任務說明已預期此詞，惟具體全名/官方寫法（AI-DLC？）未經投影片證實 | 沿用逐字稿寫法 |
| 5 | 06:13 / 06:28 / 06:56 / 07:16 | 「Keyroll」 | 反覆出現的工具/服務名，聽起來高度可疑，也可能與後段提到的「Kiro」同源被聽錯 | 完全無法確認，僅口述 |
| 6 | 06:33 | 「輕油危機」 | 語意不明確（原油？輕油？） | 僅口述，無法查證 |
| 7 | 07:38 | 「非有醫療手套」 | 語意不明，疑似品項/品牌名聽譯錯誤 | 僅口述 |
| 8 | 10:00 起多處 | 「AWS Continuum」 | 整個安全 Agent 產品家族名稱，僅口述反覆出現多次，無投影片佐證 | 出現頻率高、一致性高，但仍屬待查核等級 |
| 9 | 11:14 | 「6個Stripe類別」 | 疑似為資安領域常見框架名稱的聽譯錯誤 | 僅口述，不採用推測名稱 |
| 10 | 11:44 | 「針對城市馬漏洞的Continuum」 | 「城市馬漏洞」明顯聽譯錯誤，完全無法辨識原名 | 僅口述 |
| 11 | 13:38 | 「Amazon Backrock Agent Core」 | 疑似「Amazon Bedrock AgentCore」的聽譯錯誤，但未經投影片證實 | 之後（32:24 等）多次出現「Amazon Badrock」拼法亦不一致 |
| 12 | 15:14 | 「Agent Core Hardness」 | 疑似「harness」的聽譯，但未經投影片證實 | 僅口述 |
| 13 | 16:02 | 「Mirror 背景」 | 疑似「Memory」的聽譯，但未經投影片證實 | 僅口述 |
| 14 | 17:57 / 18:59 | 「Quick」 | 疑似「Amazon Q」的聽譯，但未經投影片證實 | Kiro、Alexa Plus 同段提及，相對可信 |
| 15 | 18:55 | 「城市馬」重複出現位置確認 | 同 #10，另一段亦有類似聽譯困難字詞 | 待與 #10 合併查核 |
| 16 | 19:47 | 「Answer BlackRock 的這個管理的知識庫」 | 產品名稱聽譯混亂，無法確認 | 僅口述 |
| 17 | 20:09 | 「ABS就可以來去接去解析」 | 疑似「AWS」的聽譯錯誤 | 僅口述 |
| 18 | 21:09 / 21:16 | 「AWC」（打造了 AWC，Iceberg 格式儲存） | 疑似「AWS Context」的聽譯，與投影片 001 標題呼應，可信度相對較高但仍未逐字對應 | 建議標記為「疑似對應投影片 001」 |
| 19 | 22:07 | 「AWC 是如何利用 AWS 來去轉型他們的業務」（介紹下一位來賓前） | 同樣聽譯為「AWC」，但語境是介紹接下來的來賓公司，疑似另有所指（例如 OpenAI 本身），與 #18 意義不同 | 兩處「AWC」不應視為同一實體，皆待查核 |
| 20 | 22:11 | 講者「Roman Farmer」，「OpenAid Codex 企業產品主管」 | 人名與公司名（OpenAid）皆疑似聽譯錯誤 | 不採用先驗知識猜測真名，僅列出聽譯原文 |
| 21 | 23:33 / 23:45 / 24:01 / 24:05 / 24:09 | GPT 版本號「5.3」「5.4」「5.5」「5.6」 | 多處版本號前後略有出入，且完全無投影片佐證 | 版本號屬高風險項目，務必查核官方發表資料 |
| 22 | 24:12 – 24:16 | 「Solitaire 還有 Luna」 | 疑似模型代號，聽譯把握度低 | 僅口述 |
| 23 | 24:41 | 「Axel」（客戶案例） | 客戶公司名，僅口述一次 | 無法確認拼寫 |
| 24 | 投影片 002 下方藍字 tagline | （模糊，未逐字抄錄） | 照片解析度/角度問題，文字與中文字幕重疊導致無法辨識 | 建議之後補拍清晰照片 |
| 25 | 全場 | 主持人（AWS 講者）本人姓名 | 逐字稿全程未清楚報出主持人名字（僅結尾提到「Rory」一詞，34:56/37:05） | 不確定 Rory 是否為正確人名拼法 |

---

## 11:30–12:15 MOD01: AI 驅動開發生命週期（AI-DLC）  ｜ 📍 Room 201DEF

**角度**：① 讓團隊用起來 — 把 AI 納進整個開發流程

**講者**：Aaron、Joe（🎤 僅口述，投影片全程未出現講者姓名/職稱/公司 slide）
- Aaron 自稱「Airbase 專業服務團隊的顧問」🎤 ⚠️（原音有雜訊，"Airbase" 拼法存疑，很可能是 AWS Professional Services，但逐字稿與投影片都查無正確拼寫，見待查核）
- Joe 自稱「雲端駕的公司」🎤 ⚠️（whisper 聽起來像「雲端駕」，公司全名不確定，見待查核）
- 兩人多次以「我們亞馬遜」「我們在座」的口吻描述 Amazon 內部研究與實驗，故推測至少一人代表 AWS；另一人可能是合作夥伴顧問公司代表

### 一句話
AI 若只加速 Coding，省下的時間會被 SDLC 其他環節（需求釐清、測試、審查、部署等待）吃掉；AI-DLC 是把「AI 負責規劃與執行、人負責驗證」這個循環套用到 Inception→Construction→Operation 全流程與跨職能協作方式上的方法論。

### 問題：AI 生產力悖論
- ✅ 003　投影片標題「AI Software Productivity Paradox」，引用論文《Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity》，作者 Joel Becker、Nate Rush、Beth Barnes、David Rein，機構 **METR**（Model Evaluation & Threat Research）。
- ✅ 003　圖表標題：「Against Expert Forecasts and Developer Self-Reports, Early-2025 AI Slows Down Experienced Open-Source Developers」。研究方法：RCT（隨機對照試驗），**16 位開發者、完成 246 個任務**，任務來自「大型複雜專案」，這些開發者平均有 **5 年**相關經驗。
- ✅ 003　圖表 X 軸五個類別（Y 軸為「Change in time when AI allowed」，範圍 -50%～+40%）：Economics expert forecasts、ML expert forecasts、Developer forecasts during study、Developer estimates after study、**Observed result**。前四項（各方賽前預測）都落在負值區間（預期 AI 會讓開發**變快** 20~40%），只有最後「Observed result」（實際觀察結果）落在正值區間。
- ✅ 003　**投影片精確原文金句**：「We find that when developers use AI tools, they take **19% longer** than without—AI makes them slower.」— METR.org
  - 換句話說，這篇 METR 研究的結論是 AI 讓資深開發者**慢了 19%**（不是「只提升 10-15%」，而是實測結果為負成長）。
- 🎤 **講者引了兩份研究,不是一份**（逐字稿 03:42–04:05 可證,順序如下）：
  1. **研究 A**：「研究顯示,其實實務上在用 AI 做軟體開發,提升可能 maybe 只有 10% 到 15%」——AI 有幫助,但遠低於體感。**這份沒有對應投影片**,來源不明。
  2. **研究 B**：「那另外我們也有**另外一個研究**,有發現說,可能在某些 Open Source 的專案中,我們在使用 AI 的開發者...反而比沒有使用 AI 來得更長」——**這份就是投影片 003 的 METR**（19% longer）。
  > 講者用「另外一個研究」明確區隔了兩者,所以「10-15% 提升」與「19% 變慢」**不是矛盾,是兩份不同的研究**。他的論證階梯是：AI 有效但比你想的少（研究 A）→ 而且在某些情境下反而更慢（研究 B / METR）→ 所以問題不在 AI,在流程。
- 🎤 現場舉手調查（投影片無此數據）：「對 AI coding 工具滿意的舉手大概只有 10%」「六到七成的人已經在用 AI coding 工具」。
- 🎤 講者論證：問題不在 AI 沒用，而是 Coding 只是整個 SDLC 的一小部分；若需求、設計、測試、部署、跨團隊協作方式都沒有跟著改變，AI 省下的時間就會被流程其他環節吃掉——這就是「AI 軟體開發的生產力悖論」：體感變快，但 End-to-End 交付效率沒有顯著提升。

### AI 工具兩種常見用法及其問題
- ✅ 004　投影片「Approach 2: AI-Assisted」：Developers still perform the **intellectual heavy lifting** and apply AI in **narrow tasks**（圖示：Business Intent → 一排人形 icon 逐層往下分工 → Software systems，AI 只在最底層小範圍協助）。警示框：「Not delivering the AI agility promise / Manual inefficiencies / Technical debts」，金句：「**Time saved in coding is still lost in other SDLC rituals.**」
- 🎤 對應到講者 Joe 口述的「第二種情況」：資深工程師不信任 AI，100 件任務裡只挑 1-2 個小 function 給 AI 做，其餘仍手動刻，AI 帶來的效率提升沒有被體現，甚至因為要人工比對兩邊而更花時間。
- 🎤 講者 Joe 口述的「第一種情況」（Vibe Coding／全部交給 AI）：直接下一個大目標（例如「幫我做一個電商平台」），AI 會做大量臆測，寫出使用者看不懂、不敢上生產環境的程式碼，改壞了修、修了又壞，最後整包 code「慢慢不是你認識的樣子」。
  - ⚠️ **這個「Approach 1／Vibe Coding」的對應投影片未被拍到**（照片編號從 003 直接跳到 004「Approach 2」），僅有講者口述，投影片版本的完整說法待查核。

### AI-DLC 是什麼

- ✅ 006　標題頁「AI-Driven Development Lifecycle (AI-DLC)」，副標：「AI-native methodology purpose-built to align tools, roles, and ceremonies for building complex systems at scale」。
- ✅ 005　投影片「We Re-imagined the Next Agile」，說明 AI-DLC 的四階段研發歷程（對應右側圖：Ideation①→Theory②→Build③→Validate④→Production Ready）：
  1. **Developer Experiences**：Worked with developers, identifying patterns and reimagining AI-Native workflows
  2. **Theoretical Foundation**：Documented and formalized the methodology with rigorous principles and guidelines
  3. **Internal Experiments**：Built systems and conducted proof-of-concept implementations internally
  4. **Customer Validation**：Engaged customers across diverse SDLC scenarios, languages, and problem statements
- ✅ 007　投影片「The Operating Model for AI」，五步驟循環圖：**AI Creates Plan → Humans Verify the Plan → AI Refines the Plan → AI Executes the Plan → Humans Verify the Outcome**（回到起點）。這是 AI-DLC 最核心的工作模式：AI 負責規劃與執行，人負責在關鍵節點驗證。
- ✅ 008　投影片「Where time goes in SDLC？」副標「Everyone waits for everyone else」。流程圖顯示 5 個角色互相等待（都標紅色 STOP 符號）：Software Development ⇄ Operations ⇄ Database ⇄ Application Security ⇄ Quality Assurance，等待內容包括：Wait for performance test／Wait for development environment setup／Wait for new test host／Work paused waiting for new table or SQL script／Wait for database host setup／Wait for database security approval／Wait for security certificate creation／Wait for manual source code inspection／Wait for security testing to complete。
- ✅ 011　投影片「THE FULL CYCLE」：**INCEPTION 構思 → CONSTRUCTION 建構 → OPERATION 維運**（中文對照為投影片原文），下方對應：
  - Mob Elaboration：Build context on existing codes／Elaborate intent with user stories／Plan with units of work
  - Mob Construction：Domain model (component model)／Add architectural components／Generate code and test
  - CI/CD：Deploy in production with IaC／Manage Incidents – AI First／Fast Feedback to Dev
  - 底部標語：「**EACH STEP BUILDS RICHER CONTEXT FOR THE NEXT**」
- ✅ 012-014（同一張投影片重複拍攝三次）　完整九步驟「AI-Driven Development Lifecycle (AI-DLC)」流程圖：

  | 階段 | 步驟 |
  |---|---|
  | **Inception**（Mob Elaboration） | 1. Build Context on Existing Code<br>2. Elaborate Intent with User Stories<br>3. Plan with Units of Work |
  | **Construction**（Mob Construction） | 4. Domain Model (Component Model)<br>5. Generate Code & Test<br>6. Add Architectural Components<br>7. Deploy with IaC & Tests |
  | **Operation** | 8. Deploy in Production with IaC<br>9. Manage Incidents |

  右側註解：「Stages are 'Adaptive' Based on the Intent」「Each stage Builds Richer Context for the Next」。
- 🎤 講者強調：這 9 個步驟**不是每次都要跑完**——如果只是修一個 bug，可能只需要跑其中幾步；如果是全新系統，才需要全部參與。AI 會依情境自己判斷該跑哪些步驟（demo 中有實際展示，見下）。
- 🎤 AI-DLC 第一個核心概念：AI 負責規劃與執行（Plan & Execute），人負責驗證（Verify）；不會讓 AI 直接開始寫程式，而是先出 Plan，人 review、給 feedback，AI 修正 Plan，人再確認，才開始執行，最後人再驗證最終產出是否符合最初業務目標。
- 🎤 講者提到現場調查：開發者一天花最多時間不是寫程式，而是開會與等待其他團隊（等 PM 澄清需求、等 QA 測試完、等 Security Review、等 PR Merge、等 DevOps 建好環境等），這與投影片 008「Where time goes in SDLC」完全對應。

### Mob Elaboration 與 Mob Construction

- ✅ 009　投影片「Mob Elaboration」：現場照片顯示多角色圍坐討論的教室場景；右側列出參與角色：**Operations、Developers、Business Analyst、Product Manager、QA**；並附一份示範文件截圖「Streamlining FinTech with AI: Solving Key Problem Statements」。
  - 🎤 概念說明：傳統開發流程是 PM 先整理需求→交給開發者→開發者卡住再回頭問 PM→開發到一半 QA/Ops/Infra 才介入，來回溝通耗時。AI 時代做法改為：一開始就給 AI 一個高階業務目標，AI 快速產出 User Story／拆解成可執行工作項目，把 PM、開發者、QA 等角色一開始就聚在一起，當場確認 AI 產出是否正確，過去要花好幾週才能定案的需求，現場幾小時到一天就能拍板。
- ✅ 010　投影片「Mob Construction」：現場照片顯示開放式工作區多人協作場景；右側「The 'Persona' of Future Developers」三點：
  - Moving up the value chain ("assigned tasks to code" to "**business ambitions to code**")
  - Iterating at the speed of judgement
  - Cross over outside rigid specialisations
  - 🎤 概念說明：需求確認後，過去是分派給不同開發團隊各自完成再交接；AI 時代改為建立一個小型、跨職能團隊（PM、開發者、維運專家等）一起做決策討論，AI 負責大量施作，好處不只是 coding 更快，更重要是大幅減少跨團隊等待、交接與 context switch 的時間。

### 怎麼衡量成效

- ✅ 030　章節標題投影片「How to measure effectiveness」（無其他內容）。
- ✅ 031　投影片「AI in Development - Outcomes」，蜂窩狀圖，9 項指標與說明（原文照錄）：

  | 指標 | 說明（原文） |
  |---|---|
  | Velocity | The time it takes to deliver an idea to the market |
  | Quality | App, Product or service meets the expectations of the market for usability, reliability etc. |
  | Market Responsiveness | The ability to pivot quickly to respond to ever-changing market demands |
  | Predictability | Teams maintain a predictable cadence of delivery enabling the business to make informed business decisions |
  | Innovation | New ideas, creative thoughts or novel imaginations provide better solutions to meet new requirements, unarticulated needs, or known market needs |
  | Developer Engagement | Developers are more satisfied in their work, willing to go the extra mile, passionate about the purpose of their jobs, and committed to the organization |
  | Continuous Improvement | The ability of the organization to relentlessly pursue optimization in all aspects of developer functions |
  | Customer Satisfaction | Customers are satisfied with the experience, benefits and outcomes when using the application or service |
  | Productivity | Increase the business value realized while maintaining or reducing the costs |

- ✅ 032　投影片「Measure End-to-End Delivery Timelines」，副標：「Take the same project estimated with story points and implement it end-to-end with AI-DLC to measure velocity improvement」。對照表（原文數字）：

  | | Traditional Approach | AI-DLC Approach |
  |---|---|---|
  | 專案規模 | Project Estimate: 120 Story Points | Same Project: 120 Story Points |
  | Timeline | 12 Weeks | 6 Weeks（標註「**50% Faster**」） |
  | Quality Score | Baseline | **+30% Improved** |
  | Delivery Velocity | 10 pts/week | — |
  | Duration 進度條 | Estimated Duration（滿格粉紅色） | Actual Duration（約一半，黃/青色） |

  Key Insight（原文）：「By implementing the same project with AI-DLC, you get a direct, quantifiable measure of velocity improvement.」
- 🎤 講者口述：不要拿不同專案比較，要拿「同一個」120 story point 的 Scrum 專案，比較傳統方式與 AI-DLC 方式，從需求到 production 上線的 end-to-end 時間差異；重點不是「AI 摳了多少程式碼」，而是整體交付時間與品質有沒有實質改善。
- 🎤 講者也提到：過去衡量開發效率常用「寫了幾行程式碼」「完成幾個 feature」「修了幾個 bug」，但 AI 時代這些指標不具代表性，因為 AI 能短時間內產生大量程式碼，但寫得多不代表交付價值高。

### 客戶案例：Wipro（健康醫療平台）

- ✅ 015　投影片「AI-DLC Experience」，右上角 **Wipro** 商標（⚠️ whisper 逐字稿誤植為「Witfrog」，已依投影片修正為 Wipro）。流程圖：One Problem Statement → Distributed teams → Epics → User Stories → Tech Maps →（Dev Task1/Dev Task2/Dev Task3 迴圈）→ Integrated Production-ready Product → Business Validation，底部橫幅標示「AI DRIVEN」。四個重點（原文）：
  - Enterprise HealthCare platform development for Payers with AI-DLC
  - 3 Distributed teams connected remotely
  - Production-ready completed in **20 Hours** time, leveraging domain driven design
  - Amazon Q Developer used for AI-Driven Development
- 🎤 講者口述補充：Wipro 是印度領先的軟體與顧問諮詢公司；此案例原規劃是三個跨團隊、花好幾個月才能完成的健康醫療平台建置，改用 AI-DLC 之後，每天投入 4 小時、共 5 天（=20 小時）就完成，且不只是速度變快，客戶回饋是**程式品質也變好**（因為流程中會持續釐清需求、做測試）。
- 🎤 講者提到此方法論已在歐洲、美洲、日本、韓國等地「好幾百個客戶」複製類似案例，但這部分僅口述、無投影片佐證細節。

### 現場 Demo：用 AI-DLC 幫 FastAPI 加 HTTP QUERY 功能

- ✅ 033　投影片為真實 GitHub issue 截圖：**fastapi/fastapi** repo，Issue 標題「Will FastAPI support QUERY http method? "app.query"」**#12965**，狀態 Open，由 **Kludex** 於 **Nov 20, 2024** 開出，內文提及「Discussed in #6049」（原始討論由 FilipeMarch 於 2022 年 12 月 16 日提出）。
  - ⚠️ 逐字稿中講者將此 issue 的時間說成「2020年」（"issue可能因為我們錄的時間比較少,是2020年"），但投影片清楚顯示是 **Nov 20, 2024**（即「11/20」被誤講/誤聽成「2020」）。以投影片為準。
  - ⚠️ 逐字稿中的「Face API」經投影片確認應為 **FastAPI**（Python web framework），whisper 誤植。
- ✅ 034　Demo 畫面：VS Code + **Amazon Q** 聊天面板（左側檔案樹可見 `.amazonq`、`.github`、`aidlc-docs` 等目錄）。對 Amazon Q 下達的指令原文（可見於畫面）：「Using AI-DLC, let's build support for HTTP Query method in FastAPI code base. Details of this feature request are present here https://github.com/fastapi/fastapi/issues/12965」。下方終端機顯示指令：
  ```
  mkdir -p .amazonq/rules && cp -R ../aidlc-workflows/aidlc-rules/aws-aidlc-rules .amazonq/rules/ && cp -R ../aidlc-workflows/aidlc-rules/aws-aidlc-rule-details .amazonq/rules/
  ```
  - ⚠️ 這解答了逐字稿裡反覆出現、聽不懂的「Stereo 5」「serial file」「Stereo file」——依投影片畫面判讀，講者實際指的應是把 **AI-DLC 的規則檔（aidlc-rules）複製進 `.amazonq/rules/` 目錄**，而不是字面上的「stereo」或「serial」。這是團隊預先準備好、可下載使用的 AI-DLC 工作流程/規則檔案包。
- ✅ 035-037　Demo 畫面顯示 Amazon Q 自動產出的完整分析與規劃文件（節錄）：
  - **INCEPTION PHASE**：Workspace Detection（COMPLETED）、Reverse Engineering（COMPLETED）、Requirements Analysis（COMPLETED）、User Stories（**SKIP**，理由：Simple feature addition following existing patterns, no user personas needed）、Workflow Planning（IN PROGRESS）、Application Design（**SKIP**，理由：No new components or services, adding methods to existing classes）、Units Generation（**SKIP**，理由：Single straightforward implementation unit, no decomposition needed）
  - **CONSTRUCTION PHASE**：Functional Design（SKIP）、NFR Requirements（SKIP）、NFR Design（SKIP）、Infrastructure Design（SKIP，理由皆為「不需要／沿用既有模式」）、Code Generation（**EXECUTE - ALWAYS**，理由：Implementation of query() methods in FastAPI and APIRouter classes；範圍：Add decorators, update OpenAPI generation, create comprehensive tests）
  - **Constraints**（原文）：Must maintain FastAPI's existing architecture patterns／Must follow FastAPI's code style and conventions／Must not break existing functionality／Must work with current Starlette version
  - **Success Metrics**（原文）：HTTP QUERY method available in FastAPI and APIRouter／OpenAPI documentation correctly represents QUERY endpoints／Test coverage maintained at 95%+／Zero breaking changes to existing APIs／Feature documented in user guide and tutorial
  - Amazon Q 的規劃摘要（節錄原文）：「I've created a comprehensive execution plan based on: Your request: Add HTTP QUERY method support to FastAPI...I recommend executing 2 stages...I recommend skipping 7 stages」，並附風險評估「Risk level: Low」「Impact: Additive API change (new decorators), no breaking changes」
  - 🎤 講者現場口述重點：Amazon Q 先做 workspace detection／reverse engineering，掃描既有 codebase 的架構、data flow，建立起「Semantic Context」之後，才開始問使用者需求細節（這就是投影片 007 的「Humans Verify」環節）；9 個步驟不是每次都要跑，AI 會自動判斷哪些該做、哪些可跳過，並附上跳過的理由；demo 只錄到 Construction 結束（程式碼刻完），後續 Operation／部署上線沒有現場展示。
  - 🎤 使用工具：**Visual Studio Code + Amazon Q**（畫面確認為 VS Code UI）；講者提到若使用 **Kiro** 或 **Kiro CLI**（🎤 逐字稿聽作「Kero」/「Kero CLI」，投影片未出現此字，拼法待查核）也有相同的「規則檔」可用。

### 收尾：What to do next

- ✅ 038　投影片「What to do next」，飛輪圖（中心：**Growth**），四個外圈階段依序：Executive Backing & Transformation → Improved Tools, Developer Experience → Signature Wins on Productivity → Wider Trials & Adoption → Repeatable Playbooks Guardrails →（回到 Executive Backing）。
- 🎤 講者提供兩個 QR code：(1) Skill Builder 上的 AI-DLC 課程；(2) AI-DLC workshop（brownfield，從既有程式碼開始）；並提到還有 greenfield（從零開始）版本的 workshop。
- 🎤 講者提到「規則檔」（即上述 aidlc-rules）可用 QR code 下載，餵進使用者自己的 AI 工具（VS Code+Amazon Q 或 Kiro/Kiro CLI）即可重現 demo 效果。
- 🎤 結語金句：「大家用 AI-DLC 的關鍵就是持續的去嘗試，用這個 AI-DLC，你就能體會出它的特點跟效率在哪裡。」
- 🎤 會後在三樓有 AWS 顧問攤位可提問。

### 值得帶走的
1. **AI-DLC 的核心循環**（✅ 007）：AI Creates Plan → Humans Verify the Plan → AI Refines the Plan → AI Executes the Plan → Humans Verify the Outcome——AI 負責規劃與執行，人永遠負責在關鍵節點驗證，不是全自動也不是全人工。
2. **金句**：「Time saved in coding is still lost in other SDLC rituals.」（✅ 004）——只加速 Coding 而不改變其他流程，AI 省下的時間會被流程其他環節吃掉。
3. **「小任務原則」**（✅ 016）：Stop giving complex tasks which "may" succeed；Start creating simple tasks which always succeed；持續拆解到具體的 function／file／flow 層級。
4. **金句**：「Ultimately, you own the code. Your name will be the author in the header section.」（✅ 029）——不管 AI 幫忙寫了多少，commit、code review、production 出包被 call 起來的責任永遠是開發者自己。
5. **可量化的成效衡量**（✅ 032）：同一個 120 story point 專案，傳統方式 12 週、AI-DLC 方式 6 週（快 50%），品質分數 +30% 改善——衡量重點是 end-to-end 交付時間與品質，不是「AI 寫了幾行程式碼」。

### ❓ 待查核
1. ~~METR 研究數字的矛盾~~ → **已排除,不是矛盾**。回頭聽逐字稿 03:42–04:05,講者明確說了「那另外我們也有**另外一個研究**」來區隔兩份研究：「10-15% 提升」是研究 A（無投影片,來源不明）、「反而花的時間更長」是研究 B（= 投影片 003 的 METR,19% longer）。**唯一還待查的是研究 A 的出處**——講者沒說是誰做的,投影片也沒放。
2. Aaron 自稱任職於「Airbase 專業服務團隊」——拼法/公司名存疑（逐字稿音譯），投影片全程未出現講者姓名與服務單位的介紹頁，無法核實正確全名（是否為 AWS Professional Services 或其他顧問公司）。
3. Joe 自稱任職於「雲端駕的公司」——同樣只有音譯，正確公司名稱待查核。
4. Demo 中提及的「Kero」/「Kero CLI」拼法待查核（投影片未出現此字樣，僅口述；有可能是 AWS 另一款 AI IDE 產品，但因指示要求不可用先驗知識填補，故僅記錄音譯待確認）。
5. Demo 中 GitHub issue 的確切時間：投影片顯示「Nov 20, 2024」，但講者口述「2020年」，已依投影片修正，但為何講者口誤成 2020 待查核（也可能是筆誤唸稿）。
6. 「Approach 1」（Vibe Coding／全部交給 AI 的情境）在投影片編號中並未被拍到對應頁面（照片從 003 跳到 004「Approach 2: AI-Assisted」），無法確認講者是否有專屬投影片描述這個情境，或僅口頭帶過。
7. 逐字稿中「我們還是建議會從一整個A2A的角度來看」一句意義不明（A2A 一詞在此上下文與 Agent-to-Agent 協議無關，也未見於任何投影片），可能是其他詞彙的辨識錯誤，本筆記未採用此說法。
8. 逐字稿裡提到「這個開發過程中所學到一些在深圳」（00:29 附近）語意不通，懷疑是「lessons」或其他詞被誤聽為「深圳」，本筆記未採用。

---

## 13:30–14:15 KIRO02: 以 Kiro 駕馭 AI 工程 ｜ 📍 Room 201ABC

**角度**:① 讓團隊用起來 — 團隊工程實踐

**講者**:Robert(AWS,職稱逐字稿雜訊太重無法確認,疑似「解決方案架構師」)與 Peggy(AWS,職稱逐字稿雜訊太重無法確認)。🎤 開場自我介紹整段逐字稿嚴重失真(例如講者名字前綴一堆亂碼),投影片全程沒有出現講者姓名或職稱的字卡,因此姓名以口述為準、職稱標記待查核。Robert 主講第一、二章(Prompt Engineering、Context Engineering),Peggy 主講第三章(Harness Engineering)與 Kiro / Amazon Bedrock AgentCore 實作段落(約從投影片 062 起換人)。

### 一句話
AI Engineering 是一套可被工程化、可學習的心智模型:先教會 AI「怎麼問」(Prompt Engineering),再給 AI「對的資訊、在對的時間點」(Context Engineering),最後在 AI 開始「自己動」時建好「控制系統」(Harness Engineering)——三層缺一不可,才能把 AI 應用從 Demo 帶進 Production。✅ 039、064

### 三層心智模型

投影片 064「完整的 AI Engineering 心智模型」把三層由下而上疊起來(✅ 064):

| Layer | 名稱 | 目的 | 涵蓋概念 |
|---|---|---|---|
| Layer 1 | **Prompt** | 設計明確的指令,讓 AI 聽得懂 | Structured I/O、Logic、Process |
| Layer 2 | **Context** | 動態組裝資訊,讓 AI 擁有正確知識 | RAG、MCP、Skills、Agents、Multi-agent |
| Layer 3 | **Harness** | 建構控制系統,讓 AI 能上線運行 | Orchestration、Eval、Observability、Recovery |

#### Layer 1｜Prompt Engineering — 學會「怎麼問」AI

- 定義(✅ 040):「Prompt 是一段自然語言文字,用來要求生成式 AI 執行特定任務。」(引用 aws.amazon.com/what-is/prompt-engineering)「Prompt 就是你跟 AI 溝通的方式,你怎麼問,決定了 AI 怎麼答。」範例:「台北到東京幾小時?」→「直飛大約 3.5 小時。」
- Prompt Engineering 定義(✅ 041):「引導生成式 AI 產出預期結果的過程」,是可被學習、可被工程化的過程,呈現為 Draft → Test → Evaluate → Refine 的疊代迴圈(ITERATIVE REFINEMENT LOOP)。
- 好 Prompt vs 壞 Prompt(✅ 042):好的「清晰、有結構」,可重現、可驗證;壞的「模糊、無結構」,AI 會自己補細節,結果常常是幻覺、每次不一致,無法重現也無法驗證。
- **好 Prompt 的三大要素 I-P-O**(✅ 043,講者稱為「把問問題變成工程的最小可行結構」):
  - **I / Input**(給 AI 看什麼):備齊要處理的資料、告訴 AI 背景資訊、指定角色、劃出可做/不可做的界線、附範例讓它照著走。
  - **P / Process**(要 AI 怎麼想):把思考過程拆成可驗證的步驟,訂下每步規則,分岔時給明確決策依據,不要讓它自己猜。
  - **O / Output**(讓 AI 交什麼):指定格式(表格、JSON、Markdown)、列必要欄位、設長度上限、說明風格。
  - 逐字稿口語版本(🎤,用天氣查詢舉例):「你今天去幫我查一個天氣…那我可能 Improve 會給它一個天氣網站…那我的 Process,請幫我找最近七天的…第一步可能是請先去閱讀這個資料,第二步先計算今天是哪一天然後往前推七天…」(講者用 Improve 代稱 Input,並用問路 / 教下屬做事的比喻:「你越明確去闡述,它給你的回答會更準確。」)
- **DEMO 1a 穩定度測試 — 旅平險比較**(✅ 044,逐字稿僅約略提及,實驗細節投影片獨有):
  - Unclear prompt「幫我比較一下旅平險。」跑三次:Run1 列出 3 家、Run2 列出 5 家、Run3 隨機 → 產出發散、欄位不一、難以比較。
  - Structured prompt(IPO 結構)「[Input] 比較 A/B/C 三家旅平險,10 天歐洲行。[Process] 依保額、自負額、除外條款逐條比對。[Output] Markdown 表格+推薦理由 ≤100 字。」跑三次結果一致(表格+結論),可重現、可驗證。
- **DEMO 1b 幻覺測試 — Legacy Code 分析**(✅ 045、046,細節投影片獨有,逐字稿只點到「金融客戶問 Legacy Code Modernization」):
  - One-liner「幫我看一下這段 COBOL。」→ AI 自行推測「1990s 銀行系統」、假設用 DB2(未驗證)、甚至編出不存在的 paragraph「CALC-VAT」→ AI 編造細節、發散、無法信任。
  - Structured prompt「[Input] COBOL 檔案+JCL job 設定 [Process] 1) 列 paragraph 2) 標 I/O 3) 找未用變數 [Output] JSON:{paragraphs, io, dead_vars}」→ 產出結構化 JSON,並延伸出完整的檔案清單表(檔名/大小/Transaction ID/功能定位)、主要實體與欄位定義(如 SEC-USER-DATA、CUSTOMER-RECORD 等 COBOL copybook 欄位),以及一張系統架構圖(Mermaid)→ 結構化、可驗證、可被下游程式消費。
- **Prompt Engineering 的天花板**(✅ 047):「寫得再好,也有 prompt 解不了的情況。」根因不是 prompt 寫得好不好,而是 LLM 根本沒有這些知識——公司內部文件(LLM 沒看過)、即時資訊(今天的股價、最新匯率)、新版 API(訓練截止後才發布)、個人化資料(行事曆、訂單)。圖示對比 **Pre-training corpus**(Past,training cutoff 之前)vs LLM 不知道的領域知識(Now & Beyond)。

#### Layer 2｜Context Engineering — 給 AI 對的資訊,且在對的時間點

- Context 定義(✅ 050):「LLM 在生成回應時,實際納入計算的所有 token——也就是上下文內容」,不只是 prompt,包括系統指令、檢索結果、工具回傳、歷史訊息等等。Context Window 組成:System prompt、User Prompt、Related Data、Knowledge Bases、Tool Results/MCP Output。
- Context Engineering 定義(✅ 048,引用 anthropic.com/engineering/effective-context-engineering):「為 LLM 動態組裝執行任務所需最佳資訊的系統化實踐。」不是把所有資料丟給 AI,而是動態組裝最適合當前任務的資訊——「把它想成 AI 的『工作記憶體管理』。」來源(Documents、Databases、APIs、User History、Tools/MCP)經過 Context Engine 組裝後才送進 LLM。
- **為什麼要做 Context Engineering**(✅ 049,THE COST OF DOING IT WRONG):
  - Token 爆炸:Context window 一旦塞滿,LLM 容易「忽略中間段」(lost-in-the-middle)。
  - 成本上升($$$):Token 越多,費用越高,回應越慢,每次請求都在燒錢。
  - 準確度下降:無關資訊干擾推理,反而稀釋了真正重要的訊號。
  - 引用論文 Multi-doc QA(Liu et al. 2023,arXiv:2307.03172)實測數據:文件在第 1 位時準確度 75.7%,拉到第 10 位(中間)掉到 **52.9%**,第 20 位回升到 76.0%;oracle(只給正確文件)88.3%;closed-book(完全不給文件)56.1%。「把 20 份文件全塞給 LLM,答案在中間段準確度 52.9%——比完全不給文件還差(56.1%),證明 context 不是越多越好,位置和篩選才是關鍵。」並補充:「即使是 1M context 的最新模型,lost-in-the-middle 依然存在——多篇研究指出這是 transformer attention 的結構性問題,不是塞更大 context 能解決的。」(另引 arXiv:2502.01951、2508.07479、2510.10275)
- **最直覺的做法——直接餵文件**(✅ 051,THE NAIVE APPROACH):把整份文件貼進 prompt,不用建 infra、不用寫 RAG,直覺、有效、是大多數 PoC 的起點。範例:`prompt.txt · HR-assistant`,把整份 200 頁員工手冊貼進 system prompt 回答「育嬰假怎麼申請?」BUT:第 2 份、第 10 份、第 100 份文件呢?Demo 能跑,但不具可擴展性,難以應用在 Production。
- **直覺但無法 scale**(✅ 052):手動操作(每次都要找對檔案整份貼進來)、無法擴展(100 份文件、跨系統資料怎麼辦?)、沒有時效性(文件版本一更新就過期)、**「context 沒被設計」**——「不是組裝出來的,是被『推』上去的。」→ 需要更系統化的方式管理 context。
- **系統化管理 Context 的兩個概念:MCP 與 Skill**(✅ 053,對應逐字稿「兩個技術,第一個叫 NTT,第二個叫 SEAL」——**whisper 誤聽,正確應為 MCP 與 Skill**):
  - **M / MCP**(拿到什麼資料):Model Context Protocol,一套開放標準協定,以統一介面連接資料庫、SaaS API、檔案系統,並可跨 LLM 重複使用。
  - **S / Skill**(怎麼用這些資料):寫給 AI 看的操作手冊,把「觸發條件、執行步驟、工具呼叫、輸出格式」封裝成可複用模板,由 AI 依情境動態載入。
- MCP 細節(✅ 054,引用 aws.amazon.com/blogs/machine-learning):「MCP 是一套開放標準,讓 AI 以統一語言與外部資料源、工具與服務溝通。」「不用重複為每個資料源客製化寫 Connector,一次寫好 MCP server,所有 LLM 都能用。」圖示:LLM(Client)透過 MCP(Open Standard: Resources/Tools/Prompts)連到 Database、SaaS API、Filesystem、Internal Tools。
- Skill 細節(✅ 055,引用 agentskills.io):「Agent Skills 是一種輕量、開放的格式,以專業知識與工作流程擴展 AI Agent 的能力。」範例程式碼 `skills/check_calendar/SKILL.md`:name: check_calendar;when: 使用者問行程相關問題;# Steps: 1. 取得使用者時區 2. 呼叫 calendar.list(today) 3. 回傳:時間+標題+地點。
- **MCP vs Skill——不是二選一,兩者互補**(✅ 056):

  | | MCP | Skill |
  |---|---|---|
  | 核心職責 | 拿到什麼資料 | 怎麼用這些資料完成任務 |
  | 技術定義 | 連接外部服務的標準協定 | 封裝任務流程的知識手冊 |
  | 適用情境 | 需要外部資料/工具 | 需要重複執行特定流程 |
  | 載入時機 | 啟動 CLI 時連線常駐可用 | 依情境動態載入 |

- 若要更多自動化(✅ 057):「把 Context、MCP、Skill——全部裝進一個 Agent,讓它自主規劃、執行、完成複雜任務。」
- Agent 定義(✅ 058,引用 aws.amazon.com/what-is/ai-agents):「Agent 是一種軟體程式,能與環境互動、蒐集資料,並運用這些資料自主執行任務,以達成預定目標。」AGENT LOOP:Input & Context → Reasoning(LLM)↔ Tool Selection ↔ Tool Execution → Response。
- **單一 Agent 無法包辦所有任務**(✅ 059):Single agent works when 範圍清楚、單一專業(單一資料源查詢、輸入輸出格式明確);Single agent breaks when 跨專業、長流程任務(同時寫程式、測試、部署),此時單一 agent 的 context 會滿、產出會發散、品質難以收斂。逐字稿補充比喻(🎤):公司裡一個很厲害的員工做出了很棒的本機 AI 工具,但沒辦法 scale 給其他 99 個員工使用,所以需要包成 agent 放上平台;複雜任務需要 multi-agent 協作(分析 agent、轉換 agent、測試 agent 等),由一個 supervisor/officer agent 指揮,「正像我們企業一樣,會有個主管指派任務給下面的 member。」
- **Context Engineering 的天花板**(✅ 060):Agent 動起來了,但同樣 context 時好時壞、手動執行成功但自動化不穩定、出錯時不知道哪一步壞了。根因:「我們只關注了『給 AI 什麼』——卻沒有設計『如何控制 AI』。」投影片示範同樣 input、同樣 context 跑三次:Run1 全部成功(plan/retrieve docs/call tool/final answer 皆✓);Run2 部分成功(tool timeout、answer incomplete);Run3 失敗(wrong doc retrieved、hallucinated answer、no trace 無法 debug)。「同樣的 input,同樣的 context——結果卻大不同,證明 context engineering 無法解決的問題。」

#### Layer 3｜Harness Engineering — 當 AI 開始「自己動」,需要控制 AI 的方向

> ⚠️ 投影片 061–064(從「What's Next」到「三層心智模型」)在逐字稿中完全找不到對應內容——逐字稿時間戳記從 24:02 跳到 29:43,中間約 5.5 分鐘沒有被轉錄到(疑似換講者交接 + 這幾張定義投影片的講解)。以下皆為 ✅ 投影片內容,逐字稿無對應口述。

- What's Next(✅ 061):「從『給對的資訊』,到『建好控制系統』。」→ Chapter 3: Harness Engineering。
- **Harness Engineering 定義**(✅ 062,引用 martinfowler.com/articles/harness-engineering.html):「Harness 如今已成為業界通稱,泛指 AI Agent 中除模型以外的所有組件——一句話概括:**Agent = Model + Harness**。」「Prompt 教 AI 怎麼說。Context 給 AI 看什麼。**Harness 決定 AI 能做什麼、做錯了怎麼辦**。」圖示(引用 langchain.com/blog/the-anatomy-of-an-agent-harness):Harness 內含 Context Injection(prompts, memory, skills, conversation)、Control(compaction, orchestration, retry loops)包圍 Model(reasons + decides),Model 再連出去做 Action(calls tools/MCPs)、Persist(filesystem, git, progress files)、Observe & Verify(browser screenshots, test results, logs)。
- **為什麼叫「Harness」**(✅ 063):「Harness(馬具),用來駕馭強大、但無法完全預測的動物。」「如同 LLM 能力強大,但需要一套控制系統才能穩定駕馭方向。」「LLM 本質上具備不確定性,因此在 Production 環境時,我們需要圍繞它來建立控制系統。」圖示為同心圓:最外層 User harness(使用者針對自己系統設置的 feedforward/feedback 控制)、中層是 coding agent 建造者建的 harness(system prompt、code search tools、orchestration 等,例如 Claude Code)、最內層是 Model。
- **Harness 的六大核心**(✅ 065),對應 Anthropic 的 **Planner → Generator → Evaluator** 三階段 loop(持續迭代):
  - **Planner**(規劃流程):① Prompt & Context(上下文工程)、② Tools System(工具系統)
  - **Generator**(執行產出):③ Orchestration(執行編排)、④ State & Memory(狀態與記憶)
  - **Evaluator**(檢驗結果):⑤ Observability(可觀測性)、⑥ Verify & Recover(驗證與恢復)
  - 逐字稿此段(🎤,約 29:43 起,把「Harness」聽成「Hot」)大致對應:「Planner 階段告訴 AI 你能做什麼、什麼能用;Generator 階段真的動手去做,會有錯誤處理機制;Evaluator 階段評估產出,不理想就打回 Planner 重新規劃——本質上是一個不斷迭代、直到越來越確定產出的過程。」

**六大 Pillar 逐一展開**(皆 ✅ 投影片,逐字稿內容較簡略籠統,已標註對應口述重點):

1. **Pillar 01・Prompt & Context —— 上下文工程,給 AI 看對的資訊**(✅ 066):System Prompt(定義角色、邊界、I/O)、Knowledge Bases(給予正確的文件與資料)、Conversation History(對話歷史資料)。「提供 LLM 正確的資訊,並讓它在可控的邊界內思考。」
2. **Pillar 02・Tools System —— 工具系統,讓 AI 能存取外部的能力**(✅ 067):Tools(調用 API、Web search)、MCPs(存取內外部資料源)、Skills(動態載入正確知識)。圖示 Agent Gateway Routing:Agent 透過 MCP Client(/mcp:list tools, invoke tool, search)連到 Agent Gateway,再導向 APIs/tools/resources。
3. **Pillar 03・Orchestration —— 執行編排,規劃 AI 每一步該做什麼**(✅ 068):Flow control(任務流程順序與分支條件)、Retry(錯誤重試與中斷條件)、Human-in-the-loop(高風險動作需要人類核准)。範例流程:Request → LLM(retry 3x)→ Circuit breaker(trip after 5 fails)→ Human review。
4. **Pillar 04・Memory & Status —— 狀態與記憶,讓 AI 記得發生過什麼**(✅ 069):Short-term memory(目前任務的資訊與狀態)、Long-term memory(跨任務的資訊與狀態)、Execution Status(任務執行進度與資料)。Memory Flow:Agent Implementation(Events、Agent State)同步到 Agent Memory(Short-term: Chat Messages/Session State;Long-term: Semantic/User Preferences/Summary),再非同步送進 Automatic Memory Extraction Module。
5. **Pillar 05・Observability —— 可觀測性,讓 AI 任務可追蹤除錯與監控**(✅ 070):Sessions(任務完整上下文脈絡)、Traces(單次 request-response 執行路徑)、Spans(每個 operation 的起訖與狀態)、Metrics(監控指標)、Logs(執行日誌)。
6. **Pillar 6・Verify & Recover —— 驗證與恢復,確保 AI 產出可信任、失敗可恢復**(✅ 071/072):Verification(以單元、整合測試驗證正確性)、Evaluation(以 **LLM-as-a-Judge** 評分 agent 品質)、Recovery(自動重試、回滾與跳脫機制)。Evaluation Flow:Agent → Agent Evaluations(呼叫 LLM judge 逐項評分、寫下含 judge 解釋的結果)→ Agent Observability。

### Skill/MCP 機制回顧、Planner-Generator-Evaluator、Amazon Bedrock AgentCore

- **How to implement a Harness Agent**(✅ 073):「用 Kiro 開發 Agent,部署到 Amazon Bedrock AgentCore。」
- **Build with Kiro**(✅ 074,逐字稿幾乎無對應口述,疑似落在 24:02–29:43 的轉錄空白區):Kiro 重構整個軟體開發生命週期(SDLC)的體驗,協助開發人員與 IT 專業人員建置並管理安全、可擴展、高度可用的應用程式;基於 Code OSS,相容 VS Code 設定與外掛;IDE、CLI、Web 三種使用介面;**Pricing:Pro Tier $20/月/人**。六大功能:
  - **Spec-Driven 開發**:一句 prompt 生成 requirements/design/tasks,結構化交付複雜功能。
  - **Steering 標案**:團隊標準與專案知識直接注入 `.kiro/steering`,跨 session 持久生效。
  - **Agent Hooks**:事件驅動自動化——存檔即測試、更新文件、提交前安全掃描。
  - **Autopilot/Supervised**:自主執行或逐步監督,依任務風險自由切換。
  - **MCP 整合**:以開放協定連接外部工具與資料源,擴充 agent 能力。
  - **Agentic Chat**:對話式完成臨時任務,支援 file/URL/docs 上下文。
- **Amazon Bedrock AgentCore**(✅ 075):「能使用任何框架和模型,安全且大規模地部署和運行高效能的代理平台。」五大模組:Runtime & identity(專為 AI Agent 設計的安全、無伺服器運行環境,內建獨立身分管理)、Memory(支援短期與長期記憶,簡化上下文管理)、Gateway(將 API、Lambda 及服務快速轉換成 Agent 工具,統一入口並強化安全連接)、Tools(快速接入各類企業工具與外部服務)、Observability(提供 Agent 行為與性能即時追蹤,可視覺化監控與除錯)。
- **AgentCore Architecture**(✅ 076,"Any model, any agent framework"):App / Any model → AgentCore Runtime(內含 Any framework、Agent instructions、Agent local tools、Agent context)↔ AgentCore Policy、AgentCore Gateway、AgentCore Browser、AgentCore Code Interpreter、AgentCore Identity ↔ AgentCore Memory、AgentCore Observability、AgentCore Evaluations。
- **Roadmap 總結圖**(✅ 077):三段旅程 01 Prompt Engineering(學會「怎麼問」)→ 02 Context Engineering(對的資訊、對的時間點)→ 03 Harness Engineering(建立控制系統);Harness 六環(Prompt & Context → Tools System → Orchestration → State & Memory → Observability → Verify & Recover,循環)置中標「AWS HARNESS」;實作路徑 Kiro(開發 Harness Agent)→ Amazon Bedrock AgentCore(安全、可擴展地部署與運行);底部標註 **Planner → Generator → Evaluator**。

### 值得帶走的

1. **「Prompt 就是你跟 AI 溝通的方式,你怎麼問,決定了 AI 怎麼答。」**(✅ 040)——把 Prompt Engineering 從玄學拉回「輸入決定輸出」的工程思維。
2. **Context 沒被設計,是被『推』上去的。**(✅ 052)——一句話點出多數 PoC 卡在 Production 的真正原因:文件複製貼上能 demo,但不是系統化組裝。
3. **lost-in-the-middle 的具體數字**:把 20 份文件塞給 LLM,答案在中間段準確度只有 52.9%,比完全不給文件的 56.1% 還差(✅ 049,Liu et al. 2023)。「不是塞更多 context 就更好」——連 1M token 的最新模型都逃不掉這個結構性問題。
4. **Harness 的馬具比喻**:LLM 像一隻強大但無法完全預測的動物,Harness 就是駕馭牠、決定方向的那套控制系統——「Agent = Model + Harness」(✅ 062、063,引用 Martin Fowler)。
5. **MCP 負責「拿到什麼資料」,Skill 負責「怎麼用這些資料」,兩者不是二選一,是互補。**(✅ 053、056)

### ❓ 待查核

| 項目 | 為什麼存疑 |
|---|---|
| 兩位講者的正確職稱/全名 | 開場自我介紹整段逐字稿嚴重失真(例如出現「以及Peggy師 Brutal Timing SA&AWS」這種無法解讀的字串),投影片全程沒有講者字卡可對照,僅能確認名字是 Robert 與 Peggy。 |
| 「SARS 的工具/服務」(逐字稿約 17:19)| 疑似「SaaS」的口誤,投影片 054 有出現「SaaS API」可間接佐證,但無直接證據證實逐字稿原意就是 SaaS。 |
| 「biosystem」(逐字稿約 17:56、19:38)| 詞義不明,可能是「ecosystem」或其他字的誤聽,找不到對應投影片佐證,未採用任何猜測寫入正文。 |
| 「Facebook、Facebook 5、Opera」「FAPOR 5」等模型名稱(逐字稿約 9:59–15:47)| 疑似前沿 LLM 模型名稱的誤聽(可能指其他廠牌模型),但沒有任何投影片列出這些名稱或拼法,無法確認正確寫法,故未收入正文。 |
| 「我們要做給大家 AXE」(逐字稿約 37:00)| Cerebras 摘要猜測是 AWS X-Ray,但找不到任何投影片提及 X-Ray 或 AXE,未採用此猜測。 |
| 「Retour 的技術」(逐字稿約 38:15、40:26)| 疑似「Recover」的誤聽(對應投影片 Pillar 6「Verify & Recover」),但發音差距較大,無法 100% 確認。 |
| 「VR.LF」「AutoZeroKey」(逐字稿約 41:33、40:26)| 意義不明,任何投影片都找不到對應詞彙,無法還原原意。 |
| 「Unrealty」(逐字稿約 37:09、38:44、38:49,原文轉錄字面如此)| 上下文疑似在講「可觀測性/透明度」,但找不到明確對應的英文原詞,未採用任何猜測寫入正文。 |
| 逐字稿 24:02–29:43 約 5.5 分鐘缺口 | 對應投影片 061(What's Next)到 064(三層心智模型)+ 換講者交接,這段完全沒有被轉錄到文字,無法確認講者實際口述內容,正文中已註記這幾張投影片為「投影片獨有」。 |
| Kiro 產品細節(定價 $20/月、Spec-Driven 等六大功能,投影片 074)| 逐字稿中幾乎沒有對應口述(落在轉錄空白或接近結尾處),內容完全依賴投影片畫面文字判讀,細節正確性建議之後對照官方 Kiro 文件二次確認。 |

---

## 14:30–15:00 KIRO05: 從 Vibe Coding 到 Spec-Driven  ｜ 📍 Room 201ABC

**角度**：① 讓團隊用起來 — 標準化 AI 開發

**講者**：詹東（Jack）。🎤 逐字稿自述：15 年 Embedded（硬體/韌體/Linux driver）背景出身，之後做過 Frontend、Backend，目前在 AWS 任職近 8 年；去年剛從上海（中國大陸）調回。（逐字稿把「Embedded」聽成「Invaded」，已依常識校正，但姓名「詹東」拼字未經投影片確認，見待查核）

### 一句話

Kiro 用 Steering（專案憲法）＋ Spec（需求→設計→任務三階段）＋ Hooks（事件自動化）＋ MCP（外部工具協定）＋ Powers（打包分享）五個概念，把 AI 寫程式從「憑感覺」的 Vibe Coding 推進成「有章法的工程交付」的 Spec-Driven development。✅ 080

### Vibe Coding 的局限

✅ 079（投影片標題：「AI 寫程式的現實」）：
- AI 編碼工具在小型任務表現出色，但在複雜專案中容易失控
- 開發者花在修正 AI 輸出的時間，和從頭寫一樣多
- Vibe Coding（氛圍編程）適合原型，但缺乏規範
- 可預測性低、追溯性差、品質不穩定
- 現有工具無法提供直觀的方法來驗證 AI 生成的程式碼是否符合開發者的品質標準

🎤 講者個人鋪陳（逐字稿）：他強調自己是 Embedded 出身，後來做過 Frontend、Backend，現在在雲端，這些 domain know-how 他已經很紮實；但他舉例說如果用 Vibe coding 去做一個遊戲，對他而言遊戲業是「非常陌生的知識盲區」——Vibe coding 會先幫你「預設好一個立場」快速生出程式碼，但往往跟真正要達到的目的差很遠，於是陷入反覆 debug 的痛苦循環，而且沒有直觀方法檢查 AI 生成的程式碼是否符合品質需求。

🎤 AWS 內部政策/統計（逐字稿，投影片未提及，數字待查核）：AWS 內部並未禁止員工使用外部 AI 工具（如 CodyCorp、Copilot、Codex），但據講者引述內部統計，AWS 國外的架構師中有 85% 以上仍直接使用 Kiro 做開發與 architecture 規劃。

### Vibe Coding vs Spec-Driven

✅ 082（完整對照表）：

| 維度 | Vibe Coding 🎵 | Spec-Driven 📋 |
|---|---|---|
| 規劃方式 | 自然語言 Prompt | 三階段結構化 Spec |
| 可預測性 | ★★☆☆☆ 低 | ★★★★★ 高 |
| 適用場景 | 原型、學習、快速驗證 | 生產級專案、團隊協作 |
| 追溯性 | 僅對話歷史 | Req → Design → Code 全鏈路 |
| 重構難度 | 高－缺少上下文 | 低－有 Spec 指導 |

🎤 講者補充：Vibe coding 給模型的是一個模糊（fuzzy）的 topic，模型靠上網搜尋、既有知識或外接知識庫去推論產出；Spec-Driven 雖然起點一樣是 Prompt，但會拆成三階段結構（需求分析 → 產生 task list → 執行，並附帶 self-test / self-debug），可預測性因此較高。

### Kiro 的核心概念：Steering / Spec / Hooks / MCP / Powers

Kiro 是一款「原生整合 AI Agent 能力的開發工具平台」，核心差異是「不是無狀態的問答工具，而是有專案上下文記憶的開發夥伴」；有三種介面：Kiro IDE（原生整合 Agentic AI 能力的桌面 IDE，可裝在 Windows/Linux/Mac）、Kiro CLI（在 Terminal 中運行的 Agent）、Kiro Autonomous Agent（在雲端沙箱環境中獨立執行，本場「今天不會介紹」）。✅ 080, 081

**Steering — 專案的「憲法」** ✅ 094
- 為 AI Agent 提供專案上下文的持久化文檔
- 路徑：`.kiro/steering/*.md`
- Agent 每次操作前自動讀取
- 定義程式碼規範、技術棧、架構約束
- 支援多文件分層（product / tech / style）
- 類比：給新同事的 Onboarding Doc
- 效果：Agent 不再「亂寫」，每次生成的程式碼都符合團隊規範

奶茶店比喻（✅ 097/098）：Steering = 員工手冊。開店前一定會先寫一本員工手冊：「我們只用鮮奶，不用植脂末」「所有杯子統一 700ml」「糖度選項：全糖/七分/半糖/三分/無糖」「員工必須在 5 秒內回應顧客」。→ Steering 就是告訴 AI Agent：在這個專案裡，你的行為準則是什麼；Agent 每次幹活前都會先翻這本手冊。

**Spec — 需求 → 設計 → 任務三階段** ✅ 092, 093
- 將一句話需求拆成「需求→設計→任務」三步，每步都有驗收標準
- ① Requirements（**EARS** 格式）：`"When <觸發>, the system shall <行為>"` → 結構化需求，避免模糊描述
  - （逐字稿把 EARS 聽成「ERR」「ERR2」「所謂的 Requirement Link」，已依投影片 085/092 校正）
- ② Design → 自動生成技術方案、數據模型、API 設計 → 人工 Review 確認後推進
- ③ Tasks → 拆解為可執行任務列表 → Agent 逐條實現，每次只處理一個 Task

**Hooks — 事件觸發自動化** ✅ 095
- 基於事件觸發的自動化指令，「如果…就自動…」— IDE 裡的智慧自動化
- File Save → 自動跑測試
- File Create → 自動生成模板程式碼
- Spec Task 完成 → 自動觸發下一步
- Agent Stop → 自動化品質審查
- 實際範例：保存 .ts 文件 → Hook 自動跑 vitest → 失敗則 Agent 自動修復

**MCP（Model Context Protocol）— 連接外部世界** ✅ 096
- Agent 連接外部工具的標準協議
- GitHub / DB / Slack / Terraform / 內部系統
- 類比：萬能充電線（USB Hub，接上就多一個功能）

**Powers — 打包分享** ✅ 096
- 將 Steering + Hooks + MCP 打包為可分享的能力包
- 一鍵安裝，團隊統一規範
- ISV 生態：社群共享最佳實踐
- 類比：加盟包——別人安裝就能直接開店
- 投影片圖示內容：「A Kiro power may contain：MCP servers for access；Steering files for context；Hooks for actions」

奶茶店比喻延伸（🎤 逐字稿，無對應獨立投影片截圖）：Hooks 例如每做完一杯自動貼標籤、每天關店自動盤點物料、上架新品自動同步到 Uber Eats／美團、原料快用完自動觸發採購單。Power 例如「我開了一家 Coco，配方/電規/員工訓練/供應商全部打包起來，你付我錢我就把這整套 SOP 給你」。

**Skill 與 Power 的差異**（🎤 僅逐字稿，投影片無此對照）：講者澄清 Skill 是比較單一（例如一個配方做法），且可以**跨平台**傳遞（例如從 Cloud Code 流到 Kiro）；Power 則是 **Kiro 專屬**打包，適合整個團隊/SOP 規模的擴散，且規定用 Kiro 才能打開統統包。

### Demo 實錄

🎤 講者說明：這段 demo 是他先前派駐上海期間、給大陸客戶體驗用的錄影（非本場現場即時操作），使用簡體介面。示範專案是用 Figma 設計稿 spec-driven 產生一個 Landing Page。

- ✅ 083 題卡（簡體）：「使用 Spec-driven development 生成一个落地页」
- ✅ 084 啟動 Prompt（終端機畫面，模型選 Claude Sonnet 4.0，Autopilot 模式）：
  > 根据 Figma 的设计生成一个 Landing Page，要求如下：
  > - 支持响应式布局
  > - 生成的代码样式与 Figma 中的设计保持一致
  > - Figma 设计中包含图片，你通过 Figma MCP 自行下载
  > - 不要生成子页面的代码
  > - 在和我交流的过程中使用中文
  > - Figma Frame Link: https://www.figma.com/design/...
  （逐字稿把「Figma」聽成「BigMar」、把「MCP」聽成「NTT」，已依投影片校正）

- **Step 1（✅ 085）：生成基於 EARS 語法的詳細需求描述** → 產生 `.kiro/specs/figma-landing-page/requirements.md`，畫面分頁為 Requirements / Design / Task list 三個 tab。截圖可見的內容片段：
  - 需求 1（用戶故事）：作為網站訪問者，我希望看到一個視覺吸引人的 Landing Page，以便了解產品或服務的核心價值。驗收標準：①當用戶訪問頁面時，系統應顯示完整的 Landing Page 佈局 ②當用戶在不同設備上訪問時，系統應提供響應式佈局適配 ③頁面應包含導航欄、英雄區域、特色卡片、客戶評價和頁腳等所有設計元素
  - 需求 2（用戶故事）：作為網站訪問者，我希望頁面的視覺效果與 Figma 設計完全一致，以便獲得專業的用戶體驗。驗收標準（截斷）：當頁面加載時，系統應顯示與 Figma 設計相同的顏色、字體和間距…

- ✅ 086 IDE 全景截圖：左側檔案樹可見 `.kiro > specs > figma-landing-page` 底下有 `design.md`、`requirements.md`，元件清單含 LandingPage / Navigation / Hero / FeatureCards / ContactSection / Footer；右側 Agent 對話面板顯示呼叫 `Called MCP tool: get_figma_data`、`Called MCP tool: download_figma_images`，並自動建立 requirements.md，之後「Accepted edits to design.md」。

- **Step 2（✅ 087）：根據當前項目上下文生成技術設計** → 產生 `design.md`

- ✅ 088/089 design.md 內容片段（組件與接口，### 組件層次結構）：
  - 2. Hero 組件：`interface HeroProps { title: string; subtitle: string; ctaText: string; heroImage: string; }`；設計規格：主標題 Inter 700 weight 64px 行高 1.21，副標題 Inter 400 weight 24px，圖片尺寸 1280×640px 8px 圓角，按鈕：與導航欄樣式一致
  - 3. FeatureCards 組件：職責＝特色功能卡片網格，展示產品特性；`interface FeatureCard { image: string; title: string; description: string; }`

- **Step 3／4（未見獨立過場投影片，但 ✅ 090 顯示執行中畫面）**：`.kiro/specs/figma-landing-page/tasks.md` 列出可執行任務清單，逐條含子步驟（如 1. 遷移 Navigation 組件、2. 遷移 Hero 組件、3. 遷移 FeatureCards 組件、4. 遷移 ContactSection 組件…），畫面左下角標「加速中」（表示播放加速跳過等待時間）；右側對話面板有「Start task」「Task in Progress」等狀態，Agent 逐一 by step by step 產生程式碼。

- **Step 5（✅ 091）：利用 Vibe 模式對局部進行調整** — Kiro 跑完 spec-driven 主流程後，講者展示可以再用「Vibe coding」的方式做局部微調。截圖列出的變更摘要（英文，來自 Agent 的 execution summary）：
  - 「4. Component Architecture」：Created new ContentCards component with proper styling；Added ContentCard subcomponent with image and text layout；Integrated new section into LandingPage component flow
  - 「5. Data Accuracy」：Updated all text content to match Figma design specifications；Fixed button labels（"Secondary button" instead of "Button"）；Ensured proper content hierarchy and flow
  - 畫面顯示「21 changes accepted（View all）」
  - 對話框內講者輸入類似「部份圖片未載入，請檢查原因」的回饋，交由 Agent 進一步修正

🎤 錯誤處理（僅逐字稿，無對應截圖佐證）：講者提到過程中若偵測到 standard error、native error（例如畫面渲染輸出過多），Kiro 會自動偵測並用 Auto 機制修正；生成完之後可透過對話回饋讓 Agent 再做一次深層校正。

### 整體工作流程

✅ 099（Key Takeaway 投影片）：
- **Steering → Spec → Coding → Hooks → Powers**，對應：設定規範 → 規劃任務 → 執行開發 → 自動化品質 → 分享複用
- **MCP** — 貫穿全流程的外部工具接入層
- 從專案初始化到能力分享，五大概念覆蓋完整開發生命週期

> **Key Takeaway：Kiro 不是替代開發者，而是讓開發者專注於「做什麼」，Agent 負責「怎麼做」。**

### 值得帶走的

1. Vibe Coding 與 Spec-Driven 不是二選一的對立關係：Spec-Driven 的 demo 流程本身在最後（Step 5）也會切回 Vibe 模式做局部微調——結構化流程負責大骨架，氛圍編程負責收尾細節。✅ 091
2. EARS 格式（`When <觸發>, the system shall <行為>`）把模糊的一句話需求，逼成可驗收的結構化敘述，是 Spec-Driven「可預測性高」的關鍵機制。✅ 085, 092
3. Powers 把 Steering + Hooks + MCP 打包成「加盟包」——別的團隊/分公司裝上 Kiro 就能直接複製整套 SOP，這是團隊擴散與規模化落地的核心賣點。✅ 096
4. 金句（奶茶店比喻）：「Steering 就是告訴 AI Agent：在這個專案裡，你的行為準則是什麼；Agent 每次幹活前都會先翻這本手冊。」✅ 097/098
5. Key Takeaway 金句：「Kiro 不是替代開發者，而是讓開發者專注於『做什麼』，Agent 負責『怎麼做』。」✅ 099

### 🔗 明天的對照點

給 Day 2 LT-006（連 HR 也能上手！用 Kiro 快速打造 HR 的 AI 小幫手）現場核對：

1. **有沒有真的寫 Steering？** LT-006 的 HR 團隊有沒有先建立 `.kiro/steering/*.md`（規範/技術棧/架構約束），還是直接開對話框讓 Agent 自己發揮？如果沒有，KIRO05 承諾的「Agent 不再亂寫，每次生成都符合團隊規範」在非技術背景的實作場景是否還成立？
2. **Spec 是不是真的用 EARS 格式？** LT-006 產出的 requirements.md 有沒有出現「When <觸發>, the system shall <行為>」這種結構化驗收標準？HR 這種非工程背景的使用者，是自己寫得出這種格式，還是完全由 Kiro 自動生成、人只按「接受」？
3. **有沒有用到 Hooks 或 Powers？** LT-006 只是做一個一次性的 HR 小幫手，KIRO05 強調的「事件觸發自動化」（Hooks）與「打包分享給其他分公司」（Powers）這兩個偏向團隊規模化的機制，在小型單次專案裡是否根本用不上，只有跨團隊/長期維護的專案才需要？

### ❓ 待查核

- 講者姓名逐字稿轉錄為「詹東」，自稱英文名「傑克」——中文姓名的語音轉錄常有誤，本場投影片未出現講者姓名字卡，拼字未經第二來源確認。
- 「AWS 內部 85% 以上架構師使用 Kiro」為講者口述數字，投影片無佐證，且無法確認統計範圍（全球？特定部門？）。
- 逐字稿多處出現「FiveCoding」「FeedbackHero」「Hero 會再去深層去校正我的底盤」等詞，研判是「Vibe Coding」與「Kiro」的重複誤聽/合併，對應到投影片 091「Step 5：利用 Vibe 模式對局部進行調整」的內容已可確認；但「Hero 會分解需求、設計、任務，產出最終 Copy」這句是否描述另一個獨立機制（而非單純 Vibe 微調），投影片未能證實，存疑，正文未採用。
- 逐字稿中「Cody」「CodyCorp」（講者舉例外部 AI 工具，與 Copilot、Codex 並列）——不確定是否指 Sourcegraph 的 Cody 產品或是其他工具的誤聽，投影片未提及，正文未採用此細節。
- 「Skill 可跨平台傳遞（例如 Cloud Code 與 Kiro 之間）、Power 僅限 Kiro」這段區分僅來自逐字稿口述，投影片沒有對照表佐證，建議查核是否為 Kiro 官方定義或講者個人理解。
- 「Kiro Autonomous Agent 在雲端沙箱獨立執行」的實際運作方式，講者明言「今天不會介紹」，僅投影片 081 一句話帶過，細節未展開。
- 開場「KiroControl」「那一直用眼鏡」等詞轉錄破碎、語意不通，無法還原講者原話，正文未採用、僅作為講者背景鋪陳略過。

---

## 15:15–16:00 MOD03: Multi-Tenant AI Platform on EKS（BitoGroup 案例）  ｜ 📍 Room 201DEF

**角度**：② 平台架構 ＋ ③ 治理與安全

> ⭐ **這場另有獨立深度分析**：[MOD03-深度分析-多租戶AI平台.md](MOD03-深度分析-多租戶AI平台.md)
> 涵蓋架構、四層租戶隔離、runtime 比較表（runc/gVisor/Kata 含精確數字）、10 層縱深防禦、ISO 27001 對照、成本控管四策略、以及可直接取用的 AWS sample。

**三句話版本**：BitoGroup（金管會監管的交易所，資料不能外流）不能用 AI SaaS、又追不上純自建的速度，最後站在開源 **OpenClaw** 上、用公司既有的 **Amazon EKS** 蓋了多租戶 AI Agent 平台 **BitoClaw**。設計哲學是「多租戶設計是讓團隊感覺不到邊界的存在」。**KEDA 把閒置租戶縮容到零，100 租戶省 80% 成本** —— 這是「每個團隊都有自己的 AI」在經濟上可行的關鍵。

**最值得帶走的**：
- 「選擇 Amazon EKS，不是追逐潮流，而是把團隊已經會的技能，變成平台的競爭力。」
- 隔離**不要一次拉到最高** —— 按 trust level 混用 runc / gVisor / Kata
- **Pod Identity 零金鑰架構** —— 把「金鑰保管」變成「金鑰不存在」
- **LiteLLM Proxy 一個元件吃三個需求**：供應商中立 + 成本歸屬 + 稽核

---

## 🚫 未參加：MOD04（16:15–17:00 ｜ 📍 Room 201DEF）

**AI 時代的 Kubernetes 平台：用 EKS Auto Mode 消除維運負擔**

臨時有事沒去，無錄音。

> 角度 ②（規模化維運）這塊由 MOD03 部分覆蓋 —— MOD03 的多租戶 AI 平台本身就跑在 EKS 上。缺的是 EKS Auto Mode 這個具體的維運免除機制。會後可看 AWS 有無放簡報/錄影。

---

## 🔗 來源與素材

| 素材 | 位置 |
|---|---|
| 錄音（5 檔，3.3 小時） | `VOICE/*.m4a` |
| 逐字稿（105,014 字） | `VOICE/transcripts/*.txt` |
| Cerebras 自動摘要（**待查核草稿**） | `VOICE/transcripts/*.summary.md` |
| 現場投影片（149 張，依場次歸檔） | `slides/0X_*/` |
| MOD03 深度分析 | [MOD03-深度分析-多租戶AI平台.md](MOD03-深度分析-多租戶AI平台.md) |

> **Cerebras 摘要只壓縮不查證** —— whisper 的同音字錯誤會被它一路帶進去（例如整份摘要把 Harness 寫成 Hot）。摘要僅供快速掌握結構，**不可當事實來源**。本筆記的每個事實都回頭對過投影片。
