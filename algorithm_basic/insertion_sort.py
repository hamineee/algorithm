def insertion_sort(arg):
    for key in range(1, len(arg)):
        if arg[key] < arg[key-1]:
            w_key =key
            while arg[w_key] < arg[w_key-1] and w_key > 0:
                arg[w_key], arg[w_key-1] = arg[w_key-1], arg[w_key]
                w_key -= 1
    return arg

l = [2,4,3,7,9,0,6,4,3]

print(insertion_sort(l))