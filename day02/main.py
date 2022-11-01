import geopandas as gpd
import matplotlib.pyplot as plt

plt.rcParams.update(
    {
        "figure.facecolor": "black",
        "text.color": "white",
        "font.family": "monospace",
        "font.weight": "bold",
        "font.size": 10,
    }
)


gdf = gpd.read_file("cornwall_devon_boundary.gpkg")

cols = 3
rows = 2

s_vals = [1, 1000, 5000, 15000, 25000, 35000]
f, axes = plt.subplots(figsize=(16, 12), ncols=cols, nrows=rows)


for i, s in zip(range(cols * rows), s_vals):
    # s_val = 10**i
    s_gdf = gdf.simplify(s)
    len = round(s_gdf.length.sum() / 1000)
    j = i % cols
    ax = axes[i // cols, j]
    ax.set_title(label=f"Simplify {s}, length {len}km", loc="left")
    ax.axis("off")
    s_gdf.plot(ax=ax, color='lime')

f.suptitle("Simplifying lines - the coastline paradox")
plt.savefig('output.png')
plt.show()
