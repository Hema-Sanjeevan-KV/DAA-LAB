def linear_search(arr, search):
    for i in range(len(arr)):
        if(arr[i]==search):
            print("The search element ", search ," is founded at the index ", i)
list = [2,4,6,7,9,10,12,14,18,20]
linear_search(list,14)