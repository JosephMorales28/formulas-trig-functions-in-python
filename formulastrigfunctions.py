import math

x=int(input("Enter number:\n"))
print ("choose you want to find the value of x\n1-sine\n2-cosine\n3-tangent\n4-squareroot\n5-pi\n6-secant\n7-cosecant\n8-cotangent\n")
value=int(input())

if value ==1:
   #find the sine of x
   result=math.sin(x)
   print("the sine value of",x,"is\n",result)
elif value ==2:
   #find the cosine of x
   result=math.cos(x)
   print("the cosine value of",x,"is\n",result)
elif value ==3:
   #find the tangent of x
   result=math.tan(x)
   print("the tangent value of",x,"is\n",result)
elif value==4:
   #find the squareroot of x
   result=math.sqrt(x)
   print("the squareroot of",x,"is\n",result)
elif value ==5:
   #use the value of pi
   result=math.pi
   print("the pi of",x,"is\n",result)
elif value==6:
   #find the secant of x
   result=1/math.cos(x)
   print("the secant value of",x,"is\n",result)
elif value==7:
   #find the cosecant of x
   result =1/math.sin(x)
   print("the cosecant value of",x,"is\n",result)
elif value==8:
   #fintbthe cotangent of x
   result=1/math.tan(x)
   print("the cotangent value of",x,"is\n",result)
else:
   print("invalid")