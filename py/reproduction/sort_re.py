import random

#N = random.randint(1000000, 9999999)
#print(N)

def buble_sort(li):
  change = True
  while change:
    change = False
    for i in range(len(li) - 1):
      if li[i] > li[i+1]:
        li[i], li[i+1] = li[i+1], li[i]
        change = True
  """for p in li:
    print(p, end="")
  print()"""


#backet使用
def bit_sort(li):
  input_data = li
  bitmap = [0 for x in range(1000000000)]
  for i in input_data:
    bitmap[i] = 1
  output_data = [p for p in range(1000000000) if bitmap[i] == 1]


  #print(f"input;{input_data}")
  #print(f"output;{output_data}")


def linked_merge_sort(lst):
    #print(lst)
    if len(lst) == 1:
        return
    
    #
    # 1. 分割
    #
    q, r = divmod(len(lst), 2)
    left = [lst.pop() for i in range(q)]
    right = [lst.pop() for i in range(q + r)]
    #print(left, right)
  
    #
    # 2. ソート
    #
    linked_merge_sort(left)
    linked_merge_sort(right)
    
    #
    # 3. 統合
    #
    left.reverse()  # 補足
    right.reverse()
    while left and right:
        if left[-1] <= right[-1]:
            lst.append(left.pop())
        else:
            lst.append(right.pop())
    while left:
        lst.append(left.pop())
    while right:
        lst.append(right.pop())
    #print(lst)

def count_sort(arr):
    max_num = max(arr)
    min_num = min(arr)
    count = [0] * (max_num - min_num + 1)
    for ele in arr:
        count[ele - min_num] += 1

    return [ele for ele, cnt in enumerate(count, start=min_num) for __ in range(cnt)]

def quick_sort(arr):
    left = []
    right = []
    if len(arr) <= 1:
        return arr

    # データの状態に左右されないためにrandom.choice()を用いることもある。
    # ref = random.choice(arr)
    ref = arr[0]
    ref_count = 0

    for ele in arr:
        if ele < ref:
            left.append(ele)
        elif ele > ref:
            right.append(ele)
        else:
            ref_count += 1
    left = quick_sort(left)
    right = quick_sort(right)
    return left + [ref] * ref_count + right