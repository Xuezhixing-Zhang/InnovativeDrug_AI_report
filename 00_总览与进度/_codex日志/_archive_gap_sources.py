import csv
import html
import os
import re
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Tuple
from urllib.parse import quote, urlparse

import requests


ROOT = Path.cwd()
DATE = "2026-06-23"
REPORT = ROOT / "00_总览与进度" / "_codex日志" / "_download_report.tsv"


SESSION = requests.Session()
SESSION.headers.update(
    {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
        ),
        "Accept": "text/html,application/xhtml+xml,application/pdf,*/*;q=0.8",
    }
)


@dataclass
class Item:
    key: str
    module: str
    title: str
    url: str
    kind: str = "网页"
    candidates: List[str] = field(default_factory=list)


def clean_url(url: str) -> str:
    url = url.strip()
    url = re.sub(r"^<|>$", "", url)
    url = url.split("；")[0].split(";官网首页")[0].split("；官网首页")[0]
    url = url.split("，")[0].split("、")[0]
    url = re.sub(r"[>。；;]+$", "", url)
    url = url.strip("<>")
    return url


def module_dir(module_short: str) -> Path:
    prefix = module_short.split("_", 1)[0]
    matches = [
        p
        for p in (ROOT / "01_技术模块检索").rglob("*")
        if p.is_dir() and p.name.startswith(prefix + "_")
    ]
    if not matches:
        raise FileNotFoundError(module_short)
    return matches[0] / "下载资料"


def safe_name(text: str, suffix: str) -> str:
    text = re.sub(r"https?://", "", text)
    text = re.sub(r"[^0-9A-Za-z\u4e00-\u9fff._-]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("._")
    return (text[:120] or "source") + suffix


def jina_url(url: str) -> str:
    return "https://r.jina.ai/" + url


def jina_url_normal(url: str) -> str:
    return "https://r.jina.ai/" + url


def jina_direct(url: str) -> str:
    return "https://r.jina.ai/" + url


def jina_plain(url: str) -> str:
    return "https://r.jina.ai/" + url


def jina(url: str) -> str:
    return "https://r.jina.ai/" + url


def jina_good(url: str) -> str:
    return "https://r.jina.ai/" + url


def rjina(url: str) -> str:
    return "https://r.jina.ai/" + url


def rjina_real(url: str) -> str:
    return "https://r.jina.ai/" + url


def r_jina(url: str) -> str:
    return "https://r.jina.ai/" + url


def jina_fetch_url(url: str) -> str:
    return "https://r.jina.ai/" + url


def rjina_doc(url: str) -> str:
    return "https://r.jina.ai/" + url


def rjina_simple(url: str) -> str:
    return "https://r.jina.ai/" + url


def rjina_slash(url: str) -> str:
    return "https://r.jina.ai/" + url


def rjina_clean(url: str) -> str:
    return "https://r.jina.ai/" + url


def rjina_correct(url: str) -> str:
    return "https://r.jina.ai/" + url


def jina_correct(url: str) -> str:
    return "https://r.jina.ai/" + url


def jina_prefix(url: str) -> str:
    return "https://r.jina.ai/" + url


def jina_actual(url: str) -> str:
    return "https://r.jina.ai/" + url


def to_markdown(raw: bytes, content_type: str, source_url: str, method: str, original: str) -> str:
    text = raw.decode("utf-8", errors="replace")
    if "<html" in text[:1000].lower() or "<!doctype html" in text[:1000].lower():
        title = ""
        m = re.search(r"<title[^>]*>(.*?)</title>", text, re.I | re.S)
        if m:
            title = html.unescape(re.sub(r"\s+", " ", m.group(1)).strip())
        text = re.sub(r"(?is)<(script|style|noscript|svg).*?</\1>", " ", text)
        text = re.sub(r"(?s)<br\s*/?>", "\n", text)
        text = re.sub(r"(?s)</(p|div|h[1-6]|li|tr)>", "\n", text)
        text = re.sub(r"(?s)<[^>]+>", " ", text)
        text = html.unescape(text)
        text = re.sub(r"[ \t\r\f\v]+", " ", text)
        text = re.sub(r"\n\s+", "\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text).strip()
        if title and title not in text[:500]:
            text = "# " + title + "\n\n" + text
    header = (
        f"原始URL：{original}\n\n"
        f"抓取方式：{method}\n\n"
        f"抓取日期：{DATE}\n\n"
        f"最终来源：{source_url}\n\n---\n\n"
    )
    return header + text.strip() + "\n"


def is_bad_text(text: str) -> bool:
    low = text.lower()
    bad_markers = [
        "just a moment",
        "enable javascript",
        "access denied",
        "not found",
        "request unsuccessful",
        "checking your browser",
        "attention required",
        "captcha",
        "blocked",
    ]
    if len(text.encode("utf-8", errors="ignore")) < 1024:
        return True
    if any(marker in low[:4000] for marker in bad_markers):
        return True
    return False


def download(url: str, timeout: int = 30):
    try:
        res = SESSION.get(url, timeout=timeout, allow_redirects=True)
        return res
    except Exception as exc:
        return exc


def save_item(item: Item, url: str, method: str):
    res = download(url)
    if isinstance(res, Exception):
        return False, f"{method}: {type(res).__name__}: {res}"
    raw = res.content or b""
    ctype = res.headers.get("content-type", "")
    if raw[:5] == b"%PDF-" and len(raw) > 5000:
        outdir = module_dir(item.module)
        outdir.mkdir(exist_ok=True)
        out = outdir / safe_name(f"{item.key}_{item.title}_{DATE}", ".pdf")
        out.write_bytes(raw)
        return True, str(out.relative_to(ROOT))
    md = to_markdown(raw, ctype, res.url, method, item.url)
    body = md.split("---", 1)[-1]
    if is_bad_text(body):
        return False, f"{method}: bad_or_tiny {len(raw)} {res.status_code} {res.url}"
    outdir = module_dir(item.module)
    outdir.mkdir(exist_ok=True)
    out = outdir / safe_name(f"{item.key}_{item.title}_{DATE}", ".md")
    out.write_text(md, encoding="utf-8")
    return True, str(out.relative_to(ROOT))


def make_items() -> List[Item]:
    items: List[Item] = []
    with REPORT.open("r", encoding="utf-8") as f:
        for row in csv.reader(f, delimiter="\t"):
            if len(row) >= 3 and row[2].startswith(("FAIL_empty", "FAIL_tiny")):
                module, url = row[0], clean_url(row[1])
                if not url.startswith("http"):
                    continue
                key = module.split("_", 1)[0]
                slug = urlparse(url).path.strip("/").split("/")[-1] or urlparse(url).netloc
                items.append(Item(key=key, module=module, title=slug[:80], url=url))

    extras = [
        Item("1.4", "1.4_分子从头生成和多参数优化", "Nature_Medicine_2025_41591_2025_3743", "https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_pdf/43/5e/41591_2025_Article_3743.PMC12353801.pdf", "论文"),
        Item("1.4", "1.4_分子从头生成和多参数优化", "Scientific_Data_2024_41597_2024_3793", "https://ftp.ncbi.nlm.nih.gov/pub/pmc/oa_pdf/9d/26/41597_2024_Article_3793.PMC11387650.pdf", "论文"),
        Item("2.2", "2.2_抗体亲和力_特异性_可开发性优化", "mAbs_KMAB_17_2598093", "https://pmc.ncbi.nlm.nih.gov/articles/PMC12688275/pdf/KMAB_17_2598093.pdf", "论文"),
        Item("2.2", "2.2_抗体亲和力_特异性_可开发性优化", "FDA_Bispecific_Antibody_Development_Programs_Guidance", "https://www.fda.gov/regulatory-information/search-fda-guidance-documents/bispecific-antibody-development-programs-guidance-industry", "监管"),
        Item("3.1", "3.1_siRNA_ASO_mRNA序列与修饰优化", "Science_adr8470", "https://www.science.org/doi/pdf/10.1126/science.adr8470", "论文"),
        Item("4.1", "4.1_多组学和疾病机制整合", "BioMap_Official_Website", "https://www.biomap.com/", "公司官网"),
    ]
    seen = {(i.module, i.url) for i in items}
    for item in extras:
        if (item.module, item.url) not in seen:
            items.append(item)
    return items


def candidates_for(item: Item) -> List[Tuple[str, str]]:
    url = clean_url(item.url)
    out = [(url, "原始/清洗URL")]
    parsed = urlparse(url)
    if parsed.netloc in {"www.businesswire.com", "businesswire.com"}:
        out.append((f"https://r.jina.ai/{url}", "r.jina.ai镜像"))
        out.append((f"https://r.jina.ai/https://web.archive.org/web/2026/{url}", "r.jina.ai+WebArchive"))
    elif parsed.netloc.endswith("biomap.com") or parsed.netloc.endswith("profluent.bio") or parsed.netloc.endswith("clinicaltrialsarena.com") or parsed.netloc.endswith("fda.gov") or parsed.netloc.endswith("sanofi.com"):
        out.append((f"https://r.jina.ai/{url}", "r.jina.ai镜像"))
        out.append((f"https://r.jina.ai/https://web.archive.org/web/2026/{url}", "r.jina.ai+WebArchive"))
    elif "science.org/doi/pdf" in url:
        article = url.replace("/doi/pdf/", "/doi/")
        out.append((article, "Science DOI页面"))
        out.append((f"https://r.jina.ai/{article}", "r.jina.ai Science DOI页面"))
    elif parsed.netloc.endswith("pmc.ncbi.nlm.nih.gov"):
        article = re.sub(r"/pdf/.*$", "/", url)
        out.append((article, "PMC文章页"))
        out.append((f"https://r.jina.ai/{article}", "r.jina.ai PMC文章页"))
    elif parsed.netloc.endswith("ftp.ncbi.nlm.nih.gov"):
        out.append((f"https://r.jina.ai/{url}", "r.jina.ai NCBI文件页"))
    else:
        out.append((f"https://r.jina.ai/{url}", "r.jina.ai镜像"))

    if "207924s006lbl.pdf" in url:
        out.extend(
            [
                ("https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/207924s006lbl.pdf", "FDA accessdata直链"),
                ("https://dailymed.nlm.nih.gov/dailymed/search.cfm?query=207924", "DailyMed检索"),
            ]
        )
    if "215390s000lbl.pdf" in url:
        out.extend(
            [
                ("https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/215390s000lbl.pdf", "FDA accessdata直链"),
                ("https://dailymed.nlm.nih.gov/dailymed/search.cfm?query=215390", "DailyMed检索"),
            ]
        )
    if "147629" in url or "bispecific-antibody" in url:
        out.extend(
            [
                ("https://www.fda.gov/media/123313/download", "FDA旧media候选"),
                ("https://www.fda.gov/regulatory-information/search-fda-guidance-documents/bispecific-antibody-development-programs-guidance-industry", "FDA指南页"),
            ]
        )
    if "PMC12353801" in url:
        out.append(("https://pmc.ncbi.nlm.nih.gov/articles/PMC12353801/", "PMC文章页"))
    if "PMC11387650" in url:
        out.append(("https://pmc.ncbi.nlm.nih.gov/articles/PMC11387650/", "PMC文章页"))
        out.append(("https://www.nature.com/articles/s41597-024-03793-8", "Nature文章页"))
    if "PMC12688275" in url:
        out.append(("https://pmc.ncbi.nlm.nih.gov/articles/PMC12688275/", "PMC文章页"))
    return out


def main() -> int:
    items = make_items()
    results = []
    for idx, item in enumerate(items, 1):
        print(f"[{idx}/{len(items)}] {item.module} {item.url}", flush=True)
        success = False
        notes = []
        for cand, method in candidates_for(item):
            ok, note = save_item(item, cand, method)
            notes.append(note)
            if ok:
                print(f"  OK {note}", flush=True)
                results.append((item.module, item.url, "OK", note))
                success = True
                break
            else:
                print(f"  miss {note}", flush=True)
            time.sleep(0.5)
        if not success:
            results.append((item.module, item.url, "FAIL", " | ".join(notes[-3:])))

    log = ROOT / "00_总览与进度" / "_codex日志" / f"_gap_archive_run_{DATE}.tsv"
    with log.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(["module", "url", "status", "note"])
        w.writerows(results)
    ok_count = sum(1 for r in results if r[2] == "OK")
    print(f"SUMMARY attempted={len(results)} ok={ok_count} fail={len(results)-ok_count}")
    print(log)
    return 0


if __name__ == "__main__":
    sys.exit(main())
