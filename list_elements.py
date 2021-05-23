def num(big_list):
    i = 0
    while i<len(big_list):
        small_list_length = len(big_list[i])
        r = 0
        while r <small_list_length:
            print (big_list[i][r])
            r+=1
        i+=1
    print ("")
big_list = [[1,2,3], [5,8,9], [4,3,77,521,31,311]]
num(big_list)
