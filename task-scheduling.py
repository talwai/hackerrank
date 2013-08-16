import sys, operator

#Open file and read in lines, exit if file does not exist
data = sys.stdin.readlines()
num_activities = int(data[0])
activity_info = [(0,0) for x in xrange(num_activities)]
max_overshoot = [-1 for x in xrange(num_activities)]
max_overshoot[0] = 0

def parse(line):
    d, m = [int(x) for x in line.strip().split(' ')]
    return d, m

for i in xrange(num_activities):
    line = data[i+1]
    activity_info[i] = parse(line)

def allocate(activities):
    if not activities:
    	return 0
    if activities[-1][0] > sum(x[1] for x in activities):
        return allocate(activities[:-1])
    max_overshoot = time = 0
    complete = 0
    while complete < len(activities):
        for i in xrange(len(activities)):
            task = activities[i]
            if task[1] > 0:
                activities[i] = (task[0], task[1] - 1)
                time += 1
                if time - task[0] > max_overshoot:
                    max_overshoot = time - task[0]
            else:
                complete += 1
    return max_overshoot



for i in range(1, num_activities):
    sorted_acts = sorted(activity_info[0:i+1])
    max_overshoot[i] = allocate(sorted_acts)

for num in max_overshoot:
	print num

exit(0)
