#!/usr/bin/env bash
# 机制图驱动：每细分代表公司 -> 选本主题下最重要技术 -> 机制说明 + 生成2张机制图(新AI/传统)。
# 用法: run_image.sh <specfile>  spec 行: ID|DIRFOLDER|MODFOLDER|SHORT
# normal档；幂等(说明md>=12行 且 新AI机制png存在 则跳过)；限额检测。运行中勿编辑。
set -u
CODEX="/c/Users/27448/AppData/Local/OpenAI/Codex/bin/8e55c2dd143b6354/codex.exe"
ROOT="/c/Users/27448/Desktop/DukeNUS/Internship/VC_Panlin/创新药开发流程总纲/AI scope for Innovative Drugs/AI Innovative Drugs Modality"
BASE="$ROOT/检索结果库"
LOGDIR="$BASE/00_总览与进度/_codex日志/stage2"
CARDDIR="$BASE/03_第二步筛选与深挖/01_重点公司研究卡"
IMGROOT="$BASE/03_第二步筛选与深挖/03_机制图"
SPEC="$1"

while IFS='|' read -r ID DIRF MODF SHORT; do
  [ -z "${ID:-}" ] && continue
  case "$ID" in \#*) continue;; esac
  RESULT="$BASE/01_技术模块检索/$DIRF/$MODF/检索结果.md"
  CARD="$CARDDIR/${ID}_代表公司研究卡.md"
  DIR="$IMGROOT/${ID}"
  MD="$DIR/${ID}_机制说明.md"; NEWPNG="$DIR/${ID}_新AI机制.png"
  LOG="$LOGDIR/img_${ID}.jsonl"; LAST="$LOGDIR/img_${ID}_last.md"; PROMPT="$LOGDIR/prompt_img_${ID}.txt"
  mkdir -p "$DIR"

  if [ -f "$MD" ] && [ "$(grep -c '' "$MD" 2>/dev/null)" -ge 12 ] && [ -f "$NEWPNG" ]; then
    echo "[$(date +%H:%M:%S)] --- 机制图 $ID 已存在，跳过" >> "$LOGDIR/_img_driver.log"; continue
  fi

  cat > "$PROMPT" <<EOF
你是资深计算药物化学/AI药物发现专家，为一份面向**领域专家读者**的投资报告撰写机制说明并生成机制配图。读者是懂行的科学家与专业投资人，因此内容必须**专业、准确、有技术细节**，不能停留在科普层面。先读资料、必要时联网核实技术细节。不要下载文件。

## 本细分主题（所选技术必须属于此主题，不得选公司在别的主题下的技术）
${ID} ${SHORT}

## 输入（先读，确定代表公司及其在本主题下的关键技术）
研究卡：${CARD}
检索结果：${RESULT}

## 步骤
1. 选定代表公司在【${SHORT}】主题下最重要、最具代表性的一项核心技术（必须紧扣本主题）。
2. 用**专家级深度**讲清其机制，必须具体到：
   - 模型/算法类型与架构（如：等变图神经网络/几何深度学习、扩散模型、Transformer/蛋白语言模型、流匹配、强化学习、主动学习、自由能微扰等——用该公司真实采用的具体方法，不可泛泛说"用AI"）；
   - 输入数据模态与表征（序列/3D结构/电子密度/组学/晶体/分子图/SMILES/构象系综等）；
   - 训练数据来源与规模、关键归纳偏置/物理先验；
   - 输出与下游如何衔接（打分、生成、排序、闭环到湿实验）；
   - 可量化的性能或工程指标（命中率、富集倍数、RMSD、成功率、通量、周期缩短等，有则给数、注明来源）。
3. 生成图像1【AI新方法机制】：一张**直观的中文科学插画/信息图(scientific illustration / infographic)**，核心要求：
   - **用真实视觉元素直接把机理"画"出来**，绝不要做成纯文字方框+箭头的流程图。按本技术画出对应的形象化图示，例如：蛋白质三维结构与结合口袋、小分子/配体停靠口袋、DNA/RNA 双螺旋、抗体 Y 形结构、细胞与细胞器、脂质纳米颗粒(LNP)包裹核酸、CRISPR-Cas 蛋白剪切 DNA、AAV 衣壳、机器人机械臂/自动化湿实验台、神经网络/扩散模型漏斗从海量分子筛出命中等；
   - **形象、直观、一眼看懂**，用箭头/流向表现机理关键步骤与物质/数据流；
   - 关键部位配**简洁中文标签**（标签短，少而精）；
   - 科学插画风格、配色专业干净、适合投资报告与路演配图。
   保存为：${NEWPNG}
4. 生成图像2【当前主流基线方法】：同样是**直观的中文科学插画**（非文字方框图），画当下创新药企业**实际成熟依赖、广泛使用**的主流方法（**不要画过时/教科书式的古老方法**）。按本主题选当下行业标准方法并**形象化呈现**：如基于物理的分子对接/自由能微扰 FEP+/分子动力学（画蛋白口袋+对接配体+能量面）、X射线晶体学/冷冻电镜（画晶体/电镜与解析出的结构）、QSAR 与体外 ADMET 测定（画化合物+96孔板/实验）、专家规则逆合成 CASP、噬菌体/酵母展示与定向进化（画噬菌体/酵母+文库轮选）、Rosetta 物理能量函数设计等。用画面表现其机理，并**直观呈现其瓶颈**（通量低/依赖人工/对新化学空间或难成药靶点受限）。关键处配简洁中文标签。保存为：${DIR}/${ID}_传统方法.png
5. 写说明文件（UTF-8，专家口吻、术语准确）→ ${MD}：
# ${ID} ${SHORT} — 代表公司核心机制（专家版）
## 代表公司 / 选定技术（为何这是本主题下最重要的技术，1-2句）
## AI新方法机制（配图：新AI机制.png）：模型架构 / 输入表征与数据 / 物理先验或归纳偏置 / 输出与闭环 / 关键创新点 / 量化指标(附来源)
## 当前主流基线方法机制（配图：传统方法.png）：当下行业实际在用的标准方法是什么、原理、为什么是"成熟可靠基线"、其瓶颈与局限
## AI方法相对当前基线的实质性进步（3-6条，针对专家：在哪些任务/指标/化学或序列空间上真正超越，哪些仍未解决）
## 图像准确性自检（图中标注/术语是否与说明一致；若生成的图内文字或公式有误，在此用准确文字校正）

重要：图像生成模型对精细文字/公式/中文字符易出错，因此：(a) 图以**形象化视觉为主**、文字标签尽量短而少；(b) md 用准确专业的中文文字把机理讲透（图为示意、文字为准）；(c) 若图内中文出现乱码或错字，在"图像准确性自检"小节用文字校正。两张图都必须是**有插画感的直观科学图**，不是文字方框流程图。完成后一句话总结：公司 + 选定技术 + 对比基线方法 + 两张图是否生成成功。
EOF

  echo "[$(date +%H:%M:%S)] >>> 机制图 $ID ($SHORT) 开始" >> "$LOGDIR/_img_driver.log"
  "$CODEX" exec --dangerously-bypass-approvals-and-sandbox -c tools.web_search=true \
    --skip-git-repo-check -C "$BASE" --json -o "$LAST" - < "$PROMPT" > "$LOG" 2>&1

  if grep -q "hit your usage limit" "$LOG" 2>/dev/null; then
    echo "[$(date +%H:%M:%S)] !!! 机制图 $ID 触发配额上限" >> "$LOGDIR/_img_driver.log"; echo "LIMIT" > "$LOGDIR/_img_STATUS"; exit 9
  fi
  if [ -f "$MD" ] && [ -f "$NEWPNG" ]; then ST="OK"; else ST="WARN 缺失"; fi
  echo "[$(date +%H:%M:%S)] <<< 机制图 $ID 结束 | $ST" >> "$LOGDIR/_img_driver.log"
done < "$SPEC"
echo "[$(date +%H:%M:%S)] ===== 机制图批次完成 =====" >> "$LOGDIR/_img_driver.log"
