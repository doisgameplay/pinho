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
    

def ex3(r1,r2):
    if (type(r1) != tuple or type(r2)!= tuple):
        print("not a tuple")
        return None

    for coordenate in r1:
        #print("asd")
        cl = r2[0]
        cr = r2[2]
        print(coordenate[0], coordenate[1]) 
        print(cl,cr)
        if( coordenate[0] >= cl[0] and coordenate[0] <= cr[0] and coordenate[1] <= cl[1] and coordenate[1] >= cr[1] ):
            return True

    return False


def ex4(**kwargs):
    colidables = []
    items = list(kwargs.items())
    for i, (n1, r1) in enumerate(items):
       for ( n2, r2) in items[i+1:]:
            if n1 == n2:
               continue
            if (type(r1) != tuple or type(r2)!= tuple):
                print("not a tuple")
                return None

            for coordenate in r1:
                cl = r2[0]
                cr = r2[2]
                if( coordenate[0] >= cl[0] and coordenate[0] <= cr[0] and coordenate[1] <= cl[1] and coordenate[1] >= cr[1] ):
                    tup = (n1,n2)
                    colidables.append(tup)
                    break
    
    print(colidables)
    return colidables

            
