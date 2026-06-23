#!/usr/bin/env bash
# 旗舰案例：英矽 + 晶泰 深度档案（并行）-> 横向对比（两档案完成后）。normal档，命中上限退避重试。
set -u
CODEX="/c/Users/27448/AppData/Local/OpenAI/Codex/bin/8e55c2dd143b6354/codex.exe"
BASE="/c/Users/27448/Desktop/DukeNUS/Internship/VC_Panlin/创新药开发流程总纲/AI scope for Innovative Drugs/AI Innovative Drugs Modality/检索结果库"
S2="$BASE/00_总览与进度/_codex日志/stage2"
OUT="$BASE/03_第二步筛选与深挖/02_旗舰案例_英矽_晶泰"
INS="$OUT/英矽智能_Insilico_深度档案.md"
XTP="$OUT/晶泰科技_XtalPi_深度档案.md"
CMP="$OUT/英矽_晶泰_横向对比.md"
WLOG="$S2/_anchor.log"
ok(){ [ -f "$1" ] && [ "$(grep -c '' "$1" 2>/dev/null)" -ge 40 ]; }
runp(){ "$CODEX" exec --dangerously-bypass-approvals-and-sandbox -c tools.web_search=true --skip-git-repo-check -C "$BASE" --json -o "$2" - < "$1" > "$3" 2>&1; }

echo "[$(date '+%F %T')] 旗舰案例编排启动" >> "$WLOG"
for i in $(seq 1 30); do
  echo "[$(date '+%F %T')] === pass $i (英矽:$(ok "$INS"&&echo Y||echo N) 晶泰:$(ok "$XTP"&&echo Y||echo N) 对比:$(ok "$CMP"&&echo Y||echo N)) ===" >> "$WLOG"
  pids=""
  ok "$INS" || { runp "$S2/prompt_insilico.txt" "$S2/ins_last.md" "$S2/ins.jsonl" & pids="$pids $!"; }
  sleep 3
  ok "$XTP" || { runp "$S2/prompt_xtalpi.txt" "$S2/xtp_last.md" "$S2/xtp.jsonl" & pids="$pids $!"; }
  [ -n "$pids" ] && wait $pids
  if ok "$INS" && ok "$XTP" && ! ok "$CMP"; then
    echo "[$(date '+%F %T')] 两档案完成，运行横向对比" >> "$WLOG"
    runp "$S2/prompt_compare.txt" "$S2/cmp_last.md" "$S2/cmp.jsonl"
  fi
  if ok "$INS" && ok "$XTP" && ok "$CMP"; then echo "[$(date '+%F %T')] 🎉 旗舰案例全部完成" >> "$WLOG"; echo DONE > "$S2/_anchor_STATUS"; break; fi
  lim=0
  for j in "$S2/ins.jsonl" "$S2/xtp.jsonl" "$S2/cmp.jsonl"; do grep -q "hit your usage limit" "$j" 2>/dev/null && lim=1; done
  [ "$lim" = "1" ] && { echo "[$(date '+%F %T')] 命中上限，退避1200s" >> "$WLOG"; sleep 1200; } || sleep 30
done
echo "[$(date '+%F %T')] 旗舰编排退出（英矽:$(ok "$INS"&&echo Y||echo N) 晶泰:$(ok "$XTP"&&echo Y||echo N) 对比:$(ok "$CMP"&&echo Y||echo N)）" >> "$WLOG"
