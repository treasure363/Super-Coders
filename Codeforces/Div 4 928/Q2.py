def checkSquare(arr, n):
  tl = -1
  ind = -1
  bl = -1
  for i in range(n):
    if 1 in arr[i]:
      tl = arr[i]
      ind = i
      break
  for i in range(n-1, -1, -1):
    if 1 in arr[i]:
      bl = ''.join(arr[i]).strip('0')
      break
  return 


for _ in range(int(input())):
  n = int(input())
  arr = []
  for i in range(n):
    arr.append(input())
  if checkSquare(arr, n):
    print("Square")
  else:
    print("Triangle")
  