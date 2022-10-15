import matplotlib.pyplot as plt
import numpy as np


labels = ['0.1', '0.3', '0.5', '0.7', '0.9']
baseline = [100.8833,
166.812,
100.083,
236.6985,
412.2987]
olken = [
49.4266,
46.7787,
48.8104,
31.3113,
26.2029
]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, baseline, width, label='Baseline')
rects2 = ax.bar(x + width/2, olken, width, label='olken')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Time (s)')
ax.set_xlabel('Scale')
ax.set_title('Time Cost of Overlapping Ratio Estimation for UQ1 ')
ax.set_xticks(x, labels)
ax.legend()
fig.tight_layout()

plt.show()