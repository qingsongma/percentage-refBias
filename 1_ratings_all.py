#***********************************************
# This scripts is to change the form of ratings.
#***********************************************

import collections

inf = './data/ratings.csv'
outf = './ratings_all'

fout = open(outf, 'w')

n_segs = 100
n_judges = 25

# read the ratings file
judgeD = {}
idx = 0
with open(inf, 'r') as f:
    for line in f.readlines():
        idx += 1 
        if idx == 1: continue
        
        parts = line.strip().split(';')
        judge_id, seg_id, rating = int(parts[0]), int(parts[1]), int(parts[2])
        
        if not judgeD.has_key(judge_id):
            judgeD[judge_id] = []
        
        judgeD[judge_id].append((seg_id, rating))

# ratings orderd by seg_id
od_judgeD = collections.OrderedDict(sorted(judgeD.items()))

# print headline
judges = []
for i in range(1, n_judges+1):
    judges.append('j' + str(i))
fout.write(";".join(judges) + "\n")

# print ratings of each judge for each seg_id 
for i in range(0, n_segs):
    ratings = []
    
    for j in range(1, n_judges+1):
        ratings.append(str(od_judgeD[j][i][1])) 
    
    fout.write(";".join(ratings) + "\n") 
