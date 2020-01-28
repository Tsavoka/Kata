# Given an array, find the integer that appears an odd number of times.

def find_it(seq):
    uniq = []
    for i in seq:
        if i not in uniq:
            uniq.append(i)
    for i in uniq:
        if seq.count(i) % 2 != 0:
            return i
            
            
            
print(find_it([1,1,1,1,1,1,10,1,1,1,1,10,10])) # 10
