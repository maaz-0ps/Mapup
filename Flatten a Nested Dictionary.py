def permute(nums, start, end, result): 
  if start == end:
    result.append(nums[:])
    return
  visited = set()
  for i in range(start, end):
    if nums[i] not in visited:
      visited.add(nums[i])
      nums[start], nums[i] = nums[i], nums[start]
      permute(nums, start + 1, end, result)
      nums[start], nums[i] = nums[i], nums[start]
def generate_permutations(nums):
  result = []
  permute(nums, 0, len(nums), result)
  return result
nums = [1, 1, 2]
permutations = generate_permutations(nums)
print(permutations)