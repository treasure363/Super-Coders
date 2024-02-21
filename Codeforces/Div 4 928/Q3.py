def digitSum(n):
  s = 0
  while(n):
    s += n%10
    n //= 10
  return s

for _ in range(int(input())):
  n = int(input())
  for i in range(1, n):
    p = i
    print(digitSum(p))
    if len(str(digitSum(p)))!=1:
      p = digitSum(p)
    # print(p, end=" ")
  print()