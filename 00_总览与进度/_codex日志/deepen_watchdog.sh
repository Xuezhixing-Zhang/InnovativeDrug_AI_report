#!/usr/bin/env bash
# 深挖补充看门狗：并行跑 19 深补，命中上限退避重试，直到 19 个补充文件齐全。
set -u
LOGD="/c/Users/27448/Desktop/DukeNUS/Internship/VC_Panlin/创新药开发流程总纲/AI scope for Innovative Drugs/AI Innovative Drugs Modality/检索结果库/00_总览与进度/_codex日志"
CARDDIR="/c/Users/27448/Desktop/DukeNUS/Internship/VC_Panlin/创新药开发流程总纲/AI scope for Innovative Drugs/AI Innovative Drugs Modality/检索结果库/03_第二步筛选与深挖/01_重点公司研究卡"
WLOG="$LOGD/stage2/_deep_watchdog.log"
BACKOFF=1200
count(){ local n=0; while IFS= read -r f; do [ "$(grep -c '' "$f" 2>/dev/null)" -ge 25 ] && n=$((n+1)); done < <(find "$CARDDIR" -name "*深度补充*.md" 2>/dev/null); echo "$n"; }
echo "[$(date '+%F %T')] 深挖看门狗启动（目标 19 补充文件）" >> "$WLOG"
for i in $(seq 1 40); do
  echo "[$(date '+%F %T')] === pass $i 开始（深补 $(count)/19）===" >> "$WLOG"
  bash "$LOGD/run_deepen_parallel.sh"
  c=$(count)
  echo "[$(date '+%F %T')] === pass $i 结束（深补 $c/19）===" >> "$WLOG"
  [ "$c" -ge 19 ] && { echo "[$(date '+%F %T')] 🎉 深挖补充全部完成" >> "$WLOG"; echo DONE > "$LOGD/stage2/_deep_STATUS"; break; }
  echo "[$(date '+%F %T')] 退避 ${BACKOFF}s" >> "$WLOG"; sleep "$BACKOFF"
done
echo "[$(date '+%F %T')] 深挖看门狗退出（深补 $(count)/19）" >> "$WLOG"
