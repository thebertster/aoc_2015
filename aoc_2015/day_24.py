import itertools

weights = (1, 3, 5, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113)

#weights = (1, 2, 3, 4, 5, 7, 8, 9, 10, 11)


found = False

for i in range(1, len(weights)-2):
    print(i)
    for arr1 in itertools.combinations(weights, i):
        weight1 = 0
        weight2 = 0
        arr2 = []
        for p in weights:
            if p in arr1:
                weight1 += p
            else:
                weight2 += p
                arr2.append(p)
        if weight2 == 3 * weight1:
            for j in range(1, len(arr2)-1):
                for arr3 in itertools.combinations(arr2, j):
                    weight3 = 0
                    weight4 = 0
                    arr4 = []
                    for p in arr2:
                        if p in arr3:
                            weight3 += p
                        else:
                            weight4 += p
                            arr4.append(p)
                    if weight3 == weight1 and weight4 == 2*weight1:
                        for k in range(1, len(arr4)//2):
                            for arr5 in itertools.combinations(arr4, k):
                                weight5 = 0
                                weight6 = 0
                                arr6 = []
                                for p in arr4:
                                    if p in arr5:
                                        weight5 += p
                                    else:
                                        weight6 += p
                                        arr6.append(p)
                                if weight5 == weight6:
                                    found = True
                                    break
                            if found: break
                        if found: break
                if found: break
            if found:
                q = 1
                for s in arr1: q *= s
                print(arr1, arr3, arr5, arr6, q)
        if found: break
    if found: break


