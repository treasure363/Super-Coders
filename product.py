def solve(arr):
  pn, pb, pa, ans = 1, 1, 1, arr[0]
  n = len(arr)

  for i in range(n):
    if arr[i] == 0: # Reset all
      ans = max(ans, pb, pa, pn)
      pb, pn, pa = 1, 1, 1
      continue

    if arr[i] < 0:
      pn *= arr[i]

    
    if pn > 0 and arr[i] > 0:
      pb *= arr[i]
    elif pn < 0 and arr[i] > 0:
      pa *= arr[i]
    elif pn > 0 and arr[i] < 0:
      pb *= pa * pn
      if pa == 1:
        pb = pn
    else:
      pa = 1
    
    # if pn > 0:
    #   pn = 1
    ans = max(ans, pb, pn, pa)
  return ans

def maxSubArray(arr: list) -> int:
  ans = max(solve(arr), solve(arr[::-1]))
  return max(arr) if max(arr) < ans else ans

arr = list(map(int, input().strip().split()))
print((maxSubArray(arr)))