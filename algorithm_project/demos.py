print("Algorithm file loaded, biatch")

def quick_sort(arg):
    if len(arg) < 2:
        return arg
    else:
        pivot = arg[-1]
        smaller, equal, larger = [], [], []
        for num in arg:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)
        return quick_sort(smaller) + equal + quick_sort(larger)

def merge_sorting(arg1, arg2):
    sorted_arg = []
    i,j = 0,0
    while i < len(arg1) and j < len(arg2):
        if arg1[i] < arg2[j]:
            sorted_arg.append(arg1[i])
            i += 1
        else:
            sorted_arg.append(arg2[j])
            j += 1
    while i < len(arg1):
        sorted_arg.append(arg1[i])
        i += 1
    while j < len(arg2):
        sorted_arg.append(arg2[j])
        j += 1
    return sorted_arg

def merge_sort(arg):
    if len(arg) < 2:
        return arg[:]
    else:
        middle = len(arg)//2
        l1 = merge_sort(arg[:middle])
        l2 = merge_sort(arg[middle:])
        return merge_sorting(l1, l2)

def bubble_sort(arg):
    swap_happened = True
    while swap_happened:
        swap_happened = False
        for num in range(len(arg)-1):
            if arg[num] > arg[num+1]:
                swap_happened = True
                arg[num], arg[num+1] = arg[num+1], arg[num]

