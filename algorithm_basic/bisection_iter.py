def bisection_iter(arg, n):
    start = 0
    end = len(arg)-1
    while start <= end:
        mid = (start + end)//2
        if arg[mid] == n:
            print(f'{n} found at index: {mid}')
        elif arg[mid] < n :
            start = mid + 1
        else:
            end = mid - 1


l = [1,2,3,4,5,6,7,8,9,10,11,13,13,14]
#    0,1,2,3,4,5,6,7,8,9, 10,11,12,13

bisection_iter(l, 10)