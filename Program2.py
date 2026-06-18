def binary_search(arr, search, low, high):
    if high>=low:
        mid = (high + low)//2
        if arr[mid] == search:
            print("The search element", search ,"is founded in index", mid )
        elif arr[mid] > search:
            return binary_search(arr, search, low, mid-1)
        else:
            return binary_search(arr, search, mid+1, high)
    else:
        print("The search is not founded")

list = [2,4,6,9,10,11,15,16,17]
binary_search(list, 11, 0, len(list)-1)

