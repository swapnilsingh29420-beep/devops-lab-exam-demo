def fact(a):
  int f=0
  if a==0:
    return 1
  for i in range(1,a+1):
    f=f*i
  return f
