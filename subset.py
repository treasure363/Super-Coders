# generate all subsets
n = int(input())
arr = list(map(int, input().strip().split()))

out = {}

for i in range(n):
  for j in range(i+1,n+1):
    temp = arr[i:j]
    temp.sort()
    out.add(temp)

for i in out:
  print(out)

