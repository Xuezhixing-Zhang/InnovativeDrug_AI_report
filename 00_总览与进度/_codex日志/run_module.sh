#!/usr/bin/env bash
# 用法: run_module.sh <specfile>
# specfile 每行: ID|DIRFOLDER|MODFOLDER|HEADING|SHORTNAME
# 幂等：已完成(检索结果.md >=25 行)的模块跳过。
# 限额保护：某模块日志出现 "hit your usage limit" 即停止本次 pass，等待配额重置后重跑。
# 注意：本脚本运行期间切勿用编辑器修改它（bash 按字节增量读取，改动会破坏正在执行的实例）。
set -u
CODEX="/c/Users/27448/AppData/Local/OpenAI/Codex/bin/8e55c2dd143b6354/codex.exe"
ROOT="/c/Users/27448/Desktop/DukeNUS/Internship/VC_Panlin/创新药开发流程总纲/AI scope for Innovative Drugs/AI Innovative Drugs Modality"
BASE="$ROOT/检索结果库"
CHECKLIST="$ROOT/AI创新药第一步检索Checklist_关键词与信息源.md"
METHOD="$ROOT/AI创新药报告_三阶段信息搜集与公司研究方法.md"
LOGDIR="$BASE/00_总览与进度/_codex日志"
SPEC="$1"

while IFS='|' read -r ID DIRF MODF HEADING SHORT; do
  [ -z "${ID:-}" ] && continue
  case "$ID" in \#*) continue;; esac
  RELP="01_技术模块检索/$DIRF/$MODF"
  OUTFILE="$BASE/$RELP/检索结果.md"
  LOG="$LOGDIR/mod_${ID}.jsonl"
  LAST="$LOGDIR/mod_${ID}_last.md"
  PROMPT="$LOGDIR/prompt_${ID}.txt"

  if [ -f "$OUTFILE" ] && [ "$(grep -c '' "$OUTFILE" 2>/dev/null)" -ge 25 ]; then
    echo "[$(date +%H:%M:%S)] --- 模块 $ID 已完成，跳过" >> "$LOGDIR/_driver.log"
    continue
  fi

  cat > "$PROMPT" <<EOF
你是药物发现行业资深 VC 研究分析师。执行 AI 创新药「第一步行业扫描」的一个技术模块（Stage 1，目标覆盖率/宽进，不做最终投资定论）。真实联网检索，不要编造；找不到如实标注。

## 本模块
${ID} ${SHORT}

## 关键词来源（先读取这两个文件，按本模块章节执行检索）
1. 检索 Checklist：${CHECKLIST}
   定位「${HEADING}」小节，执行其 A–G 六类的全部中文与英文查询式。
2. 方法论文档（更丰富关键词）：${METHOD}
   定位对应「${SHORT}」章节，补充其中英文关键词。

## 必须覆盖信息源
覆盖该模块 Checklist「必须检索的信息源」全部；尽量覆盖推荐源（bioRxiv、行业媒体、微信公众号 site:mp.weixin.qq.com）。中英文都要搜。

## 执行顺序（重要，避免预算耗尽）
1) 先完成 A–F 六类宽搜，收敛候选公司；
2) 立刻把结果写入主文件（见下）——最高优先级，先写文件再做别的；
3) 有余量再补证据与查询留痕；
4) 不要尝试下载任何文件。PDF/论文/公告/专利只在「待下载」表登记可直接下载的直链 URL，由编排方统一抓取。

## 主文件（UTF-8 写入）
相对路径：${RELP}/检索结果.md
结构：
# ${ID} ${SHORT} — 检索结果
## 一、搜索发现表（14字段：公司名称(中英)|国家/地区|技术一级方向|技术细分|具体技术流|主要输入|主要输出|湿实验能力|自研管线|最高资产阶段|商业模式|代表合作(含日期)|主要证据(类型+链接)|初步判断）— 目标 2–4 国外 + 1–3 国内
## 二、A 公司发现  ## 三、B 技术路线  ## 四、C 实验验证  ## 五、D 资产验证  ## 六、E 商业验证  ## 七、F 负面验证
（每条重大事实标 发生日期/披露日期/来源类型；区分 公司自述/合作方/论文/专利/监管）
## 八、信息源覆盖清单（逐项打勾 + 实际查询式）
## 九、证据分级（A监管/临床注册/合作方/财务 · B论文/专利/会议 · C公司公告官网 · D媒体 · E宣传）
## 十、待下载/未获取资料（表格：标题 | 类型 | 直链URL | 受阻原因/为何需要）

## 硬性目标
≥1 合作/授权案例；≥1 实验或PCC/IND/临床资产；≥1 失败/终止/转型案例。排除纯临床运营、患者招募、监管写作、医院管理、纯人力CRO。
完成后一句话总结：N公司/N合作/N负面/N待下载。
EOF

  echo "[$(date +%H:%M:%S)] >>> 模块 $ID ($SHORT) 开始" >> "$LOGDIR/_driver.log"
  "$CODEX" exec \
    --dangerously-bypass-approvals-and-sandbox \
    -c tools.web_search=true \
    --skip-git-repo-check \
    -C "$BASE" \
    --json -o "$LAST" \
    - < "$PROMPT" > "$LOG" 2>&1
  RC=$?

  if grep -q "hit your usage limit" "$LOG" 2>/dev/null; then
    echo "[$(date +%H:%M:%S)] !!! 模块 $ID 触发配额上限，停止本次 pass，等待重置后重跑" >> "$LOGDIR/_driver.log"
    echo "USAGE_LIMIT_HIT" > "$LOGDIR/_STATUS"
    exit 9
  fi

  if [ -f "$OUTFILE" ] && [ "$(grep -c '' "$OUTFILE" 2>/dev/null)" -ge 25 ]; then ST="OK 文件已生成"; else ST="WARN 文件缺失"; fi
  echo "[$(date +%H:%M:%S)] <<< 模块 $ID 结束 rc=$RC | $ST" >> "$LOGDIR/_driver.log"
done < "$SPEC"

echo "[$(date +%H:%M:%S)] ===== 本批次处理完成 =====" >> "$LOGDIR/_driver.log"
echo "PASS_DONE" > "$LOGDIR/_STATUS"
