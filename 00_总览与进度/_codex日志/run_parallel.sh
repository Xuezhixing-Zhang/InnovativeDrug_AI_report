#!/usr/bin/env bash
# 并行启动所有未完成模块（每个一个 codex exec，priority/fast 档），最后 wait。
# 复用 run_module.sh（含幂等跳过 + 限额检测）。日志各模块独立，互不冲突。
set -u
LD="/c/Users/27448/Desktop/DukeNUS/Internship/VC_Panlin/创新药开发流程总纲/AI scope for Innovative Drugs/AI Innovative Drugs Modality/检索结果库/00_总览与进度/_codex日志"
SPEC="$LD/spec_remaining.txt"
cd "$LD"

echo "[$(date '+%F %T')] ===== 并行启动剩余模块（priority 档）=====" >> "$LD/_parallel.log"
pids=""
while IFS='|' read -r ID DIRF MODF HEADING SHORT; do
  [ -z "${ID:-}" ] && continue
  case "$ID" in \#*) continue;; esac
  single="$LD/spec_single_${ID}.txt"
  printf '%s|%s|%s|%s|%s\n' "$ID" "$DIRF" "$MODF" "$HEADING" "$SHORT" > "$single"
  echo "[$(date '+%F %T')] 启动 $ID ($SHORT)" >> "$LD/_parallel.log"
  bash run_module.sh "$single" &
  pids="$pids $!"
  sleep 3   # 错开启动，降低同时初始化的峰值
done < "$SPEC"

echo "[$(date '+%F %T')] 全部已启动，pids:$pids，等待完成..." >> "$LD/_parallel.log"
wait
echo "[$(date '+%F %T')] ===== 并行批次全部退出 =====" >> "$LD/_parallel.log"
