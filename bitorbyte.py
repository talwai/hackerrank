"""Solution to IXL Learning: last character of byte array problem.
Problem statement: Characters can be denoted in two ways, as a single byte, with value in the range [0,127] inclusive,
or as two bytes: [x][y] where x is in range [128,255] inclusive and y is in range[0,255] inclusive.
The problem is: for a given array of bytes, find the size of the last character denoted in that byte array
Assume that the byte array is correctly formatted, and all values are within their appropriate ranges.
"""


"""
 Basic algorithm is as follows.
Check last three elements in byte array [len-3], [len-2], [len-1], and verify them as one of four possibilities:
  ( [x] indicates 'Don't care' : byte value can be anything )
Case 1. [x][x][>127] : Since last byte is >127, last char has to be of size 2
Case 2. [x][<=127][<=127] : Since last two bytes can't form a char together, last char has to be of size 1
Case 3. [<=127][>127][<=127] : Last two bytes must surely form a char together, hence last char has to be of size 2
Case 4. [>127][>127][<=127] : In this case, we cannot be sure of the size of the last char by only inspecting the last 3 bytes
                       We must trace backward until we hit a byte that is <= 127, incrementing a counter at each step.
                       The final value of this counter % (modulo) 2 indicates the size of the last char.
                       This is because, at each iteration, the boundaries between known characters alternately shift left and right.
                       If we iterate through the entire array, the size of the last char is indicated by the last known boundary
"""

def trace_backward(array):
    """
    Function to step backward through the byte array until we hit a byte that is <= 127
    Increments 'count', Returns value of last char size after 'count' # of shifts
    """

    count = 4 #We start our trace from the 4th-to-last byte

    while (count <= len(array)):
        if array[-count] > 127:
            count += 1 #Increment count until array[-count] <= 127, or until count > len(array)
        else:
            break

    return 1 if count % 2 == 0 else 2 #Return size of last char after 'count' shifts


def sizeoflastchar(array):
    """
    Function that takes in byte array, returns size of last char in byte array
    """

    if len(array) <= 1:
        return len(array)

    if array[-1] > 127:
    	return 2 #See Case 1, above
    else:
        if array[-2] <= 127:
            return 1 #See Case 2,above
        elif len(array) == 2:
            return 2 #Fast-return if array is of length 2
        else:
            if array[-3] > 127:
                return trace_backward(array) # See Case 4, above
            else:
                return 2 # See Case 3, above


#Long test cases
test_1 = [126,126,128,250,128,251,124,128,124] # Last char is [128, 124] of size 2
test_2 = [126,126,128,250,128,251,124,128,124,126,126,128,250,128,251,124,128,124,122] #Last char is [122] of size 1
test_3 = [126,126,128,250,128,251,124,128,124,126,126,128,250,128,251,124,128,124,122,
        126,126,124,128,124,126,126,128,250,128,251,124,128,124,122,250,122] #Last char is [250, 122] of size 2
test_4 = [126,126,128,250,128,251,124,128,124,126,126,128,250,128,251,124,128,124,80] #Last char is [80] of size 1


#Short test cases
test_5 = [126,250,128,128,126] #Last char is [128, 126] of size 2
test_6 = [128,250] # Size 2
test_7 = [126] # Size 1
test_8 = [128,128,128,128,128,126] # Last char is [128,126] of size 2

#Edge case
test_9 = []

print "Size of last char in test_1 is %s" % str(sizeoflastchar(test_1)) #Should return 2
print "Size of last char in test_2 is %s" % str(sizeoflastchar(test_2)) #Should return 1
print "Size of last char in test_3 is %s" % str(sizeoflastchar(test_3)) #Should return 2
print "Size of last char in test_4 is %s" % str(sizeoflastchar(test_4)) #Should return 1

print "Size of last char in test_5 is %s" % str(sizeoflastchar(test_5)) #Should return 2
print "Size of last char in test_6 is %s" % str(sizeoflastchar(test_6)) #Should return 2
print "Size of last char in test_7 is %s" % str(sizeoflastchar(test_7)) #Should return 1
print "Size of last char in test_8 is %s" % str(sizeoflastchar(test_8)) #Should return 2

print "Size of last char in test_9 is %s" % str(sizeoflastchar(test_9)) #Should return 0
