import sys

#Open file and read in lines, exit if file does not exist
data = sys.stdin.readlines()

NUM_CITIES = int(data[0])
construct = [[0 for x in xrange(NUM_CITIES)] for x in xrange(NUM_CITIES)]
manage = [[0 for x in xrange(NUM_CITIES)] for x in xrange(NUM_CITIES)]

UNDEFINED = 1000000
min_cost = [[UNDEFINED for x in xrange(NUM_CITIES)] for x in xrange(NUM_CITIES)]

ALL_CITIES = [x for x in xrange(NUM_CITIES)]

for i in range(1,NUM_CITIES+1):
    line = data[i]
    tokens = line.strip().split(' ')
    for j in range(0,len(tokens)):
        construct [i-1][j] = int(tokens[j])

for i in range(1+NUM_CITIES,2*NUM_CITIES+1):
    line = data[i]
    tokens = line.strip().split(' ')
    for j in range(0,len(tokens)):
        manage [i-NUM_CITIES-1][j] = int(tokens[j])


def direct_min_cost(i,j):
    return min(construct[i][j] + manage[i][j], construct[j][i] + manage[j][i])

def intermediate_min_cost(i,j, cities = ALL_CITIES):
    print cities, j
    cities.remove(i)
    return min([overall_min_cost(i,k) + overall_min_cost(k,j) for k in cities])

def overall_min_cost(i,j, cities = ALL_CITIES):
    if i == j:
    	return 0
    return min(direct_min_cost(i,j),direct_min_cost(j,i),
            intermediate_min_cost(i,j, cities),intermediate_min_cost(j,i, cities))

def min_path(i, cities):
    cities.remove(i)

    if not cities:
    	return 0
    else:
        return min(min_cost[i][k] + min_path(k, cities) for k in cities)

for i in xrange(NUM_CITIES):
    for j in xrange(NUM_CITIES):
    	min_cost[i][j] = direct_min_cost(i,j)


for i in xrange(NUM_CITIES):
    for j in xrange(NUM_CITIES):
    	min_cost[i][j] = overall_min_cost(i,j)

def global_min():
    return min(min_path(city, ALL_CITIES) for city in ALL_CITIES)

print construct[8][3] + manage[8][3]

print direct_min_cost(8,3)
print global_min()

exit(0)
