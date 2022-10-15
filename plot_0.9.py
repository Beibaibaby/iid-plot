import matplotlib.pyplot as plt
import numpy as np


labels = ['J1', 'J2', 'J3', 'J4', 'J5']

oklen = np.asarray([0.49278152, 0.49121216 ,0.48689639, 0.48846576 ,0.56317888				])
baseline = np.asarray([0.5797769034473631, 0.5802586944183976, 0.5796119014982525, 0.579331712665365, 0.5810500815040042])

baseline_07=np.asarray( [0.3553260385881075, 0.35311801380939567, 0.3549910439746062, 0.3534004777910202, 0.3532277274210819		])
olken_07=np.asarray( [0.45167624 ,0.52573651, 0.51285285 ,0.48913583, 0.51908688			 ])
differnece_07=olken_07-baseline_07
difference_09=np.absolute(oklen-baseline)

baseline_05=np.asarray( [0.27510453746524066, 0.274484620886037, 0.2757956204470265, 0.27463220897665924, 0.2780256477605313])
olken_05=np.asarray( [0.43058724, 0.44163679, 0.46850102, 0.4399103,  0.40252598							 ])
differnece_05=olken_05-baseline_05


olken_01 = np.asarray([0.48732978, 0.46666915 ,0.47772912 ,0.51367401, 0.45089846				])
baseline_01 = np.asarray([0.2123694262505772, 0.2088836061672904, 0.20748851293288578, 0.20915545825342605, 0.2116581594955531])
differnece_01=olken_01-baseline_01

olken_03 = np.asarray([0.45906421, 0.49342971 ,0.53472606, 0.52842528 ,0.49146071])
baseline_03= np.asarray([0.23476893416727146, 0.23606997863841048, 0.23530219050984424, 0.23527198035762067, 0.23807574412274873])

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
ax.set_title('|Ji|/|U| estimation error (UQ1) ')
ax.set_xticks(x, labels)
ax.legend(loc='center', bbox_to_anchor=(0.12, 0.6, 0.5, 0.5),fontsize='small')

#ax.bar_label(rects1, padding=3)
#ax.bar_label(rects2, padding=3)

fig.tight_layout()
plt.savefig('UQ1')
plt.show()

