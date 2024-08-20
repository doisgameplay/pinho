def ex1(n):
    if type(n) != int:
        print("Type Error")
        return None
    winner = 0 # the winner will have zero traingles in total at the begining
    current = 0
    answer = 0
    for p in range(n+1):
        if p < 3:
            continue
        for a in range(p):
            if a == 0:
                continue
            for b in range(p):
                if b == 0:
                    continue
                for c in range(p):
                    if c == 0:
                        continue
                    if( a*a == b*b + c*c and a+b+c == p):
                        #print(a,b,c,f"perimeter = {p}")
                        current +=1
        if current > winner:
            winner = current
            answer = p
        current = 0
    
    return answer


def ex2(m,n):
    if m >= n or type(m) != int or type(n) != int or m < 0 or n < 0:
        print("ERROR")
        return None
    list = []
    for index1 in range(n):
        templist = []
        for index2 in range(n):
            templist.append(0)        
        list.append(templist)
    
    index = 0
    for i in range(n*n):
        y = index // n
        y = y % n
        x = index - y*n
        x = x % n 
        if y == 0:
            x = index
            x = x % n
        #print(y,x,"asdasd", index)
        list[y][x] = i + 1
        index += m
        

    for l in list:
        print(l)
    

ex2(3,5)

