test_1 = [126,126,128,250,128,251,124,128,124] # Last char is [128, 124] of size 2

test_2 = [126,126,128,250,128,251,124,128,124,126,126,128,250,128,251,124,128,124,122] #Last char is [122] of size 1

test_3 = [126,126,128,250,128,251,124,128,124,126,126,128,250,128,251,124,128,124,122,
        126,126,124,128,124,126,126,128,250,128,251,124,128,124,122,250,122] #Last char is [250, 122] of size 2

test_4 = [126,126,128,250,128,251,124,128,124,126,126,128,250,128,251,124,128,124,80] #Last char is [80] of size 1


test_5 = [126,250,128,128,126]
test_6 = [128,250]
test_7 = [126]
test_8 = [128,128,128,128,128,126]

#Basic algorithm is as follows.
#Check last three elements in byte array, and verify them as one of three possibilities:
#[x][x][>127] : Since last element is >127, last char has to be of size 2
#[<127][>127][<127]: Since third-last element is <127, it cannot form a char with second-last element. Hence last char is of size 2
#[>127][>127][<127]


UNDEFINED = -1

my_dict = {
        11 : UNDEFINED,
        10 : 1,
        00 : 1,
        01 : 2
    }

def recurse_backward(array, count):

    if count > len(array):
        return 1 if count % 2 == 0 else 2

    if array[-count] > 127:
        count += 1
        return recurse_backward(array, count)
    else:
        return 1 if count % 2 == 0 else 2

def greaterThan127(num):
    return 1 if num > 127 else 0

def sizeoflastchar(array):
    if len(array) <= 1:
        return len(array)

    if array[-1] > 127:
    	return 2
    else:
        if array[-2] < 127:
            return 1
        elif len(array) == 2:
            return 2

        to_return = my_dict[int(str( greaterThan127(array[-2] ) )
                            + str( greaterThan127(array[-3] ) ) ) ]
        return recurse_backward(array, 4) if to_return == UNDEFINED else to_return

print "Size of last char in test_1 is %s" % str(sizeoflastchar(test_5)) #Should return 2
print "Size of last char in test_2 is %s" % str(sizeoflastchar(test_6)) #Should return 1
print "Size of last char in test_3 is %s" % str(sizeoflastchar(test_7)) #Should return 2
print "Size of last char in test_5 is %s" % str(sizeoflastchar(test_8)) #Should return 1
