import matplotlib.pyplot as plt
import numpy as np


labels = ['J1', 'J2', 'J3', 'J4', 'J5']
baseline = [0.47949696  ,     0.44702107   , 0.41755397  ,   0.48561006    ,  0.4495284]
olken = [0.235377279,	0.237835659,	0.235620118,	0.235421667,	0.231342123]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, baseline, width, label='FullJoin')
rects2 = ax.bar(x + width/2, olken, width, label='Olken')
ax.set_ylim(0,1)
# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Ratio')
ax.set_title('Overlapping Ratio Estimation for UQ1 (scale=0.3) ')
ax.set_xticks(x, labels)
ax.legend()

#ax.bar_label(rects1, padding=3)
#ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()

