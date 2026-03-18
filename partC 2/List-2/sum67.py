def sum67(nums):
  total = 0
  add = True
  
  for n in nums:
    if n == 6:
      add = False
    
    if add:
      total += n
    
    if n == 7 and not add:
      add = True
      
  return total