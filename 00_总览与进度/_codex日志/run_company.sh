#!/usr/bin/env bash
# 深挖驱动：每个技术细分 -> Codex 自选 1 家代表公司 -> 深度研究卡（重创始人/团队/新闻）。
# 用法: run_company.sh <specfile>   spec 每行: ID|DIRFOLDER|MODFOLDER|SHORT
# priority(fast) 档；幂等跳过；限额检测。运行中勿编辑本脚本。
set -u
CODEX="/c/Users/27448/AppData/Local/OpenAI/Codex/bin/8e55c2dd143b6354/codex.exe"
ROOT="/c/Users/27448/Desktop/DukeNUS/Internship/VC_Panlin/创新药开发流程总纲/AI scope for Innovative Drugs/AI Innovative Drugs Modality"
BASE="$ROOT/检索结果库"
LOGDIR="$BASE/00_总览与进度/_codex日志/stage2"
CARDDIR="$BASE/03_第二步筛选与深挖/01_重点公司研究卡"
SPEC="$1"

while IFS='|' read -r ID DIRF MODF SHORT; do
  [ -z "${ID:-}" ] && continue
  case "$ID" in \#*) continue;; esac
  RESULT="$BASE/01_技术模块检索/$DIRF/$MODF/检索结果.md"
  CARD="$CARDDIR/${ID}_代表公司研究卡.md"
  LOG="$LOGDIR/card_${ID}.jsonl"; LAST="$LOGDIR/card_${ID}_last.md"; PROMPT="$LOGDIR/prompt_card_${ID}.txt"

  if [ -f "$CARD" ] && [ "$(grep -c '' "$CARD" 2>/dev/null)" -ge 25 ]; then
    echo "[$(date +%H:%M:%S)] --- 卡 $ID 已存在，跳过" >> "$LOGDIR/_driver.log"; continue
  fi

  cat > "$PROMPT" <<EOF
你是药物发现行业资深VC分析师，执行「第三步：单公司深度研究」。任务：从指定技术细分的第一轮检索结果中**自动挑选 1 家最具代表性的公司**（平台+实验+资产+商业化证据最强者；可与其它细分重复），对其做深度尽调。真实联网检索，不编造，标注日期与来源。先写文件骨架再补充，避免预算耗尽；不要下载文件。

## 输入
技术细分：${ID} ${SHORT}
该模块第一轮检索结果（含候选公司与证据，先读取）：${RESULT}

## 联网深挖（针对所选公司，中英双语）
- 创始人/CEO：\`公司名 founder\`、\`公司名 创始人 采访\`、\`公司名 CEO interview\`、创始人姓名 + drug discovery / publications / patents / 过往任职
- 资本与管线：\`公司名 funding/investors\`、\`公司名 pipeline/PCC/IND/clinical/NCT\`
- 商业化：\`公司名 partnership/licensing/upfront/milestone\`、合作药企名+公司名
- 反面：\`公司名 layoffs/discontinued/terminated/pivot/controversy\`

## 输出研究卡（UTF-8 写入）→ ${CARD}
# ${ID} ${SHORT} — 代表公司深度研究卡
## 0. 选择理由（为何这家代表本细分）
## 1. 基本信息与时间线（成立/总部/历轮融资与投资人/当前阶段/上市或私有；关键里程碑时间线，区分 公司宣布/实验完成/数据公开/临床注册/首例入组/结果发布）
## 2. 创始人与核心团队【重点】（创始人背景=AI/计算/生物/药化/临床？是否曾推进药物入临床？核心团队药化/DMPK/毒理/CMC/临床是否齐全？关键人物过往经历、前公司、代表成果，逐条附来源）
## 3. 技术平台（输入/任务/输出/湿实验/自动化/闭环/跨靶点-疾病-模态复用）
## 4. 数据壁垒（来源/是否含负数据/是否持续产生/是否独占/数据飞轮）
## 5. 管线与资产（自研vs合作分列：靶点/适应症/模态/阶段/AI贡献/最新进展；PCC/IND/临床/终止）
## 6. 商业化与BD（合作方质量/模式/首付款/里程碑/权益/重复或扩大；区分理论总额vs实际收入）
## 7. 论文/专利/外部验证（方法vs药物项目论文；专利保护对象；按证据级别 A监管/临床·B论文/专利·C公司公告·D媒体·E宣传 标注）
## 8. 反面信息与风险（临床失败/管线停更/合作退出/裁员/转型/叙事变化）
## 9. 投资判断（问题是否重要/AI是否不可替代/闭环是否真实/是否已产资产/壁垒/最大风险/2-3年价值拐点/重点投资|持续跟踪|仅案例）
## 10. 关键事实来源清单（链接 + 证据级别）
## 11. 本技术细分价值定性【降本增效 vs 范式重构】（用户重点要求，针对本细分而非仅这家公司）
判断本细分属于：
- (A) **降本增效**：不改变创新药研发基本流程，只提升效率/准确性/成功率/资本效率。论证：替代了哪些计算/实验/人工；是否减少需合成、表达或测试的候选物数量；是否提高筛选命中率；是否缩短研发周期；是否提前识别成药性/毒性/可开发性风险；是否有量化数据与外部验证；未来 3-5 年能否形成规模化商业价值。
- (B) **范式重构**：使传统方法难以在可接受成本/时间/数据规模下完成的任务首次具备规模化实施可能。论证：传统方法为何难；新一代 AI 相比早期单输入/低性能模型新增了什么能力；是否已有真实公司/实验/药物资产/商业合作验证；革命性价值是已实现还是仍处理论与早期；距大规模产业应用还缺什么。
给出结论：**A / B / 兼有**，并标注当前阶段（已成熟应用 / 初步商业化 / 产业验证期 / 科研与概念验证期 / 长期前沿）及判断依据。避免"过去完全做不到""AI必然颠覆"等绝对表述。

最近核验日期 2026-06-23。完成后一句话总结：代表公司名 + 最高验证级别 + 投资定位 + 本细分价值定性(降本增效/范式重构/兼有 + 阶段)。
EOF

  echo "[$(date +%H:%M:%S)] >>> 卡 $ID ($SHORT) 开始" >> "$LOGDIR/_driver.log"
  "$CODEX" exec --dangerously-bypass-approvals-and-sandbox -c tools.web_search=true \
    --skip-git-repo-check -C "$BASE" --json -o "$LAST" - < "$PROMPT" > "$LOG" 2>&1

  if grep -q "hit your usage limit" "$LOG" 2>/dev/null; then
    echo "[$(date +%H:%M:%S)] !!! 卡 $ID 触发配额上限" >> "$LOGDIR/_driver.log"; echo "USAGE_LIMIT_HIT" > "$LOGDIR/_STATUS"; exit 9
  fi
  if [ -f "$CARD" ] && [ "$(grep -c '' "$CARD" 2>/dev/null)" -ge 25 ]; then ST="OK"; else ST="WARN 缺失"; fi
  echo "[$(date +%H:%M:%S)] <<< 卡 $ID 结束 | $ST" >> "$LOGDIR/_driver.log"
done < "$SPEC"
echo "[$(date +%H:%M:%S)] ===== 批次完成 =====" >> "$LOGDIR/_driver.log"
