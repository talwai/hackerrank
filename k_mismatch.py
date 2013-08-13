import sys
from collections import defaultdict

#Open file and read in lines, exit if file does not exist
data = sys.stdin.readlines()

k = int(data[0].strip())
string = data[1].strip()

labels = {
        'a' : 0,
        'b' : 1,
        'c' : 2,
        'd' : 3,
        'e' : 4,
        'f' : 5,
        'g' : 6,
        'h' : 7,
        'i' : 8,
        'j' : 9,
        'k' : 10,
        'l' : 11,
        'm' : 12,
        'n' : 13,
        'o' : 14,
        'p' : 15,
        'q' : 16,
        'r' : 17,
        's' : 18,
        't' : 19,
        'u' : 20,
        'v' : 21,
        'w' : 22,
        'x' : 23,
        'y' : 24,
        'z' : 25
        }
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

def get_indices_of (char, string):
    ret_list = []
    for i in xrange(len(string)):
        if string[i] == char:
        	ret_list.append(i)
    return ret_list

def k_mismatches(pattern, string):
    ALL_CHARS = [ [] for x in xrange(26)]
    string_marks = [0 for x in xrange(len(string))]
    uniq_symbols = 0
    for char in pattern:
        if not ALL_CHARS[labels[char]]:
            uniq_symbols = uniq_symbols + 1
            ALL_CHARS[labels[char]] = get_indices_of(char, pattern)

    for i in xrange(len(string)):
    	char = string[i]
        if i in ALL_CHARS[labels[char]]:
            for offset in ALL_CHARS[labels[char]]:
                if i - offset >= 0:
                    string_marks[i - offset] = string_marks[i - offset] + 1
    p_len = len(pattern)
    count = 0

    for i in xrange(len(string_marks)):
    	string_marks[i] = uniq_symbols - string_marks[i]
        if string_marks[i] <= k:
            count = count + 1

    return count

def hamming_distance(s1, s2):
    assert len(s1) == len(s2)
    return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))


def substrings (s):
    ALL_SUBSTRINGS = []
    sames = 0
    a = len(s)
    for i in xrange(0, a):
        for j in xrange(i, a): # ensures that j >= i, no test required
            part = buffer(s, i, j+1-i) # don't duplicate data
            if len(part) > 0:
                ALL_SUBSTRINGS.append(part)
    return ALL_SUBSTRINGS



count = 0
ALL_SUBSTRINGS = substrings(string)



exit(0)
