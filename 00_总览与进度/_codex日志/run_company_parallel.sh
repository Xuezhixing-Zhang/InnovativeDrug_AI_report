#!/usr/bin/env bash
# 并行跑 19 张代表公司研究卡，最多 MAXJ 个并发，避免机器过载。
set -u
LD="/c/Users/27448/Desktop/DukeNUS/Internship/VC_Panlin/创新药开发流程总纲/AI scope for Innovative Drugs/AI Innovative Drugs Modality/检索结果库/00_总览与进度/_codex日志/stage2"
SPEC="$LD/spec_companies.txt"
MAXJ=6
cd "$LD/.."
echo "[$(date '+%F %T')] ===== 并行启动 19 张研究卡（并发上限 $MAXJ，priority 档）=====" >> "$LD/_parallel.log"
while IFS='|' read -r ID DIRF MODF SHORT; do
  [ -z "${ID:-}" ] && continue
  case "$ID" in \#*) continue;; esac
  while [ "$(jobs -rp | wc -l)" -ge "$MAXJ" ]; do sleep 5; done
  single="$LD/spec_single_${ID}.txt"
  printf '%s|%s|%s|%s\n' "$ID" "$DIRF" "$MODF" "$SHORT" > "$single"
  echo "[$(date '+%F %T')] 启动卡 $ID ($SHORT)" >> "$LD/_parallel.log"
  bash "$LD/../run_company.sh" "$single" &
  sleep 3
done < "$SPEC"
wait
echo "[$(date '+%F %T')] ===== 19 张研究卡批次全部退出 =====" >> "$LD/_parallel.log"
