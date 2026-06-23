from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


OUT_DIR = Path(__file__).resolve().parent
AI_OUT = OUT_DIR / "2.3_新AI机制.png"
BASELINE_OUT = OUT_DIR / "2.3_传统方法.png"


COLORS = {
    "blue": "#4E79A7",
    "sky": "#A0CBE8",
    "orange": "#F28E2B",
    "green": "#59A14F",
    "red": "#E15759",
    "purple": "#B07AA1",
    "gray": "#6B7280",
    "lightgray": "#F3F4F6",
    "dark": "#111827",
    "yellow": "#EDC948",
    "teal": "#76B7B2",
}


def setup_ax(title):
    fig, ax = plt.subplots(figsize=(16, 9), dpi=220)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis("off")
    ax.text(
        0.35,
        8.68,
        title,
        fontsize=17,
        fontweight="bold",
        color=COLORS["dark"],
        va="top",
    )
    ax.text(
        15.65,
        8.36,
        "Technical schematic; labels abbreviated",
        fontsize=8.0,
        color=COLORS["gray"],
        ha="right",
        va="top",
    )
    return fig, ax


def box(ax, x, y, w, h, text, fc, ec=None, lw=1.4, fontsize=10.5, weight="normal"):
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.018,rounding_size=0.08",
        linewidth=lw,
        edgecolor=ec or COLORS["dark"],
        facecolor=fc,
    )
    ax.add_patch(patch)
    ax.text(
        x + w / 2,
        y + h / 2,
        text,
        ha="center",
        va="center",
        fontsize=fontsize,
        fontweight=weight,
        color=COLORS["dark"],
        linespacing=1.22,
    )
    return patch


def arrow(ax, x1, y1, x2, y2, color=None, lw=1.8, style="-|>", rad=0.0, label=None, label_pos=0.5):
    arr = FancyArrowPatch(
        (x1, y1),
        (x2, y2),
        arrowstyle=style,
        mutation_scale=13,
        linewidth=lw,
        color=color or COLORS["gray"],
        connectionstyle=f"arc3,rad={rad}",
    )
    ax.add_patch(arr)
    if label:
        lx = x1 + (x2 - x1) * label_pos
        ly = y1 + (y2 - y1) * label_pos
        ax.text(
            lx,
            ly + 0.12,
            label,
            fontsize=8.5,
            color=color or COLORS["gray"],
            ha="center",
            va="bottom",
            bbox=dict(boxstyle="round,pad=0.12", fc="white", ec="none", alpha=0.92),
        )


def draw_ai():
    fig, ax = setup_ax("AI method: Generate:Biomedicines Chroma + generate-build-measure-learn loop")

    # Inputs.
    box(ax, 0.45, 6.9, 2.65, 0.72, "Public structure data\nPDB / CATH", COLORS["sky"], fontsize=10)
    box(ax, 0.45, 5.95, 2.65, 0.72, "Sequence & family data\nUniProt / PFAM", COLORS["sky"], fontsize=10)
    box(ax, 0.45, 5.0, 2.65, 0.72, "Therapeutic constraints\ntarget, epitope, function", "#DDEB9D", fontsize=10)
    box(ax, 0.45, 4.05, 2.65, 0.72, "Internal assays\nbinding, function, developability", "#DDEB9D", fontsize=10)
    box(ax, 0.45, 3.1, 2.65, 0.72, "Structural feedback\nCryoEM / X-ray / models", "#DDEB9D", fontsize=10)
    ax.text(1.78, 7.92, "Data modalities", ha="center", fontsize=11.5, fontweight="bold", color=COLORS["dark"])

    # Core Chroma model.
    core = FancyBboxPatch(
        (3.55, 2.65),
        7.35,
        5.35,
        boxstyle="round,pad=0.04,rounding_size=0.16",
        linewidth=1.8,
        edgecolor=COLORS["blue"],
        facecolor="#EFF6FF",
    )
    ax.add_patch(core)
    ax.text(7.22, 7.68, "Chroma programmable protein generative model", ha="center", fontsize=13.2, fontweight="bold", color=COLORS["blue"])

    box(ax, 3.9, 6.65, 2.55, 0.78, "Correlated backbone\nDDPM / polymer prior", "white", ec=COLORS["blue"], fontsize=9.8)
    box(ax, 6.85, 6.65, 2.95, 0.78, "Random / equivariant GNN\ndenoiser; long-range reasoning", "white", ec=COLORS["blue"], fontsize=9.3)
    box(ax, 3.9, 5.32, 2.55, 0.78, "Inter-residue geometry\nbackbone synthesis", "white", ec=COLORS["blue"], fontsize=9.8)
    box(ax, 6.85, 5.32, 2.95, 0.78, "Sequence + side-chain design\nCRF / diffusion-aware decoder", "white", ec=COLORS["blue"], fontsize=9.3)
    box(ax, 3.9, 4.0, 2.55, 0.82, "Bayesian conditioning\nmotif, shape, symmetry,\nsemantic/NL guidance", "white", ec=COLORS["purple"], fontsize=9.1)
    box(ax, 6.85, 4.0, 2.95, 0.82, "Scoring & triage\nfoldability, expression,\nspecificity, immunogenicity", "white", ec=COLORS["purple"], fontsize=9.1)
    box(ax, 5.15, 2.98, 3.45, 0.72, "Output: all-atom protein complex\nsequence + structure + design rationale", "#FFF7ED", ec=COLORS["orange"], fontsize=9.8, weight="bold")

    arrow(ax, 6.45, 7.04, 6.85, 7.04, COLORS["blue"])
    arrow(ax, 8.32, 6.65, 8.32, 6.1, COLORS["blue"])
    arrow(ax, 6.45, 5.71, 6.85, 5.71, COLORS["blue"])
    arrow(ax, 5.18, 6.65, 5.18, 6.1, COLORS["blue"], rad=0.0)
    arrow(ax, 5.18, 5.32, 5.18, 4.82, COLORS["purple"])
    arrow(ax, 6.45, 4.41, 6.85, 4.41, COLORS["purple"])
    arrow(ax, 8.32, 4.0, 7.4, 3.7, COLORS["orange"], rad=-0.2)
    arrow(ax, 5.4, 4.0, 6.3, 3.7, COLORS["orange"], rad=0.2)

    # Arrows from data to Chroma.
    for yy in [7.25, 6.3, 5.36, 4.42, 3.46]:
        arrow(ax, 3.1, yy, 3.55, yy, COLORS["gray"], lw=1.4)

    # Wet lab and learning loop.
    box(ax, 11.55, 6.75, 3.65, 0.78, "Build\nDNA synthesis, cloning,\nexpression, purification", "#ECFDF5", ec=COLORS["green"], fontsize=9.5, weight="bold")
    box(ax, 11.55, 5.55, 3.65, 0.86, "Measure\nSPR/BLI, cell assays, MS,\nDSF/SEC, CryoEM/X-ray", "#ECFDF5", ec=COLORS["green"], fontsize=9.5, weight="bold")
    box(ax, 11.55, 4.28, 3.65, 0.86, "Learn\nnegative data + structure/function\nupdate active-learning priors", "#ECFDF5", ec=COLORS["green"], fontsize=9.2, weight="bold")
    box(ax, 11.55, 3.0, 3.65, 0.86, "Candidate package\npotency + specificity +\ndevelopability + CMC risk", "#FFF7ED", ec=COLORS["orange"], fontsize=9.4, weight="bold")
    arrow(ax, 8.6, 3.34, 11.55, 7.1, COLORS["orange"], label="ranked designs")
    arrow(ax, 13.38, 6.75, 13.38, 6.41, COLORS["green"])
    arrow(ax, 13.38, 5.55, 13.38, 5.14, COLORS["green"])
    arrow(ax, 13.38, 4.28, 13.38, 3.86, COLORS["green"])
    arrow(ax, 11.55, 4.72, 10.85, 4.72, COLORS["green"], label="closed-loop data", label_pos=0.42)

    # Metric callouts.
    box(ax, 0.55, 0.62, 3.52, 1.1, "Published Chroma validation\n310 proteins characterized;\n2 crystal structures: 1.0/1.1 A backbone RMSD", "#F9FAFB", ec=COLORS["gray"], fontsize=9.0)
    box(ax, 4.37, 0.62, 3.52, 1.1, "Company scale disclosure\n42,000 proteins generated,\nbuilt and tested", "#F9FAFB", ec=COLORS["gray"], fontsize=9.0)
    box(ax, 8.18, 0.62, 3.52, 1.1, "De novo binders\nreported across 9 targets;\nstructural confirmation disclosed", "#F9FAFB", ec=COLORS["gray"], fontsize=9.0)
    box(ax, 12.0, 0.62, 3.52, 1.1, "Clinical caveat\nGB-0895 is AI-optimized;\nnot proof of de novo antibody scaffold", "#FFF1F2", ec=COLORS["red"], fontsize=9.0)

    ax.text(0.48, 0.25, "Sources: Nature 2023 Chroma paper; Generate platform / news releases. Exact claims and caveats are documented in the accompanying Markdown.", fontsize=8.3, color=COLORS["gray"])
    fig.tight_layout(pad=0.25)
    fig.savefig(AI_OUT, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def draw_baseline():
    fig, ax = setup_ax("Mainstream baseline: display/directed evolution + Rosetta-guided engineering")

    y = 6.05
    xs = [0.45, 2.92, 5.55, 8.12, 10.82, 13.22]
    ws = [1.95, 2.18, 2.15, 2.15, 1.95, 2.15]
    labels = [
        "Target antigen\nor structure",
        "Library design\nimmune/synthetic\nCDR/scaffold",
        "Display screen\nphage / yeast /\nmammalian\npanning/FACS",
        "Clone recovery\nNGS, hit picking,\nsequence clustering",
        "Wet validation\nSPR/BLI, assays,\nexpression",
        "Lead optimization\naffinity maturation;\ndevelopability filters",
    ]
    colors = ["#DBEAFE", "#FEF3C7", "#FEF3C7", "#E0F2FE", "#DCFCE7", "#FCE7F3"]
    for x, w, lab, c in zip(xs, ws, labels, colors):
        box(ax, x, y, w, 1.08, lab, c, ec=COLORS["gray"], fontsize=7.8, weight="bold")
    for i in range(len(xs) - 1):
        arrow(ax, xs[i] + ws[i], y + 0.54, xs[i + 1], y + 0.54, COLORS["gray"])

    # Computational branch.
    box(ax, 1.12, 4.12, 2.52, 0.85, "Structure biology input\nX-ray / CryoEM /\nhomology / AF2", "#DBEAFE", ec=COLORS["blue"], fontsize=8.6)
    box(ax, 4.18, 4.12, 2.68, 0.85, "Rosetta / FoldX / MD\nenergy scoring, docking,\nside-chain packing", "#EEF2FF", ec=COLORS["purple"], fontsize=9.0)
    box(ax, 7.43, 4.12, 2.52, 0.85, "Expert rules\nhumanized frameworks,\nliabilities, epitope hypotheses", "#F3F4F6", ec=COLORS["gray"], fontsize=9.0)
    box(ax, 10.58, 4.12, 2.52, 0.85, "Focused library\nor point mutants\nfor next selection round", "#FEF3C7", ec=COLORS["orange"], fontsize=9.0)
    arrow(ax, 2.4, 6.05, 2.38, 4.97, COLORS["blue"], rad=0.1)
    arrow(ax, 3.64, 4.55, 4.18, 4.55, COLORS["purple"])
    arrow(ax, 6.86, 4.55, 7.43, 4.55, COLORS["purple"])
    arrow(ax, 9.95, 4.55, 10.58, 4.55, COLORS["orange"])
    arrow(ax, 11.84, 4.97, 11.75, 6.05, COLORS["orange"], rad=-0.1)

    # Iteration loop.
    arrow(ax, 14.3, 6.05, 14.3, 3.0, COLORS["red"], lw=2.0, rad=-0.15, label="repeat 2-6 rounds")
    arrow(ax, 14.3, 3.0, 3.55, 3.0, COLORS["red"], lw=2.0)
    arrow(ax, 3.55, 3.0, 3.9, 6.05, COLORS["red"], lw=2.0, rad=-0.18)

    # Bottleneck lane.
    ax.text(0.55, 2.35, "Typical bottlenecks in the mature baseline", fontsize=12.5, fontweight="bold", color=COLORS["dark"])
    box(ax, 0.55, 1.35, 2.75, 0.72, "Library-bounded search\n10^7-10^11 variants;\nnot continuous space", "#FFF1F2", ec=COLORS["red"], fontsize=8.0)
    box(ax, 3.58, 1.35, 2.75, 0.72, "Indirect epitope control\npanning enriches binders;\nmechanism not guaranteed", "#FFF1F2", ec=COLORS["red"], fontsize=8.0)
    box(ax, 6.61, 1.35, 2.75, 0.72, "Physics scoring is brittle\nmisses solubility,\nexpression, dynamics", "#FFF1F2", ec=COLORS["red"], fontsize=8.0)
    box(ax, 9.64, 1.35, 2.75, 0.72, "Costly wet-lab cycles\nbuild-measure bottleneck;\nslow iteration", "#FFF1F2", ec=COLORS["red"], fontsize=8.0)
    box(ax, 12.67, 1.35, 2.75, 0.72, "Hard targets persist\nmembrane proteins;\ntransient epitopes;\nmultispecifics", "#FFF1F2", ec=COLORS["red"], fontsize=8.0)

    ax.text(0.55, 0.58, "Why this is still the relevant baseline: display and directed evolution are experimentally grounded, genotype-phenotype coupled, and widely used for therapeutic antibodies and protein engineering; Rosetta-style scoring remains a mature structure-guided design layer.", fontsize=8.7, color=COLORS["gray"])
    ax.text(0.55, 0.28, "Sources: Frontiers Immunology 2024 display review; Rosetta Commons software documentation; Rosetta all-atom energy-function literature.", fontsize=8.3, color=COLORS["gray"])
    fig.tight_layout(pad=0.25)
    fig.savefig(BASELINE_OUT, bbox_inches="tight", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    draw_ai()
    draw_baseline()
    print("generated 2 PNG files")
