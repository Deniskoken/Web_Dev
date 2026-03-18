def centered_average(nums):
  sum_all = sum(nums)
  max_val = max(nums)
  min_val = min(nums)
  
  centered_sum = sum_all - max_val - min_val
  count = len(nums) - 2
  
  return centered_sum // count