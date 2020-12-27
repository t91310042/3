a= float(input("x2 nin katsayısı"))
b= float(input("x in katsayısı"))
c= float(input("c nin katsayısı"))
delta= b**2-(4*a*c)
print("delta:"+str(delta))
if delta>0: 
  print("reel 2 kök var")
  kök1= float((-b+(delta**1/2))/2*a)
  kök2= float((-b-(delta**1/2))/2*a)
  print("1. kök="+str(kök1)+" 2.kök="+str(kök2))

elif delta<0:
  print("reel kök yok")
else:
  print("eş reel kök var")
  kök0= -b/2*a
  print("kök="+str(kök0))