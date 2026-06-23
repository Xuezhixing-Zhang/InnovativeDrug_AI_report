#!/usr/bin/env bash
# 自治看门狗：等待配额重置 -> 跑一轮检索 pass -> 命中上限则退避重试 -> 直到 19 模块全部完成。
# 用法: watchdog.sh [first_reset "YYYY-MM-DD HH:MM:SS"]
set -u
LOGDIR="/c/Users/27448/Desktop/DukeNUS/Internship/VC_Panlin/创新药开发流程总纲/AI scope for Innovative Drugs/AI Innovative Drugs Modality/检索结果库/00_总览与进度/_codex日志"
MODROOT="/c/Users/27448/Desktop/DukeNUS/Internship/VC_Panlin/创新药开发流程总纲/AI scope for Innovative Drugs/AI Innovative Drugs Modality/检索结果库/01_技术模块检索"
DRIVER="$LOGDIR/run_module.sh"
SPEC="$LOGDIR/spec_remaining.txt"
WLOG="$LOGDIR/_watchdog.log"
FIRST_RESET="${1:-2026-06-23 02:10:00}"
BACKOFF=1500   # 命中上限后退避 25 分钟再试（窗口为滚动式，重试很廉价）
MAXPASS=60

count_done() {
  local n=0
  while IFS= read -r f; do
    [ "$(grep -c '' "$f" 2>/dev/null)" -ge 25 ] && n=$((n+1))
  done < <(find "$MODROOT" -name "检索结果.md" 2>/dev/null)
  echo "$n"
}

echo "[$(date '+%F %T')] 看门狗启动；目标 19 模块；首个重置 $FIRST_RESET" >> "$WLOG"

# 初次等待到已知重置时刻
tgt=$(date -d "$FIRST_RESET" +%s 2>/dev/null || echo "")
now=$(date +%s)
if [ -n "$tgt" ] && [ "$tgt" -gt "$now" ]; then
  wait_s=$((tgt-now))
  echo "[$(date '+%F %T')] 等待配额重置，sleep ${wait_s}s" >> "$WLOG"
  sleep "$wait_s"
fi

for i in $(seq 1 $MAXPASS); do
  d0=$(count_done)
  echo "[$(date '+%F %T')] === pass $i 开始（已完成 ${d0}/19）===" >> "$WLOG"
  bash "$DRIVER" "$SPEC"
  rc=$?
  d1=$(count_done)
  echo "[$(date '+%F %T')] pass $i 结束 rc=$rc（已完成 ${d1}/19）" >> "$WLOG"
  if [ "$d1" -ge 19 ]; then
    echo "[$(date '+%F %T')] 🎉 全部 19 模块完成" >> "$WLOG"
    echo "ALL_DONE" > "$LOGDIR/_STATUS"
    break
  fi
  echo "[$(date '+%F %T')] 退避 ${BACKOFF}s 后重试（配额未恢复或仍有缺口）" >> "$WLOG"
  sleep "$BACKOFF"
done

echo "[$(date '+%F %T')] 看门狗退出，最终完成 $(count_done)/19" >> "$WLOG"
