import matplotlib.pyplot as plt
import numpy as np


labels = ['J1', 'J2', 'J3']

oklen = [0.45876965 ,      0.53267034  ,  0.48918705  ,  0.45328197     ,  0.4584038				]
baseline = [0.580011597	,0.579988536	,0.579259441	,0.580066442	,0.577503364]

baseline_07=np.asarray( [0.44921153294765154, 0.45022409476493647, 0.451149619664422])
olken_07=np.asarray( [0.6012656,  0.65711698 ,0.64132738		 ])
differnece_07=np.absolute(olken_07-baseline_07)

difference_09=np.asarray([0.70046616, 0.76614669 ,0.74705292])-np.asarray([0.6578845512743807, 0.6551085247187375, 0.6574557920149217	])


baseline_05=np.asarray( [0.38237573065960845, 0.38169583073068464, 0.38263374564723207])
olken_05=np.asarray( [0.50019992 ,0.54583688 ,0.46689184				 ])
differnece_05=np.absolute(olken_05-baseline_05)


olken_01 = np.asarray([00.41103192 ,0.44894557 ,0.41082163			])
baseline_01 = np.asarray([0.34047915656627337, 0.3398350500939109, 0.338090490117754])
differnece_01=olken_01-baseline_01

olken_03 = np.asarray([0.44603128, 0.45957642 ,0.47578368])
baseline_03= np.asarray([0.35384758314212456, 0.3542221576280155, 0.35019166209860186])

differnece_03=olken_03-baseline_03

x = np.arange(len(labels))  # the label locations
width = 0.085  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x-2*width , differnece_01, width, label='scale-0.1')
rects3 = ax.bar(x-1*width , differnece_03, width, label='scale-0.3')
rects5 = ax.bar(x , differnece_05, width, label='scale-0.5')
rects7 = ax.bar(x + 1*width, differnece_07, width, label='scale-0.7')
rects9 = ax.bar(x + 2*width, difference_09, width, label='scale-0.9')
#ax.set_ylim(0,1)
# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('error in  |J|/|U| estimation')
ax.set_title('|Ji|/|U| estimation error (UQ3) ')
ax.set_xticks(x, labels)
ax.legend(loc='center', bbox_to_anchor=(0.11, 0.6, 0.5, 0.5),fontsize='small')

#ax.bar_label(rects1, padding=3)
#ax.bar_label(rects2, padding=3)

fig.tight_layout()
plt.savefig('UQ3')
plt.show()

