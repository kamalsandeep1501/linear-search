def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1
user_input = input("Enter the list elements separated by spaces: ")
arr = list(map(int, user_input.split()))
target = int(input("Enter the target value to search for: "))
index = linear_search(arr, target)
if index != -1:
    print(f'Target {target} found at index {index}')
else:
    print(f'Target {target} not found')
