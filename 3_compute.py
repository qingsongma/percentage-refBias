import os, sys

cwd = os.getcwd()

Dir = cwd + '/kappas/'
same_inf = 'same_ref_kappas.txt'
diff_inf = 'diff_ref_kappas.txt'
src_inf = 'src_kappas.txt'

def readTable(inf):
    idx = -1
    klowL, kuppL = [], []
    with open(Dir + inf, 'r') as f:
        for line in f.readlines():
            idx += 1
            if idx == 0: continue
            parts = line.strip().split()
            klow, kupp = float(parts[1]), float(parts[3])
            klowL.append(klow)
            kuppL.append(kupp)
    return klowL, kuppL

def is_overlap(a_low, a_upp, b_low, b_upp):
    
    if (a_upp < b_low or a_low > b_upp):
        return False
    return True


def compute_percentage(fileA, fileB, tagA, tagB):
    
    a_klowL, a_kuppL = readTable(fileA)
    b_klowL, b_kuppL = readTable(fileB)

    count, total = 0., 0.
    
    if tagA == tagB:
        for i in range(0, len(a_klowL)):
            for j in range(i+1, len(b_klowL)):
                a_low, a_upp = a_klowL[i], a_kuppL[i]
                b_low, b_upp = b_klowL[j], b_kuppL[j]

                if not is_overlap(a_low, a_upp, b_low, b_upp):
                    count += 1
                
                total += 1
    else:
         for i in range(0, len(a_klowL)):
             for j in range(0, len(b_klowL)):
                 a_low, a_upp = a_klowL[i], a_kuppL[i]
                 b_low, b_upp = b_klowL[j], b_kuppL[j]
                 
                 if not is_overlap(a_low, a_upp, b_low, b_upp):    
                    count += 1
                 
                 total += 1
    
    #print count, total
    p = int(round(count / total * 100))
    line = tagA + ' vs ' + tagB + ':' + str(p) + '%(' + str(int(total)) + ')'
    print line

if __name__ == '__main__':
    compute_percentage(src_inf, src_inf, 'SOURCE', 'SOURCE')
    compute_percentage(src_inf, same_inf, 'SOURCE', 'SAME')
    compute_percentage(src_inf, diff_inf, 'SOURCE', 'DIFF')
    compute_percentage(same_inf, same_inf, 'SAME', 'SAME')
    compute_percentage(same_inf, diff_inf, 'SAME', 'DIFF')
    compute_percentage(diff_inf, diff_inf, 'DIFF', 'DIFF')
