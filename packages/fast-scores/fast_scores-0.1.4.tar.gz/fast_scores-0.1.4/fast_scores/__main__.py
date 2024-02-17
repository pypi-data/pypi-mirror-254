"""Calculate corr matrix for given en and zh.

en = loatext(filename)

en_p = process_en(en)
en_tr = en2zh(en_p)

s = fast_scores(en_tr, zh)

plt.ion()
sns.set()
sns.set_style("darkgrid")
sns.heatmap(s, cmap="viridis_r").invert_yaxis()

aset = cmat2aset(s)

df = pd.DataFrame(aset, columns=list("xyz")).replace("", np.nan).dropna()
df.plot.scatter("x", "y", c="z")

"""
