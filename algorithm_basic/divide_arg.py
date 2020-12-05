from Algorithm.merge_sort import merge_sorted

def divide_arg(arg):
    if len(arg) < 2:
        return arg[:]
    else:
        middle = len(arg)//2
        l1 = divide_arg(arg[:middle])
        l2 = divide_arg(arg[middle:])
        return merge_sorted(l1, l2)

l = [8,6,2,5]
divide_arg(l)

