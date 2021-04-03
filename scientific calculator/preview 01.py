# -----------------------------------------------------------------------------
# Copyright (c) 2015, Nicolas P. Rougier. All Rights Reserved.
# Distributed under the (new) BSD License. See LICENSE.txt for more info.
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
a=int(input("请输入a的值："))
b=int(input("请输入b的值："))
c=int(input("请输入c的值："))
fenmu=2*a
delta=b**2-4*a*c
b2=-1*b
a=str(a)
b=str(b)
c=str(c)
b2=str(b2)
fenmu=str(fenmu)
delta=str(delta)
eqs = []

eqs.append((r"$x_1=\frac{"+b2+"+\sqrt{"+delta+"}}{"+fenmu+"}$"))
plt.axes([0.025,0.025,0.95,0.95])

for i in range(1):
    index = np.random.randint(0,len(eqs))
    eq = eqs[index]
    size = 25
    x,y = 0.5,0.5
    alpha = 1.0
    plt.text(x, y, eq, ha='center', va='center', color="#11557c", alpha=alpha,
             transform=plt.gca().transAxes, fontsize=size, clip_on=True)

plt.xticks([]), plt.yticks([])
# savefig('../figures/text_ex.png',dpi=48)
plt.show()
eqs.append((r"$x_2=\frac{"+b2+"-\sqrt{"+delta+"}}{"+fenmu+"}$"))
plt.axes([0.025,0.025,0.95,0.95])

for i in range(1):
    index = np.random.randint(0,len(eqs))
    eq = eqs[index]
    size = 25
    x,y = 0.5,0.5
    alpha = 1.0
    plt.text(x, y, eq, ha='center', va='center', color="#11557c", alpha=alpha,
             transform=plt.gca().transAxes, fontsize=size, clip_on=True)

plt.xticks([]), plt.yticks([])
# savefig('../figures/text_ex.png',dpi=48)
plt.show()