#!/usr/bin/env bash
# 并行跑 19 个深挖补充，最多 MAXJ 并发。
set -u
LOGD="/c/Users/27448/Desktop/DukeNUS/Internship/VC_Panlin/创新药开发流程总纲/AI scope for Innovative Drugs/AI Innovative Drugs Modality/检索结果库/00_总览与进度/_codex日志"
SPEC="$LOGD/stage2/spec_companies.txt"
MAXJ=6
echo "[$(date '+%F %T')] ===== 并行启动 19 深挖补充（并发 $MAXJ，normal 档）=====" >> "$LOGD/stage2/_deep_parallel.log"
while IFS='|' read -r ID DIRF MODF SHORT; do
  [ -z "${ID:-}" ] && continue
  case "$ID" in \#*) continue;; esac
  while [ "$(jobs -rp | wc -l)" -ge "$MAXJ" ]; do sleep 5; done
  single="$LOGD/stage2/deep_single_${ID}.txt"
  printf '%s|%s|%s|%s\n' "$ID" "$DIRF" "$MODF" "$SHORT" > "$single"
  echo "[$(date '+%F %T')] 启动深补 $ID ($SHORT)" >> "$LOGD/stage2/_deep_parallel.log"
  bash "$LOGD/run_deepen.sh" "$single" &
  sleep 3
done < "$SPEC"
wait
echo "[$(date '+%F %T')] ===== 深挖补充批次全部退出 =====" >> "$LOGD/stage2/_deep_parallel.log"
