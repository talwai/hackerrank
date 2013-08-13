import sys

#Open file and read in lines, exit if file does not exist
data = sys.stdin.readlines()

NUM_CITIES = int(data[0])
construct = [[0 for x in xrange(NUM_CITIES)] for x in xrange(NUM_CITIES)]
manage = [[0 for x in xrange(NUM_CITIES)] for x in xrange(NUM_CITIES)]

UNDEFINED = 1000000
min_cost = [[UNDEFINED for x in xrange(NUM_CITIES)] for x in xrange(NUM_CITIES)]
managed = []


class City:
    def __init__ (self, id):
        self.id = id
        self.managed_by = -1
        self.in_road = -1
        self.out_road = -1

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

#for i in ALL_CITIES:
	#construct[i][i] = UNDEFINED

def total_cost(i,j,k):
    return construct[i][j] + manage[i][k]

def get_min_construct(i, path):
    return construct[i].index(min(construct[i][k] for k in ALL_CITIES if k not in path))

def get_min_manager(i, managers):
    return manage[i].index(min(manage[i][x] for x in ALL_CITIES if x not in managers))

def min_path(i, path, managers):
    if len(path) == 0:
    	path.append(i)
    elif len(path) == NUM_CITIES:
        print path
        print managers
        return 0
    j = get_min_construct(i, path)
    k = get_min_manager(i, managers)
    managers.append(k)
    path.append(j)
    return total_cost(i, j, k) + min_path(j,path,managers)

def global_min():
    return min(min_path(city, [],[]) for city in ALL_CITIES)



print global_min()

exit(0)
