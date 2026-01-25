import matplotlib.pyplot as plt

def marker_for_threshold(threshold):
    match threshold:
        case "0%":
            return "o"      # Kreis
        case "0.1%":
            return "s"      # Quadrat
        case "0.5%":
            return "^"      # Dreieck oben
        case "1%":
            return "D"      # Raute
        case "5%":
            return "P"      # Plus (gefüllt)
        case "10%":
            return "X"      # Kreuz (gefüllt)
        case "50%":
            return "*"      # Stern
        case _:
            return "o"
        
def plot_stop_threshold_tradeoff(
    data,
    xlabel="complete cost in $ (GPT process + Claude process)",
    ylabel="Translation correctness",
):
    """
    data: list of dicts with keys
        - name: label shown next to point (e.g. 'GPT Only', 'Claude Only', None)
        - cost: x value
        - quality: y value
        - threshold: string label for legend (e.g. '0%', '0.1%', ..., '75%')
        - color: matplotlib color
    """

def plot_stop_threshold_tradeoff(
    data,
    xlabel="Complete costs in $",
    ylabel="Translation correctness",
):
    fig, ax = plt.subplots(figsize=(8, 6))

    for d in data:
        marker = marker_for_threshold(d["threshold"])

        ax.scatter(
            d["cost"],
            d["quality"],
            s=120,
            color=d["color"],
            # marker=marker
            marker="o"
        )
        if d.get("name"):
            ax.text(
                d["cost"] + 2.5,
                d["quality"],
                d["name"],
                fontsize=10,
                va="center",
                weight="bold",
            )

    # ---- logarithmic-like scaling near 1 (logit) ----
    ax.set_yscale("logit")
    ax.set_ylim(0.88, 0.9999)

    # custom ticks: show "1" at 0.9999
    yticks = [0.88, 0.9, 0.95, 0.97, 0.99, 0.999, 0.9999]
    yticklabels = ["88%", "90%", "95%", "97%", "99%", "99.9%", "100%"]

    ax.set_yticks(yticks)
    ax.set_yticklabels(yticklabels)

    # ---- static legend ----
    legend_handles = [
        plt.Line2D([], [], marker="o", linestyle="", color="#9E0059", markersize=10, label="CS"),
        plt.Line2D([], [], marker="o", linestyle="", color="#FF0054", markersize=10, label="GG"),
        plt.Line2D([], [], marker="o", linestyle="", color="#E47A00", markersize=10, label="OC"),
    ]

    ax.legend(handles=legend_handles, title="Model", loc="upper right")

    ax.set_xlabel(xlabel, fontsize=13, weight="bold")
    ax.set_ylabel(ylabel, fontsize=13, weight="bold")

    ax.grid(True, which="major", linestyle="-", alpha=0.6)

    plt.tight_layout()
    plt.show()
data = [
    {"threshold": "0%",   "cost": 29.425218000355127, "quality": 0.9765714285714285, "color": "#9E0059"},
    {"threshold": "0.1%", "cost": 30.147334080216122, "quality": 0.9725714285714285, "color": "#9E0059"},
    {"threshold": "0.5%", "cost": 32.24474736013855, "quality": 0.9697142857142858, "color": "#9E0059"},
    {"threshold": "1%",   "cost": 33.06962064011346, "quality": 0.9694285714285714, "color": "#9E0059"},
    {"threshold": "5%",   "cost": 36.08361840008385, "quality": 0.9674285714285714, "color": "#9E0059"},
    {"threshold": "10%",  "cost": 36.08361840008385, "quality": 0.9674285714285714, "color": "#9E0059"},
    {"threshold": "50%",  "cost": 38.473141200071176, "quality": 0.9662857142857143, "color": "#9E0059"},
    {"threshold": "CS Only", "cost": 45.534660000052504, "quality": 0.9634285714285714, "color": "#9E0059",   "name": "CS Only"},
    {"threshold": "OG Only",    "cost": 6.891569288785499,  "quality": 0.90, "color": "#390099", "name": "GPT Only"},
    {"threshold": "0%"  ,    "cost": 67.44148888447913,  "quality": 0.998, "color": "#FF0054"},
    {"threshold": "0.1%",    "cost": 76.59781886175912,  "quality": 0.998, "color": "#FF0054"},
    {"threshold": "0.5%",    "cost": 88.00911398030455,  "quality": 0.9977142857142857, "color": "#FF0054"},
    {"threshold": "1%"  ,    "cost": 96.91432799585345,  "quality": 0.9974285714285714, "color": "#FF0054"},
    {"threshold": "5%"  ,    "cost": 114.70372325636986,  "quality": 0.9974285714285714, "color": "#FF0054"},
    {"threshold": "10%" ,    "cost": 114.70372325636986,  "quality": 0.9971428571428571, "color": "#FF0054"},
    {"threshold": "50%" ,    "cost": 132.08433693923317,  "quality": 0.9971428571428571, "color": "#FF0054"},
    {"threshold": "GG Only", "cost": 174.9649956669675, "quality": 0.9971428571428571, "color": "#FF0054",   "name": "GG Only"},
   
   
    {"threshold": "0%"  ,    "cost": 20.338807286046375,  "quality": 0.9999, "color": "#E47A00"},
    {"threshold": "0.1%",    "cost": 20.256442294473498,  "quality": 0.9997142857142857, "color": "#E47A00"},
    {"threshold": "0.5%",    "cost": 21.824087717247167,  "quality": 0.9994285714285714, "color": "#E47A00"},
    {"threshold": "1%"  ,    "cost": 23.316462068646963,  "quality": 0.9994285714285714, "color": "#E47A00"},
    {"threshold": "5%"  ,    "cost": 27.0984491143236,  "quality": 0.9994285714285714, "color": "#E47A00"},
    {"threshold": "10%" ,    "cost": 27.0984491143236,  "quality": 0.9994285714285714, "color": "#E47A00"},
    {"threshold": "50%" ,    "cost": 30.951221914303428,  "quality": 0.9994285714285714, "color": "#E47A00"},
    {"threshold": "OC Only", "cost": 43.36929964283288, "quality": 0.9994285714285714, "color": "#E47A00",   "name": "OC Only"},
   ]

plot_stop_threshold_tradeoff(data)