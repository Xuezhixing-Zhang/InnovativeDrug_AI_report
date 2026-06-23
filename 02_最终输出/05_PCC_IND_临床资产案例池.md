# PCC、IND和临床资产案例池

> 各模块 D 资产验证（Hit/Lead/PCC/IND/临床）。 汇总自 19 个模块各自的对应小节。生成 2026-06-23。

### 1.1_靶点结构和结合位点预测
## 五、D 资产验证
- **Relay**：RLY-4008（lirafugratinib，FGFR2）授权 Elevar Therapeutics，2026 推进 NDA/FDA 受理 [待核日期]；RLY-2608（PI3Kα 变构，突变选择性）临床。
- **Schrödinger**：SGR-1505（MALT1）等自研管线进入临床。
- **深势/星药**：Hit–Lead 阶段，公开披露深度弱于国外（标公司/合作方口径）。

### 1.2_虚拟筛选和Hit发现
## 五、D 资产验证

| 资产/项目 | 发生/披露日期 | 当前可核验状态 | 来源类型与判断 |
|---|---|---|---|
| SGR-1505（MALT1） | IND 2022-06 获 FDA 放行；试验 2023-04-10 启动 | Phase I，Recruiting（截至 2026-06-22） | **A SEC + 临床注册**：[2026Q1 10-Q](https://www.sec.gov/Archives/edgar/data/1490978/000149097826000037/sdgr-20260331.htm)、[NCT05544019](https://clinicaltrials.gov/study/NCT05544019) |
| SGR-3515（Wee1/Myt1） | IND 2024-04 放行；2024-07 开始给药 | Phase I，Recruiting（截至 2026-06-22） | **A SEC + 临床注册**：[2026Q1 10-Q](https://www.sec.gov/Archives/edgar/data/1490978/000149097826000037/sdgr-20260331.htm)、[NCT06463340](https://clinicaltrials.gov/study/NCT06463340) |
| MDR-001（口服小分子 GLP-1RA） | 美国 IND 2022-12（公司时间线）；I/IIa 2023-06-09 启动；III 期登记计划 2026-02 开始 | NCT06778850 为 Phase I/IIa、Recruiting；NCT07274137 为 Phase III、Not yet recruiting；公司“已进入 III 期”表述不等同已开始招募 | **A 临床注册 + C 公司**：[NCT06778850](https://clinicaltrials.gov/study/NCT06778850)、[NCT07274137](https://clinicaltrials.gov/study/NCT07274137)、[管线页](https://www.mindrank.ai/en/pipeline) |
| Aqemia 自有项目 | 截至 2026-06-22 官网状态 | 临床前/体内；项目名与靶点未公开，未检出 IND/临床注册 | **C 公司官网**；信息不足，不上调阶段 |
| 晶泰 GPX4 | 2024-11-21 公司披露 | Hit，未见 PCC/IND | **C 公司案例**；不可将合作目标“交付候选化合物”写成已完成交付 |

> 临床注册只能验证资产、阶段和招募状态，不能独立证明该分子由 AI 发现，也不能证明 AI 提高了临床成功率；AI 贡献仍需项目论文、合作方说明或可审计发现记录验证。

### 1.3_ADMET_DMPK_毒性_可开发性预测
## 五、D 资产验证

1. **MDR-001（MindRank）**：ClinicalTrials.gov 的 [NCT07274137](https://clinicaltrials.gov/study/NCT07274137) 登记为肥胖/超重 III 期，首次公开 2025-12-10；登记截至 2025-12-22 仍为 `NOT_YET_RECRUITING`。公司新闻列表称 2026-02-26 已完成首例给药。两者可能是注册更新时差，但在获得更近期注册/中心证据前应保留冲突。
2. **EXS21546（Exscientia）**：曾进入 Phase 1/2 IGNITE；公司 2023Q3 SEC 文件披露停止内部开发并关闭试验。它既满足“临床资产验证”，也构成关键负面案例。
3. **EXS73565/EXS74539（Exscientia）**：2022 年 20-F 披露 IND-enabling/临床前及 ADME、PK、毒理结果；其后管线在并购/重排中发生变化，不能沿用旧阶段作当前状态。
4. **晶泰合作资产**：晶泰 2024-08-13 自述与希格生科发现的弥漫性胃癌小分子获 FDA IND；本轮未找到 FDA/合作方可直接对应的分子编号，暂按 C 级。
5. **VeriSIM 管线**：管线页仅列治疗领域，未披露候选编号、权属和监管阶段；暂按发现/临床前，不计入硬性临床资产数。

### 1.4_分子从头生成和多参数优化
## 五、D 资产验证

| 资产 | 公司 | 截至 2026-06-23 的可核验状态 | 日期/来源类型 | 结论 |
|---|---|---|---|---|
| rentosertib/ISM001-055（TNIK/IPF） | Insilico | 随机 Phase 2a 结果已发表 | 2025-06-03 online，Nature Medicine 论文 B；官网管线 C | 达到临床 PoC 级证据；仍需后续更大样本和注册路径验证 |
| IAM1363（HER2 TKI） | Iambic | NCT06253871，Phase 1/1b，Recruiting；起始 2024-03-25，最近更新 2026-06-04 | ClinicalTrials.gov A | 临床早期资产，尚不能判断有效性/注册成功率 |
| ISM3091/XL309（USP1） | Insilico → Exelixis | NCT05932862，Phase 1，Recruiting；2024-04-03 起始；由 Exelixis 申办 | ClinicalTrials.gov A；2023-09-12 许可公告 C | 说明生成平台资产可转化为外部许可并由药企推进 |
| EXS21546（A2A antagonist） | Exscientia | NCT05920408，Phase 1/2，Terminated；实际入组 6；停止原因为难以达到合适治疗指数 | 2023-11-08 注册更新 A；2024-03-21 20-F A | 明确失败/终止案例 |
| MDR-001（口服小分子 GLP-1RA） | MindRank | NCT06778850 Phase I/II Recruiting；NCT07274137 Phase III Not yet recruiting、计划 738 人 | 注册首次披露 2025-01-16 / 2025-12-10，ClinicalTrials.gov A | 已有较高阶段注册，但“Phase III 已注册”不等于已招募/已验证疗效 |
| MRANK-106（WEE1/YES1） | MindRank | 公司称 2025-03 获 FDA IND clearance；本轮未检出 ClinicalTrials.gov 对应试验 | 公司里程碑 C | 作为 IND 线索保留，待 FDA/注册号或临床启动进一步核验 |

### 1.5_AI逆合成_可合成性_自动化化学
## 五、D 资产验证

- **Rentosertib/ISM001-055（Insilico）**：ClinicalTrials.gov NCT05938920 显示 Phase 2、71例、2023-06-19开始、2024-08-08完成、已提交结果；这是本模块候选池中最强监管级资产证据。必须强调：它验证端到端生成式AI/实验闭环，不等于逆合成单模块的因果验证。
- **PostEra COVID Moonshot**：公司称2021年完成 Development Candidate nomination、准备进入 IND-enabling；截至2026-06-23未检出对应临床注册，官网仍称 live phase planned。
- **Iktos**：管线页标示 MTHFD2 等项目并有“Preclinical Candidate”栏位；目前仅公司披露，未检出IND/临床注册。
- **晶泰科技**：2026-05-29公司公告称DoveTree合作首个肿瘤PCC已进入IND-enabling，并确认已收到第二笔$19m；这是“闭环平台→PCC”的较强资产/现金验证，但尚未等于IND获批。公司2024-08-13另称平台发现的多条合作小分子管线已获IND，仍须逐项目以 CDE/NMPA/ClinicalTrials.gov 和合作方公告核验平台贡献与权属。
- **Chemify、Chemical.AI**：未检出明确自研 PCC/IND/临床资产；目前主要验证停留在路线、实体合成、合作发现和商业部署。

### 3.1_siRNA_ASO_mRNA序列与修饰优化
## 五、D 资产验证

|公司/资产|发生/披露日期|资产与阶段|验证结论|
|---|---|---|---|
|Deep Genomics / DG12P1|2019-10-10|针对 ATP7B M645R 导致 exon skipping 的 oligo 候选；从数千个化合物中筛到 12 个 leads，结合体外效力、毒性/耐受实验后提名，目标为推进 IND|满足“PCC/临床前资产”硬目标；截至 2026-06-22 以公司名和 DG12P1 检索 ClinicalTrials.gov 未见注册，不能写成 IND 或临床。|
|Creyon / 3 个 wholly-owned products|官网访问 2026-06-22|CNS、免疫、晚发 Pompe 等方向；CNS 披露临床前 POC，具体候选编号/IND 时间未公开|可认定临床前资产/项目簇，不可认定 PCC 或 IND。|
|Inceptive|2026-06-03 合作披露|与 Alnylam 联合预测并优选进入临床前模型的 siRNA 候选|属于合作发现阶段；无公开的 Inceptive 自有 PCC/临床资产。|
|衡昱/Raina|2025-08-28|多应用实验分子（疫苗、EPO、CAR-T/circRNA）；公司称正准备建立内部管线|是实验 POC，不是命名药物资产；无 IND/临床注册。|
|Therna|官网访问 2026-06-22|未披露命名项目|仅平台验证，不足以作为资产验证。|

ClinicalTrials.gov 实际检索（2026-06-22）：`"Deep Genomics"`、`"Creyon Bio"`、`"Inceptive Nucleics"`、`"Raina Biosciences"` 未返回可归属临床研究；相邻负面资产 WVE-004 返回 `NCT04931862` 与 `NCT05683860`，均为 **TERMINATED**。

### 3.2_LNP和非病毒递送材料设计
## 五、D 资产验证

| 资产/平台 | 归属 | 阶段与日期 | 证据边界 |
|---|---|---|---|
| MTS109（mRNA-LNP） | METiS协作；上海长征医院申办 | Early Phase 1/IIT；实际启动2026-03-24；首次公示2026-04-13；截至2026-06-23招募中 | **监管/注册A级。** 注册未公开完整货物机制和脂质结构；公司与医院权利归属未披露 |
| CD8-targeted LNP + CD20 CAR mRNA | Mirai | 临床前NHP功能PoC；2026-05-12披露 | **公司/会议C级。** 未见IND、正式资产编码、完整海报或同行评议 |
| MB-LNP-05肺靶向系列 | Mana | 临床前小鼠/NHP；页面2026-05-18更新 | **公司海报C级。** 未见IND/GLP毒理/正式开发候选声明 |
| 体内T细胞/CAR-T LNP | Mana | 临床前小鼠/NHP；预印本2025-12-04 | **预印本B级+公司C级。** 尚未同行评议 |

**未找到** Mana.bio 或 Mirai Bio 作为申办方/协作方的ClinicalTrials.gov命中；不等于“无临床资产”，仅表示截至检索日未在该注册库以公司名检出。

### 3.3_CRISPR酶_gRNA_碱基_先导编辑器
## 五、D 资产验证

- Arbor ABO-101：NCT06839235，Phase 1/2 recruiting，actual start 2025-06-16；适应症 PH1；intervention 为 ABO-101 IV infusion；药物组成由 Arbor 官网披露为 LNP mRNA expressing novel Type V CRISPR Cas12i2 nuclease + optimized gRNA targeting HAO1。
- Scribe STX-1150：NCT07428473，Phase 1 not yet recruiting，estimated start 2026-06-01；Monash University sponsor，Scribe collaborator；适应症 elevated LDL-C/high cholesterol；mRNA + gRNA + LNP，epigenetically silences PCSK9。
- 正序 CS-101：NCT06024876，Early Phase 1 completed，actual start 2023-08-26，completion 2025-07-01；公司披露 2024-04-02 NMPA IND 默示许可；Nature 2026 临床结果直链已登记。
- Metagenomi MGX-001：2025/2026 SEC 年报披露为 lead wholly owned hemophilia A program，在 NHP 中 demonstrated targeted genome editing and durable gene expression；但 SEC 同时提示仍 very early，未检出临床注册/IND。
- Profluent：未检出自研治疗资产；主要为工具/合作输出。
- EdiGene：官网披露 DMD/通用型 CAR-T 等方向，未检出本模块具体 IND/临床注册。

### 3.4_AAV和病毒载体衣壳设计
## 五、D 资产验证

- Affinia AFTX-201：ClinicalTrials.gov NCT07426419，Phase 1/2，NOT_YET_RECRUITING，start 2026-06，适应症 BAG3-associated DCM；来源类型：临床注册。
- 4DMT 4D-150：ClinicalTrials.gov NCT06864988 和 NCT07064759 为 Phase 3 wet AMD；NCT05930561 Phase 2 DME；NCT05197270 Phase 1/2 wet AMD；来源类型：临床注册。
- 4DMT 4D-710：NCT05248230 Phase 2 cystic fibrosis；来源类型：临床注册。
- 4DMT 4D-310：NCT04519749 和 NCT05629559 Phase 1/2 Fabry disease；来源类型：临床注册。
- Frontera FT-002：NCT05874310 Early Phase 1、NCT06492850 Phase 1/2，RPGR mutation-associated X-linked retinitis pigmentosa；来源类型：临床注册。
- Dyno：本轮未检出 Dyno 自研资产注册；资产验证主要是 partner exercised capsid license and will handle preclinical/clinical/commercialization；来源类型：公司公告。
- Avista、Byongen、Capsigen：未检出公开 ClinicalTrials.gov/NMPA 资产注册；以平台/会议/合作线索为主。

### 2.1_蛋白和复合物结构预测
## 五、D 资产验证

| 公司 | 资产 | 截止日阶段 | 核验 |
|---|---|---|---|
| Generate | GB-0895，AI 工程化长效抗 TSLP 单抗 | **III 期，两项试验均招募中** | [NCT07276724](https://clinicaltrials.gov/study/NCT07276724) 于 2025-12-03 启动；[NCT07359846](https://clinicaltrials.gov/study/NCT07359846) 于 2026-01-20 启动（A级监管）。公司还披露 GB-4362、GB-5267 的 IND 于 2025-12 获 FDA clearance（[SEC 10-Q, 2026-05-07](https://www.sec.gov/Archives/edgar/data/2100782/000119312526210059/ck0002100782-20260331.htm)，A级财务） |
| Iambic | IAM1363，HER2 选择性小分子抑制剂 | I/1b 期，招募中 | [NCT06253871](https://clinicaltrials.gov/study/NCT06253871)：2024-03-25 启动，计划 383 人（A级监管）；2025-10-20 公司披露初步人体数据（C级） |
| 深势科技 | 口服 Kv1.3 抑制剂 | PCC/临床前（公司称 2024-01-30 提名） | [公司公众号直链](https://mp.weixin.qq.com/s/6B2cnGpXSAvvh1iQeR3-9w)（C/E级）；截至截止日未检出 IND、CDE 或 ClinicalTrials.gov 注册，阶段需二次核验 |
| Isomorphic Labs | 未命名自研项目 | 未披露 | 官网有“自研项目/向临床推进”表述，但未检出命名候选、IND 或临床注册；不把招聘 CMO 等同于资产进入临床 |
| BioMap | 未命名 | 未披露 | 与科兴制药的大分子合作指向临床前研发，但未披露靶点、候选物、PCC/IND |

### 2.2_抗体亲和力_特异性_可开发性优化
## 五、D 资产验证

| 资产 | 阶段与日期 | 验证来源 | Stage 1判断 |
|---|---|---|---|
| HXN-1001（Earendil，anti-TL1A） | 2026-04-02公司称IIa首例给药；一期健康志愿者已完成入组 | C级公司新闻稿：[IIa首例](https://www.prnewswire.com/news-releases/earendil-labs-announces-first-patient-dosed-in-a-phase-iia-trial-of-a-half-life-extended-anti-tl1a-antibody-hxn-1001-in-patients-with-ulcerative-colitis-302732675.html) | 本扫描最高阶段资产；尚未检出ClinicalTrials.gov NCT或可核验的澳洲/中国注册号，阶段暂标“公司披露IIa” |
| ABCL635（AbCellera，anti-NK3R） | 2025-06-23注册起始；2026-02-24 10-K称Phase 1/2，2026-06-23注册状态ACTIVE_NOT_RECRUITING | A级：[NCT07118891](https://clinicaltrials.gov/study/NCT07118891)、[2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1703057/000170305726000012/abcl-20251231.htm) | 临床/监管证据较强；但需进一步证明AI优化对分子差异化的具体贡献 |
| ABS-201（Absci，anti-PRLR） | 2025-12-03试验开始；2026-06-23注册状态RECRUITING，Phase 1/2 | A级：[NCT07317544](https://clinicaltrials.gov/study/NCT07317544)、[Absci 2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1672688/000167268826000068/absi-20251231.htm) | 证明Absci已有第二项临床抗体；目前仍以安全性/剂量爬坡为主，尚无疗效PoC |
| ABS-101（Absci，anti-TL1A） | 2025-05启动I期；2026-03-24 10-K披露公司不再自行推进后期、将寻求合作方 | A级：[2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1672688/000167268826000068/absi-20251231.htm) | 既是临床验证也是负面/资本配置信号；不能把“进入I期”写成平台已验证成功 |
| LGTX-101（LabGenius，Nectin-4×CD3） | 临床前Lead；截至2026-06-23未检出IND/临床注册 | C级：[公司管线](https://labgeniustx.com/pipeline/)；B级平台论文为相邻HER2×CD3案例 | 有体外/体内信号，PCC/IND状态待核 |
| BigHat合作序列 | 2025-10-28称多条新序列进入后续开发 | C级公司公告 | 未命名、未披露PCC/IND，不上调阶段 |
| BioMap—科兴项目 | 发现/临床前规划 | A级合作方公告 | 未披露靶点、候选物、PCC或IND |

### 2.3_抗体_蛋白_酶_多肽从头生成
## 五、D 资产验证

| 资产 | 公司 | 阶段与日期 | AI/从头口径 | 证据与限制 |
|---|---|---|---|---|
| GB-0895（anti-TSLP） | Generate | Phase III；SOLAIRIA-1 2025-12-03 起、SOLAIRIA-2 2026-01-20 起，2026-06-23 均 Recruiting | 公司称用生成优化 stack 改善 potency、半衰期和特异性；不是已证明从零生成新抗体骨架 | A：[NCT07276724](https://clinicaltrials.gov/study/NCT07276724)、[NCT07359846](https://clinicaltrials.gov/study/NCT07359846)；B：[US12110324B2](https://patents.google.com/patent/US12110324B2/en) |
| ABS-201（anti-PRLR） | Absci | Phase I/IIa；2025-12-03 开始，2026-06-23 Recruiting | 生成式/多参数平台参与设计；完全从头程度未从专利序列谱系独立确认 | A：[NCT07317544](https://clinicaltrials.gov/study/NCT07317544)、[2025 10-K](https://www.sec.gov/Archives/edgar/data/1672688/000167268826000068/absi-20251231.htm) |
| ABS-101（anti-TL1A） | Absci | 2025-05 启动 Phase I；2025-11 披露 positive interim 后，公司决定不自行进入后期、改为寻求合作 | 公司称 Integrated Drug Creation Platform 用于表位/免疫原性/单体和三聚体结合设计 | A：[2025 10-K](https://www.sec.gov/Archives/edgar/data/1672688/000167268826000068/absi-20251231.htm)；C：[开发海报页](https://www.absci.com/abs-101-development/) |
| HXN-1001（anti-TL1A） | Earendil/Helixon | 2026-04-02 公司宣布 UC Phase IIa 首例给药 | 半衰期延长抗体；AI 贡献为设计/优化，未见“全新骨架”一手证明 | C：[公司新闻稿](https://www.prnewswire.com/news-releases/earendil-labs-announces-first-patient-dosed-in-a-phase-iia-trial-of-a-half-life-extended-anti-tl1a-antibody-hxn-1001-in-patients-with-ulcerative-colitis-302732675.html)；未检出可匹配的 ClinicalTrials.gov 条目，需核对 ANZCTR/中国注册 |
| HXN-1011（TSLP biparatopic Ab） | Earendil/Helixon | 2026-05-18 公司宣布 Phase I 首队列给药 | AI/高通量平台产生的双表位抗体；从头程度待核 | C：[公司新闻稿](https://www.prnewswire.com/news-releases/earendil-labs-announces-first-cohort-dosed-in-phase-i-study-of-novel-biparatopic-antibody-targeting-thymic-stromal-lymphopoietin-tslp-302774497.html) |
| TNFR1 miniprotein 等 | AI Proteins | 临床前/体内 PoC；截至 2026-06 未披露 IND | 新骨架 miniprotein，为本模块“从头生成”纯度较高的资产类型 | C：[管线页](https://www.aiproteins.com/pipeline)；缺少同行评议药物项目数据 |

### 2.4_多目标大分子优化
## 五、D 资产验证

- **Absci ABS-201（A，ClinicalTrials.gov）**：NCT07317544，Phase 1/2a，招募中；首次登记 2026-01-05（研究开始 2025-12-03），申办方 Absci Pty Ltd.，计划入组 227 名健康成人/雄激素性脱发人群。来源：[NCT07317544](https://clinicaltrials.gov/study/NCT07317544)。截至 SEC 2025 年报披露日 2026-03-24，公司称前三个 SAD 队列已给药；这是公司披露，尚无注册结果。
- **Absci ABS-101（A，SEC）**：公司称 2025-05 启动健康志愿者 I 期；2025-11 披露积极中期结果后仍决定不自行推进后期、转为寻求合作方。来源：[2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/1672688/000167268826000068/absi-20251231.htm)。
- **LabGenius LGTX-101（C，公司）**：IND-enabling；未检出 ClinicalTrials.gov/监管受理记录。BigHat 的 BHB810/BHB299 处发现/临床前。国内两家未检出公开命名自研临床大分子资产。
- 结论仅限 Stage 1：**已有“实验→IND-enabling→人体试验”纵向覆盖，但尚无该模块公司自研资产获得批准或披露临床疗效证明。**

### 4.1_多组学和疾病机制整合
## 五、D 资产验证

| 公司/资产 | 阶段与状态 | 发生/披露日期 | 证据与边界 |
|---|---|---|---|
| 英矽智能 INS018_055/rentosertib | 已发表随机 Phase 2a；ClinicalTrials.gov 有完成及招募中的 Phase 2 记录 | Phase 2a 论文在线披露 2025-06-03；注册状态访问 2026-06-22 | **A/B**：[NCT05938920](https://clinicaltrials.gov/study/NCT05938920)、[NCT05975983](https://clinicaltrials.gov/study/NCT05975983)、[Nature Medicine](https://doi.org/10.1038/s41591-025-03743-2) |
| Owkin/affiliate OKN4395 | Phase 1，招募中；为引进资产，不能证明 Owkin 多组学平台从零发现该药 | 开始 2025-01-23；注册状态核验 2026-06-22 | **A**：[NCT06789172](https://clinicaltrials.gov/study/NCT06789172)；**C**：[2024-05-23 引进公告](https://www.owkin.com/newsfeed/owkin-unveils-ai-driven-oncology-and-immunology-pipeline-in-licenses-best-in-class-asset-okn4395) |
| BenevolentAI BEN-8744 | Phase 1a 完成；公司 2024-03-25 披露健康志愿者安全性/PK 顶线结果 | 试验 2023-08-30 开始、2024-03-18 完成 | **A**：[NCT06118385](https://clinicaltrials.gov/study/NCT06118385)；**C**：[公司结果公告](https://www.benevolent.com/news-and-media/press-releases-and-in-media/benevolentai-announces-positive-topline-safety-and-pharmacokinetic-data-phase-ia-clinical-study-ben-8744-healthy-volunteers/) |
| Verge VRG50635 | 历史 Phase 1/1b；ALS 研究 **TERMINATED**，原因是 sponsor 认为缺乏风险—收益数据 | 研究 2024-01-15 开始、2025-07-07结束；终止状态 2025-12-15 发布 | **A监管**：[NCT06215755](https://clinicaltrials.gov/study/NCT06215755)；健康志愿者研究完成：[NCT06286475](https://clinicaltrials.gov/study/NCT06286475) |
| Relation / BioMap | 未检出命名 PCC、IND 或临床资产 | 截至 2026-06-22 | Relation 仅披露 discovery/骨病项目；BioMap 披露 20+ PoC 但未绑定命名资产。不得把 PoC 当 PCC。 |

### 4.2_药物再定位
## 五、D 资产验证

- BioXcel（2022 / FDA 监管）：FDA Drugs@FDA 显示 IGALMI（dexmedetomidine hydrochloride buccal/sublingual film）NDA 215390 已批准；官网管线页说明 IGALMI 获 FDA 批准用于成人 schizophrenia 或 bipolar I/II disorder 相关 acute agitation。[FDA NDA 215390](https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&ApplNo=215390)；[Pipeline](https://www.bioxceltherapeutics.com/our-pipeline/)
- BioXcel（ClinicalTrials / 临床注册）：BXCL501 schizophrenia agitation Phase 3 试验 NCT04268303 completed；dementia agitation Phase 2 NCT05276830 terminated。[NCT04268303](https://clinicaltrials.gov/study/NCT04268303)；[NCT05276830](https://clinicaltrials.gov/study/NCT05276830)
- SOM Biotech（ClinicalTrials / 临床注册）：SOM3355 Huntington’s disease chorea 两项 Phase 2 均 completed：NCT03575676、NCT05475483。[NCT03575676](https://clinicaltrials.gov/study/NCT03575676)；[NCT05475483](https://clinicaltrials.gov/study/NCT05475483)
- SOM Biotech（官网披露 / 公司自述）：SOM3355 管线页称 proof-of-concept 与 Phase 2b 结果为 positive，2025-09 完成 FDA end-of-Phase 2 meeting 后准备进入 Phase 3；该表述需后续以 FDA meeting minutes/公司公告补强。[Pipeline](https://www.sombiotech.com/pipeline/)
- Lantern（ClinicalTrials / 临床注册）：LP-300 + carboplatin + pemetrexed 用于 never-smoker advanced lung adenocarcinoma，NCT05456256 Phase 2，status recruiting。[NCT05456256](https://clinicaltrials.gov/study/NCT05456256)
- Healx（ClinicalTrials / 临床注册）：HLX-0201（sulindac）/HLX-0206（gaboxadol）用于 male Fragile X syndrome，NCT04823052 Phase 2，status withdrawn。[NCT04823052](https://clinicaltrials.gov/study/NCT04823052)
- BenevolentAI/baricitinib（2022-06-13 / 监管）：FDA Drugs@FDA 显示 Olumiant/baricitinib NDA 207924 于 2022-06-13 SUPPL-7 “Efficacy-New Indication” 获批，作为 AI 再定位进入监管批准的行业案例；资产归 Eli Lilly，不归 BenevolentAI。[FDA NDA 207924](https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&ApplNo=207924)

### 4.3_靶点疾病药物关系建模
## 五、D 资产验证

| 公司 | 资产/项目 | 适应症/靶点 | 最高阶段 | 日期/状态 | 来源类型 | 证据 |
|---|---|---|---|---|---|---|
| Insilico | INS018_055 | Idiopathic Pulmonary Fibrosis；公司称 novel AI-discovered target / generated molecule | Phase II | ClinicalTrials.gov：RECRUITING；Start 2024-02-08；Completion 2026-02-28；Enrollment 40 | 临床注册 | [NCT05975983](https://clinicaltrials.gov/study/NCT05975983) |
| Insilico | INS018_055 Phase I | IPF/healthy subjects | Phase I completed | Start 2022-02-21；Completion 2022-12-02；Enrollment 78 | 临床注册 | [NCT05154240](https://clinicaltrials.gov/study/NCT05154240) |
| Insilico | ISM3091 | USP1 inhibitor；synthetic lethality in BRCA-mutated tumors | FDA IND cleared / 授权后临床开发权给 Exelixis | 2023-04 IND cleared；2023-09-12 global license | 合作/授权公告 | [BusinessWire](https://www.businesswire.com/news/home/20230912041846/en/Exelixis-and-Insilico-Medicine-Enter-into-Exclusive-Global-License-Agreement-for-ISM3091-a-Potentially-Best-in-Class-USP1-Inhibitor) |
| Insilico | 公司整体管线 | 多项目 | 公司自述 13 pipelines received IND approval；31 PCC nominated since 2021 | 2026-06-23 访问 | 公司管线页 | [Insilico Pipeline](https://insilico.com/pipeline) |
| Verge | VRG50635 | ALS / PIKfyve inhibitor | Phase 1 healthy completed；ALS Phase 1 terminated | 健康志愿者 NCT06286475 completed；ALS NCT06215755 terminated | 临床注册 | [NCT06286475](https://clinicaltrials.gov/study/NCT06286475)；[NCT06215755](https://clinicaltrials.gov/study/NCT06215755) |
| BenevolentAI | BEN-2293 | Mild-to-moderate atopic dermatitis | Phase 1/2 completed | Start 2020-10-14；Completion 2023-01-26；Enrollment 123 | 临床注册 | [NCT04737304](https://clinicaltrials.gov/study/NCT04737304) |
| CytoReason | 未检出 | 不适用 | 未检出自研资产 | 2026-06-23 | 官网/检索 | [CytoReason](https://www.cytoreason.com/) |
| BioMap | 未检出 | 不适用 | 未检出 PCC/IND/临床资产 | 2026-06-23 | 官网/检索 | [BioMap](https://www.biomap.com/) |

### 4.4_虚拟细胞和疾病模型
## 五、D 资产验证

- Recursion（监管/临床注册，访问 2026-06-23）：
  - REC-4881 FAP：ClinicalTrials.gov NCT05552755，Phase 1/2，Recruiting。来源：https://clinicaltrials.gov/study/NCT05552755
  - REC-1245：ClinicalTrials.gov NCT06678659，Phase 1/2，Recruiting。来源：https://clinicaltrials.gov/study/NCT06678659
  - EXS73565、EXS74539/REC-4539：ClinicalTrials.gov 列示 Exscientia AI Ltd. as wholly owned subsidiary of Recursion Pharmaceuticals, Inc. 的 Phase 1 项目。来源：https://clinicaltrials.gov/study/NCT06980116；https://clinicaltrials.gov/study/NCT07517198
- Cellarity（公司自述/官网，访问 2026-06-23）：CLY-124 为 sickle cell disease 的 first-in-class globin-switching oral medicine；公司称 2025-06 启动 first-in-human study，但本轮按 CLY-124 在 ClinicalTrials.gov API 未检出，需后续核查澳大利亚/新西兰/欧盟或其他注册库。来源：https://www.cellarity.com/pipeline
- Relation：官网仅披露 Discovery 阶段、bone disease/Osteoporosis/Osteomics；未检出 IND/临床资产。来源：https://www.relationrx.com/pipeline
- CytoReason：公司新闻稿明确“tech company, not a biotech company”“not to develop our own drugs”，未纳入资产验证。来源：https://cytoreason.com/resources/cytoreason-extends-its-collaboration-with-sanofi-to-advance-ai-driven-drug-discovery/
- BioMap：未检出公开自研临床管线/PCC/IND；当前以模型、系统与服务验证为主。来源：https://www.biomap.com/

### 4.5_药物组合和干预结果模拟
## 五、D 资产验证

- 2022-07-13 首次发布；2026-04 状态核验 / ClinicalTrials.gov / Lantern Pharma LP-300：NCT05456256，Phase II，LP-300 in Combination with Pemetrexed and Carboplatin vs pemetrexed/carboplatin，适应症为 never-smoker advanced lung adenocarcinoma/NSCLC；2026-04 verified，overall status Recruiting。来源：ClinicalTrials.gov API/页面 <https://clinicaltrials.gov/study/NCT05456256>。
- Exscientia/Turbine/KYAN：本轮未确认与本模块直接相关的 PCC/IND/临床组合资产；若有公司整体管线，不在本轮作为 4.5 强证据。

### 4.6_虚拟患者和数字孪生
## 五、D 资产验证

- 2026-06-23 / ClinicalTrials.gov：英矽智能 INS018_055/IPF 有 Phase I 完成、Phase II 完成/进行中记录：NCT05154240、NCT05938920、NCT05975983。证据类型：临床注册，https://clinicaltrials.gov/study/NCT05938920、https://clinicaltrials.gov/study/NCT05975983。
- 2026-06-23 / 公司官网：英矽智能 pipeline 页披露 40+ programs、31 PCC、13 pipelines received IND approval；但其并非严格虚拟患者/数字孪生公司。证据类型：公司自述，https://insilico.com/pipeline。
- 2026-06-23 / 公司官网：VeriSIM Life pipeline 页披露 PAH、substance use disorder、oncology 等资产组合，但未公开具体资产编号、IND/临床注册。证据类型：公司自述，https://www.verisimlife.com/our-pipeline。
- 2026-06-23 / ClinicalTrials.gov：VectorY PIONEER-ALS 相关 VTx-002 试验 NCT07287397 正在招募，Unlearn press 页披露其将应用数字孪生支持该研究；该资产属于合作方 VectorY。证据类型：临床注册/公司新闻，https://clinicaltrials.gov/study/NCT07287397、https://www.unlearn.ai/press。
- 2026-06-23 / 检索结果：Unlearn、QuantHealth、InSilicoTrials 未检出自研药物资产，更多是临床开发/模型平台。

