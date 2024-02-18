x = 123
def combo(b,n):
  i = 1
  while n:
    i *= b
    n-=1
  return i
