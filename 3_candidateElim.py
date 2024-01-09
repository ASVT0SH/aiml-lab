import csv

data = []

with open('datasets/trainingexamples.csv') as csvFile:
    for line in csv.reader(csvFile):
        data.append(tuple(line))

def Domain():
    d = []
    for i in range(len(data[0])):
        l = []
        for ele in data:
            if ele[i] not in l:
                l.append(ele[i])
        d.append(l)
    return d

D = Domain()

def consistant(h1, h2):
    # Compare the 2 participating hypotheses for compatibility
    for x, y in zip(h1, h2):
        if not (x == "?" or (x != "ɸ" and (x == y or y == "ɸ"))):
            return False
    return True

def candidate_elimination():
    G = {('?',)*(len(data[0]) - 1),}
    S = ['ɸ'] * (len(data[0]) - 1)
    no = 0

    print("\nG:", G)
    print("\nS:", S)

    for item in data:
        no += 1
        inp, res = item[:-1], item[-1]
        if res in "Yy":  # For +ve examples
            i = 0
            G = {g for g in G if consistant(g, inp)}
            for s, x in zip(S, inp):
                if not s == x:
                    S[i] = '?' if s != 'ɸ' else x
                i += 1
        else:  # For -ve examples
            S = S

            Gprev = G.copy()
            for g in Gprev:
                for i in range(len(g)):
                    if g[i] == "?":
                        for val in D[i]:
                            if inp[i] != val and val == S[i]:
                                g_new = g[:i] + (val,) + g[i+1:]
                                G.add(g_new)
                    else:
                        G.add(g)
            if ('?', '?', '?', '?', '?', '?') in G:
                G.remove(('?', '?', '?', '?', '?', '?'))

        print("\nG:", G)
        print("\nS:", S)

candidate_elimination()
