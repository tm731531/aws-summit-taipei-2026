# 2026-07-16（四）AWS Summit Taipei 2026 — Day 2

> 場地：TICC 台北國際會議中心
> 議程來源：[我的推薦文](https://blog.tomting.com/2026/07/10/aws-summit-taipei-2026-enterprise-ai-sessions/)

**實際跑的 4 場**（跟原訂計畫不同）：

| 時間 | 場次 | 📍 | 角度 |
|------|------|-----|------|
| 10:00–11:00 | KEY002 Day 2 Keynote | 3F 大會堂 | 閉幕定調 |
| 11:30–12:15 | AIML05: 企業級 AI Agent（HOYA BIT × Bedrock AgentCore）| 3F 大會堂 | ② 平台落地 |
| 13:30–13:58 | 社群 LT：Nitro Enclaves 保護 LLM 推論 | 2F Dev Community Zone | ③ 治理與安全 |
| 13:55–14:20 | LT-006: 用 Kiro 打造 HR 的 AI 小幫手 | 2F Dev Community Zone | ① 讓團隊用起來 |

> **下午改走社群開放區（2F Developer Community Zone）**：原訂的 SEC01 / FINTECH02 / SEC03 / SEC04 都沒去，改聽 LT-006 和它前一場、同場地相接的一場社群 Lightning Talk（Nitro Enclaves）。兩場連著坐、中間不用移動——前一場講者 Ray Lin 甚至在結尾把下一位講者 RuRu 的 HR 工具當例子引出，直接把兩場串起來。

---

## 🔍 這份筆記怎麼來的、可信度如何

現場錄音（4 段共 2.4 小時）→ 本地 faster-whisper 轉錄 → 逐字稿與現場投影片逐一交叉比對。**whisper 把技術名詞聽壞很多，一律以投影片為準。**

**可信度標記（沿用 Day 1）**：

- ✅ 投影片可查證（附張數）
- 🎤 僅講者口述，投影片無
- 🔎 無投影片，但經 AWS/新聞公開資訊查證過（僅用於 Keynote，因該場沒拍投影片）
- ⚠️ 聽不清或有疑義 → 一律進各節「待查核」，**不寫進正文假裝是事實**

**可查證率跟該場拍了幾張投影片直接相關**：

| 場次 | 投影片 | ✅ 可查證 | 🎤 口述 | ⚠️ 存疑 |
|---|---|---|---|---|
| KEY002 Keynote | **0 張** | 0 | 多數 | 多 |
| AIML05 | 46 張 | ~62 | ~16 | 7 |
| 社群 LT（Nitro）| 15 張 | ~41 | ~17 | 5 |
| LT-006 | 30 張 | 見獨立文章 | — | — |

> ⚠️ **Keynote 那節請當口述紀錄讀**：現場完全沒拍投影片（第一張照片是 11:30 的 AIML05），所有產品名、數字都是從中/英/韓三語逐字稿聽出來的。幾個關鍵名詞我另用公開資訊查證（標 🔎），其餘存疑一律進待查核。

---

## 重點摘要

1. **Keynote 用三個客戶講同一句話：雲是地基、AI 是加速器、信任是決勝點。** NASDAQ（金融，把交易系統搬上 AWS、SEC 核准的 AI 訂單類型 Dynamic M-ELO）、KBS（媒體，一台 8K 攝影機用 AI 生全團直拍、世界盃即時戰術筆記）、Anthropic（Natalie Lee：Opus 4.8 能連續自主工作約 12 小時；「40% 的 agent 專案會失敗，不是模型問題，是交付問題」）。
2. **AIML05 是今年 AWS 主推的 agent 上 production 方案：Amazon Bedrock AgentCore**（9 大託管模組：Runtime/Memory/Gateway/Policy/Identity/Observability/Registry…）。HOYA BIT（台灣合規加密貨幣交易所）是「真的做出來」的案例——開發者只寫 agent 邏輯 + 一份 YAML，平台統一接管部署／工具／存取／追蹤／治理。
3. **社群 LT（Nitro Enclaves）補上「使用中資料」這塊**：資料三態裡靜態、傳輸大家都會加密，唯獨「使用中」一進記憶體就是明文、連 root/雲端管理者都看得到。機密運算用硬體隔離的 TEE + KMS 遠端驗證（attestation），只有未被竄改的程式才拿得到金鑰解密，用來保護 LLM 推論。
4. **LT-006 是角度①的收成**：非工程背景的 HR 用 Kiro 一個晚上做出內部工具。**已寫成獨立文章**（見下方連結），不在此重複。
5. **一個貫穿 Day 1+Day 2 的張力**：兩天所有場次都在講「怎麼讓 AI 可控、可信、可治理」，沒有一場在拚模型能力。AIML05（金融平台治理）、Nitro LT（機密運算）、Day 1 MOD03（BitoGroup 同樣是受金管會監管的加密貨幣平台）連成一條線——**今年的主題是治理，不是 AI。**

---

## 10:00–11:00 KEY002: Day 2 大會主題演講 ｜ 📍 3F 大會堂

**角度**：閉幕定調 — 今年主軸

> 🎤 **這節全部是講者口述，沒有一張投影片可查證**（現場沒拍 Keynote 投影片，第一張照片是 11:30 的 AIML05）。錄音本身完整（00:00–54:44），夾中/英/韓三語。所有產品名、數字都是 whisper 聽出來的。
>
> 標記：**🎤** 僅口述、未查證 ｜ **🔎** 經公開資訊查證過（非投影片）｜ **⚠️** 存疑、進待查核

### 一句話

三個客戶（NASDAQ 金融、KBS 媒體、Anthropic AI）串成同一論點：**雲是地基、AI 是加速器、信任是決勝點**。收尾兩個 takeaway——(1) 把 AI 當「7×24 的數位員工／夥伴」重新設計流程，不是拿來加速舊流程的工具；(2) 轉型要選「可信任」的夥伴（合規、規模、穩定）。

### 開場：Robert Wong（AWS 台灣董事總經理）

- 🎤 前兩年（2023、2024）Day 2 都因**颱風停班停課取消**，今年颱風上週過境、天公作美，第二天活動正常辦成。
- 🎤 AWS 在台灣紮根 **14 年**；去年 6 月啟用**台北 Region**（逐字稿聽成「Tiger Region / Type A Region / A-Class」，⚠️ 實際應為 **AWS 亞太（台北）Region**）。強調設計與全球一致、**三個可用區（AZ）物理距離隔離**、符合台灣資料落地與合規要求，服務對象含半導體、製造、物流、零售、媒體。

### 客戶一：NASDAQ（Gabriel Walker）

> ⚠️ 講者名 whisper 聽成「Gay Worker」，應為 **Gabriel Walker**。

- 🎤 NASDAQ 與 AWS 合作近 20 年（口述另提「始於 2008」「18 年」，數字不一）。
- 🎤 2022 年把美國最大的選擇權交易市場搬上 AWS；每天處理約 **20 億則訊息**（⚠️ 口述數字）。
- 🎤 NASDAQ 轉向 **23 小時 × 5 日交易**（always-on market），維護窗口越來越小 → 需要 real-time controls、強資安、韌性基礎設施。
- 🔎 提到一個 AI 驅動訂單類型（逐字稿聽成「SDC-approved… VLOG」）→ 查證為 **Dynamic M-ELO（Dynamic Midpoint Extended Life Order）**，NASDAQ 首個 AI 驅動訂單類型、**SEC 於 2023/9 核准**；每 30 秒分析 140+ 個資料點動態調整持有期，測試中 fill rate +20.3%。
- ⚠️ 受管服務方案「NASDAQ CapCloud on AWS」（treasury / trading / risk / settlement 單一平台），拼法待查核。

### 客戶二：KBS 韓國（AI 專案團隊，李雲杰／音譯）

> ⚠️ 這段夾大量韓文，whisper 亂碼嚴重（「수위 전신」重複多次為亂碼），產品名以公開報導查證為準。

- 🎤 主題：AI + AWS 消除「直播的物理限制」（畫框、距離、延遲）。
- 🔎 **K-POP 直拍**：產品名逐字稿聽成「벌티곤/Multigon」→ 查證為 **VVERTIGO**（KBS 自 2018 年開發的 AI 直拍引擎）。舞台觀眾席裝一台 8K 攝影機，AI 做「Reframing」——辨識+追蹤每位成員、裁成 9:16，**一台攝影機生出全部成員的直拍**；遮擋座位從 30–40 個降到 5–10 個。用 **AWS Inferentia** 做推論，數小時 → 數分鐘。技術已外擴到日本 KDDI、朝日電視，韓國 SBS 於 2026 初開始用。🎤 逐字稿另稱《Music Bank》每年產 2250 部（每天約 6 部）——⚠️ 與公開報導「年產超過一萬支 fancam」層級不同，數字待釐清。
- 🎤 **世界盃 AI 戰術筆記**：2 週開發，用於 **2026 FIFA 世界盃**轉播，解說員在墨西哥轉播席即時使用。架構（⚠️ 拼法待查核）：**AWS MediaConnect**（墨西哥→首爾約 1 萬公里、SRT 傳輸）、**AWS S3**、**AWS Step Functions**、AI 模型用 **Twelve Labs 的 Pegasus API**。強調 device 端處理、零延遲、後製消失。

### 台灣案例：老系統現代化（Robert，35:00–37:01）

- 🎤 台灣某客戶用 AI agentive platform 做 **reverse engineering**：讀懂沒人看得懂的老系統 → 生技術文件 → 生新程式改造，**一個下午完成過去團隊兩個月做不到的事**。點題：AI 不只做創新，也能救沒有 security patch 的核心舊系統。

### 客戶三：Anthropic（Natalie Lee，APAC Applied AI 負責人）

> 這段英文清楚，可信度相對高，但仍屬 🎤（無投影片）。人名/書名 whisper 有錯。

- 🎤 **自主工作時長的演進**：Opus 3（2024/3）分鐘級 → Opus 4（2025/5）1.7 小時 → 2025/11 約 4.9 小時 → **Opus 4.8 約 12 小時**連續自主工作。
- 🎤 技術史：2017 Google transformer 論文 → 2020 **scaling laws**（聽成「scaling wash」），提出者為 Anthropic 首席科學家 **Jared Kaplan**（聽成「Jerry Kaepern」）。
- 🎤 **Eric 的 bug 故事**：team 成員 Eric 在 Slack 回報 connector bug → 工程師拉進 **Claude in Slack（逐字稿「Claw Tag」）** + Claude → 約 5 行 code、**22 分鐘**修好並一起 review。用來說明「月 → 分鐘」的節奏。
- 🎤 **Gartner：2027 年 40% 的 agent 專案會被取消**——「不是模型問題，是交付問題（delivery problem）」。
- 🎤 差異化：**Constitutional AI**、**Responsible Scaling Policy**（產業在抄）、**MCP 是 Anthropic 創的產業標準**、Skills。對受監管企業「部署姿態是可稽核的，不是理想化的」。
- 🎤 **市佔**：3 年前 12% → 2026 年 **企業市場 40%**（Menlo 的 Tim Tully 背書）。⚠️ 口述數字。
- 🎤 AWS 是 primary cloud、數十億美元互相投資、用 **Trainium** 訓練晶片共同工程。
- 🎤 三支柱：smart employees（Claude Code / Claude Cowork）→ faster processes（agents 壓縮 contract review / KYC / claims）→ transformative products（把 Claude 嵌進自家產品）。
- 🎤 台灣案例：**ASUS 華碩**（聽成 ASUIS）用 Claude enterprise 賦能員工。模型分層：Opus（長任務）／Sonnet（通用）／Haiku（對話、成本敏感）。
- 🎤 引 Dario Amodei 的《**Machines of Loving Grace**》（聽成「machines without embrace」）：AI 走向要靠人主動「往正確方向傾斜」。

### 收尾（Robert）

- 🎤 兩個 takeaway：(1) **AI 原生思維**——不是把 AI 當工具加速舊流程，而是當「7×24 的代理人/團隊成員」重新打造流程（例：24 小時盯產線缺陷、發現後自動查 log / 過往 RCA report、推算原因與解法給工程師）；(2) 轉型規模龐大且面對監管合規，要選**可信任的夥伴**確保穩定、保住商譽。

---

## 11:30–12:15 AIML05: 在 AWS 上打造企業級 AI Agent（HOYA BIT × Amazon Bedrock AgentCore）｜ 📍 3F 大會堂

**角度**：② 平台落地實作

> 講者：Rick Lin（AWS Solutions Architect）＋ Zoe Peng／彭云嫻（HOYA BIT 創辦人/董事長）＋ Mars Li（HOYA BIT Head of AI Engineering）✅ 010/042
> 交叉查核基準：投影片 46 張（010–055）＋ 42 分鐘逐字稿。凡衝突一律以投影片為準。

### 一句話

前半 Rick 用一張「9 大模組圖」逐塊拆解 Amazon Bedrock AgentCore（把 agent 從 POC 推上 production 需要的託管能力）；後半台灣合規加密貨幣交易所 HOYA BIT 分享如何在 AgentCore 上蓋一個「開發者只寫 agent 邏輯 + 一份 YAML、平台統一接管部署/工具/存取/追蹤/治理」的內部 agent 平台，強調金融高度監管下的 human-in-the-loop 與 governance。

### Whisper 聽錯對照表（比對投影片後確認）

| 逐字稿聽成 | 實際（投影片為準） | 佐證 |
|---|---|---|
| Berat Agent Code、被ROCK | **Amazon Bedrock AgentCore** | ✅ 015 |
| Gay 位 | **Gateway** | ✅ 026 |
| Symmetric Search | **Semantic Search** | ✅ 028 |
| station 隔離、2500 個 station | **Session 隔離 / 2,500 active session workloads** | ✅ 020/021 |
| framegraph、entropic model | **LangGraph、Anthropic model** | ✅ 019 |
| MCB/SCP/NCP Server、MCD Tool | **MCP Server / MCP Tool** | ✅ 015/025 |
| ERD 系統 | **ERP 系統** | ✅ 025 |
| Octet（入口） | **Orchestrator** | ✅ 050/052 |
| A to A、Torque Calling | **A2A protocol、Tool Calling** | ✅ 019/054 |
| Garreal、Pumped Injection | **Guardrail、Prompt Injection** | ✅ 048 / 🎤 |
| Code View 會去 Build、Push 到 EC2 | **CodeBuild、Push 到 ECR** | ✅ 051 |
| R&D 的方式、如果 base、country review | **RAG、rule-based、Contract Review** | ✅ 047/046 |
| 創辦人云爛、今晚會登記 | **彭云嫻（Zoe Peng）、金管會登記** | ✅ 042/043 |
| 構寫的 | **Go 寫的（Golang）** | ✅ 052 |

### AWS Bedrock AgentCore 平台（前半，Rick Lin）

**開場鋪陳**
- The evolution into Agentic AI：Generative AI assistants → agents → Agentic AI systems，軸線「More human oversight → Less human oversight」✅ 013
- The prototype-to-production **"chasm"**：POC → 四道關卡 **Performance / Scalability / Security / Governance** → 真正的商業價值 ✅ 014
- 🎤 Rick 口述趨勢：2028 年約 1/3 企業會把生成式 AI 嵌入系統、約 15% 日常工作由 agent 協助（投影片無此數字）
- Agent hosting challenges：Platform owner 側「5 frameworks / 10 teams / **1,000 agents planned**」✅ 016

**9 大模組**（以 015 為準）：Runtime, Memory, Identity, Gateway, Code Interpreter, Browser, Observability, Policy, Evaluations ✅ 015（另有 Agent Registry(Preview) 與 AgentCore CLI，見 038/039）

#### Runtime ✅ 017–022
- 支援 **Any framework**（Strands、LangGraph、CrewAI…）＋ **Any model**（Claude/Nova/OpenAI…），對外 A2A/MCP、對內 OTEL ✅ 017–019
- 三大賣點（018 原文）：**Time to value**（few lines of code, serverless, deploy in <1 min）／**Secure**（session isolation, built-in auth, PrivateLink, VPC）／**Scalable**（large payloads, multi-hour workloads, async, bi-directional streaming）
- **True Session Isolation**（020）：每個 session 跑在**完全獨立的 microVM（compute + memory + filesystem）**，底層 **Firecracker MicroVM**；其他 serverless 方案多個 session 可能共用 microVM → 檔案/狀態可能被跨 session 存取
- **Session 限制數字（務必以投影片為準）**✅ 021/022：**2,500 active session workloads in most regions（as of Jul 2026）**／**5 mins → session suspended**（暫停但保留狀態）／**15 mins request timeout**／**60 mins of streaming**
  - ⚠️ 逐字稿另稱「某些區域 5,000 session」「業界最長 8 小時連續 session」——**投影片沒有**，進待查核，勿引用

#### Memory ✅ 023–024
- **Short term**：Chat Messages、Session State
- **Long term** 五策略：**Semantic、User Preferences、Summary、Episodic、Custom Strategy**
- 短期記憶經 **Automatic Memory Extraction Module** 以 async 萃取成長期記憶

#### Gateway ✅ 025–028
- 對接 APIs/microservices、MCP servers、Databases、CRMs/ERPs/ITSM ✅ 025
- Agent(MCP Client) → **AgentCore Gateway** → **API Endpoint Target**（OpenAPI schema）＋ **AWS Lambda Target** ✅ 026/027
- **Semantic Search 省 context**：不搜尋 → 回傳全部 **300 tools**；用搜尋（"create a monthly report"）→ 只回 **4 個最相關**；後端 Target 分別 200 / 150 / 50 tools ✅ 028
  - ⚠️ 別採信逐字稿的「550/300」，正解為 200/150/50、回傳 4 個

#### Policy（NEW）✅ 029–032
- User → Agents/MCP clients →(**Requested tool calls**)→ Gateway →(**Allowed tool calls**)→ Protected resources ✅ 030
- **Dynamic policy evaluation（Allow/deny）**＋ Policy Lifecycle Management ＋ **Policy Authoring（自然語言 or Cedar）**＋ Policy Admin ✅ 031/032

#### Identity ✅ 033
- **Inbound Auth**：OAuth Token（from User IdP）→ Agent Inbound Auth → Agent
- **Outbound Auth**：Agent →(IAM)→ AWS 資源；Agent →(OAuth/API key)→ 外部資源；Gateway Inbound/Outbound Auth 串下游

#### Observability ✅ 034–037
- 全棧 telemetry → **AgentCore Observability**，出口 OTEL；三種採集（自家 / 3P 工具 / service-level traces）
- **AI Agent Telemetry + Service Telemetry** 自動連結，導向自家或第三方 dashboards

#### Registry（Preview）✅ 038
- 入口：AWS Console、boto3 SDK、RESTful APIs & MCP tool → **AgentCore Registry**
- 能力：Unified catalog、Agents & Tools registration、Semantic/Lexical/Filter search、Metadata sync、**Workflow approval hooks**

#### CLI + 全景 ✅ 039
- **AgentCore CLI** 快速產 POC 範本、部署 production；039「at a Glance」一頁含全部模組 + Any Models/Any Agents(A2A/MCP) + Evaluation + OTEL

### HOYA BIT 實戰（後半，Zoe Peng ＋ Mars Li）

**公司背景（合規重點）✅ 043**
- 禾亞數位科技股份有限公司，**台灣合規加密貨幣交易所**，創辦人彭云嫻，2022 年創立
- **持有金管會洗錢防制登記（金管證券字第 1140349566 號）**、**通過 ISO/IEC 27001**、**與台新商業銀行信託合作**守護用戶資產
- 特點：業界高競爭力閃兌價格、**每張訂單 7 秒零滑價交易保障**、日日生幣、**最低 70 TWD 建立策略交易**
- 🎤 Zoe：台灣「第一家也是唯一一家」在 App 內導入自然語言 AI、可用語音調動 App 所有功能

**對外產品：AI 金寶-交易管家 ✅ 044**
- **全台首家導入 AI 交易系統的加密貨幣交易所**；四大功能：開口即執行、資料健診、智慧決策、貼身客服
- 🎤 Zoe 理念：導入 AI 非為裁員；工程師數不變、每人多了 AI token 預算，目標團隊戰力 5~10 倍（🎤 口述）

**方法論（Mars Li）**
- **Adoption ≠ Impact** ✅ 045：**95%** 無可衡量 P&L 影響（MIT NANDA）／**38%→11%** Piloting→Production（Deloitte）／**40%+** 預估取消（Gartner）。"AI adoption is easy to start, but hard to scale."
- **Not Every Problem Needs AI** ✅ 046：Rule-based（明確規則、可預測）vs AI Agent（脈絡、模糊、推理）。"Use rules for certainty. Use AI where context matters."
- **Contract Review Agent** ✅ 047：人工流程 vs Agent（**RAG + Web Search** / LLM 標風險 / **人工確認**）。"AI assists the workflow. **The domain owner still decides.**"
  - 🎤 金融高度監管，最後一定人工介入（human-in-the-loop / human-on-loop）；可讓 AI 查詢商品，但不讓 AI 執行下單類動作
- **From One Agent to Many** ✅ 048：單 agent 的手動部署/直接接工具/本地存取規則 → 多 agent 時全變成**平台責任**（標準化部署、共享工具、集中存取、端到端追蹤、平台級 guardrails）

**平台設計目標 ✅ 049**
- **Developers own**：Agent logic、Use-case workflow、**YAML declaration**
- **Platform provides**：Standardized deploy、Shared tools、Centralized access、End-to-end tracing、Guardrails
- 核心句："Developers build the agent. The platform enforces the foundation."

**架構：HOYA Agent Platform（AgentCore Reference Architecture + Self-Service Portal）✅ 050–053**
- 部署在 **AWS Cloud / HoyaBit Account / ap-northeast-1（Tokyo）** ✅ 051
- **Deploy path**：Developer → Portal → Build → Register；**Runtime flow**：Service → Orchestrator → Agent → Gateway → Tools ✅ 050
- Agent Deployment ✅ 051：開發者上傳 **Code + YAML** → Portal → **CodeBuild** build image → push **ECR** → 在 AgentCore 註冊供其他 agent/service 調用
- AgentCore Runtime ✅ 052：**One entry point / Route to the right agent / Bring your own stack / Same invocation path, different implementations**；agent 間以 **A2A** 溝通，不需知道對方是 Python/Go/LangChain/AgentCore SDK
- Governance ✅ 053：**Who owns this agent? / What can it do? / Can we trace it? / Governance belongs in the platform layer**
- 架構圖可讀元件（小字，部分模糊，⚠️ 建議調原始高解析投影片核對）：Self-Service Portal（ECS、Cognito、DynamoDB、S3(YAML)）、Deploy Pipeline（CodeBuild、ECR）、Bedrock（Claude/Nova）+ **Guardrails（PII/topic filter）**、Runtime（Orchestrator、hoya-review(LangGraph, Python)、compliance agent）、Governance（**Policy: Cedar ABAC per-agent ACL**、Agent Registry、Observability: OTEL + CloudWatch）、Capabilities（Identity、Memory）、Tools（Gateway、Browser、Code Interpreter）

**Before & After ✅ 054**：Before 每個 team 為每個 agent 重造輪子（Deploy/Tools/Access/Tracing/Guardrails）→ After 開發者只做 Agent logic + YAML，平台把那 5 項標準化

**Key Takeaways ✅ 055**
1. Start from a real workflow
2. Use rules for certainty, AI for context
3. Measure the before
4. Prove value with one POC
5. Design for more than one agent
> "Start lightweight. But design for more than one."

---

## 13:30–13:58 社群 LT：用 AWS Nitro Enclaves 保護 LLM 推論（機密運算）｜ 📍 2F Developer Community Zone

**角度**：③ 治理與安全

> 台灣 AWS User Group 社群 Lightning Talk（LT-006 前一場、同場地，兩場相接）。**無官方場次代號**。主持人 Frankie，講者林家瑋（Ray Lin）。約 28 分鐘，投影片 15 張（058–072）。

### 一句話

資料有「靜態 / 傳輸 / 使用」三態，前兩態大家都會加密，但「使用中資料」一進記憶體就是明文、連 root/雲端管理者都看得到；**AWS Nitro Enclaves 用硬體隔離的「小房間」（TEE）搭配 KMS 遠端驗證（Attestation），只有未被竄改、通過度量值驗證的程式才能拿到金鑰解密**，用來保護 LLM 推論等最敏感的那段運算。

### 講者：林家瑋 Ray Lin ✅ 058
- 🎤 軟體業 20 年，四大領域：資安、雲端、AI、專案管理。**全球首批 GCR 首位 AWS Security Hero**（✅ 058）、台灣 AWS User Group Leader、**AWS 全 13 張證照全取**、去年拿 **AWS Golden Jacket**（戲稱「JoJo 黃金戰衣」）。
- 徽章牆（✅ 058）：CISSP、CCSP、CISA、CSSLP、SSCP、CEH Master、OSWP、AWS Security/Advanced Networking/ML Specialty、SA Pro、DevOps Pro、PfMP、PMP…
- 🎤 非全職講師，是兩間公司高階主管（iFUS CISO/CAIO、DataBrushing.ai CDO 等）。開場說「翹課來講」，另一邊在上美國國防部供應鏈課程（逐字稿「CNNC」→ **CMMC**）。

### Whisper 聽錯對照表

| 聽成 | 實際 |
|---|---|
| Nitro N-CAP / Intellect | **Nitro Enclaves** |
| 機密預算、電腦集合 | 機密運算、電腦稽核 |
| Low Harmony | **Rowhammer** |
| Visaki | **vsock**（Secure Local Socket） |
| DAC / Dock | **Docker** |
| Ecliff | **EIF**（Enclave Image File） |
| Quamerton、ON 架構 | **Graviton、Arm 架構** |
| KNS、精要管理 | **KMS、金鑰管理** |
| Golden JP、CNNC | **Golden Jacket、CMMC** |

### 技術主軸

**（a）資料三態與「使用中」風險** ✅ 061/062
- 三態：靜態（存 S3/EBS 用 AES/RSA）、傳輸（TLS 1.3/VPN，AWS 憑證由 ACM 免費簽發）、**使用（最常被忽略）**
- 使用中風險：資料進記憶體即明文，OS/雲端管理者理論上看得到。四類攻擊：**Memory Dump**（Key/Token/PII/模型權重都在裡面）、**Rowhammer**、**Side-channel（Cache Timing）**、**惡意 Library/Injection**
- **Rowhammer** ✅ 063：利用 DRAM 電荷洩漏效應反覆存取同一記憶體列，讓隔壁 bit flip，**最快 109 秒取得系統控制權**（投影片明確標 109 秒，署名 COMSEC, ETH Zurich）。🎤 bit flip 可把 page table 權限位 0→1，非 root 變 root。

**（b）機密運算 / TEE** ✅ 064
- 保護「使用中資料」，補上靜態/傳輸之外的缺口。在**硬體式、可證明的可信任執行環境（TEE）**內運算。
- 適用：PII/PHI/PFI/IP；領域金融、醫療、AI 模型訓練、區塊鏈錢包。
- 🎤 AWS 把 Hypervisor、網路/儲存管理、TPM 等獨立成專用 Nitro「卡」，設計 Nitro Hypervisor 做隔離。

**（c）威脅模型：防誰／不防誰** ✅ 065
- ✅ 要防：Cloud Operator/Host Admin、Hypervisor/Host OS、惡意管理流程（Debug/Dump/Snapshot）、多方資料合作
- ⚠️ 不保證防：**應用程式本身漏洞**（SQLi/RCE/邏輯錯誤）、資料**離開 TEE 後**的濫用、Side-channel（可降風險非完全消除）

**（d）Nitro Enclaves 是什麼** ✅ 066/067
- 從 EC2 Instance 切出更小信任邊界的隔離 VM；Parent 僅能以 **vsock** 連 Enclave，Parent 的 process/kernel/users 都存取不到 Enclave 內容
- 可整合 **KMS / ACM / CloudTrail**；**無持久儲存、無互動存取、無外部網路、無法 SSH**；就算 Parent 被拿到 root 也讀不到 Enclave 記憶體
- 🎤「會用 Docker 就會用它」；開一台 Parent EC2 在裡面切小房間

**（e）四個基礎元件與流程** ✅ 068
1. **TEE Enclave 啟動** → 2. **產生 Measurement（度量值）** → 3. **Attestation 驗證可信** → 4. **Key Release 解密**（僅通過證明的程式取得解密能力）
- 🎤 度量值是「連環 Hash」：Docker 轉 **EIF** 時產生，**PCR0=EIF 整體 / PCR1=Kernel / PCR2=程式碼**（✅ 071/072 顯示 PCR0/1/2、Attestation **SHA384**）。任一 PCR 被竄改，KMS 就不發 key（policy 寫在 KMS）。

**（f）需求與費率** ✅ 069/070
- Parent：Nitro-based instance；**Intel/AMD ≥4 vCPU 或 Graviton ≥2 vCPU**；OS Linux 或 Windows 2016+
- 費率表（✅ 070，隨需/時、皆 2 vCPU）：t4g.nano $0.0054 … **c6g.large $0.0856（4 GiB，紅框標註）**。🎤 講者說 c6g.large（Graviton/Arm）是最便宜可用規格，Demo 就用這台，提醒「Demo 完記得關掉」。

**（g）保護 LLM 推論的架構** ✅ 071
- VPC/Public subnet/EC2 內：**Parent instance（Chatbot Web）** + **Nitro Enclave（Chatbot App + LLM Model）**，兩者以 **vsock** 相連；旁掛 IAM/CloudTrail/KMS
- 流程①–⑦：User 送敏感 query(HTTPS) → Chatbot Web → 加密資料經 vsock → **Attestation 驗 PCR0/1/2** → LLM 推論 → 結果回傳 → 回 User。🎤 解密只在小房間內，管理者進不來；驗證通過 KMS 才給解密權限。

### Demo ✅ 069/072
- **GitHub：`github.com/cheng-ruru/AWS_NitroEnclaves`**（✅ 069，含安裝/設定/執行步驟；投影片右下 QR Code 可下載簡報 PDF）
- 線上 Demo（✅ 072）：`tool.ifus.tw/admin-console?category=aws-demo`，畫面顯示「建置 EIF 成功」、**Nitro CLI 1.4.4**、SHA384、PCR0/1/2
- 🎤 現場三項驗證：① 記憶體隔離（Parent 上 grep enclave 名稱查不到 process）；② `/proc` 讀檔回傳「Invalid」證明 root 也讀不到；③ 防篡改（Dockerfile 加一行 → PCR0/PCR2 變、PCR1 不變 → KMS 拒發 key）

---

## 13:55–14:20 LT-006: 用 Kiro 打造 HR 的 AI 小幫手 ｜ 📍 2F Developer Community Zone

**角度**：① 讓團隊用起來 — Day 1 KIRO02/KIRO05 方法論的落地版

> 講者 RuRu（HR / AWS Community Builder）。這場**已寫成一篇獨立文章**（給非工程背景同事看的推廣文），內容、投影片、逐字稿引言都在裡面，此處不重複。

**📄 文章**：[不會寫程式的 HR，如何用 Kiro 一個晚上做出內部工具](https://blog.tomting.com/2026/07/16/hr-kiro-build-internal-tool-one-night/)

**跟 Day 1 Kiro 場次的接點**：Day 1 KIRO02（prompt/context/harness 工程實踐）+ KIRO05（vibe → spec-driven 方法論）是理論，LT-006 是拿 Kiro 真的做出一個 HR 工具的落地。一個對照點——RuRu 逐字稿裡**親口建議用 Spec 模式**（因她做專案管理習慣先理清規格），但投影片標題卻是「我的 **Vibe** 原則」，她自己沒收斂這個矛盾，文章照原樣呈現。

---

## ❓ 待查核（彙整）

**Keynote（無投影片，全需查）**
- 台北 Region 正式名稱（逐字稿 Tiger/Type A/A-Class）
- NASDAQ「20 億訊息/日」「CapCloud」拼法；KBS《Music Bank》年產量（2250 vs 一萬）；世界盃架構 MediaConnect/S3/Step Functions/Twelve Labs Pegasus 拼法
- Anthropic 市佔 40%（口述數字）

**AIML05**
- Runtime「8 小時連續 session」「某些區域 5,000 session」——投影片 021/022 只有 2,500 / 5min / 15min / 60min，其餘勿引用
- Mars 口述「70% 用戶不希望高風險動作」數字來源
- HOYA 出入金幣別（043 該字模糊）；架構圖 050–053 小字（Cedar ABAC 等）需原圖核對

**社群 LT（Nitro）**
- 逐字稿「NSP」證照對不上徽章牆；「Sickle Injection」攻擊名（062 只寫「惡意 Library/Injection」）

---

## 🔗 參考來源（查核用）

- [NASDAQ Dynamic M-ELO（SEC 核准的 AI 訂單類型）](https://www.nasdaq.com/solutions/dynamic-m-elo)
- KBS VVERTIGO / AI fancam — INSIDE 報導（AWS Summit Taipei 專文）
- [Amazon Bedrock AgentCore 官方文件](https://docs.aws.amazon.com/bedrock-agentcore/)
- [AWS Nitro Enclaves 官方文件](https://docs.aws.amazon.com/enclaves/)
- GitHub: `cheng-ruru/AWS_NitroEnclaves`（講者 Demo repo）
