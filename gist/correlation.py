import pandas as pd
from scipy import stats
from scipy.stats import kendalltau, pearsonr, spearmanr

rvs1 = stats.norm.rvs(loc=5, scale=10, size=500)
rvs2 = stats.norm.rvs(loc=5, scale=10, size=500)
rvs3 = stats.norm.rvs(loc=5.5, scale=9, size=500)

print(stats.ttest_ind(rvs1, rvs2))
print(stats.ttest_ind(rvs1, rvs3))

print(stats.ttest_rel(rvs1, rvs2))
print(stats.ttest_rel(rvs1, rvs3))

x = [1, 2, 3, 4, 5]
y = [4, 6, 20, 16, 25]


print(pearsonr(x, y))
print(spearmanr(x, y))
print(kendalltau(x, y))

Xs = pd.Series(x)
Ys = pd.Series(y)
print(Xs.corr(Ys, method="pearson"))
print(Xs.corr(Ys, method="spearman"))
print(Xs.corr(Ys, method="kendall"))
