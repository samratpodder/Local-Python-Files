# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %%
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# %% [markdown]
# Learning **Matplotlib** and *Line Graphs*

# %%
x = np.linspace(0, 5, 10)
y = np.cos(x)
plt.plot(x, y)
print(x)


# %%
randarr = np.random.randint(0,20,size=10)
print(randarr)


# %%
plt.plot(randarr)


# %%
plt.plot(randarr+10)#creating an offset of 10


# %%
plt.plot(randarr+10,x)

# %% [markdown]
# Usage of *Line charts*

# %%
precip2019 = [[],[],[],[],[],[],[],[],[],[],[],[]]
for i in range(12):
    pr = int(input("Precipitation in Month {}".format(i+1)))
    precip2019[i].append(i+1)
    precip2019[i].append(pr)
print(precip2019)


# %%
plt.plot(precip2019)

# %% [markdown]
# Using *xticks* marked the **x axis** with *labels*
# %% [markdown]
# Usage of *yticks* is similar but could not show here due to * **Unicode-ASCII** encoding error*

# %%
month = np.linspace(1,12,12)
mnames = np.array(["jan", 'feb', 'mar','apr','jun','jul','aug','sep','oct','nov','dec'])
plt.xticks(ticks = month, labels = mnames)
plt.plot(precip2019)

# %% [markdown]
# *Learning Histograms*

# %%
randnums = (np.random.randn(1000))


# %%
randnumspos = (np.random.uniform(low = 0, high = 9999999999,size = 1000))


# %%
plt.hist(randnums)


# %%
plt.hist(randnumspos)


# %%
plt.hist(randnums,bins = 20)


# %%
plt.hist(randnumspos,bins = 20)


# %%
plt.hist2d(randnums,randnumspos)


# %%
plt.hist2d(randnums,randnumspos,bins=200)

# %% [markdown]
# Learning ** Bar Charts **

# %%
bardata1 = np.array(['ind','pak','ban','srl','chn','nep'])
bardata2 = np.array([10,3,8,5,1,8])
plt.bar(np.arange(len(bardata2)),bardata2)
plt.xticks(ticks= np.arange(len(bardata1)),labels=bardata1 )   #bad method when i already have bardata1 beforehand
print("my likeness chart")

# %% [markdown]
# Rotating the above chart * **Horizontally** *

# %%
plt.barh(bardata1,bardata2)
print("my likeness chart rotated")


# %%
mylikeness1 = np.array([10,3,8,5,1,8])
mylikeness2 = np.array([9,3,5,7,2,8 ])
mylikeness3 = np.array([5,8,2,5,6,7 ])


# %%
plt.bar(bardata1,mylikeness1)
plt.bar(bardata1,mylikeness2)
plt.bar(bardata1,mylikeness3)
print("stacked bar chart")


# %%
plt.bar(bardata1,mylikeness1)
plt.bar(bardata1,mylikeness2,bottom = mylikeness1)
plt.bar(bardata1,mylikeness3,bottom = mylikeness1+ mylikeness2)
print("stacked bar chart")


# %%


