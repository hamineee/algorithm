li_1 = [ 6,8,1,4,10,7,8,9,3,2,5]

def bubble_sort(arg):
    swap_happened = True
    while swap_happened:
        swap_happened = False
        print(arg)
        for num in range(len(arg)-1):
            if arg[num] > arg[num+1]:
                swap_happened = True
                arg[num], arg[num+1] = arg[num+1], arg[num]

# 1. grab the first element in the list, compare it to second element
#     arg[0] > arg[1]
# 2. compare for the remainder of the list, not just first two element
#     for num in range(len(arg)-1):
#         arg[num] > arg[num+1]
# 3. performing swap
#     for num in range(len(arg)-1):
#         if arg[num] > arg[num+1]:
#             arg[num],arg[num+1] = arg[num+1] > arg[num]
# 4. make any other iteration that necessary to get a completely sorted

# way 1 - run a loop for the number of elements that you have in the list
# if you nest this for loop inside another for loop which runs eleven times, then you'll end up with sorted array
# but this is not effcient, because it could end up with sorted list at fifth or sixth iteration, then it's running some extra steps 
# way 2 - use a 'flag' to track if a swap happened
# anytime there's a swap that takes place in this for loop, we're going to set the flag to true
# and then keep running it till it has a full run through this for loop through all the elements where no swap takes place

def bubble_bubble(arg):
    swap_happened = True # make boolean variable
    comparision = 0
    while swap_happened: # check for if swap_happened is true, and keep running this as long as swap_happend is True
        comparision += 1
        swap_happened = False
        print('bubble sort status:' + str(arg))
        for num in range(len(arg)-1):
            comparision += 1
            if arg[num] > arg[num+1]: 
                swap_happened = True
                arg[num],arg[num+1] = arg[num+1],arg[num]

bubble_bubble(li_1)
