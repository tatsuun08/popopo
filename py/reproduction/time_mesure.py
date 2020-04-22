import time 
import random
import sort_re as sr

li = random.sample(range(0,999999999), 10000000)
random.shuffle(li)

def run_timer(func):
  start = time.time()
  func(li)
  end = time.time()
  runtime = end - start
  print(runtime)

def  Noarg_timer(func):
  start = time.time()
  func()
  end = time.time()
  runtime = end - start 
  print(runtime)


#run_timer(sr.buble_sort)
#run_timer(sr.bit_sort)
run_timer(sr.linked_merge_sort)
#run_timer(sr.quick_sort)
run_timer(sr.count_sort)


