def max_marks(students):
    i=0
    while i<len(students):
        j=0
        max=0
        while j<len(students[i]):
            if students[i][j]>max:
                max=students[i][j]
            j+=1
        i+=1
        print(max)
students= [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
max_marks(students)