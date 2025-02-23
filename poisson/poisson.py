#Swamini Shirsat - 2103138
from scipy.stats import poisson
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
no_arrivals=1000
l1=1
l2=2
l3=3
#poisson process of l1
senior_q=poisson.rvs(l1, size=no_arrivals)
gen_q = poisson.rvs(l2, size=no_arrivals)# pisson process for l2
merged_q = senior_q + gen_q #poisson process for l3
data = pd.Series(merged_q).value_counts().sort_index().to_dict()
merged_pmf=[]
for i in data.values():
  i/=no_arrivals
  merged_pmf.append(i)
fig,ax=plt.subplots()
ax.bar(range(len(data)),merged_pmf)
plt.xticks(range(len(data)), list(data.keys()))
plt.title("pmf of entire queue")
plt.xlabel("k(number of arrivals")
plt.ylabel("P(x=k)")
plt.show()
