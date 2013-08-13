import sys
from collections import defaultdict

#Open file and read in lines, exit if file does not exist
data = sys.stdin.readlines()

k = int(data[0].strip())
string = data[1].strip()

def sort_bucket(str, bucket, order):
        d = defaultdict(list)
        for i in bucket:
            key = str[i:i+order]
            d[key].append(i)
        result = []
        for k,v in sorted(d.iteritems()):
            if len(v) > 1:
                result += sort_bucket(str, v, order*2)
            else:
                result.append(v[0])
        return result

def suffix_array(str):
    return sort_bucket(str, (i for i in range(len(str))), 1)

def lcp_array(suffix_array):
    for i in range(0, len(suffix_array)):
    	return

def hamming_distance(s1, s2):
    assert len(s1) == len(s2)
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

def substrings (s):
    a = len(s)
    for i in xrange(0, a):
        for j in xrange(i, a): # ensures that j >= i, no test required
            part = buffer(s, i, j+1-i) # don't duplicate data
            if len(part) > 0:
                yield part

my_dict = {k: [] for k in range(len(string)+1)}
count = 0

print suffix_array(string)


print count
exit(0)
