def linear_search(list, target):
    """
    returns the index position of the target if found, else returns none
    """
    for i in range(0,len(list)):
        if list[i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print("target found at index: ", index)
    else:
        print("target not found in list")

number = [1,2,3,4,5,6,7,8,9]

result = linear_search(number,12)
verify(result)
result = linear_search(number,6)
verify(result)