for i in range(6):
    list = []
    for j in range(i):
        list.append('*')
    print(''.join(list))
    
    if i == 5:
        while(i-1):
            list = []
            for k in range(i-1):
                list.append('*')
            print(''.join(list))
            i -= 1