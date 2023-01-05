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

    counter = 1
    i=number[0]
    j=number[1]
    k=number[2]
    l=number[3]


    for a in range(10):#bulls digit1 and digit2
        if a!=i and a!=j and a!=k and a!=l:
           for b in range(10):
               if b!=i and b!=j and b!=k and b!=l and b!=a:
                   print(i,j,a,b)
                   counter+=1

    for a in range(10):#bulls digit1 and digit3
       if a!=i and a!=j and a!=k and a!=l:
           for b in range(10):
               if b!=i and b!=j and b!=k and b!=l and b!=a:
                   print(i,a,k,b)
                   counter+=1

    for a in range(10):#bulls digit1 and digit4
       if a!=i and a!=j and a!=k and a!=l:
           for b in range(10):
               if b!=i and b!=j and b!=k and b!=l and b!=a:
                   print(i,a,b,l)
                   counter+=1

    for a in range(10):  # bulls digit2 and digit3
        if a != i and a != j and a != k and a != l:
            for b in range(10):
                if b != i and b != j and b != k and b != l and b != a:
                    print(i, j, k, b)
                    counter += 1

    for a in range(10):  # bulls digit2 and digit4
        if a != i and a != j and a != k and a != l:
            for b in range(10):
                if b != i and b != j and b != k and b != l and b != a:
                    print(a, j, b, l)
                    counter += 1

    for a in range(10):  # bulls digit3 and digit4
        if a != i and a != j and a != k and a != l:
            for b in range(10):
                if b != i and b != j and b != k and b != l and b != a:
                    print(a, b, k, l)
                    counter += 1

    print(f"2 bulls: there are {counter-1} numbers")#24


def two_bull_two_cows(number):
    print(f"Options for 2 bulls and 2 cows for {number}: ")
    counter=1
    values = [[],[],[],[],[],[]]
    i=number[0]#1
    j=number[1]#2
    k=number[2]#3
    l=number[3]#4

    values[0]=[i,j,l,k]#1243
    values[1]=[i,l,k,j]#1432
    values[2]=[i,k,j,l]#1324
    values[3]=[l,j,k,i]#4231
    values[4]=[k,j,i,l]#3214
    values[5]=[j,i,k,l]#2134

    for i in range(6):
        print(i+1, ":", values[i])

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

def one_cow(number):
    print(f"Options for 1 cow for {number}: ")
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
                            counter+=1
    print(f"{counter}")

    for a in range(10):#cow digit1 from place3
        if a!=i and a!=j and a!=k and a!=l:
            for b in range(10):
                if b!=a and b!=i and b!=j and b!=k  and b!=l:
                    for c in range(10):
                        if c!=a and c!=b and c!=i and c!=j and c!=k and c!=l:
                            #print(k,a,b,c )
                            counter+=1

    for a in range(10):#cow digit1 from place4
        if a!=i and a!=j and a!=k and a!=l:
            for b in range(10):
                if b!=a and b!=i and b!=j and b!=k  and b!=l:
                    for c in range(10):
                        if c!=a and c!=b and c!=i and c!=j and c!=k and c!=l:
                            #print(l,a,b,c )
                            counter+=1

    for a in range(10):#cow digit2 from place1
        if a!=i and a!=j and a!=k and a!=l:
            for b in range(10):
                if b!=a and b!=i and b!=j and b!=k  and b!=l:
                    for c in range(10):
                        if c!=a and c!=b and c!=i and c!=j and c!=k and c!=l:
                            #print(a,i,b,c )
                            counter+=1

    for a in range(10):#cow digit2 from place3
        if a!=i and a!=j and a!=k and a!=l:
            for b in range(10):
                if b!=a and b!=i and b!=j and b!=k  and b!=l:
                    for c in range(10):
                        if c!=a and c!=b and c!=i and c!=j and c!=k and c!=l:
                            #print(a,k,b,c )
                            counter+=1

    for a in range(10):#cow digit2 from place4
        if a!=i and a!=j and a!=k and a!=l:
            for b in range(10):
                if b!=a and b!=i and b!=j and b!=k  and b!=l:
                    for c in range(10):
                        if c!=a and c!=b and c!=i and c!=j and c!=k and c!=l:
                            #print(a,l,b,c )
                            counter+=1

    for a in range(10):#cow digit3 from place1
        if a!=i and a!=j and a!=k and a!=l:
            for b in range(10):
                if b!=a and b!=i and b!=j and b!=k  and b!=l:
                    for c in range(10):
                        if c!=a and c!=b and c!=i and c!=j and c!=k and c!=l:
                            #print(a,b,i,c )
                            counter+=1

    for a in range(10):#cow digit3 from place2
        if a!=i and a!=j and a!=k and a!=l:
            for b in range(10):
                if b!=a and b!=i and b!=j and b!=k  and b!=l:
                    for c in range(10):
                        if c!=a and c!=b and c!=i and c!=j and c!=k and c!=l:
                            #print(a,b,j,c )
                            counter+=1

    for a in range(10):#cow digit3 from place4
        if a!=i and a!=j and a!=k and a!=l:
            for b in range(10):
                if b!=a and b!=i and b!=j and b!=k  and b!=l:
                    for c in range(10):
                        if c!=a and c!=b and c!=i and c!=j and c!=k and c!=l:
                            #print(a,b,l,c )
                            counter+=1

    for a in range(10):#cow digit4 from place1
        if a!=i and a!=j and a!=k and a!=l:
            for b in range(10):
                if b!=a and b!=i and b!=j and b!=k  and b!=l:
                    for c in range(10):
                        if c!=a and c!=b and c!=i and c!=j and c!=k and c!=l:
                            #print(a,b,c,i )
                            counter+=1


    for a in range(10):#cow digit4 from place2
        if a!=i and a!=j and a!=k and a!=l:
            for b in range(10):
                if b!=a and b!=i and b!=j and b!=k  and b!=l:
                    for c in range(10):
                        if c!=a and c!=b and c!=i and c!=j and c!=k and c!=l:
                            #print(a,b,c,j )
                            counter+=1


    for a in range(10):#cow digit4 from place3
        if a!=i and a!=j and a!=k and a!=l:
            for b in range(10):
                if b!=a and b!=i and b!=j and b!=k  and b!=l:
                    for c in range(10):
                        if c!=a and c!=b and c!=i and c!=j and c!=k and c!=l:
                            #print(a,b,c, k )
                            counter+=1
    print(f"There are {counter-1} one cow ")#1440 units


def two_bulls_one_cow(number):
    print(f"Options for 2 bulls and one cow for {number}: ")
    counter=1
    values = [[],[],[],[],[],[]]
    i=number[0]#1
    j=number[1]#2
    k=number[2]#3
    l=number[3]#4

    for a in range(10):#124x
        if a!=i and a!=j and a!=l:
            print([i,j,l,a])
            counter+=1

    for a in range(10):  # 12x4
        if a != i and a != j and a != k:
            print([i, j, a, k])
            counter += 1

    for a in range(10):  # 143x
        if a != i and a !=l and a!=k:
            print([i, l, k, a])
            counter += 1

    for a in range(10):  # 12x4
        if a != i and a != j and a != l:
            print([i, j, l, a])
            counter += 1

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


number=[1,2,3,4]
#two_bull_two_cows(number)#6
#bull_3_cows(number)#8
#four_cows(number)#9
#three_bulls(number)#24
#two_bulls_one_cow(number)#72
#two_bulls(number)#180
#bull_2_cows(number)#216
#three_cows(number)#264
#no_bulls_no_cows(number)#360
#one_bull(number)#480
#bull_one_cow(number)#720
#two_cows(number)#1260
one_cow(number)#1440
