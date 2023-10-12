"""Binary Search works only for lists in sorted order.
    If item is in the list, function returns it's position."""

my_list = [1, 3, 5, 7, 9]

def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high)//2
        guess = list[mid]
        if guess == item:
            return mid
        elif guess > item:
            # guess is too high
            high = mid - 1
        else:
            # guess is too low
            low = mid + 1
    return None

print(binary_search(my_list, 3))# => 1
print(binary_search(my_list, -1)) # => None
