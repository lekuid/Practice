#Task
#Mix -nacci sequences using a given pattern p.
#Return the first n elements of the mixed sequence.
#CodeWars-Micbonacci-By Suic

def mixbonacci(pattern, length):
    fib = [0, 1]; tri = [0, 0, 1]; tet = [0, 0, 0, 1]
    pad = [1, 0, 0]; jac = [0, 1, 1]; pel = [0, 1]
    n=length
    while n>=0:
        fib.append(sum(fib[-2:]))
        pad.append(pad[-2] + pad[-3])
        jac.append(jac[-1] + 2*jac[-2])
        pel.append(pel[-2] + 2*pel[-1])
        tri.append(sum(tri[-3:]))
        tet.append(sum(tet[-4:]))
        n-=1

    seq = {'fib':fib, 'pad':pad, 'jac':jac, 'pel':pel, 'tri':tri, 'tet':tet}; output = []
    while len(output)<length>n:
        try:
            pattern.append(pattern[0])
            output.append(seq[pattern[0]][0])
            seq[pattern[0]].pop(0)
            pattern.pop(0)
        except:
            return []
    return output   

#Tests and answers to verify from.
tests = [
[[[], 10], []],
[[['fib'], 0], []],
[[['fib'], 10], [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]],
[[['pad'], 10], [1, 0, 0, 1, 0, 1, 1, 1, 2, 2]],
[[['jac'], 10], [0, 1, 1, 3, 5, 11, 21, 43, 85, 171]],
[[['pel'], 10], [0, 1, 2, 5, 12, 29, 70, 169, 408, 985]],
[[['tri'], 10], [0, 0, 1, 1, 2, 4, 7, 13, 24, 44]],
[[['tet'], 10], [0, 0, 0, 1, 1, 2, 4, 8, 15, 29]],
[[['fib', 'tet'], 10], [0, 0, 1, 0, 1, 0, 2, 1, 3, 1]],
[[['jac', 'jac', 'pel'], 10], [0, 1, 0, 1, 3, 1, 5, 11, 2, 21]],
]

for inp, exp in tests:
    print(mixbonacci(*inp), exp)