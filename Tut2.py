from matplotlib import pyplot as p 
import numpy as n 

p.style.use("fivethirtyeight")

co_x = ["Maha","Ker","Har","UP","Kar","Del","La","Tel","Raj","J&K","AP","Od","Pun","TN","Ut","WB"]

x_indexes = n.arange(len(co_x))
width = 0.25

co_y = [42,27,14,14,13,8,6,5,4,3,1,1,1,1,1,1]

p.bar(x_indexes - width, co_y, width=width, linestyle='-',label="Active Cases")#u can also use format strings like k--

ran_2 = [21,24,11,13,5,7,4,3,9,12,1,2,1,0,0,0]

p.bar(x_indexes,ran_2, width=width,linestyle='-',linewidth=3,label="Random")

ran_3 = [12,11,10,9,8,7,6,5,4,3,2,1+4,4,3,2,1]

p.bar(x_indexes+width,ran_3,width=width,linestyle="-",linewidth=3,label="More Random")

p.xlabel("States")
p.ylabel("No. of active cases")
p.title("COVID-19 in India")

p.legend()

p.xticks(ticks=x_indexes,labels=co_x)

p.grid(True)

p.tight_layout()

p.savefig('plot.png')

p.show()
