import sys

#Open file and read in lines, exit if file does not exist
data = sys.stdin.readlines()

k = int(data[0].strip())
string = data[1].strip()

def mismatch(a,b):
    ret = 0
    for i in xrange(len(a)):
        if a[i] is not b[i]:
        	ret = ret+1
    return ret

def substrings (s):
    a = len(s)
    for i in xrange(0, a):
        for j in xrange(i, a): # ensures that j >= i, no test required
            part = buffer(s, i, j+1-i) # don't duplicate data
            if len(part) > 0:
                yield part

count = 0
all_pairs = []

my_list = [x for x in substrings(string)]

for i in range(0,len(my_list)):
    s, rest = my_list[i], my_list[i+1:]
    for t in rest:
        if len(t) == len(s):
        	all_pairs.append( (s,t) )

for s,t in all_pairs:
    if mismatch(s,t) <= k:
    	count = count + 1

print count
exit(0)
