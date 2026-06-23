#!/usr/bin/env bash
# 深挖补充驱动：对每个细分已选代表公司，补【创始人画像·商业风格·业务历史·公开观点】。
# 用法: run_deepen.sh <specfile>  spec 行: ID|DIRFOLDER|MODFOLDER|SHORT
# normal 档；幂等（补充文件>=25行则跳过）；限额检测。运行中勿编辑。
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
  SUPP="$CARDDIR/${ID}_深度补充_创始人与商业.md"
  LOG="$LOGDIR/deep_${ID}.jsonl"; LAST="$LOGDIR/deep_${ID}_last.md"; PROMPT="$LOGDIR/prompt_deep_${ID}.txt"

  if [ -f "$SUPP" ] && [ "$(grep -c '' "$SUPP" 2>/dev/null)" -ge 25 ]; then
    echo "[$(date +%H:%M:%S)] --- 深补 $ID 已存在，跳过" >> "$LOGDIR/_deep_driver.log"; continue
  fi

  cat > "$PROMPT" <<EOF
你是资深VC尽调分析师，对一家已初步研究的AI制药公司做**深度补充尽调**，重点不在AI技术本身，而在【创始人画像·商业风格·业务历史·公开观点】——这是 AI制药投资策略 的核心：范式变迁(用AI加速旧流程 vs 用AI创造新可能性)、商业模式(服务型类CRO / 自主新药研发 / 兼具)、以及"创始人是AI背景还是生物背景，如何决定研发思路与业务模式"。真实联网深挖，标注来源与日期，先写文件骨架再补，不要下载文件。

## 输入
技术细分：${ID} ${SHORT}
已有研究卡（先读，沿用其选定的代表公司；若原卡创始人/团队为"待补充"，本次必须补全）：${CARD}
第一轮检索结果：${RESULT}

## 必须深挖维度（中英双语，逐条附来源链接+日期，区分一手公司/本人 vs 二手媒体）
A. 创始人深度画像：每位创始人/CEO/CSO 的 姓名 / 教育(学校·博士导师·专业) / 履历(前公司·职位·年限) / 背景定性(AI-计算 / 生物-医学 / 药化 / 临床 / 商业) / 是否曾把药物推进到临床或上市 / 代表论文专利成果。搜 创始人姓名+LinkedIn / Google Scholar / 前公司、\`公司名 founder background\`。
B. 创始人背景→战略影响【投资策略核心问题】：该团队是AI背景主导还是生物/药背景主导？这如何决定 平台优先 vs 资产优先、业务模式、管线策略？与同赛道不同背景创始人公司相比的显著差异。
C. 商业风格与模式分类：归入 服务型(类CRO) / 自主主导新药研发 / 两者兼具；收入结构(软件/服务/首付/里程碑/自研资产)；是否保留资产权益；属"用AI加速旧流程"还是"用AI创造新可能性"。
D. 业务历史与叙事变迁：创立故事、历轮融资时间线、重大转折/转型/更名、并购或上市、技术叙事是否随时间漂移、是否反复更换故事。
E. 公开演讲与公开观点：创始人/高管的会议主旨演讲(JPM/BIO/AACR/炉边对话)、播客、深度采访、署名观点/社交媒体；其对AI制药的判断/预测/大胆主张，以及事后是否兑现。搜 \`创始人姓名 interview/keynote/podcast/talk\`、\`公司名 founder opinion\`。

## 输出（UTF-8 写入，不覆盖原卡）→ ${SUPP}
# ${ID} ${SHORT} — 深度补充：创始人画像·商业风格·公开观点
## 代表公司：<沿用原卡公司名>
## A 创始人深度画像（逐人，附来源）
## B 创始人背景 → 研发思路与商业模式 的影响分析【核心】
## C 商业风格与模式分类（服务/自主/兼具 + 收入结构 + 资产权益 + 加速旧流程/创造新可能性）
## D 业务历史与叙事变迁（时间线 + 转型/更名/并购/上市 + 叙事是否漂移）
## E 公开演讲与公开观点（演讲/采访/播客/署名观点 + 关键主张 + 是否兑现，逐条链接+日期）
## F 仍缺口（仍未找到、建议进一步检索的点）

完成后一句话总结：代表公司 + 创始人背景类型 + 商业模式归类 + 是否"创造新可能性"。
EOF

  echo "[$(date +%H:%M:%S)] >>> 深补 $ID ($SHORT) 开始" >> "$LOGDIR/_deep_driver.log"
  "$CODEX" exec --dangerously-bypass-approvals-and-sandbox -c tools.web_search=true \
    --skip-git-repo-check -C "$BASE" --json -o "$LAST" - < "$PROMPT" > "$LOG" 2>&1

  if grep -q "hit your usage limit" "$LOG" 2>/dev/null; then
    echo "[$(date +%H:%M:%S)] !!! 深补 $ID 触发配额上限" >> "$LOGDIR/_deep_driver.log"; echo "LIMIT" > "$LOGDIR/_deep_STATUS"; exit 9
  fi
  if [ -f "$SUPP" ] && [ "$(grep -c '' "$SUPP" 2>/dev/null)" -ge 25 ]; then ST="OK"; else ST="WARN 缺失"; fi
  echo "[$(date +%H:%M:%S)] <<< 深补 $ID 结束 | $ST" >> "$LOGDIR/_deep_driver.log"
done < "$SPEC"
echo "[$(date +%H:%M:%S)] ===== 深补批次完成 =====" >> "$LOGDIR/_deep_driver.log"
