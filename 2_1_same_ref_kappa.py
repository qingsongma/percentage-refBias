inf = './kappas/kappas_all.txt' 
outf = './kappas/same_ref_kappas.txt'

batch1 = [1, 4, 10, 20, 21]
batch2 = [5, 7, 16, 19, 22]
batch3 = [2, 6, 8, 15, 25]
batch4 = [9, 13, 14, 18, 24]
batch5 = [3, 11, 12, 17, 23]
batch_all = [batch1, batch2, batch3, batch4]

fout = open(outf, 'w')
fout.write("klo	k	kup	kwlo	kw	kwup\n")

judgePair_kappaD = {}
with open(inf, 'r') as f:
    for line in f.readlines():
        ll = line.strip().split("\t")
        if ll[0] == 'klo': continue

        judgePair = ll[0]
        kappas = ll[1:]
		
        j1, j2 = judgePair.split('_')
        j1 = int(j1[1:])
        j2 = int(j2[1:])
		
        for i in range(1,5):
            batch = batch_all[i-1]
            if j1 < j2 and j1 in batch and j2 in batch:
                fout.write(line)

