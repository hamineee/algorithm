def merge_sorted(arg1, arg2):
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

def divide_arg(arg):
    if len(arg) < 2:
        return arg[:]
    else:
        middle = len(arg)//2
        l1 = divide_arg(arg[:middle])
        l2 = divide_arg(arg[middle:])
        return merge_sorted(l1, l2)

l = [8,6,2,5]
print(divide_arg(l))


