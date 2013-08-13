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

def total_cost(i,j, k):
    return construct[i][j] + manage[i][k]

def get_min_construct(i, path = []):
    return construct[i].index(min(construct[i][k] for k in ALL_CITIES if k not in path))

def get_min_manager(i, managers = []):
    ret = manage[i].index(min(manage[i][x] for x in ALL_CITIES if x not in managers))
    return ret

def get_optimal_managers(i, managers = [], cities = ALL_CITIES):
    optimal_managers = [UNDEFINED for x in ALL_CITIES]
    j = get_min_manager(i, managers)
    optimal_managers[i] = j
    managers.append(j)
    for j in cities:
        if j != i:
            x = get_min_manager(j, managers)
            optimal_managers[j] = x
            managers.append(x)

    total_sum = 0

    for x in cities:
        total_sum = total_sum + manage[x][optimal_managers[x]]

    return total_sum , optimal_managers

def optimal_manage_cost(path):
    print path
    total_sum, optimal_managers = min(get_optimal_managers(i, [], cities = path[:-1]) for i in path[:-1])
    return total_sum

OPTIMAL_COSTS = []
PATHS = []

def min_path(i, path, managers):
    if len(path) == 0:
    	path.append(i)
    elif len(path) == NUM_CITIES:
        PATHS.append(path)
        OPTIMAL_COSTS.append(optimal_manage_cost(path))
        return 0
    j = get_min_construct(i, path)
    path.append(j)
    return construct[i][j] + min_path(j,path,managers)

def global_min():
    curr_min = UNDEFINED
    optimal_cost = UNDEFINED

    all_costs = [min_path(city,[],[]) for city in ALL_CITIES]
    for i in xrange(len(all_costs)):
    	optimal_cost = OPTIMAL_COSTS[i] + all_costs[i]
        if optimal_cost < curr_min:
        	curr_min = optimal_cost
    return curr_min

print global_min()

exit(0)
