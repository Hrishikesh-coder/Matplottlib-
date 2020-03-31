from matplotlib import pyplot as p 

p.xkcd()

co_x = ["Maha","Ker","Har","UP","Kar","Del","La","Tel","Raj","J&K","AP","Od","Pun","TN","Ut","WB"]

co_y = [42,27,14,14,13,8,6,5,4,3,1,1,1,1,1,1]

p.plot(co_x,co_y, color='#444444', linestyle='--' ,marker='.',label="Active Cases")#u can also use format strings like k--

ran_2 = [21,24,11,13,5,7,4,3,9,12,1,2,1,0,0,0]

p.plot(co_x,ran_2,  color='#5a7d9a', linestyle='-',linewidth=3,marker='o' ,label="Random")

ran_3 = [12,11,10,9,8,7,6,5,4,3,2,1+4,4,3,2,1]

p.plot(co_x,ran_3,color = "#adad3b",linestyle="-",linewidth=3,label="More Random")

p.xlabel("States")
p.ylabel("No. of active cases")
p.title("COVID-19 in India")

p.legend()

p.grid(True)

p.tight_layout()

p.savefig('plot.png')

p.show()
