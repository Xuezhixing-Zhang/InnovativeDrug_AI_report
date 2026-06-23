#!/usr/bin/env bash
# 读取 _待下载清单_汇总.tsv（列: 模块短名<TAB>URL），智能下载到各模块 下载资料/。
# 校验文件头：%PDF -> .pdf；HTML -> .html；空/拦截页 -> 记入 gap 报告。
set -u
BASE="/c/Users/27448/Desktop/DukeNUS/Internship/VC_Panlin/创新药开发流程总纲/AI scope for Innovative Drugs/AI Innovative Drugs Modality/检索结果库"
TSV="$BASE/00_总览与进度/_待下载清单_汇总.tsv"
REPORT="$BASE/00_总览与进度/_codex日志/_download_report.tsv"
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
> "$REPORT"

dirfolder() {
  case "$1" in
    1.*) echo "方向一_AI小分子药物";;
    2.*) echo "方向二_AI大分子生物药";;
    3.*) echo "方向三_CGT核酸和递送";;
    4.*) echo "方向四_数字生物模型";;
  esac
}

while IFS=$'\t' read -r mod url; do
  [ -z "${mod:-}" ] && continue
  id="${mod%%_*}"
  df=$(dirfolder "$id")
  outdir="$BASE/01_技术模块检索/$df/$mod/下载资料"
  mkdir -p "$outdir"
  # curl.exe(原生 Windows) 不能正确处理含中文的 -o 路径；改为 cd 进目录用 ASCII 相对名
  cd "$outdir" || { printf "%s\t%s\tFAIL_cd\t-\n" "$mod" "$url" >> "$REPORT"; continue; }

  # 跳过专利检索式（非单一文档）
  case "$url" in
    *"patents.google.com/?q="*|*"scholar.google.com/scholar?"*|*"google.com/search?"*|*"bing.com/search?"*)
      printf "%s\t%s\tSKIP_search_query\t-\n" "$mod" "$url" >> "$REPORT"; continue;;
  esac

  # 目标文件名
  base=$(echo "$url" | sed -E 's#https?://##; s#[/?&=:]+#_#g; s#_+#_#g' | cut -c1-90)
  tmp=".__tmp__"   # ASCII 相对名（cwd 已是 outdir）
  rm -f "$tmp"

  # 路由
  fetchurl="$url"
  case "$url" in
    *nature.com/articles/*)
      case "$url" in *.pdf) ;; *) fetchurl="${url}.pdf";; esac;;
    *pmc.ncbi.nlm.nih.gov/articles/PMC*/pdf/*)
      pmcid=$(echo "$url" | grep -oE 'PMC[0-9]+' | head -1)
      fetchurl="https://europepmc.org/backend/ptpmcrender.fcgi?accid=${pmcid}&blobtype=pdf";;
  esac

  curl.exe -sSL -A "$UA" --max-time 150 -o "$tmp" "$fetchurl" 2>/dev/null
  # PMC europepmc 偶发 HTTP/2 流错误时，用 http1.1 重试一次
  if [ ! -s "$tmp" ] && echo "$fetchurl" | grep -q europepmc; then
    curl.exe -sSL --http1.1 -A "$UA" --max-time 150 -o "$tmp" "$fetchurl" 2>/dev/null
  fi
  if [ ! -s "$tmp" ]; then
    printf "%s\t%s\tFAIL_empty\t%s\n" "$mod" "$url" "$fetchurl" >> "$REPORT"; rm -f "$tmp"; continue
  fi
  head4=$(head -c4 "$tmp" | tr -d '\0')
  sz=$(stat -c%s "$tmp")
  if [ "$head4" = "%PDF" ]; then
    out="$outdir/${base}.pdf"; mv -f "$tmp" "$out"
    printf "%s\t%s\tOK_pdf_%s\t%s\n" "$mod" "$url" "$sz" "$out" >> "$REPORT"
  elif [ "$sz" -lt 2500 ]; then
    # 太小，多半是拦截页/挑战页
    printf "%s\t%s\tFAIL_tiny_%s\t%s\n" "$mod" "$url" "$sz" "$fetchurl" >> "$REPORT"; rm -f "$tmp"
  else
    out="$outdir/${base}.html"; mv -f "$tmp" "$out"
    printf "%s\t%s\tOK_html_%s\t%s\n" "$mod" "$url" "$sz" "$out" >> "$REPORT"
  fi
done < "$TSV"

echo "=== 下载汇总 ==="
echo "OK_pdf : $(grep -c $'\tOK_pdf' "$REPORT")"
echo "OK_html: $(grep -c $'\tOK_html' "$REPORT")"
echo "SKIP   : $(grep -c 'SKIP_' "$REPORT")"
echo "FAIL   : $(grep -cE 'FAIL_' "$REPORT")"
