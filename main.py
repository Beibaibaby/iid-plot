# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib.pyplot as plt
import numpy as np


labels = ['J1', 'J2', 'J3', 'J4', 'J5']
baseline = [0.54123815,       0.51369635,    0.52204235 ,    0.48707857   ,   0.52329425				]
olken = [0.210706266,	0.207417634,	0.209604777	, 0.209127639,	0.211297298]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, baseline, width, label='Baseline')
rects2 = ax.bar(x + width/2, olken, width, label='olken')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Ratio')
ax.set_ylim(0,1)
ax.set_title('Overlapping Ratio Estimation for UQ1 (scale=0.1) ')
ax.set_xticks(x, labels)
ax.legend()

#ax.bar_label(rects1, padding=3)
#ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()

plt.show()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
