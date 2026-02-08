count = 0
def tof(n,fromm,to,aux):
    global count
    if n==1:
        print(f'move disc{n} fromm {fromm} to {to}')
        count=count+1
    else:
        count = count + 1
        tof(n-1,fromm,aux,to)
        print(f'move disc{n} fromm {fromm} to {to}')
        # count = count + 1
        tof(n-1,aux,to,fromm)
tof(3, 1, 3,2)
print(count)