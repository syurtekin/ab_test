import pandas as pd
import numpy as np
import itertools
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, pearsonr, spearmanr, kendalltau, \
    f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest
from helpers import *
import scipy.stats as stats

#max bidding
df = pd.read_excel("ab_testing.xlsx", sheet_name= "Control Group")
df.head()
df.drop(['Unnamed: 4','Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9','Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13'],axis='columns', inplace=True)

df.head()
#average bidding
df2 = pd.read_excel("ab_testing.xlsx", sheet_name= "Test Group")
df2.head()
df2.drop(['Unnamed: 4','Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9','Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13'],axis='columns', inplace=True)
check_df(df)
check_df(df2)

df.groupby("Purchase").mean()
df2.groupby("Purchase").mean()
df["Purchase"].mean()

# HO : M1 = M2
#Bir sitede yapılan değişikliğin kontrol grubu ile önceki halinin test grubu arasında satın alma bakımından istatistiksel olarak anlamlı bir fark yoktur.
# H1 : M1!= M2
#Bir sitede yapılan değişikliğin kontrol grubu ile önceki halinin test grubu arasında satın alma bakımından istatistiksel olarak anlamlı bir fark yoktur.
test_stat, pvalue = shapiro(df["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# p_value = 0.5891, p> 0.05 h0 red edilemez.
test_stat, pvalue = shapiro(df2["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# p value = 0.15, p > 0.05 ho red edilemez.
# normal dağılım varsayımı sağlanmaktadır.

# varyans homojenliği
test_stat, pvalue = levene(df["Purchase"], df2["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# p value = 0.108, p > 0.05 ho red edilemez. Varyanslar homojendir.

# hipotezin uygulanması

# 1. Varsayımlar sağlanıyorsa bağımsız iki örneklem t testi (parametrik test)
# 2. Varsayımlar sağlanmıyorsa mannwhitneyu testi (non-parametrik test)

print(df["Purchase"].mean(), df2["Purchase"].mean())
#control : 550.894
#test : 582.106
# istatistiksel olarak anlamlı bir ilişki var mı?

# Varsayımlar sağlandığı için t testi parametrik;
test_stat, pvalue = ttest_ind(df["Purchase"], df2["Purchase"], equal_var=True)
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# p value = 0.34 p>0.05 h0 red edilemez. Veriler arasında istatistiksel anlamda anlamlı bir fark yoktur.

# Normal dağılım ve varyans homojenliği sağlandığı için parametrik ( iki örneklem t ) hipotez testi kullandım.

# A/B Testi için bu problem de istatistiksel olarak anlamlı bir fark yoktur. Bu örnekte sadece satın alma sayısını ele aldık. Ancak tıklanma ve görüntülenme sayısı da göz önünde bulundurulabilir.
# maliyeti az olan seçilebilir.

