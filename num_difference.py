"""Given N integers [N<=10^5], count the total pairs of integers that have a difference of K. [K>0 and K<1e9]. Each of the N integers will be greater than 0 and at least K away from 2^31-1 (Everything can be done with 32 bit integers)."""

import sys

#Open file and read in lines, exit if file does not exist
data = sys.stdin.readlines()
num_pairs, k = [int(x) for x in data[0].strip().split(' ')]

def generate():
    for x in data[1].strip().split(' '):
    	yield int(x)

pairs = 0
awaiting = []

for num in generate():
    if num + k in awaiting:
        pairs = pairs + 1
        awaiting.remove(num+k)
    if num - k in awaiting:
    	pairs = pairs + 1
    	awaiting.remove(num - k)
    else:
    	awaiting.append(num)

print pairs

exit(0)
