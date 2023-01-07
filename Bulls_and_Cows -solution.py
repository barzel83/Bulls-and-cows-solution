
def convert_2_number(a,b,c,d):
    return a*1000+b*100+c*10+d

def convert_2_array(number):
    array=[]
    #print(number)
    d=number % 10
    number  =number-d
    number=number/10
    c=int(number%10)
    number=number-c
    number=number/10
    b=int(number%10)
    number=number-b
    number=number/10
    a=int(number)

    array = [a,b,c,d]
    return array

def intersection(arr1,arr2):
    common_list = list(set(arr1).intersection(arr2))
    return common_list

def two_cows(number):
    i=number[0]
    j=number[1]
    k=number[2]
    l=number[3]
    counter = 1
    two_cows_array = []


    print("Original number: ", number)

    a=l
    d=k
    for b in range(10):#4c 65 3c
        if b!=i and b!=j and b!=k and b!=l:
            for c in range(10):
                if c!=b and c!=i and c!=j and c!=k and c!=l:
                    #print(f"{counter}: {a}{b}{c}{d}" )
                    two_cows_array.append(convert_2_number(a,b,c,d))
                    counter+=1

    a=l
    d=j
    for b in range(10):#4c 65 2c
        if b!=i and b!=j and b!=k and b!=l:
            for c in range(10):
                if c!=b and c!=i and c!=j and c!=k and c!=l:
                    #print(f"{counter}: {a}{b}{c}{d}" )
                    two_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=l
    d=i
    for b in range(10):#4c 65 1c
        if b!=i and b!=j and b!=k and b!=l:
            for c in range(10):
                if c!=b and c!=i and c!=j and c!=k and c!=l:
                    #print(f"{counter}: {a}{b}{c}{d}" )
                    two_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=k
    d=i
    for b in range(10):#3c 65 1c
        if b!=i and b!=j and b!=k and b!=l:
            for c in range(10):
                if c!=b and c!=i and c!=j and c!=k and c!=l:
                    #print(f"{counter}: {a}{b}{c}{d}" )
                    two_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=k
    d=j
    for b in range(10):#3c 65 2c
        if b!=i and b!=j and b!=k and b!=l:
            for c in range(10):
                if c!=b and c!=i and c!=j and c!=k and c!=l:
                    #print(f"{counter}: {a}{b}{c}{d}" )
                    two_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=j
    d=k
    for b in range(10):#2c 65 3c
        if b!=i and b!=j and b!=k and b!=l:
            for c in range(10):
                if c!=b and c!=i and c!=j and c!=k and c!=l:
                    #print(f"{counter}: {a}{b}{c}{d}" )
                    two_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=j
    d=i
    for b in range(10):#2c 65 1c
        if b!=i and b!=j and b!=k and b!=l:
            for c in range(10):
                if c!=b and c!=i and c!=j and c!=k and c!=l:
                    #print(f"{counter}: {a}{b}{c}{d}" )
                    two_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=l
    c=j
    for b in range(10):#4c 6 2c 5
        if b!=i and b!=j and b!=k and b!=l:
            for d in range(10):
                if d!=b and d!=i and d!=j and d!=k and d!=l:
                    #print(f"{counter}: {a}{b}{c}{d}" )
                    two_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=l
    c=i
    for b in range(10):#4c 6 1c 5
        if b!=i and b!=j and b!=k and b!=l:
            for d in range(10):
                if d!=b and d!=i and d!=j and d!=k and d!=l:
                    #print(f"{counter}: {a}{b}{c}{d}" )
                    two_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=k
    c=j
    for b in range(10):#3c 6 2c 5
        if b!=i and b!=j and b!=k and b!=l:
            for d in range(10):
                if d!=b and d!=i and d!=j and d!=k and d!=l:
                    #print(f"{counter}: {a}{b}{c}{d}" )
                    two_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=k
    c=i
    for b in range(10):#3c 6 1c 5
        if b!=i and b!=j and b!=k and b!=l:
            for d in range(10):
                if d!=b and d!=i and d!=j and d!=k and d!=l:
                    #print(f"{counter}: {a}{b}{c}{d}" )
                    two_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=k
    c=l
    for b in range(10):#3c 6 4c 5
        if b!=i and b!=j and b!=k and b!=l:
            for d in range(10):
                if d!=b and d!=i and d!=j and d!=k and d!=l:
                    #print(f"{counter}: {a}{b}{c}{d}" )
                    two_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=j
    c=i
    for b in range(10):#2c 6 1c 5
        if b!=i and b!=j and b!=k and b!=l:
            for d in range(10):
                if d!=b and d!=i and d!=j and d!=k and d!=l:
                    #print(f"{counter}: {a}{b}{c}{d}" )
                    two_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=j
    c=l
    for b in range(10):#2c 6 4c 5
        if b!=i and b!=j and b!=k and b!=l:
            for d in range(10):
                if d!=b and d!=i and d!=j and d!=k and d!=l:
                    #print(f"{counter}: {a}{b}{c}{d}" )
                    two_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=l
    b=i
    for c in range(10):#4c 1c 65
        if c!=i and c!=j and c!=k and c!=l:
            for d in range(10):
                if d!=b and d!=i and d!=j and d!=k and d!=l:
                    #print(f"{counter}: {a}{b}{c}{d}" )
                    two_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=l
    b=k
    for c in range(10):#4c 3c 65
        if c!=i and c!=j and c!=k and c!=l:
            for d in range(10):
                if d!=b and d!=i and d!=j and d!=k and d!=l:
                    #print(f"{counter}: {a}{b}{c}{d}" )
                    two_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=k
    b=i
    for c in range(10):#3c 1c 65
        if c!=i and c!=j and c!=k and c!=l:
            for d in range(10):
                if d!=b and d!=i and d!=j and d!=k and d!=l:
                    #print(f"{counter}: {a}{b}{c}{d}" )
                    two_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1


    a=k
    b=l
    for c in range(10):#3c 4c 65
        if c!=i and c!=j and c!=k and c!=l:
            for d in range(10):
                if d!=b and d!=i and d!=j and d!=k and d!=l:
                    #print(f"{counter}: {a}{b}{c}{d}" )
                    two_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=j
    b=k
    for c in range(10):#2c 3c 65
        if c!=i and c!=j and c!=k and c!=l:
            for d in range(10):
                if d!=b and d!=i and d!=j and d!=k and d!=l:
                    #print(f"{counter}: {a}{b}{c}{d}" )
                    two_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=j
    b=i
    for c in range(10):#2c 1c 65
        if c!=i and c!=j and c!=k and c!=l:
            for d in range(10):
                if d!=b and d!=i and d!=j and d!=k and d!=l:
                    #print(f"{counter}: {a}{b}{c}{d}" )
                    two_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=j
    b=l
    for c in range(10):#2c 4c 65
        if c!=i and c!=j and c!=k and c!=l:
            for d in range(10):
                if d!=b and d!=i and d!=j and d!=k and d!=l:
                    #print(f"{counter}: {a}{b}{c}{d}" )
                    two_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    c=i
    d=j
    for a in range(10):#65 1c 2c 
        if a!=i and a!=j and a!=k and a!=l:
            for b in range(10):
                if b!=a and b!=i and b!=j and b!=k and b!=l:
                    #print(f"{counter}: {a}{b}{c}{d}" )
                    two_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    c=j
    d=i
    for a in range(10):#65 2c 1c 
        if a!=i and a!=j and a!=k and a!=l:
            for b in range(10):
                if b!=a and b!=i and b!=j and b!=k and b!=l:
                    #print(f"{counter}: {a}{b}{c}{d}" )
                    two_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    c=j
    d=k
    for a in range(10):#65 2c 3c 
        if a!=i and a!=j and a!=k and a!=l:
            for b in range(10):
                if b!=a and b!=i and b!=j and b!=k and b!=l:
                    #print(f"{counter}: {a}{b}{c}{d}" )
                    two_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    c=i
    d=k
    for a in range(10):#65 1c 3c 
        if a!=i and a!=j and a!=k and a!=l:
            for b in range(10):
                if b!=a and b!=i and b!=j and b!=k and b!=l:
                    #print(f"{counter}: {a}{b}{c}{d}" )
                    two_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    c=l
    d=i
    for a in range(10):#65 4c 1c 
        if a!=i and a!=j and a!=k and a!=l:
            for b in range(10):
                if b!=a and b!=i and b!=j and b!=k and b!=l:
                    #print(f"{counter}: {a}{b}{c}{d}" )
                    two_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    c=l
    d=j
    for a in range(10):#65 4c 2c 
        if a!=i and a!=j and a!=k and a!=l:
            for b in range(10):
                if b!=a and b!=i and b!=j and b!=k and b!=l:
                    #print(f"{counter}: {a}{b}{c}{d}" )
                    two_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    b=i
    d=k
    for a in range(10):#6 1c 5 3c 
        if a!=i and a!=j and a!=k and a!=l:
            for c in range(10):
                if c!=a and c!=i and c!=j and c!=k and c!=l:
                    #print(f"{counter}: {a}{b}{c}{d}" )
                    two_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    b=k
    d=i
    for a in range(10):#6 3c 5 1c 
        if a!=i and a!=j and a!=k and a!=l:
            for c in range(10):
                if c!=a and c!=i and c!=j and c!=k and c!=l:
                    #print(f"{counter}: {a}{b}{c}{d}" )
                    two_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    b=k
    d=j
    for a in range(10):#6 3c 5 2c 
        if a!=i and a!=j and a!=k and a!=l:
            for c in range(10):
                if c!=a and c!=i and c!=j and c!=k and c!=l:
                   # print(f"{counter}: {a}{b}{c}{d}" )
                    two_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    b=i
    d=j
    for a in range(10):#6 1c 5 2c 
        if a!=i and a!=j and a!=k and a!=l:
            for c in range(10):
                if c!=a and c!=i and c!=j and c!=k and c!=l:
                    #print(f"{counter}: {a}{b}{c}{d}" )
                    two_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    b=l
    d=j
    for a in range(10):#6 4c 5 2c 
        if a!=i and a!=j and a!=k and a!=l:
            for c in range(10):
                if c!=a and c!=i and c!=j and c!=k and c!=l:
                   # print(f"{counter}: {a}{b}{c}{d}" )
                    two_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    b=l
    d=i
    for a in range(10):#6 4c 5 1c 
        if a!=i and a!=j and a!=k and a!=l:
            for c in range(10):
                if c!=a and c!=i and c!=j and c!=k and c!=l:
                    #print(f"{counter}: {a}{b}{c}{d}" )
                    two_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    b=k
    c=i
    for a in range(10):#6 3c 1c 5 
        if a!=i and a!=j and a!=k and a!=l:
            for d in range(10):
                if d!=a and d!=i and d!=j and d!=k and d!=l:
                    #print(f"{counter}: {a}{b}{c}{d}" )
                    two_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    b=k
    c=j
    for a in range(10):#6 3c 2c 5 
        if a!=i and a!=j and a!=k and a!=l:
            for d in range(10):
                if d!=a and d!=i and d!=j and d!=k and d!=l:
                    #print(f"{counter}: {a}{b}{c}{d}" )
                    two_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    b=k
    c=l
    for a in range(10):#6 3c 4c 5 
        if a!=i and a!=j and a!=k and a!=l:
            for d in range(10):
                if d!=a and d!=i and d!=j and d!=k and d!=l:
                    #print(f"{counter}: {a}{b}{c}{d}" )
                    two_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1
                    
    b=i
    c=k
    for a in range(10):#6 1c 4c 5 
        if a!=i and a!=j and a!=k and a!=l:
            for d in range(10):
                if d!=a and d!=i and d!=j and d!=k and d!=l:
                    #print(f"{counter}: {a}{b}{c}{d}" )
                    two_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1
                    
    print(f"Total two cows {counter-1} numbers")
    return two_cows_array

def three_cows(number):
    i=number[0]#1
    j=number[1]#2
    k=number[2]#3
    l=number[3]#4
    counter = 1
    three_cows_array = []
    print("Original number: ", number)

    a=l
    c=j
    d=k
    for b in range(10):#4c x 2c 3c  
        if b!=i and b!=j and b!=k and b!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1
    a=l
    c=i
    d=j
    for b in range(10):#4c x 1c 2c  
        if b!=i and b!=j and b!=k and b!=l:
                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=l
    c=j
    d=i
    for b in range(10):#4c x 2c 1c  
        if b!=i and b!=j and b!=k and b!=l:
                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=l
    c=i
    d=k
    for b in range(10):#4c x 1c 3c  
        if b!=i and b!=j and b!=k and b!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1
    a=k
    c=j
    d=i
    for b in range(10):#3c x 2c 1c 
        if b!=i and b!=j and b!=k and b!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=k
    c=i
    d=j
    for b in range(10):#3c x 1c 2c 
        if b!=i and b!=j and b!=k and b!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1
                    
    a=k
    c=l
    d=i
    for b in range(10):#3c x 4c 1c 
        if b!=i and b!=j and b!=k and b!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=k
    c=l
    d=j
    for b in range(10):#3c x 4c 2c 
        if b!=i and b!=j and b!=k and b!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=j
    c=l
    d=k
    for b in range(10):#2c x 4c 3c 
        if b!=i and b!=j and b!=k and b!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=j
    c=l
    d=i
    for b in range(10):#2c x 4c 1c 
        if b!=i and b!=j and b!=k and b!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1
                    
    a=j
    c=i
    d=k
    for b in range(10):#2c x 1c 3c 
        if b!=i and b!=j and b!=k and b!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    b=i
    c=j
    d=k
    for a in range(10):#x 1c 2c 3c 
        if a!=i and a!=j and a!=k and a!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    b=i
    c=l
    d=k
    for a in range(10):#x 1c 4c 3c 
        if a!=i and a!=j and a!=k and a!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1
                    
    b=k
    c=l
    d=i
    for a in range(10):#x 3c 4c 1c 
        if a!=i and a!=j and a!=k and a!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    b=l
    c=i
    d=k
    for a in range(10):#x 4c 1c 3c 
        if a!=i and a!=j and a!=k and a!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    b=l
    c=i
    d=j
    for a in range(10):#x 4c 1c 2c 
        if a!=i and a!=j and a!=k and a!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1
                    
    b=k
    c=j
    d=i
    for a in range(10):#x 3c 2c 1c 
        if a!=i and a!=j and a!=k and a!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1
    b=k
    c=l
    d=j
    for a in range(10):#x 3c 4c 2c 
        if a!=i and a!=j and a!=k and a!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    b=i
    c=l
    d=j
    for a in range(10):#x 1c 4c 2c 
        if a!=i and a!=j and a!=k and a!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1
                    
    b=l
    c=j
    d=k
    for a in range(10):#x 4c 2c 3c 
        if a!=i and a!=j and a!=k and a!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1
    b=l
    c=j
    d=i
    for a in range(10):#x 4c 2c 1c 
        if a!=i and a!=j and a!=k and a!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    b=k
    c=i
    d=j
    for a in range(10):#x 3c 1c 2c 
        if a!=i and a!=j and a!=k and a!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=l
    b=i
    d=k
    for c in range(10):#4c 1c x 3c 
        if c!=i and c!=j and c!=k and c!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=l
    b=k
    d=i
    for c in range(10):#4c 3c x 1c 
        if c!=i and c!=j and c!=k and c!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=l
    b=k
    d=j
    for c in range(10):#4c 3c x 2c 
        if c!=i and c!=j and c!=k and c!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=l
    b=i
    d=j
    for c in range(10):#4c 1c x 2c 
        if c!=i and c!=j and c!=k and c!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=k
    b=l
    d=j
    for c in range(10):#3c 4c x 2c 
        if c!=i and c!=j and c!=k and c!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=k
    b=l
    d=i
    for c in range(10):#3c 4c x 1c 
        if c!=i and c!=j and c!=k and c!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=k
    b=i
    d=j
    for c in range(10):#3c 1c x 2c 
        if c!=i and c!=j and c!=k and c!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=j
    b=l
    d=i
    for c in range(10):#2c 4c x 1c 
        if c!=i and c!=j and c!=k and c!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=j
    b=l
    d=k
    for c in range(10):#2c 4c x 3c 
        if c!=i and c!=j and c!=k and c!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=j
    b=i
    d=k
    for c in range(10):#2c 1c x 3c 
        if c!=i and c!=j and c!=k and c!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=j
    b=k
    d=i
    for c in range(10):#2c 3c x 1c 
        if c!=i and c!=j and c!=k and c!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=l
    b=i
    c=j
    for d in range(10):#4c 1c 2c x  
        if d!=i and d!=j and d!=k and d!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1
                    
    a=l
    b=k
    c=i
    for d in range(10):#4c 3c 1c x  
        if d!=i and d!=j and d!=k and d!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=l
    b=k
    c=j
    for d in range(10):#4c 3c 2c x  
        if d!=i and d!=j and d!=k and d!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=k
    b=i
    c=l
    for d in range(10):#3c 1c 4c x  
        if d!=i and d!=j and d!=k and d!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=k
    b=l
    c=j
    for d in range(10):#3c 4c 2c x  
        if d!=i and d!=j and d!=k and d!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=k
    b=l
    c=i
    for d in range(10):#3c 4c 1c x  
        if d!=i and d!=j and d!=k and d!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=k
    b=i
    c=j
    for d in range(10):#3c 1c 2c x  
        if d!=i and d!=j and d!=k and d!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=j
    b=k
    c=i
    for d in range(10):#2c 3c 1c x  
        if d!=i and d!=j and d!=k and d!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=j
    b=i
    c=l
    for d in range(10):#2c 1c 4c x  
        if d!=i and d!=j and d!=k and d!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=j
    b=k
    c=l
    for d in range(10):#2c 3c 4c x  
        if d!=i and d!=j and d!=k and d!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1

    a=j
    b=l
    c=i
    for d in range(10):#2c 4c 1c x  
        if d!=i and d!=j and d!=k and d!=l:

                    three_cows_array.append(convert_2_number(a, b, c, d))
                    counter+=1
                    
    print(f"Total three cows {counter-1} numbers")
    return three_cows_array

def one_bull_two_cows(number):
    i = number[0]  # 1
    j = number[1]  # 2
    k = number[2]  # 3
    l = number[3]  # 4
    counter = 1
    one_bull_two_cows_array =[]
    print("Original number: ", number)

    a = i
    b = k
    c = j
    for d in range(10):  # 1b 3c2cx
        if d != i and d != j and d != k and d != l:

            one_bull_two_cows_array.append(convert_2_number(a,b,c,d))
            counter += 1

    a = i
    b = k
    d = j
    for c in range(10):  # 1b 3cx2c
        if c != i and c != j and c != k and c != l:

            one_bull_two_cows_array.append(convert_2_number(a, b, c, d))
            counter += 1

    a = i
    c = j
    d = k
    for b in range(10):  # 1b x2c3c
        if b != i and b != j and b != k and b != l:

            one_bull_two_cows_array.append(convert_2_number(a, b, c, d))
            counter += 1

    a = i
    b = l
    c = j
    for d in range(10):  # 1b 4c2cx
        if d != i and d != j and d != k and d != l:

            one_bull_two_cows_array.append(convert_2_number(a, b, c, d))
            counter += 1

    a = i
    b = l
    d = j
    for c in range(10):  # 1b 4cx2c
        if c != i and c != j and c != k and c != l:

            one_bull_two_cows_array.append(convert_2_number(a, b, c, d))
            counter += 1

    a = i
    c = l
    d = j
    for b in range(10):  # 1b x4c2c
        if b != i and b != j and b != k and b != l:

            one_bull_two_cows_array.append(convert_2_number(a, b, c, d))
            counter += 1

    a = i
    c = l
    d = k
    for b in range(10):  # 1b x4c3c
        if b != i and b != j and b != k and b != l:

            one_bull_two_cows_array.append(convert_2_number(a, b, c, d))
            counter += 1

    a = i
    b = k
    c = l
    for d in range(10):  # 1b 3c4cx
        if d != i and d != j and d != k and d != l:

            one_bull_two_cows_array.append(convert_2_number(a, b, c, d))
            counter += 1

    a = i
    b = l
    d = k
    for c in range(10):  # 1b 4cx3c
        if c != i and c != j and c != k and c != l:

            one_bull_two_cows_array.append(convert_2_number(a, b, c, d))
            counter += 1

    b = j
    c = i
    d = k
    for a in range(10):  # x 2b 1c3c
        if a != i and a != j and a != k and a != l:

            one_bull_two_cows_array.append(convert_2_number(a, b, c, d))
            counter += 1

    b = j
    c = l
    d = i
    for a in range(10):  # x 2b 4c 1c
        if a != i and a != j and a != k and a != l:

            one_bull_two_cows_array.append(convert_2_number(a, b, c, d))
            counter += 1

    b = j
    c = l
    d = k
    for a in range(10):  # x 2b 4c 3c
        if a != i and a != j and a != k and a != l:

            one_bull_two_cows_array.append(convert_2_number(a, b, c, d))
            counter += 1

    a = k
    b = j
    d = i
    for c in range(10):  # 3c 2b x 1c
        if c != i and c != j and c != k and c != l:

            one_bull_two_cows_array.append(convert_2_number(a, b, c, d))
            counter += 1

    a = l
    b = j
    d = k
    for c in range(10):  # 4c 2b x 3c
        if c != i and c != j and c != k and c != l:

            one_bull_two_cows_array.append(convert_2_number(a, b, c, d))
            counter += 1

    a = l
    b = j
    d = i
    for c in range(10):  # 4c 2b x 1c
        if c != i and c != j and c != k and c != l:

            one_bull_two_cows_array.append(convert_2_number(a, b, c, d))
            counter += 1

    a = k
    b = j
    c = i
    for d in range(10):  # 3c 2b 1c x
        if d != i and d != j and d != k and d != l:

            one_bull_two_cows_array.append(convert_2_number(a, b, c, d))
            counter += 1

    a = k
    b = j
    c = l
    for d in range(10):  # 3c 2b 4c x
        if d != i and d != j and d != k and d != l:

            one_bull_two_cows_array.append(convert_2_number(a, b, c, d))
            counter += 1

    a = l
    b = j
    c = i
    for d in range(10):  # 4c 2b 1c x
        if d != i and d != j and d != k and d != l:

            one_bull_two_cows_array.append(convert_2_number(a, b, c, d))
            counter += 1

    a = j
    b = l
    c = k
    for d in range(10):  # 2с 4c 3b x
        if d != i and d != j and d != k and d != l:

            one_bull_two_cows_array.append(convert_2_number(a, b, c, d))
            counter += 1

    a = l
    b = i
    c = k
    for d in range(10):  # 4с 1c 3b x
        if d != i and d != j and d != k and d != l:

            one_bull_two_cows_array.append(convert_2_number(a, b, c, d))
            counter += 1

    a = j
    b = l
    c = k
    for d in range(10):  # 2с 4c 3b x
        if d != i and d != j and d != k and d != l:

            one_bull_two_cows_array.append(convert_2_number(a, b, c, d))
            counter += 1

    b = i
    c = k
    d = j
    for a in range(10):  # x 1с 3b 2c
        if a != i and a != j and a != k and a != l:

            one_bull_two_cows_array.append(convert_2_number(a, b, c, d))
            counter += 1

    b = l
    c = k
    d = i
    for a in range(10):  # x 4с 3b 1c
        if a != i and a != j and a != k and a != l:

            one_bull_two_cows_array.append(convert_2_number(a, b, c, d))
            counter += 1

    b = l
    c = k
    d = j
    for a in range(10):  # x 4с 3b 2c
        if a != i and a != j and a != k and a != l:

            one_bull_two_cows_array.append(convert_2_number(a, b, c, d))
            counter += 1

    a = j
    c = k
    d = i
    for b in range(10):  # 2c x 3b 1c
        if b != i and b != j and b != k and b != l:

            one_bull_two_cows_array.append(convert_2_number(a, b, c, d))
            counter += 1

    a = l
    c = k
    d = j
    for b in range(10):  # 4c x 3b 2c
        if b != i and b != j and b != k and b != l:

            one_bull_two_cows_array.append(convert_2_number(a, b, c, d))
            counter += 1

    a = l
    c = k
    d = i
    for b in range(10):  # 4c x 3b 1c
        if b != i and b != j and b != k and b != l:

            one_bull_two_cows_array.append(convert_2_number(a, b, c, d))
            counter += 1

    b = i
    c = j
    d = l
    for a in range(10):  # x 1c2c 4b
        if a != i and a != j and a != k and a != l:

            one_bull_two_cows_array.append(convert_2_number(a, b, c, d))
            counter += 1

    b = k
    c = i
    d = l
    for a in range(10):  # x 3c 1c 4b
        if a != i and a != j and a != k and a != l:

            one_bull_two_cows_array.append(convert_2_number(a, b, c, d))
            counter += 1

    b = k
    c = j
    d = l
    for a in range(10):  # x 3c 2c 4b
        if a != i and a != j and a != k and a != l:

            one_bull_two_cows_array.append(convert_2_number(a, b, c, d))
            counter += 1

    a = j
    c = i
    d = l
    for b in range(10):  # 2c x 1c 4b
        if b != i and b != j and b != k and b != l:

            one_bull_two_cows_array.append(convert_2_number(a, b, c, d))
            counter += 1

    a = k
    c = i
    d = l
    for b in range(10):  # 3c x 1c 4b
        if b != i and b != j and b != k and b != l:

            one_bull_two_cows_array.append(convert_2_number(a, b, c, d))
            counter += 1

    a = k
    c = j
    d = l
    for b in range(10):  # 3c x 2c 4b
        if b != i and b != j and b != k and b != l:

            one_bull_two_cows_array.append(convert_2_number(a, b, c, d))
            counter += 1

    a = j
    b = i
    d = l
    for c in range(10):  # 2c 1c x 4b
        if c != i and c != j and c != k and c != l:

            one_bull_two_cows_array.append(convert_2_number(a, b, c, d))
            counter += 1

    a = k
    b = i
    d = l
    for c in range(10):  # 3c 1c x 4b
        if c != i and c != j and c != k and c != l:

            one_bull_two_cows_array.append(convert_2_number(a, b, c, d))
            counter += 1

    a = j
    b = k
    d = l
    for c in range(10):  # 2c 3c x 4b
        if c != i and c != j and c != k and c != l:
            print(f"{counter}: {a}{b}{c}{d}")
            one_bull_two_cows_array.append(convert_2_number(a, b, c, d))
            counter += 1

    print(f"Total one bull and two cows {counter - 1} numbers")
    return one_bull_two_cows_array

def one_bull(number):
    i=number[0]
    j=number[1]
    k=number[2]
    l=number[3]
    counter = 1
    one_bull_array = []
    print("Original number: ", number)

    a=i
    for b in range(10):#1 digit=bull
        if b!=a and b!=j and b!=k and b!=l:
            for c in range(10):
                if c!=a and c!=b and c!=j and c!=k and c!=l:
                    for d in range(10):
                        if d!=a and d!=b and d!=c and d!=j and d!=k and d!=l:
                            #print(f"{counter}: {a}{b}{c}{d}" )
                            one_bull_array.append(convert_2_number(a,b,c,d))
                            counter+=1
    b=j
    for a in range(10):#2 digit=bull
        if a!=b and a!=i and a!=k and a!=l:
            for c in range(10):
                if c!=a and c!=b and c!=i and c!=k and c!=l:
                    for d in range(10):
                        if d!=a and d!=b and d!=c and d!=i and d!=k and d!=l:
                            #print(f"{counter}: {a}{b}{c}{d}" )
                            one_bull_array.append(convert_2_number(a, b, c, d))
                            counter+=1
    c=k
    for a in range(10):#3 digit=bull
        if a!=c and a!=i and a!=j and a!=l:
            for b in range(10):
                if b!=a and b!=c and b!=i and b!=j and b!=l:
                    for d in range(10):
                        if d!=a and d!=b and d!=c and d!=i and d!=j and d!=l:
                            #print(f"{counter}: {a}{b}{c}{d}" )
                            one_bull_array.append(convert_2_number(a, b, c, d))
                            counter+=1

    d=l

    for a in range(10):#4 digit is bull
        if a!=d and a!=i and a!=j and a!=k:
            for b in range(10):
                if b!=a and b!=d and b!=i and b!=j and b!=k:
                    for c in range(10):
                        if c!=a and c!=b and c!=d and c!=i and c!=j and c!=k:
                            #print(f"{counter}: {a}{b}{c}{d}" )
                            one_bull_array.append(convert_2_number(a, b, c, d))
                            counter+=1
    print(f"Total one bull {counter-1} numbers")#480
    print(one_bull_array)

def no_bulls_no_cows(number):
    i=number[0]
    j=number[1]
    k=number[2]
    l=number[3]
    counter = 1
    no_bulls_no_cows_array = []
    print("Original number: ", number)
    for a in range(10):
        if a!=i and a!=j and a!=k and a!=l:
            for b in range(10):
                if b!=i and b!=j and b!=k and b!=l and b!=a:
                    for c in range(10):
                        if c!=i and c!=j and c!=k and c!=l and c!=a and c!=b:
                            for d in range(10):
                                if d!=i and d!=j and d!=k and d!=l and d!=a and d!=b and d!=c:
                    #               print(f"{counter}: {a}{b}{c}{d}" )
                                    no_bulls_no_cows_array.append(convert_2_number(a,b,c,d))
                                    counter+=1
    print(f"Total no bulls and cows {counter-1} numbers")#360
    return no_bulls_no_cows_array

def three_bulls(number):
    print(f"Options for 3 bulls for {number}: ")
    array = number.copy()
    three_bulls_array=[]
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
                #print("#", counter, ": ", array)
                three_bulls_array.append(convert_2_number(array[0], array[1], array[2], array[3]))
                counter+=1
    #print(f"3 bulls: there are {counter-1} numbers")#24
    # print(three_bulls_array)
    return three_bulls_array

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

    #print("two_bull_two_cows_array: ", two_bull_two_cows_array)
    #print(f"Total two bulls and two cows {counter} numbers")
    return two_bull_two_cows_array
    #print(f"{counter}: {a}{b}{c}{d}")

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
    return one_cow_array

def four_cows(number):
    print(f"Options for 4 cows for {number}: ")
    counter=1
    four_cows_array=[]
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
                                #print("#", counter, ": ", a,b, c, d)
                                four_cows_array.append(convert_2_number(a,b,c,d))
                                counter+=1

    #print(f"4 cows: there are  {counter -1} numbers")#9
    #print(four_cows_array)
    return four_cows_array

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

    return two_bulls_one_cow_array
    #print(f"There are {counter-1} in 2 bulls and one cow ")#72 units

def one_bull_3_cows(number):
    print(f"Options for one bull and 3 cows for {number}: ")
    counter=1
    one_bull_3_cows_array = []
    i=number[0]#1
    j=number[1]#2
    k=number[2]#3
    l=number[3]#4

    one_bull_3_cows_array.append(convert_2_number(i,k,l,j))#1342
    one_bull_3_cows_array.append(convert_2_number(i, l, j, k))#1423
    one_bull_3_cows_array.append(convert_2_number(k,j,l,i))  #3241
    one_bull_3_cows_array.append(convert_2_number(l,j,i,k)) #4213
    one_bull_3_cows_array.append(convert_2_number(j,l,k,i)) #2431
    one_bull_3_cows_array.append(convert_2_number(l,i,k,j))  #4132
    one_bull_3_cows_array.append(convert_2_number(j, k, i, l))  # 2314
    one_bull_3_cows_array.append(convert_2_number(k, i, j, l))  # 3124
    #print(one_bull_3_cows_array)
    return one_bull_3_cows_array

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
    return one_bull_one_cow_array

#begging
function_dict = {'0b2c':two_cows, '0b3c':three_cows, '1b2c':one_bull_two_cows, '1b0c':one_bull, '0b0c':no_bulls_no_cows,
                 '3b0c':three_bulls, '2b0c':two_bulls, '2b2c': two_bull_two_cows, '0b1c':one_cow, '0b4c':four_cows, '2b1c': two_bulls_one_cow,
                 '1b3c':one_bull_3_cows, '1b1c':one_bull_one_cow}


number1 = int(input("Step 1 :Input  4-digit number: "))
convert_2_array(number1)
number = convert_2_array(number1)
func = input('Input your operation: ')
step1=function_dict[func](number)
print("step1: ", len(step1))

print("three_cows")
number2 = int(input("Step 2 : Input  4-digit number: "))
convert_2_array(number2)
number=convert_2_array(number2)
func = input('Input your operation: ')
#0b3c
step2 = function_dict[func](number)
common_step2 = intersection(step1, step2)
print("Common elements of step2:", len(common_step2))

number3 = int(input("Step 3 :Input  4-digit number: "))
convert_2_array(number3)
number=convert_2_array(number3)
func = input('Input your operation: ')
step3=function_dict[func](number)
common_step3 = intersection(common_step2, step3)
if len(common_step3)<30:
    print("Common elements of step3 :", common_step3)
else:
    print("Common elements of step3 :", len(common_step3))

number4 = int(input("Step 4 :Input  4-digit number: "))
convert_2_array(number4)
number=convert_2_array(number4)
func = input('Input your operation: ')
step4=function_dict[func](number)
common_step4 = intersection(common_step3, step4)
if len(common_step4)<30:
    print("Common elements of step4 :", common_step4)
else:
    print("Common elements of step4 :", len(common_step4))

number5 = int(input("Step 5 :Input  4-digit number: "))
convert_2_array(number5)
number=convert_2_array(number5)
func = input('Input your operation: ')
step5=function_dict[func](number)
common_step5 = intersection(common_step4, step5)
if len(common_step5)<30:
    print("Common elements of step5 :", common_step5)
else:
    print("Common elements of step5 :", len(common_step5))
