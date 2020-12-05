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