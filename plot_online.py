import matplotlib.pyplot as plt
import numpy as np


labels = ['J1', 'J2', 'J3']

oklen = np.asarray([0.7619148 , 0.80528676, 0.76772297	])
baseline = np.asarray([ 0.732082838083237, 0.7324391398905571, 0.7291214561229776])

baseline_07=np.asarray( [0.5109107395291225, 0.5074448480694187, 0.5090948682384148		])
olken_07=np.asarray( [0.4956242 , 0.5099371 , 0.52563383			 ])
differnece_07=np.absolute(olken_07-baseline_07)
difference_09=np.absolute(oklen-baseline)

baseline_05=np.asarray( [0.41670554240937463, 0.41795841391681565, 0.41616674640758494])
olken_05=np.asarray( [0.43705989, 0.41575908 ,0.40040972						 ])
differnece_05=np.absolute(olken_05-baseline_05)


oklen_01 = np.asarray([0.39933511 ,0.35348806, 0.30083172	])
baseline_01 = np.asarray([ 0.3426698025180238, 0.3395739977281823, 0.3453173577854641])
differnece_01= np.absolute(oklen_01-baseline_01)

olken_03 = np.asarray([0.35190138, 0.38993984, 0.36703004])
baseline_03= np.asarray([0.37229374155966083, 0.37120372554179804, 0.36511414830055416])

differnece_03=np.absolute(olken_03-baseline_03)

x = np.arange(len(labels))  # the label locations
width = 0.085  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x-2*width , differnece_01, width, label='scale-0.1')
rects3 = ax.bar(x-1*width , differnece_03, width, label='scale-0.3')
rects5 = ax.bar(x , differnece_05, width, label='scale-0.5')
rects7 = ax.bar(x + 1*width, differnece_07, width, label='scale-0.7')
rects9 = ax.bar(x + 2*width, difference_09, width, label='scale-0.9')

ax.set_ylim(0,0.3)
# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('error in  |J|/|U| estimation')
ax.set_title('|Ji|/|U| estimation error (UQ4) ')
ax.set_xticks(x, labels)

#ax.legend(loc='center', bbox_to_anchor=(0.12, 0.6, 0.5, 0.5),fontsize='small')
ax.legend()
#ax.bar_label(rects1, padding=3)
#ax.bar_label(rects2, padding=3)

fig.tight_layout()
plt.savefig('UQ4_online')
plt.show()

