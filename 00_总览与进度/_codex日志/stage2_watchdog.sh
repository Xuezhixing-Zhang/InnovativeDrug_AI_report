#!/usr/bin/env bash
# Stage2 看门狗（normal 档）：等配额重置 -> 跑 19 研究卡 + 分类 + 下载重试 -> 直到完成；命中上限退避重试。
set -u
CODEX="/c/Users/27448/AppData/Local/OpenAI/Codex/bin/8e55c2dd143b6354/codex.exe"
BASE="/c/Users/27448/Desktop/DukeNUS/Internship/VC_Panlin/创新药开发流程总纲/AI scope for Innovative Drugs/AI Innovative Drugs Modality/检索结果库"
LOGD="$BASE/00_总览与进度/_codex日志"
S2="$LOGD/stage2"
CARDS="$BASE/03_第二步筛选与深挖/01_重点公司研究卡"
CLASSD="$BASE/03_第二步筛选与深挖/00_Stage2分类"
WLOG="$S2/_watchdog.log"
FIRST_RESET="${1:-2026-06-23 16:50:00}"
BACKOFF=1500

count_cards(){ local n=0; while IFS= read -r f; do [ "$(grep -c '' "$f" 2>/dev/null)" -ge 25 ] && n=$((n+1)); done < <(find "$CARDS" -name "*.md" 2>/dev/null); echo "$n"; }
count_class(){ find "$CLASSD" -name "*.md" 2>/dev/null | grep -c ''; }

run_one(){ # promptfile lastfile logfile
  "$CODEX" exec --dangerously-bypass-approvals-and-sandbox -c tools.web_search=true \
    --skip-git-repo-check -C "$BASE" --json -o "$2" - < "$1" > "$3" 2>&1
}

tgt=$(date -d "$FIRST_RESET" +%s 2>/dev/null || echo ""); now=$(date +%s)
if [ -n "$tgt" ] && [ "$tgt" -gt "$now" ]; then
  echo "[$(date '+%F %T')] 等待配额重置至 $FIRST_RESET（sleep $((tgt-now))s）" >> "$WLOG"; sleep $((tgt-now))
fi

for i in $(seq 1 60); do
  echo "[$(date '+%F %T')] === pass $i 开始（卡 $(count_cards)/19，分类 $(count_class)）===" >> "$WLOG"
  bash "$LOGD/run_company_parallel.sh"
  if [ "$(count_class)" -lt 3 ]; then run_one "$S2/prompt_stage2_class.txt" "$S2/class_last.md" "$S2/class.jsonl"; fi
  if [ ! -f "$S2/_dl_done" ]; then
    run_one "$S2/prompt_download_retry.txt" "$S2/dl_last.md" "$S2/dl_retry.jsonl"
    grep -q "hit your usage limit" "$S2/dl_retry.jsonl" 2>/dev/null || touch "$S2/_dl_done"
  fi
  c=$(count_cards); cl=$(count_class)
  echo "[$(date '+%F %T')] === pass $i 结束（卡 $c/19，分类 $cl）===" >> "$WLOG"
  if [ "$c" -ge 19 ] && [ "$cl" -ge 3 ] && [ -f "$S2/_dl_done" ]; then
    echo "[$(date '+%F %T')] 🎉 Stage2 全部完成" >> "$WLOG"; echo "ALL_DONE" > "$S2/_STATUS"; break
  fi
  echo "[$(date '+%F %T')] 退避 ${BACKOFF}s 后重试" >> "$WLOG"; sleep "$BACKOFF"
done
echo "[$(date '+%F %T')] 看门狗退出（卡 $(count_cards)/19，分类 $(count_class)）" >> "$WLOG"
