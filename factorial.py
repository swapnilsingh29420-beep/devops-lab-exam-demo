def fact(a):
  f=1
  if a==0:
    return f
  for i in range(1,a+1):
    f=f*i
  return f
