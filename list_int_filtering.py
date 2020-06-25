def func(x):
  y=[]
  for i in x:
    if (type(i)==int):
      y.append(i)
  return y
l=[1,5,"ram",10, "apple",12, 70, "mango"]
z=func(l)
print(z)

