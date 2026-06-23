import textwrap
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


OUT_DIR = Path(__file__).resolve().parent

COLORS = {
    "blue": "#4E79A7",
    "sky": "#A0CBE8",
    "orange": "#F28E2B",
    "green": "#59A14F",
    "yellow": "#EDC948",
    "red": "#E15759",
    "purple": "#B07AA1",
    "teal": "#76B7B2",
    "gray": "#6B7280",
    "light": "#F7F9FB",
    "ink": "#1F2937",
}


def setup_canvas(title, subtitle=None):
    fig, ax = plt.subplots(figsize=(16, 9), dpi=220)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")
    fig.patch.set_facecolor("white")
    ax.text(0.03, 0.955, title, fontsize=20, weight="bold", color=COLORS["ink"], va="top")
    if subtitle:
        ax.text(0.03, 0.915, subtitle, fontsize=10.5, color=COLORS["gray"], va="top")
    return fig, ax


def wrap_label(text, width=26):
    return "\n".join(textwrap.wrap(text, width=width, break_long_words=False))


def box(ax, xy, wh, text, fc, ec=None, fontsize=9.5, weight="normal", radius=0.014, lw=1.2):
    x, y = xy
    w, h = wh
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle=f"round,pad=0.012,rounding_size={radius}",
        linewidth=lw,
        edgecolor=ec or fc,
        facecolor=fc,
        zorder=2,
    )
    ax.add_patch(patch)
    ax.text(
        x + w / 2,
        y + h / 2,
        wrap_label(text, max(12, int(w * 70))),
        ha="center",
        va="center",
        fontsize=fontsize,
        color=COLORS["ink"],
        weight=weight,
        linespacing=1.22,
        zorder=3,
    )
    return patch


def group_label(ax, text, x, y, color):
    ax.text(x, y, text, fontsize=12.5, weight="bold", color=color, va="bottom")


def arrow(ax, start, end, color=COLORS["gray"], lw=1.7, style="-|>", rad=0.0, dashed=False):
    arr = FancyArrowPatch(
        start,
        end,
        arrowstyle=style,
        mutation_scale=14,
        linewidth=lw,
        color=color,
        connectionstyle=f"arc3,rad={rad}",
        linestyle="--" if dashed else "-",
        shrinkA=4,
        shrinkB=4,
        zorder=1,
    )
    ax.add_patch(arr)
    return arr


def save(fig, stem):
    fig.savefig(OUT_DIR / f"{stem}.png", bbox_inches="tight", facecolor="white")
    fig.savefig(OUT_DIR / f"{stem}.svg", bbox_inches="tight", facecolor="white")
    plt.close(fig)


def ai_mechanism():
    fig, ax = setup_canvas(
        "METiS NanoForge / AiLNP: closed-loop AI design of LNP delivery materials",
        "Generative lipid design, property prediction, physics filters, active learning and wet-lab feedback",
    )

    group_label(ax, "Multimodal input layer", 0.045, 0.835, COLORS["blue"])
    inputs = [
        ("Public patents + literature\n~14k seed lipids", 0.045, 0.725, COLORS["sky"]),
        ("METiS ionizable lipid library\n>10M virtual structures", 0.045, 0.59, COLORS["sky"]),
        ("Wet-lab labels\n>100k lipid/LNP data points\npositive + negative outcomes", 0.045, 0.415, COLORS["sky"]),
        ("Design context\ncargo, route, target organ/cell,\nsafety and CMC constraints", 0.045, 0.235, COLORS["sky"]),
    ]
    for text, x, y, c in inputs:
        box(ax, (x, y), (0.22, 0.105), text, c, fontsize=9.2)

    group_label(ax, "Foundation models and physics filters", 0.35, 0.835, COLORS["purple"])
    box(ax, (0.335, 0.70), (0.20, 0.11), "LipidFLAG\nfragment-based RL generator\n7-12 chemically meaningful fragments", "#E6D3E7", fontsize=9.0, weight="bold")
    box(ax, (0.57, 0.70), (0.20, 0.11), "PhatGPT\nconditional Transformer generator\norgan/stability/formulation goals", "#E6D3E7", fontsize=9.0, weight="bold")
    box(ax, (0.335, 0.53), (0.20, 0.115), "LipidBERT\nBERT-like MLM + auxiliary lipid tasks\nfine-tuned on LNP wet-lab labels", "#D9EAD3", fontsize=9.0, weight="bold")
    box(ax, (0.57, 0.53), (0.20, 0.115), "MD / quantum / rule filters\nbilayer behavior, self-assembly,\nendosomal escape, pKa, synth.", "#D9EAD3", fontsize=9.0, weight="bold")
    box(ax, (0.415, 0.355), (0.275, 0.095), "METiS Agent + active learning\nselect models, rank uncertainty,\npropose next experiments", "#FFF2CC", fontsize=9.4, weight="bold")

    group_label(ax, "Candidate outputs", 0.81, 0.835, COLORS["green"])
    box(ax, (0.805, 0.70), (0.16, 0.11), "Ranked ionizable lipids\nnovel, synthesizable,\nIP/FTO-aware shortlist", "#D5E8D4", fontsize=9.0)
    box(ax, (0.805, 0.53), (0.16, 0.11), "LNP formulation recipe\nionizable/helper/chol/PEG ratios\nN/P, process window", "#D5E8D4", fontsize=9.0)
    box(ax, (0.805, 0.36), (0.16, 0.11), "Predicted profile\n>20 physchem + functional endpoints\npayload, tropism, safety", "#D5E8D4", fontsize=9.0)

    group_label(ax, "DATALOTS wet-lab closure", 0.35, 0.245, COLORS["orange"])
    box(ax, (0.335, 0.115), (0.19, 0.105), "Automated LNP make/test\nHTS formulation, in vitro reporter,\ncytotoxicity, encapsulation", "#FCE4D6", fontsize=8.8)
    box(ax, (0.565, 0.115), (0.19, 0.105), "In vivo validation\nmouse, rat, NHP biodistribution\norgan/cell functional readout", "#FCE4D6", fontsize=8.8)
    box(ax, (0.795, 0.115), (0.17, 0.105), "Model update\nmonthly library refresh\nsupervised fine-tuning", "#FCE4D6", fontsize=8.8)

    for y in [0.775, 0.64, 0.47, 0.29]:
        arrow(ax, (0.268, y), (0.335, 0.755 if y > 0.65 else 0.585 if y > 0.5 else 0.405))
    arrow(ax, (0.535, 0.755), (0.57, 0.755), COLORS["purple"])
    arrow(ax, (0.435, 0.70), (0.435, 0.645), COLORS["purple"])
    arrow(ax, (0.67, 0.70), (0.67, 0.645), COLORS["purple"])
    arrow(ax, (0.535, 0.585), (0.57, 0.585), COLORS["green"])
    arrow(ax, (0.48, 0.53), (0.48, 0.45), COLORS["gray"])
    arrow(ax, (0.67, 0.53), (0.64, 0.45), COLORS["gray"])
    arrow(ax, (0.69, 0.405), (0.805, 0.755), COLORS["green"], rad=-0.12)
    arrow(ax, (0.69, 0.405), (0.805, 0.585), COLORS["green"])
    arrow(ax, (0.69, 0.405), (0.805, 0.415), COLORS["green"], rad=0.08)
    arrow(ax, (0.885, 0.36), (0.525, 0.22), COLORS["orange"], rad=0.15)
    arrow(ax, (0.525, 0.168), (0.565, 0.168), COLORS["orange"])
    arrow(ax, (0.755, 0.168), (0.795, 0.168), COLORS["orange"])
    arrow(ax, (0.795, 0.16), (0.18, 0.405), COLORS["orange"], rad=-0.24)

    ax.text(0.033, 0.055, "Evidence boundary: architecture and metrics are from METiS disclosures, HKEX listing document and LipidBERT preprint; exact proprietary model weights, loss functions and raw datasets are not public.", fontsize=8.2, color=COLORS["gray"])
    save(fig, "3.2_新AI机制")


def baseline_mechanism():
    fig, ax = setup_canvas(
        "Current mature baseline for LNP discovery: DoE/HTS + microfluidic formulation + in vivo counterscreening",
        "Industry-standard, experimentally reliable workflow; strong for local optimization, expensive for broad de novo chemical-space search",
    )

    group_label(ax, "Design space definition", 0.04, 0.84, COLORS["blue"])
    box(ax, (0.04, 0.69), (0.18, 0.12), "Expert lipid families\nMC3/SM-102/ALC-0315-like lipids,\nDOTAP or ligand variants", "#DCEBFA", fontsize=8.8)
    box(ax, (0.04, 0.51), (0.18, 0.12), "DoE / QbD variables\nmolar ratios, N/P, buffer pH,\nFRR, TFR, concentration", "#DCEBFA", fontsize=8.8)
    box(ax, (0.04, 0.33), (0.18, 0.12), "Target product profile\nroute, cargo, organ, CQA ranges,\nGMP comparability needs", "#DCEBFA", fontsize=8.8)

    group_label(ax, "Make and characterize", 0.29, 0.84, COLORS["orange"])
    box(ax, (0.275, 0.67), (0.19, 0.12), "Microfluidic or IJM mixing\norganic lipid phase + aqueous RNA\ncontrolled particle formation", "#FCE4D6", fontsize=8.8, weight="bold")
    box(ax, (0.275, 0.49), (0.19, 0.12), "Analytical CQAs\nsize, PDI, encapsulation,\npKa, zeta, stability, endotoxin", "#FCE4D6", fontsize=8.8)
    box(ax, (0.275, 0.31), (0.19, 0.12), "In vitro screens\nreporter expression, viability,\nserum stability, uptake", "#FCE4D6", fontsize=8.8)

    group_label(ax, "In vivo evidence", 0.55, 0.84, COLORS["green"])
    box(ax, (0.535, 0.67), (0.19, 0.12), "Barcoded pool screen\n96-122 LNPs per animal cohort\nDNA/RNA barcode deconvolution", "#D5E8D4", fontsize=8.8, weight="bold")
    box(ax, (0.535, 0.49), (0.19, 0.12), "Functional counterscreen\nluciferase, Cre reporter,\nflow cytometry, histology", "#D5E8D4", fontsize=8.8)
    box(ax, (0.535, 0.31), (0.19, 0.12), "Lead confirmation\nrepeat dosing, tox panel,\nmouse to NHP bridge", "#D5E8D4", fontsize=8.8)

    group_label(ax, "Development decision", 0.79, 0.84, COLORS["purple"])
    box(ax, (0.785, 0.67), (0.17, 0.12), "Rank leads\npotency vs tropism vs tolerability", "#E6D3E7", fontsize=8.8)
    box(ax, (0.785, 0.49), (0.17, 0.12), "Scale-up and CMC\nTFF, sterile filtration,\ncomparability, stability", "#E6D3E7", fontsize=8.8)
    box(ax, (0.785, 0.31), (0.17, 0.12), "Nominate candidate\nIND-enabling tox and GMP batch", "#E6D3E7", fontsize=8.8)

    for y in [0.75, 0.57, 0.39]:
        arrow(ax, (0.22, y), (0.275, y), COLORS["gray"])
        arrow(ax, (0.465, y), (0.535, y), COLORS["gray"])
        arrow(ax, (0.725, y), (0.785, y), COLORS["gray"])
    ax.text(0.47, 0.225, "iterative empirical optimization", fontsize=9, color=COLORS["gray"], ha="center")

    group_label(ax, "Bottlenecks versus AI-first closed loop", 0.04, 0.205, COLORS["red"])
    bottlenecks = [
        "Sparse exploration of lipid chemistry; hundreds to thousands tested, not 10M-scale virtual search",
        "In vitro results often poorly predict in vivo biodistribution and extrahepatic tropism",
        "Animal, synthesis and analytics cost constrain active learning; false negatives are common",
        "Mouse-to-NHP/human translation, repeat dosing immunotoxicity and CMC scale-up remain hard",
    ]
    for i, text in enumerate(bottlenecks):
        y = 0.155 - i * 0.045
        ax.text(0.055, y, f"{i+1}. {text}", fontsize=9.2, color=COLORS["ink"], va="center")

    ax.text(0.79, 0.08, "Reliable baseline: DoE/QbD, controlled mixing, CQAs,\nbarcoded in vivo screening and counterscreening.", fontsize=8.5, color=COLORS["gray"], ha="left")
    save(fig, "3.2_传统方法")


if __name__ == "__main__":
    ai_mechanism()
    baseline_mechanism()
