li = [6, 8, 1, 4, 10, 7, 8, 9, 3, 2, 5]

def selection_sort(arg):
    spot_marker = 0
    while spot_marker < len(arg):
        for num in range(spot_marker, len(li)):
            if arg[spot_marker] > arg[num]:
                arg[spot_marker], arg[num] = arg[num],arg[spot_marker]
        print(arg)
        spot_marker += 1
    print(arg) 

selection_sort(li)