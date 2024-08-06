def binary_search(a_list, an_item):
    first = 0 
    last = len(a_list) - 1

    while first <= last:
        mid_point = (first + last) // 2
        if a_list[mid_point] == an_item :
            return True
        else:
            if an_item < a_list[mid_point]:
                last = mid_point - 1
            else:
                first = mid_point +1
    return False

def binary_searching(a_list, first, last, an_item):
    if len(a_list) == 0:
        return False
    else:
        mid_point = (first + last) // 2
        if a_list[mid_point] == an_item :
            return True
        else:
            if an_item < a_list[mid_point]:
                last = mid_point - 1
                return binary_searching(a_list, first, last, an_item)
            else:
                first = mid_point +1
                return binary_searching(a_list, first, last, an_item)
            
if __name__ =='__main__':
    user_input = input("Enter a sorted list of numbers separated by spaces: ")
    a_list = list(map(int, user_input.split()))
    an_item = int(input("Enter the number to search for: "))
    print('Binary Search Recursive:',binary_searching(a_list, 0, len(a_list) -1, an_item))
