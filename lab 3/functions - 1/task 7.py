def CONSECUTIVETHREE(SEQUENCEOFTHREEQUESTIONMARK):
    for i in range(len(SEQUENCEOFTHREEQUESTIONMARK)-1):
        if SEQUENCEOFTHREEQUESTIONMARK[i] == 3 and SEQUENCEOFTHREEQUESTIONMARK[i+1] == 3:
            return True
    return False

seq1 = [1,2,3,4,5]  #should be false
seq2 = [1,2,3,3,3]  #should be true
seq3 = [1,3,2,3,4]  #should be false
seq4 = [3,3,3,3,3]  #shoudl be true

print(CONSECUTIVETHREE(seq1))
print(CONSECUTIVETHREE(seq2))
print(CONSECUTIVETHREE(seq3))
print(CONSECUTIVETHREE(seq4))

"""
Output is:
---
False
True
False
True
---
which is correct order
"""