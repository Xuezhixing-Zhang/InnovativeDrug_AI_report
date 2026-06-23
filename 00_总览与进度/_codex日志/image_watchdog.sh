#!/usr/bin/env bash
# 机制图看门狗：并行(cap4)跑19个机制图，命中上限退避重试，直到19套(说明md+新AI机制png)齐全。
set -u
LOGD="/c/Users/27448/Desktop/DukeNUS/Internship/VC_Panlin/创新药开发流程总纲/AI scope for Innovative Drugs/AI Innovative Drugs Modality/检索结果库/00_总览与进度/_codex日志"
SPEC="$LOGD/stage2/spec_companies.txt"
IMGROOT="/c/Users/27448/Desktop/DukeNUS/Internship/VC_Panlin/创新药开发流程总纲/AI scope for Innovative Drugs/AI Innovative Drugs Modality/检索结果库/03_第二步筛选与深挖/03_机制图"
WLOG="$LOGD/stage2/_img_watchdog.log"
MAXJ=10; BACKOFF=1200
count(){ local n=0 id; for id in 1.1 1.2 1.3 1.4 1.5 2.1 2.2 2.3 2.4 3.1 3.2 3.3 3.4 4.1 4.2 4.3 4.4 4.5 4.6; do
  [ -f "$IMGROOT/$id/${id}_机制说明.md" ] && [ -f "$IMGROOT/$id/${id}_新AI机制.png" ] && n=$((n+1)); done; echo "$n"; }
parallel_pass(){
  while IFS='|' read -r ID DIRF MODF SHORT; do
    [ -z "${ID:-}" ] && continue; case "$ID" in \#*) continue;; esac
    while [ "$(jobs -rp | wc -l)" -ge "$MAXJ" ]; do sleep 5; done
    single="$LOGD/stage2/img_single_${ID}.txt"
    printf '%s|%s|%s|%s\n' "$ID" "$DIRF" "$MODF" "$SHORT" > "$single"
    bash "$LOGD/run_image.sh" "$single" & sleep 2
  done < "$SPEC"
  wait
}
echo "[$(date '+%F %T')] 机制图看门狗启动（目标19）" >> "$WLOG"
for i in $(seq 1 40); do
  echo "[$(date '+%F %T')] === pass $i 开始（机制图 $(count)/19）===" >> "$WLOG"
  parallel_pass
  c=$(count); echo "[$(date '+%F %T')] === pass $i 结束（机制图 $c/19）===" >> "$WLOG"
  [ "$c" -ge 19 ] && { echo "[$(date '+%F %T')] 🎉 机制图全部完成" >> "$WLOG"; echo DONE > "$LOGD/stage2/_img_STATUS"; break; }
  echo "[$(date '+%F %T')] 退避 ${BACKOFF}s" >> "$WLOG"; sleep "$BACKOFF"
done
echo "[$(date '+%F %T')] 机制图看门狗退出（机制图 $(count)/19）" >> "$WLOG"
