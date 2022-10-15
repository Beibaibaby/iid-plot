import matplotlib.pyplot as plt
import numpy as np


labels = ['0.1', '0.3', '0.5', '0.7', '0.9']

oklen = np.asarray([58.9153,51.1244,36.3301	,32.8342, 21.9142 ])
baseline = np.asarray([171.2432, 228.2039 , 299.4648, 368.1399, 377.9457])

oklen_3 = np.asarray([15.7063,18.5923,21.2877	,25.1182, 29.9306 ])
baseline_3 = np.asarray([628.883, 644.8716 , 625.0206, 580.9270, 567.9948])

x = np.arange(len(labels))  # the label locations
width = 0.1 # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x-1*width , oklen , width, label='Direct-UQ1')
rects2 = ax.bar(x-1*width , baseline, width,bottom=oklen, label='FullJoin-UQ1')

rects3 = ax.bar(x , oklen_3 , width, label='Direct-UQ3')
rects4 = ax.bar(x , baseline_3, width,bottom=oklen_3, label='FullJoin-UQ3')

#ax.set_ylim(0,1)
# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Time Cost (s)')
ax.set_title('|Ji|/|U| estimation time ')
ax.set_xticks(x, labels)
ax.legend(loc='center', bbox_to_anchor=(0.2, 0.6, 0.4, 0.5),fontsize=8)
#ax.legend()
#ax.bar_label(rects1, padding=3)
#ax.bar_label(rects2, padding=3)

fig.tight_layout()
plt.savefig('Time')
plt.show()