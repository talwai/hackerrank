import sys,fileinput


#Open file and read in lines, exit if file does not exist
data = sys.stdin.readlines()
for line in reversed(data):
    print line.strip()[::-1]

exit(0)
