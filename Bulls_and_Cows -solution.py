def two_cows(number):
    i=number[0]
    j=number[1]
    k=number[2]
    l=number[3]
    counter = 1
    print("Original number: ", number)

    a=l
    d=k
    for b in range(10):#4c 65 3c
        if b!=i and b!=j and b!=k and b!=l:
            for c in range(10):
                if c!=b and c!=i and c!=j and c!=k and c!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=l
    d=j
    for b in range(10):#4c 65 2c
        if b!=i and b!=j and b!=k and b!=l:
            for c in range(10):
                if c!=b and c!=i and c!=j and c!=k and c!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=l
    d=i
    for b in range(10):#4c 65 1c
        if b!=i and b!=j and b!=k and b!=l:
            for c in range(10):
                if c!=b and c!=i and c!=j and c!=k and c!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=k
    d=i
    for b in range(10):#3c 65 1c
        if b!=i and b!=j and b!=k and b!=l:
            for c in range(10):
                if c!=b and c!=i and c!=j and c!=k and c!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=k
    d=j
    for b in range(10):#3c 65 2c
        if b!=i and b!=j and b!=k and b!=l:
            for c in range(10):
                if c!=b and c!=i and c!=j and c!=k and c!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=j
    d=k
    for b in range(10):#2c 65 3c
        if b!=i and b!=j and b!=k and b!=l:
            for c in range(10):
                if c!=b and c!=i and c!=j and c!=k and c!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=j
    d=i
    for b in range(10):#2c 65 1c
        if b!=i and b!=j and b!=k and b!=l:
            for c in range(10):
                if c!=b and c!=i and c!=j and c!=k and c!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=l
    c=j
    for b in range(10):#4c 6 2c 5
        if b!=i and b!=j and b!=k and b!=l:
            for d in range(10):
                if d!=b and d!=i and d!=j and d!=k and d!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=l
    c=i
    for b in range(10):#4c 6 1c 5
        if b!=i and b!=j and b!=k and b!=l:
            for d in range(10):
                if d!=b and d!=i and d!=j and d!=k and d!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=k
    c=j
    for b in range(10):#3c 6 2c 5
        if b!=i and b!=j and b!=k and b!=l:
            for d in range(10):
                if d!=b and d!=i and d!=j and d!=k and d!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=k
    c=i
    for b in range(10):#3c 6 1c 5
        if b!=i and b!=j and b!=k and b!=l:
            for d in range(10):
                if d!=b and d!=i and d!=j and d!=k and d!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=k
    c=l
    for b in range(10):#3c 6 4c 5
        if b!=i and b!=j and b!=k and b!=l:
            for d in range(10):
                if d!=b and d!=i and d!=j and d!=k and d!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=j
    c=i
    for b in range(10):#2c 6 1c 5
        if b!=i and b!=j and b!=k and b!=l:
            for d in range(10):
                if d!=b and d!=i and d!=j and d!=k and d!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=j
    c=l
    for b in range(10):#2c 6 4c 5
        if b!=i and b!=j and b!=k and b!=l:
            for d in range(10):
                if d!=b and d!=i and d!=j and d!=k and d!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1                    

    a=l
    b=i
    for c in range(10):#4c 1c 65
        if c!=i and c!=j and c!=k and c!=l:
            for d in range(10):
                if d!=b and d!=i and d!=j and d!=k and d!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=l
    b=k
    for c in range(10):#4c 3c 65
        if c!=i and c!=j and c!=k and c!=l:
            for d in range(10):
                if d!=b and d!=i and d!=j and d!=k and d!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=k
    b=i
    for c in range(10):#3c 1c 65
        if c!=i and c!=j and c!=k and c!=l:
            for d in range(10):
                if d!=b and d!=i and d!=j and d!=k and d!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1


    a=k
    b=l
    for c in range(10):#3c 4c 65
        if c!=i and c!=j and c!=k and c!=l:
            for d in range(10):
                if d!=b and d!=i and d!=j and d!=k and d!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=j
    b=k
    for c in range(10):#2c 3c 65
        if c!=i and c!=j and c!=k and c!=l:
            for d in range(10):
                if d!=b and d!=i and d!=j and d!=k and d!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=j
    b=i
    for c in range(10):#2c 1c 65
        if c!=i and c!=j and c!=k and c!=l:
            for d in range(10):
                if d!=b and d!=i and d!=j and d!=k and d!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=j
    b=l
    for c in range(10):#2c 4c 65
        if c!=i and c!=j and c!=k and c!=l:
            for d in range(10):
                if d!=b and d!=i and d!=j and d!=k and d!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    c=i
    d=j
    for a in range(10):#65 1c 2c 
        if a!=i and a!=j and a!=k and a!=l:
            for b in range(10):
                if b!=a and b!=i and b!=j and b!=k and b!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    c=j
    d=i
    for a in range(10):#65 2c 1c 
        if a!=i and a!=j and a!=k and a!=l:
            for b in range(10):
                if b!=a and b!=i and b!=j and b!=k and b!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    c=j
    d=k
    for a in range(10):#65 2c 3c 
        if a!=i and a!=j and a!=k and a!=l:
            for b in range(10):
                if b!=a and b!=i and b!=j and b!=k and b!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    c=i
    d=k
    for a in range(10):#65 1c 3c 
        if a!=i and a!=j and a!=k and a!=l:
            for b in range(10):
                if b!=a and b!=i and b!=j and b!=k and b!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    c=l
    d=i
    for a in range(10):#65 4c 1c 
        if a!=i and a!=j and a!=k and a!=l:
            for b in range(10):
                if b!=a and b!=i and b!=j and b!=k and b!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    c=l
    d=j
    for a in range(10):#65 4c 2c 
        if a!=i and a!=j and a!=k and a!=l:
            for b in range(10):
                if b!=a and b!=i and b!=j and b!=k and b!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    b=i
    d=k
    for a in range(10):#6 1c 5 3c 
        if a!=i and a!=j and a!=k and a!=l:
            for c in range(10):
                if c!=a and c!=i and c!=j and c!=k and c!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    b=k
    d=i
    for a in range(10):#6 3c 5 1c 
        if a!=i and a!=j and a!=k and a!=l:
            for c in range(10):
                if c!=a and c!=i and c!=j and c!=k and c!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    b=k
    d=j
    for a in range(10):#6 3c 5 2c 
        if a!=i and a!=j and a!=k and a!=l:
            for c in range(10):
                if c!=a and c!=i and c!=j and c!=k and c!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    b=i
    d=j
    for a in range(10):#6 1c 5 2c 
        if a!=i and a!=j and a!=k and a!=l:
            for c in range(10):
                if c!=a and c!=i and c!=j and c!=k and c!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    b=l
    d=j
    for a in range(10):#6 4c 5 2c 
        if a!=i and a!=j and a!=k and a!=l:
            for c in range(10):
                if c!=a and c!=i and c!=j and c!=k and c!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    b=l
    d=i
    for a in range(10):#6 4c 5 1c 
        if a!=i and a!=j and a!=k and a!=l:
            for c in range(10):
                if c!=a and c!=i and c!=j and c!=k and c!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    b=k
    c=i
    for a in range(10):#6 3c 1c 5 
        if a!=i and a!=j and a!=k and a!=l:
            for d in range(10):
                if d!=a and d!=i and d!=j and d!=k and d!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    b=k
    c=j
    for a in range(10):#6 3c 2c 5 
        if a!=i and a!=j and a!=k and a!=l:
            for d in range(10):
                if d!=a and d!=i and d!=j and d!=k and d!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    b=k
    c=l
    for a in range(10):#6 3c 4c 5 
        if a!=i and a!=j and a!=k and a!=l:
            for d in range(10):
                if d!=a and d!=i and d!=j and d!=k and d!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1
                    
    b=i
    c=k
    for a in range(10):#6 1c 4c 5 
        if a!=i and a!=j and a!=k and a!=l:
            for d in range(10):
                if d!=a and d!=i and d!=j and d!=k and d!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1
                    
    print(f"Total two cows {counter-1} numbers")

def three_cows(number):
    array=[0]*4
    i=number[0]#1
    j=number[1]#2
    k=number[2]#3
    l=number[3]#4
    counter = 1
    print("Original number: ", number)

    a=l
    c=j
    d=k
    for b in range(10):#4c x 2c 3c  
        if b!=i and b!=j and b!=k and b!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1
    a=l
    c=i
    d=j
    for b in range(10):#4c x 1c 2c  
        if b!=i and b!=j and b!=k and b!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=l
    c=j
    d=i
    for b in range(10):#4c x 2c 1c  
        if b!=i and b!=j and b!=k and b!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=l
    c=i
    d=k
    for b in range(10):#4c x 1c 3c  
        if b!=i and b!=j and b!=k and b!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1
    a=k
    c=j
    d=i
    for b in range(10):#3c x 2c 1c 
        if b!=i and b!=j and b!=k and b!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=k
    c=i
    d=j
    for b in range(10):#3c x 1c 2c 
        if b!=i and b!=j and b!=k and b!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1
                    
    a=k
    c=l
    d=i
    for b in range(10):#3c x 4c 1c 
        if b!=i and b!=j and b!=k and b!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=k
    c=l
    d=j
    for b in range(10):#3c x 4c 2c 
        if b!=i and b!=j and b!=k and b!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=j
    c=l
    d=k
    for b in range(10):#2c x 4c 3c 
        if b!=i and b!=j and b!=k and b!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=j
    c=l
    d=i
    for b in range(10):#2c x 4c 1c 
        if b!=i and b!=j and b!=k and b!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1
                    
    a=j
    c=i
    d=k
    for b in range(10):#2c x 1c 3c 
        if b!=i and b!=j and b!=k and b!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    b=i
    c=j
    d=k
    for a in range(10):#x 1c 2c 3c 
        if a!=i and a!=j and a!=k and a!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    b=i
    c=l
    d=k
    for a in range(10):#x 1c 4c 3c 
        if a!=i and a!=j and a!=k and a!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1
                    
    b=k
    c=l
    d=i
    for a in range(10):#x 3c 4c 1c 
        if a!=i and a!=j and a!=k and a!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    b=l
    c=i
    d=k
    for a in range(10):#x 4c 1c 3c 
        if a!=i and a!=j and a!=k and a!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    b=l
    c=i
    d=j
    for a in range(10):#x 4c 1c 2c 
        if a!=i and a!=j and a!=k and a!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1
                    
    b=k
    c=j
    d=i
    for a in range(10):#x 3c 2c 1c 
        if a!=i and a!=j and a!=k and a!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1
    b=k
    c=l
    d=j
    for a in range(10):#x 3c 4c 2c 
        if a!=i and a!=j and a!=k and a!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    b=i
    c=l
    d=j
    for a in range(10):#x 1c 4c 2c 
        if a!=i and a!=j and a!=k and a!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1
                    
    b=l
    c=j
    d=k
    for a in range(10):#x 4c 2c 3c 
        if a!=i and a!=j and a!=k and a!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1
    b=l
    c=j
    d=i
    for a in range(10):#x 4c 2c 1c 
        if a!=i and a!=j and a!=k and a!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    b=k
    c=i
    d=j
    for a in range(10):#x 3c 1c 2c 
        if a!=i and a!=j and a!=k and a!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=l
    b=i
    d=k
    for c in range(10):#4c 1c x 3c 
        if c!=i and c!=j and c!=k and c!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=l
    b=k
    d=i
    for c in range(10):#4c 3c x 1c 
        if c!=i and c!=j and c!=k and c!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=l
    b=k
    d=j
    for c in range(10):#4c 3c x 2c 
        if c!=i and c!=j and c!=k and c!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=l
    b=i
    d=j
    for c in range(10):#4c 1c x 2c 
        if c!=i and c!=j and c!=k and c!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=k
    b=l
    d=j
    for c in range(10):#3c 4c x 2c 
        if c!=i and c!=j and c!=k and c!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=k
    b=l
    d=i
    for c in range(10):#3c 4c x 1c 
        if c!=i and c!=j and c!=k and c!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=k
    b=i
    d=j
    for c in range(10):#3c 1c x 2c 
        if c!=i and c!=j and c!=k and c!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=j
    b=l
    d=i
    for c in range(10):#2c 4c x 1c 
        if c!=i and c!=j and c!=k and c!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=j
    b=l
    d=k
    for c in range(10):#2c 4c x 3c 
        if c!=i and c!=j and c!=k and c!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=j
    b=i
    d=k
    for c in range(10):#2c 1c x 3c 
        if c!=i and c!=j and c!=k and c!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=j
    b=k
    d=i
    for c in range(10):#2c 3c x 1c 
        if c!=i and c!=j and c!=k and c!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=l
    b=i
    c=j
    for d in range(10):#4c 1c 2c x  
        if d!=i and d!=j and d!=k and d!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1
                    
    a=l
    b=k
    c=i
    for d in range(10):#4c 3c 1c x  
        if d!=i and d!=j and d!=k and d!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=l
    b=k
    c=j
    for d in range(10):#4c 3c 2c x  
        if d!=i and d!=j and d!=k and d!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=k
    b=i
    c=l
    for d in range(10):#3c 1c 4c x  
        if d!=i and d!=j and d!=k and d!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=k
    b=l
    c=j
    for d in range(10):#3c 4c 2c x  
        if d!=i and d!=j and d!=k and d!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=k
    b=l
    c=i
    for d in range(10):#3c 4c 1c x  
        if d!=i and d!=j and d!=k and d!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=k
    b=i
    c=j
    for d in range(10):#3c 1c 2c x  
        if d!=i and d!=j and d!=k and d!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=j
    b=k
    c=i
    for d in range(10):#2c 3c 1c x  
        if d!=i and d!=j and d!=k and d!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=j
    b=i
    c=l
    for d in range(10):#2c 1c 4c x  
        if d!=i and d!=j and d!=k and d!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=j
    b=k
    c=l
    for d in range(10):#2c 3c 4c x  
        if d!=i and d!=j and d!=k and d!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1

    a=j
    b=l
    c=i
    for d in range(10):#2c 4c 1c x  
        if d!=i and d!=j and d!=k and d!=l:
                    print(f"{counter}: {a}{b}{c}{d}" )
                    counter+=1
                    
    print(f"Total three cows {counter-1} numbers")


def one_bull_two_cows(number):
    i = number[0]  # 1
    j = number[1]  # 2
    k = number[2]  # 3
    l = number[3]  # 4
    counter = 1
    print("Original number: ", number)

    a = i
    b = k
    c = j
    for d in range(10):  # 1b 3c2cx
        if d != i and d != j and d != k and d != l:
            print(f"{counter}: {a}{b}{c}{d}")
            counter += 1

    a = i
    b = k
    d = j
    for c in range(10):  # 1b 3cx2c
        if c != i and c != j and c != k and c != l:
            print(f"{counter}: {a}{b}{c}{d}")
            counter += 1

    a = i
    c = j
    d = k
    for b in range(10):  # 1b x2c3c
        if b != i and b != j and b != k and b != l:
            print(f"{counter}: {a}{b}{c}{d}")
            counter += 1

    a = i
    b = l
    c = j
    for d in range(10):  # 1b 4c2cx
        if d != i and d != j and d != k and d != l:
            print(f"{counter}: {a}{b}{c}{d}")
            counter += 1

    a = i
    b = l
    d = j
    for c in range(10):  # 1b 4cx2c
        if c != i and c != j and c != k and c != l:
            print(f"{counter}: {a}{b}{c}{d}")
            counter += 1

    a = i
    c = l
    d = j
    for b in range(10):  # 1b x4c2c
        if b != i and b != j and b != k and b != l:
            print(f"{counter}: {a}{b}{c}{d}")
            counter += 1

    a = i
    c = l
    d = k
    for b in range(10):  # 1b x4c3c
        if b != i and b != j and b != k and b != l:
            print(f"{counter}: {a}{b}{c}{d}")
            counter += 1

    a = i
    b = k
    c = l
    for d in range(10):  # 1b 3c4cx
        if d != i and d != j and d != k and d != l:
            print(f"{counter}: {a}{b}{c}{d}")
            counter += 1

    a = i
    b = l
    d = k
    for c in range(10):  # 1b 4cx3c
        if c != i and c != j and c != k and c != l:
            print(f"{counter}: {a}{b}{c}{d}")
            counter += 1
    print("")

    b = j
    c = i
    d = k
    for a in range(10):  # x 2b 1c3c
        if a != i and a != j and a != k and a != l:
            print(f"{counter}: {a}{b}{c}{d}")
            counter += 1

    b = j
    c = l
    d = i
    for a in range(10):  # x 2b 4c 1c
        if a != i and a != j and a != k and a != l:
            print(f"{counter}: {a}{b}{c}{d}")
            counter += 1

    b = j
    c = l
    d = k
    for a in range(10):  # x 2b 4c 3c
        if a != i and a != j and a != k and a != l:
            print(f"{counter}: {a}{b}{c}{d}")
            counter += 1

    a = k
    b = j
    d = i
    for c in range(10):  # 3c 2b x 1c
        if c != i and c != j and c != k and c != l:
            print(f"{counter}: {a}{b}{c}{d}")
            counter += 1

    a = l
    b = j
    d = k
    for c in range(10):  # 4c 2b x 3c
        if c != i and c != j and c != k and c != l:
            print(f"{counter}: {a}{b}{c}{d}")
            counter += 1

    a = l
    b = j
    d = i
    for c in range(10):  # 4c 2b x 1c
        if c != i and c != j and c != k and c != l:
            print(f"{counter}: {a}{b}{c}{d}")
            counter += 1

    a = k
    b = j
    c = i
    for d in range(10):  # 3c 2b 1c x
        if d != i and d != j and d != k and d != l:
            print(f"{counter}: {a}{b}{c}{d}")
            counter += 1

    a = k
    b = j
    c = l
    for d in range(10):  # 3c 2b 4c x
        if d != i and d != j and d != k and d != l:
            print(f"{counter}: {a}{b}{c}{d}")
            counter += 1

    a = l
    b = j
    c = i
    for d in range(10):  # 4c 2b 1c x
        if d != i and d != j and d != k and d != l:
            print(f"{counter}: {a}{b}{c}{d}")
            counter += 1

    a = j
    b = l
    c = k
    for d in range(10):  # 2с 4c 3b x
        if d != i and d != j and d != k and d != l:
            print(f"{counter}: {a}{b}{c}{d}")
            counter += 1

    a = l
    b = i
    c = k
    for d in range(10):  # 4с 1c 3b x
        if d != i and d != j and d != k and d != l:
            print(f"{counter}: {a}{b}{c}{d}")
            counter += 1

    a = j
    b = l
    c = k
    for d in range(10):  # 2с 4c 3b x
        if d != i and d != j and d != k and d != l:
            print(f"{counter}: {a}{b}{c}{d}")
            counter += 1

    b = i
    c = k
    d = j
    for a in range(10):  # x 1с 3b 2c
        if a != i and a != j and a != k and a != l:
            print(f"{counter}: {a}{b}{c}{d}")
            counter += 1

    b = l
    c = k
    d = i
    for a in range(10):  # x 4с 3b 1c
        if a != i and a != j and a != k and a != l:
            print(f"{counter}: {a}{b}{c}{d}")
            counter += 1

    b = l
    c = k
    d = j
    for a in range(10):  # x 4с 3b 2c
        if a != i and a != j and a != k and a != l:
            print(f"{counter}: {a}{b}{c}{d}")
            counter += 1

    a = j
    c = k
    d = i
    for b in range(10):  # 2c x 3b 1c
        if b != i and b != j and b != k and b != l:
            print(f"{counter}: {a}{b}{c}{d}")
            counter += 1

    a = l
    c = k
    d = j
    for b in range(10):  # 4c x 3b 2c
        if b != i and b != j and b != k and b != l:
            print(f"{counter}: {a}{b}{c}{d}")
            counter += 1

    a = l
    c = k
    d = i
    for b in range(10):  # 4c x 3b 1c
        if b != i and b != j and b != k and b != l:
            print(f"{counter}: {a}{b}{c}{d}")
            counter += 1

    b = i
    c = j
    d = l
    for a in range(10):  # x 1c2c 4b
        if a != i and a != j and a != k and a != l:
            print(f"{counter}: {a}{b}{c}{d}")
            counter += 1

    b = k
    c = i
    d = l
    for a in range(10):  # x 3c 1c 4b
        if a != i and a != j and a != k and a != l:
            print(f"{counter}: {a}{b}{c}{d}")
            counter += 1

    b = k
    c = j
    d = l
    for a in range(10):  # x 3c 2c 4b
        if a != i and a != j and a != k and a != l:
            print(f"{counter}: {a}{b}{c}{d}")
            counter += 1

    a = j
    c = i
    d = l
    for b in range(10):  # 2c x 1c 4b
        if b != i and b != j and b != k and b != l:
            print(f"{counter}: {a}{b}{c}{d}")
            counter += 1

    a = k
    c = i
    d = l
    for b in range(10):  # 3c x 1c 4b
        if b != i and b != j and b != k and b != l:
            print(f"{counter}: {a}{b}{c}{d}")
            counter += 1

    a = k
    c = j
    d = l
    for b in range(10):  # 3c x 2c 4b
        if b != i and b != j and b != k and b != l:
            print(f"{counter}: {a}{b}{c}{d}")
            counter += 1

    a = j
    b = i
    d = l
    for c in range(10):  # 2c 1c x 4b
        if c != i and c != j and c != k and c != l:
            print(f"{counter}: {a}{b}{c}{d}")
            counter += 1

    a = k
    b = i
    d = l
    for c in range(10):  # 3c 1c x 4b
        if c != i and c != j and c != k and c != l:
            print(f"{counter}: {a}{b}{c}{d}")
            counter += 1

    a = j
    b = k
    d = l
    for c in range(10):  # 2c 3c x 4b
        if c != i and c != j and c != k and c != l:
            print(f"{counter}: {a}{b}{c}{d}")
            counter += 1

    print(f"Total one bull and two cows {counter - 1} numbers")

def one_bull(number):
    array=[0]*4
    i=number[0]
    j=number[1]
    k=number[2]
    l=number[3]
    counter = 1
    print("Original number: ", number)

    a=i
    for b in range(10):#1 digit=bull
        if b!=a and b!=j and b!=k and b!=l:
            for c in range(10):
                if c!=a and c!=b and c!=j and c!=k and c!=l:
                    for d in range(10):
                        if d!=a and d!=b and d!=c and d!=j and d!=k and d!=l:
                            #print(f"{counter}: {a}{b}{c}{d}" )
                            counter+=1
    b=j
    for a in range(10):#2 digit=bull
        if a!=b and a!=i and a!=k and a!=l:
            for c in range(10):
                if c!=a and c!=b and c!=i and c!=k and c!=l:
                    for d in range(10):
                        if d!=a and d!=b and d!=c and d!=i and d!=k and d!=l:
                            #print(f"{counter}: {a}{b}{c}{d}" )
                            counter+=1
    c=k
    for a in range(10):#3 digit=bull
        if a!=c and a!=i and a!=j and a!=l:
            for b in range(10):
                if b!=a and b!=c and b!=i and b!=j and b!=l:
                    for d in range(10):
                        if d!=a and d!=b and d!=c and d!=i and d!=j and d!=l:
                            #print(f"{counter}: {a}{b}{c}{d}" )
                            counter+=1

    d=l

    for a in range(10):#4 digit is bull
        if a!=d and a!=i and a!=j and a!=k:
            for b in range(10):
                if b!=a and b!=d and b!=i and b!=j and b!=k:
                    for c in range(10):
                        if c!=a and c!=b and c!=d and c!=i and c!=j and c!=k:
                            #print(f"{counter}: {a}{b}{c}{d}" )
                            counter+=1
    print(f"Total one bull {counter-1} numbers")#480

def no_bulls_no_cows(number):
    array=[0]*4
    i=number[0]
    j=number[1]
    k=number[2]
    l=number[3]
    counter = 1
    print("Original number: ", number)
    for a in range(10):
        if a!=i and a!=j and a!=k and a!=l:
            for b in range(10):
                if b!=i and b!=j and b!=k and b!=l and b!=a:
                    for c in range(10):
                        if c!=i and c!=j and c!=k and c!=l and c!=a and c!=b:
                            for d in range(10):
                                if d!=i and d!=j and d!=k and d!=l and d!=a and d!=b and d!=c:
                    #                print(f"{counter}: {a}{b}{c}{d}" )
                                    counter+=1
    print(f"Total no bulls and cows {counter-1} numbers")#360

def three_bulls(number):
    print(f"Options for 3 bulls for {number}: ")
    array = number.copy()
    counter = 1
    i=number[0]
    j=number[1]
    k=number[2]
    l=number[3]

    for n in range(4):
        if n>0:
            array[n-1]=number[n-1]#restore element
        for a in range(10):
            if a!=j and a!=k and a!=l and a!=i:
                array[n]=a
                print("#", counter, ": ", array)
                counter+=1
    print(f"3 bulls: there are {counter-1} numbers")#24

def two_bulls(number):
    print(f"Options for 2 bulls for {number}: ")
    two_bulls_array=[]
    counter = 1
    i=number[0]
    j=number[1]
    k=number[2]
    l=number[3]

    for a in range(10):#bulls digit1 and digit2
        if a!=i and a!=j and a!=k and a!=l:
           for b in range(10):
               if b!=i and b!=j and b!=k and b!=l and b!=a:
                   two_bulls_array.append(convert_2_number(i,j,a,b))
                   counter+=1

    for a in range(10):#bulls digit1 and digit3
       if a!=i and a!=j and a!=k and a!=l:
           for b in range(10):
               if b!=i and b!=j and b!=k and b!=l and b!=a:
                   two_bulls_array.append(convert_2_number(i, a, k, b))
                   counter+=1

    for a in range(10):#bulls digit1 and digit4
       if a!=i and a!=j and a!=k and a!=l:
           for b in range(10):
               if b!=i and b!=j and b!=k and b!=l and b!=a:
                   two_bulls_array.append(convert_2_number(i, a, b, l))
                   counter+=1

    for a in range(10):  # bulls digit2 and digit3
        if a != i and a != j and a != k and a != l:
            for b in range(10):
                if b != i and b != j and b != k and b != l and b != a:
                    two_bulls_array.append(convert_2_number(a, j, k, b))
                    counter += 1

    for a in range(10):  # bulls digit2 and digit4
        if a != i and a != j and a != k and a != l:
            for b in range(10):
                if b != i and b != j and b != k and b != l and b != a:
                    two_bulls_array.append(convert_2_number(a, j, b, l))
                    counter += 1

    for a in range(10):  # bulls digit3 and digit4
        if a != i and a != j and a != k and a != l:
            for b in range(10):
                if b != i and b != j and b != k and b != l and b != a:
                    two_bulls_array.append(convert_2_number(a, b, k, l))
                    counter += 1
    print("two_bulls_array: ",two_bulls_array)
    print(f"2 bulls: there are {counter-1} numbers")#180

def two_bull_two_cows(number):
    print(f"Options for 2 bulls and 2 cows for {number}: ")
    two_bull_two_cows_array = []
    counter = 0
    i=number[0]#1
    j=number[1]#2
    k=number[2]#3
    l=number[3]#4

    #[i,j,l,k]#1243
    a=i
    b=j
    c=l
    d=k
    two_bull_two_cows_array.append(convert_2_number(a, b, c, d))
    counter+=1

    #[i,l,k,j]#1432
    a=i
    b=l
    c=k
    d=j
    two_bull_two_cows_array.append(convert_2_number(a, b, c, d))
    counter+=1

    #[i,k,j,l]#1324
    a=i
    b=k
    c=j
    d=l
    two_bull_two_cows_array.append(convert_2_number(a, b, c, d))
    counter += 1

    #[l,j,k,i]#4231
    a=l
    b=j
    c=k
    d=i
    two_bull_two_cows_array.append(convert_2_number(a, b, c, d))
    counter += 1

    #[k,j,i,l]#3214
    a=k
    b=j
    c=i
    d=l
    two_bull_two_cows_array.append(convert_2_number(a, b, c, d))
    counter += 1

    #[j,i,k,l]#2134
    a=j
    b=i
    c=k
    d=l
    two_bull_two_cows_array.append(convert_2_number(a, b, c, d))
    counter += 1

    print("two_bull_two_cows_array: ", two_bull_two_cows_array)
    print(f"Total two bulls and two cows {counter} numbers")
   

 def one_cow(number):
    print(f"Options for 1 cow for {number}: ")
    one_cow_array = []
    counter=1
    i=number[0]#1
    j=number[1]#2
    k=number[2]#3
    l=number[3]#4

    for a in range(10):#cow digit1 from place2
        if a!=i and a!=j and a!=k and a!=l:
            for b in range(10):
                if b!=a and b!=i and  b!=j and b!=k  and b!=l:
                    for c in range(10):
                        if c!=a and c!=b and c!=i and c!=j and c!=k and c!=l:
                            #print(j,a,b,c )
                            one_cow_array.append(convert_2_number(j,a,b,c))
                            counter+=1
    print(f"{counter}")

    for a in range(10):#cow digit1 from place3
        if a!=i and a!=j and a!=k and a!=l:
            for b in range(10):
                if b!=a and b!=i and b!=j and b!=k  and b!=l:
                    for c in range(10):
                        if c!=a and c!=b and c!=i and c!=j and c!=k and c!=l:
                            #print(k,a,b,c )
                            one_cow_array.append(convert_2_number(k, a, b, c))
                            counter+=1

    for a in range(10):#cow digit1 from place4
        if a!=i and a!=j and a!=k and a!=l:
            for b in range(10):
                if b!=a and b!=i and b!=j and b!=k  and b!=l:
                    for c in range(10):
                        if c!=a and c!=b and c!=i and c!=j and c!=k and c!=l:
                            #print(l,a,b,c )
                            one_cow_array.append(convert_2_number(l, a, b, c))
                            counter+=1

    for a in range(10):#cow digit2 from place1
        if a!=i and a!=j and a!=k and a!=l:
            for b in range(10):
                if b!=a and b!=i and b!=j and b!=k  and b!=l:
                    for c in range(10):
                        if c!=a and c!=b and c!=i and c!=j and c!=k and c!=l:
                            #print(a,i,b,c )
                            one_cow_array.append(convert_2_number(a, i, b, c))
                            counter+=1

    for a in range(10):#cow digit2 from place3
        if a!=i and a!=j and a!=k and a!=l:
            for b in range(10):
                if b!=a and b!=i and b!=j and b!=k  and b!=l:
                    for c in range(10):
                        if c!=a and c!=b and c!=i and c!=j and c!=k and c!=l:
                            #print(a,k,b,c )
                            one_cow_array.append(convert_2_number(a, k, b, c))
                            counter+=1

    for a in range(10):#cow digit2 from place4
        if a!=i and a!=j and a!=k and a!=l:
            for b in range(10):
                if b!=a and b!=i and b!=j and b!=k  and b!=l:
                    for c in range(10):
                        if c!=a and c!=b and c!=i and c!=j and c!=k and c!=l:
                            #print(a,l,b,c )
                            one_cow_array.append(convert_2_number(a, l, b, c))
                            counter+=1

    for a in range(10):#cow digit3 from place1
        if a!=i and a!=j and a!=k and a!=l:
            for b in range(10):
                if b!=a and b!=i and b!=j and b!=k  and b!=l:
                    for c in range(10):
                        if c!=a and c!=b and c!=i and c!=j and c!=k and c!=l:
                            #print(a,b,i,c )
                            one_cow_array.append(convert_2_number(a, b,i, c))
                            counter+=1

    for a in range(10):#cow digit3 from place2
        if a!=i and a!=j and a!=k and a!=l:
            for b in range(10):
                if b!=a and b!=i and b!=j and b!=k  and b!=l:
                    for c in range(10):
                        if c!=a and c!=b and c!=i and c!=j and c!=k and c!=l:
                            #print(a,b,j,c )
                            one_cow_array.append(convert_2_number(a, b,j, c))
                            counter+=1

    for a in range(10):#cow digit3 from place4
        if a!=i and a!=j and a!=k and a!=l:
            for b in range(10):
                if b!=a and b!=i and b!=j and b!=k  and b!=l:
                    for c in range(10):
                        if c!=a and c!=b and c!=i and c!=j and c!=k and c!=l:
                            #print(a,b,l,c )
                            one_cow_array.append(convert_2_number(a, b,l, c))
                            counter+=1

    for a in range(10):#cow digit4 from place1
        if a!=i and a!=j and a!=k and a!=l:
            for b in range(10):
                if b!=a and b!=i and b!=j and b!=k  and b!=l:
                    for c in range(10):
                        if c!=a and c!=b and c!=i and c!=j and c!=k and c!=l:
                            #print(a,b,c,i )
                            one_cow_array.append(convert_2_number(a, b, c,i))
                            counter+=1


    for a in range(10):#cow digit4 from place2
        if a!=i and a!=j and a!=k and a!=l:
            for b in range(10):
                if b!=a and b!=i and b!=j and b!=k  and b!=l:
                    for c in range(10):
                        if c!=a and c!=b and c!=i and c!=j and c!=k and c!=l:
                            #print(a,b,c,j )
                            one_cow_array.append(convert_2_number(a, b, c,j))
                            counter+=1


    for a in range(10):#cow digit4 from place3
        if a!=i and a!=j and a!=k and a!=l:
            for b in range(10):
                if b!=a and b!=i and b!=j and b!=k  and b!=l:
                    for c in range(10):
                        if c!=a and c!=b and c!=i and c!=j and c!=k and c!=l:
                            #print(a,b,c, k )
                            one_cow_array.append(convert_2_number(a, b, c,k))
                            counter+=1
    print(f"There are {counter-1} one cow combination ")#1440 units
    print(len(one_cow_array))


def four_cows(number):
    print(f"Options for 4 cows for {number}: ")
    counter=1
    i=number[0]#1
    j=number[1]#2
    k=number[2]#3
    l=number[3]#4

    values_1=[j,k,l]#values for 1st digit
    values_2=[i,k,l]#values for 2nd digit
    values_3=[i,j,l]#values for 3rd digit
    values_4=[i,j,k]#values for 4th digit


    for a in values_1:
        for b in values_2:
            if b!=a:
                for c in values_3:
                    if c!=a and c!=b:
                        for d in values_4:
                            if d!=a and d!=b and d!=c:
                                print("#", counter, ": ", a,b, c, d)
                                counter+=1

    print(f"4 cows: there are  {counter -1} numbers")#9

def two_bulls_one_cow(number):
    print(f"Options for 2 bulls and one cow for {number}: ")
    counter=1
    two_bulls_one_cow_array = []
    i=number[0]#1
    j=number[1]#2
    k=number[2]#3
    l=number[3]#4

    a=i
    b=j
    c=l
    for d in range(10):#124x
        if d!=a and d!=b and d!=c and d!=k:
            two_bulls_one_cow_array.append(convert_2_number(a,b,c,d))
            counter+=1

    a=i
    b=l
    c=k
    for d in range(10):  # 143x
        if d!=a and d!=b and d!=c and d!=j:
            two_bulls_one_cow_array.append(convert_2_number(a, b, c, d))
            counter += 1

    a=l
    b=j
    c=k
    for d in range(10):  # 423x
        if d!=a and d!=b and d!=c and d!=i:
            two_bulls_one_cow_array.append(convert_2_number(a, b, c, d))
            counter += 1

    a=i
    b=j
    d=k
    for c in range(10):  # 12x3
        if c != a and c != b and c != d and c!=l:
            two_bulls_one_cow_array.append(convert_2_number(a, b, c, d))
            counter += 1

    a=i
    b=k
    d=l
    for c in range(10):  # 13x4
        if c != a and c != b and c != d  and c!=j:
            two_bulls_one_cow_array.append(convert_2_number(a, b, c, d))
            counter += 1

    a=k
    b=j
    d=l
    for c in range(10):  # 32x4
        if c != a and c != b and c != d  and c!=i:
            two_bulls_one_cow_array.append(convert_2_number(a, b, c, d))
            counter += 1

    a=i
    c=j
    d=l
    for b in range(10):  # 1x24
        if b != a and b != c and b != d  and b!=k:
            two_bulls_one_cow_array.append(convert_2_number(a, b, c, d))
            counter += 1

    a=j
    c=k
    d=l
    for b in range(10):  # 2x34
        if b != a and b != c and b != d and b!=i:
            two_bulls_one_cow_array.append(convert_2_number(a, b, c, d))
            counter += 1

    a=i
    c=k
    d=j
    for b in range(10):  # 1x32
        if b != a and b != c and b != d and b!=l:
            two_bulls_one_cow_array.append(convert_2_number(a, b, c, d))
            counter += 1

    b=j
    c=k
    d=i
    for a in range(10):  # x231
        if a != b and a != c and a != d and a!=l:
            two_bulls_one_cow_array.append(convert_2_number(a, b, c, d))
            counter += 1

    b=j
    c=i
    d=l
    for a in range(10):  # x214
        if a != b and a != c and a != d and a!=k:
            two_bulls_one_cow_array.append(convert_2_number(a, b, c, d))
            counter += 1

    b=i
    c=k
    d=l
    for a in range(10):  # x134
        if a != b and a != c and a != d and a!=j:
            two_bulls_one_cow_array.append(convert_2_number(a, b, c, d))
            counter += 1

    print(two_bulls_one_cow_array)
    print(f"There are {counter-1} in 2 bulls and one cow ")#72 units

def bull_3_cows(number):
    print(f"Options for one bull and 3 cows for {number}: ")
    counter=1
    values = [[],[],[],[],[],[],[],[]]
    i=number[0]#1
    j=number[1]#2
    k=number[2]#3
    l=number[3]#4

    values[0] = [i,k,l,j]#1342
    values[1] = [i,l,j,k]#1423
    values[2] = [k,j,l,i]#3241
    values[3] = [l,j,i,k]#4213
    values[4] = [j,l,k,i]#2431
    values[5] = [l,i,k,j]#4132
    values[6] = [j, k, i, l]  # 2314
    values[7] = [k, i, j, l]  # 3124

    for i in range(8):
        print(i+1, ":", values[i])


def one_bull_one_cow(number):
    one_bull_one_cow_array = []
    i = number[0]  # 1
    j = number[1]  # 2
    k = number[2]  # 3
    l = number[3]  # 4
    counter = 1
    print("Original number: ", number)

    a = i
    c = j
    for b in range(10):  # 1 digit is bull, 3digit cow from 2 place
        if b != i and b != j and b != k and b != l:
            for d in range(10):
                if d != b and d != i and d != j and d != k and d != l:
                    #print(f"{counter}: {a}{b}{c}{d}")
                    one_bull_one_cow_array.append(convert_2_number(a,b,c,d))
                    counter += 1

    a = i
    d = j
    for b in range(10):  # 1 digit is bull, 4digit cow from 2 place
        if b != i and b != j and b != k and b != l:
            for c in range(10):
                if c != b and c != i and c != j and c != k and c != l:
                    #print(f"{counter}: {a}{b}{c}{d}")
                    one_bull_one_cow_array.append(convert_2_number(a, b, c, d))
                    counter += 1

    a = i
    b = k
    for c in range(10):  # 1 digit is bull, 2digit cow from 3 place
        if c != i and c != j and c != k and c != l:
            for d in range(10):
                if d != c and d != i and d != j and d != k and d != l:
                    #print(f"{counter}: {a}{b}{c}{d}")
                    one_bull_one_cow_array.append(convert_2_number(a, b, c, d))
                    counter += 1

    a = i
    d = k
    for b in range(10):  # 1 digit is bull, 4digit cow from 3 place
        if b != i and b != j and b != k and b != l:
            for c in range(10):
                if c != b and c != i and c != j and c != k and c != l:
                    #print(f"{counter}: {a}{b}{c}{d}")
                    one_bull_one_cow_array.append(convert_2_number(a, b, c, d))
                    counter += 1

    a = i
    b = l
    for c in range(10):  # 1 digit is bull, 2digit cow from 4 place
        if c != i and c != j and c != k and c != l:
            for d in range(10):
                if d != c and d != i and d != j and d != k and d != l:
                    #print(f"{counter}: {a}{b}{c}{d}")
                    one_bull_one_cow_array.append(convert_2_number(a, b, c, d))
                    counter += 1

    a = i
    c = l
    for b in range(10):  # 1 digit is bull, 3digit cow from 4 place
        if b != i and b != j and b != k and b != l:
            for d in range(10):
                if d != b and d != i and d != j and d != k and d != l:
                    #print(f"{counter}: {a}{b}{c}{d}")
                    one_bull_one_cow_array.append(convert_2_number(a, b, c, d))
                    counter += 1

    b = j
    c = i
    for a in range(10):  # 2 digit is bull, 3digit cow from 1 place
        if a != i and a != j and a != k and a != l:
            for d in range(10):
                if d != a and d != i and d != j and d != k and d != l:
                    #print(f"{counter}: {a}{b}{c}{d}")
                    one_bull_one_cow_array.append(convert_2_number(a, b, c, d))
                    counter += 1

    b = j
    d = i
    for a in range(10):  # 2 digit is bull, 4digit cow from 1 place
        if a != i and a != j and a != k and a != l:
            for c in range(10):
                if c != a and c != i and c != j and c != k and c != l:
                    #print(f"{counter}: {a}{b}{c}{d}")
                    one_bull_one_cow_array.append(convert_2_number(a, b, c, d))
                    counter += 1

    a = k
    b = j
    for c in range(10):  # 2 digit is bull, 1digit cow from 3 place
        if c != i and c != j and c != k and c != l:
            for d in range(10):
                if d != c and d != i and d != j and d != k and d != l:
                    #print(f"{counter}: {a}{b}{c}{d}")
                    one_bull_one_cow_array.append(convert_2_number(a, b, c, d))
                    counter += 1

    b = j
    d = k
    for a in range(10):  # 2 digit is bull, 4digit cow from 3 place
        if a != i and a != j and a != k and a != l:
            for c in range(10):
                if c != a and c != i and c != j and c != k and c != l:
                    #print(f"{counter}: {a}{b}{c}{d}")
                    one_bull_one_cow_array.append(convert_2_number(a, b, c, d))
                    counter += 1

    a = l
    b = j
    for c in range(10):  # 2 digit is bull, 1digit cow from 4 place
        if c != i and c != j and c != k and c != l:
            for d in range(10):
                if d != c and d != i and d != j and d != k and d != l:
                    #print(f"{counter}: {a}{b}{c}{d}")
                    one_bull_one_cow_array.append(convert_2_number(a, b, c, d))
                    counter += 1

    b = j
    c = l
    for a in range(10):  # 2 digit is bull, 3digit cow from 4 place
        if a != i and a != j and a != k and a != l:
            for d in range(10):
                if d != a and d != i and d != j and d != k and d != l:
                    #print(f"{counter}: {a}{b}{c}{d}")
                    one_bull_one_cow_array.append(convert_2_number(a, b, c, d))
                    counter += 1

    b = i
    c = k
    for a in range(10):  # 3 digit is bull, 2digit cow from 1 place
        if a != i and a != j and a != k and a != l:
            for d in range(10):
                if d != a and d != i and d != j and d != k and d != l:
                    #print(f"{counter}: {a}{b}{c}{d}")
                    one_bull_one_cow_array.append(convert_2_number(a, b, c, d))
                    counter += 1

    d = i
    c = k
    for a in range(10):  # 3 digit is bull, 4digit cow from 1 place
        if a != i and a != j and a != k and a != l:
            for b in range(10):
                if b != a and b != i and b != j and b != k and b != l:
                    #print(f"{counter}: {a}{b}{c}{d}")
                    one_bull_one_cow_array.append(convert_2_number(a, b, c, d))
                    counter += 1
    a = j
    c = k
    for b in range(10):  # 3 digit is bull, 1digit cow from 2 place
        if b != i and b != j and b != k and b != l:
            for d in range(10):
                if d != b and d != i and d != j and d != k and d != l:
                    #print(f"{counter}: {a}{b}{c}{d}")
                    one_bull_one_cow_array.append(convert_2_number(a, b, c, d))
                    counter += 1
    d = j
    c = k
    for a in range(10):  # 3 digit is bull, 4digit cow from 2 place
        if a != i and a != j and a != k and a != l:
            for b in range(10):
                if b != a and b != i and b != j and b != k and b != l:
                    #print(f"{counter}: {a}{b}{c}{d}")
                    one_bull_one_cow_array.append(convert_2_number(a, b, c, d))
                    counter += 1

    a = l
    c = k
    for b in range(10):  # 3 digit is bull, 1digit cow from 4 place
        if b != i and b != j and b != k and b != l:
            for d in range(10):
                if d != b and d != i and d != j and d != k and d != l:
                    #print(f"{counter}: {a}{b}{c}{d}")
                    one_bull_one_cow_array.append(convert_2_number(a, b, c, d))
                    counter += 1
    b = l
    c = k
    for a in range(10):  # 3 digit is bull, 2digit cow from 4 place
        if a != i and a != j and a != k and a != l:
            for d in range(10):
                if d != a and d != i and d != j and d != k and d != l:
                    #print(f"{counter}: {a}{b}{c}{d}")
                    one_bull_one_cow_array.append(convert_2_number(a, b, c, d))
                    counter += 1

    b = i
    d = l
    for a in range(10):  # 4 digit is bull, 2digit cow from 1 place
        if a != i and a != j and a != k and a != l:
            for c in range(10):
                if c != a and c != i and c != j and c != k and c != l:
                   # print(f"{counter}: {a}{b}{c}{d}")
                    one_bull_one_cow_array.append(convert_2_number(a, b, c, d))
                    counter += 1

    c = i
    d = l
    for a in range(10):  # 4 digit is bull, 3digit cow from 1 place
        if a != i and a != j and a != k and a != l:
            for b in range(10):
                if b != a and b != i and b != j and b != k and b != l:
                    #print(f"{counter}: {a}{b}{c}{d}")
                    one_bull_one_cow_array.append(convert_2_number(a, b, c, d))
                    counter += 1
    a = j
    d = l
    for b in range(10):  # 4 digit is bull, 1digit cow from 2 place
        if b != i and b != j and b != k and b != l:
            for c in range(10):
                if c != b and c != i and c != j and c != k and c != l:
                    #print(f"{counter}: {a}{b}{c}{d}")
                    one_bull_one_cow_array.append(convert_2_number(a, b, c, d))
                    counter += 1

    c = j
    d = l
    for a in range(10):  # 4 digit is bull, 3digit cow from 2 place
        if a != i and a != j and a != k and a != l:
            for b in range(10):
                if b != a and b != i and b != j and b != k and b != l:
                    #print(f"{counter}: {a}{b}{c}{d}")
                    one_bull_one_cow_array.append(convert_2_number(a, b, c, d))
                    counter += 1

    a = k
    d = l
    for b in range(10):  # 4 digit is bull, 1digit cow from 3 place
        if b != i and b != j and b != k and b != l:
            for c in range(10):
                if c != b and c != i and c != j and c != k and c != l:
                   # print(f"{counter}: {a}{b}{c}{d}")
                    one_bull_one_cow_array.append(convert_2_number(a, b, c, d))
                    counter += 1

    b = k
    d = l
    for a in range(10):  # 4 digit is bull, 2digit cow from 3 place
        if a != i and a != j and a != k and a != l:
            for c in range(10):
                if c != a and c != i and c != j and c != k and c != l:
                   # print(f"{counter}: {a}{b}{c}{d}")
                    one_bull_one_cow_array.append(convert_2_number(a, b, c, d))
                    counter += 1

    print(f"Total one bull and one cow {counter - 1} numbers")
    print(one_bull_one_cow_array)
    
number=[1,2,3,4]
#two_bull_two_cows(number)#6
#bull_3_cows(number)#8
#four_cows(number)#9
#three_bulls(number)#24
two_bulls_one_cow(number)#72
#two_bulls(number)#180
#one_bull_two_cows(number)#216
#three_cows(number)#264
#no_bulls_no_cows(number)#360
#one_bull(number)#480
#one_bull_one_cow(number)#720
#two_cows(number)#1260
#one_cow(number)#1440
