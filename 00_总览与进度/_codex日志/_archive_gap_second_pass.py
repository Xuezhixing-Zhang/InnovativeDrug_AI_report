import csv
import sys
from pathlib import Path

import _archive_gap_sources as base


ROOT = Path.cwd()
DATE = base.DATE


def run():
    tasks = [
        (
            base.Item(
                "3.4",
                "3.4_AAV和病毒载体衣壳设计",
                "Biogen_Capsigen_AAV_Capsids_Collaboration_2021",
                "https://capsigen.com/images/BIOGEN_AND_CAPSIGEN_ANNOUNCE-COLLABORATION.docx.pdf",
            ),
            "https://investors.biogen.com/news-releases/news-release-details/biogen-and-capsigen-announce-collaboration-discover-and-develop",
            "Biogen IR官方新闻稿替代",
        ),
        (
            base.Item(
                "4.4",
                "4.4_虚拟细胞和疾病模型",
                "ARC_Virtual_Cell_Challenge_2025_BioMap_Winner",
                "https://www.biomap.com/news/outperforming-thousands-of-teams-worldwide-biomap-wins-arcs-virtual-cell-challenge-2025",
            ),
            "https://arcinstitute.org/news/virtual-cell-challenge-2025-wrap-up",
            "ARC Institute官方获奖总结替代",
        ),
        (
            base.Item(
                "4.5",
                "4.5_药物组合和干预结果模拟",
                "Recursion_Exscientia_Complete_Business_Combination_2024",
                "https://investors.recursion.com/news-releases/news-release-details/recursion-and-exscientia-complete-business-combination",
            ),
            "https://ir.recursion.com/news-releases/news-release-details/recursion-and-exscientia-two-leaders-ai-drug-discovery-space/",
            "Recursion IR新域名官方新闻稿替代",
        ),
        (
            base.Item(
                "4.5",
                "4.5_药物组合和干预结果模拟",
                "KYAN_Technologies_Official_Website",
                "https://www.kyantherapeutics.com/",
            ),
            "https://kyantechnologies.com/",
            "KYAN更名/新官网替代",
        ),
        (
            base.Item(
                "4.5",
                "4.5_药物组合和干预结果模拟",
                "Sanofi_Exscientia_AI_Driven_Pipeline_2022",
                "https://www.sanofi.com/en/media-room/press-releases/2022/2022-01-07-07-00-00-2356182",
            ),
            "https://www.sanofi.com/en/media-room/press-releases/2022/2022-01-07-06-00-00-2362917",
            "Sanofi正确press-release ID官方稿替代",
        ),
        (
            base.Item(
                "4.6",
                "4.6_虚拟患者和数字孪生",
                "GNS_Rebrands_as_Aitia_2023",
                "https://www.businesswire.com/news/home/20220510005493/en/GNS-Healthcare-Rebrands-as-Aitia-to-Transform-Drug-Discovery-and-Development-with-Causal-AI-and-Digital-Twins",
            ),
            "https://www.prnewswire.com/news-releases/gns-rebrands-as-aitia-to-focus-on-ai-enabled-drug-discovery-301716045.html",
            "PRNewswire同主题新闻稿替代",
        ),
        (
            base.Item(
                "4.6",
                "4.6_虚拟患者和数字孪生",
                "FDA_AI_Regulatory_Decision_Making_Drug_Biological_Products_2025",
                "https://www.fda.gov/regulatory-information/search-fda-guidance-documents/artificial-intelligence-support-regulatory-decision-making-drug-and-biological-products",
            ),
            "https://www.fda.gov/media/184830/download",
            "FDA正确media ID PDF",
        ),
        (
            base.Item(
                "4.6",
                "4.6_虚拟患者和数字孪生",
                "FDA_AI_Regulatory_Decision_Making_Drug_Biological_Products_2025_Page",
                "https://www.fda.gov/regulatory-information/search-fda-guidance-documents/artificial-intelligence-support-regulatory-decision-making-drug-and-biological-products",
            ),
            "https://r.jina.ai/https://www.fda.gov/regulatory-information/search-fda-guidance-documents/considerations-use-artificial-intelligence-support-regulatory-decision-making-drug-and-biological",
            "r.jina.ai FDA正确指南页",
        ),
    ]
    rows = []
    for item, url, method in tasks:
        ok, note = base.save_item(item, url, method)
        if not ok and not url.startswith("https://r.jina.ai/"):
            ok, note = base.save_item(item, "https://r.jina.ai/" + url, "r.jina.ai " + method)
        print(("OK" if ok else "FAIL") + "\t" + item.module + "\t" + item.url + "\t" + note, flush=True)
        rows.append([item.module, item.url, "OK" if ok else "FAIL", note])
    log = ROOT / "00_总览与进度" / "_codex日志" / f"_gap_archive_second_pass_{DATE}.tsv"
    with log.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(["module", "url", "status", "note"])
        w.writerows(rows)
    print(log)


if __name__ == "__main__":
    sys.exit(run())
