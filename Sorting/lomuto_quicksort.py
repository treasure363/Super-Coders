'''
partition (arr, s, e) {
  pi = arr[e]
  i = s
  j = s-1
  for i to (e-1) {
    if (arr[i] < arr[pi]) {
      j++;
      swap(arr[i], arr[j])
    }
  }
  return j
}

sort (arr, s, e) {
  if (s <= e) {
    pi = partition(arr, 0, e)
    sort(arr, 0, pi-1)
    sort(arr, pi+1, e)
  }
}
'''

def partition(arr, s, e):
  pivot = arr[e]
  i, j = s, s-1
  while(i<=e-1):
    # print(f'i={i}\tj={j}')
    if arr[i] < pivot:
      j += 1
      arr[i], arr[j] = arr[j], arr[i]
    # print(arr)
    i+=1
  j += 1
  arr[j], arr[e] = arr[e], arr[j]
  # print(arr)
  return j

def quick_sort(arr, s, e):
  if (s <= e):
    pi = partition(arr, 0, e)
    # print(pi)
    # return
    quick_sort(arr, 0, pi-1)
    quick_sort(arr, pi+1, e)

arr = list(map(int, input().strip().split()))
print("Input Array:\t", *arr)
quick_sort(arr, 0, len(arr)-1)
print("Sorted Array:\t", *arr)
