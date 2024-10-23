def reverse_groups(lst, n):
  num_full_groups = len(lst) // n
  for i in range(num_full_groups):
    start_index = i * n
    end_index = start_index + n
    left = start_index
    right = end_index - 1
    while left < right:
      lst[left], lst[right] = lst[right], lst[left]
      left += 1
      right -= 1
  remaining_elements = len(lst) % n
  if remaining_elements > 0:
    start_index = num_full_groups * n
    end_index = len(lst) - 1
    left = start_index
    right = end_index
    while left < right:
      lst[left], lst[right] = lst[right], lst[left]
      left += 1
      right -= 1

  return lst
user_input = input("Enter the list elements separated by spaces: ")
lst = [int(x) for x in user_input.split()]
n = int(input("Enter the group size: "))
result = reverse_groups(lst, n)
print("The modified list is:", result)