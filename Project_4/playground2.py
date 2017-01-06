# p4 Playground2
import sys
import time
import multiprocessing as mp

def main():

    inFile = open(str(sys.argv[2]))
    seqList = []
    for line in inFile:
        seqList.append(tuple(line.split()))

    procs = []; answerQ = mp.Queue(); numProcs = int(sys.argv[1]); procShare = int(len(seqList)/numProcs) + 1

    for i in range(numProcs):
        section = seqList[(i*procShare):((i+1)*procShare+1)]
        p = mp.Process(target=process_function, args=(section, seqList[i*procShare:], answerQ))
        procs.append(p)

    startTime = time.time()

    for p in procs: p.start()
    for p in procs: p.join()

    print("Processes ran for: %0.4f" % (time.time() - startTime))

    finalAnswer = (0,)
    for p in procs:
        potential = answerQ.get()
        if potential[0] > finalAnswer[0]:
            finalAnswer = potential
    print(finalAnswer[0], finalAnswer[1], finalAnswer[2])

    inFile.close()



def process_function(section, seqList, answerQ):
    procAnswer = ()
    for i in range(len(section)):
        for j in range(len(seqList)):
            if (procAnswer.__len__() == 0) and (section[i][0] != seqList[j][0]):
                procAnswer = lcs(section[i], seqList[j])
            elif (section[i][0] != seqList[j][0]):
                newAnswer = lcs(section[i], seqList[j])
                if (newAnswer[0] > procAnswer[0]):
                    procAnswer = newAnswer
    answerQ.put(procAnswer)

def lcs(S,T):
    m = len(S[1]); n = len(T[1])
    counter = [[0]*(n+1) for x in range(m+1)]
    longest = 0; lcs_set = set()
    for i in range(m):
        for j in range(n):
            if S[1][i] == T[1][j]:
                c = counter[i][j] + 1
                counter[i+1][j+1] = c
                if c > longest:
                    lcs_set = set()
                    longest = c
                    lcs_set.add(S[1][i-c+1:i+1])
                elif c == longest:
                    lcs_set.add(S[1][i-c+1:i+1])
    substring = lcs_set.pop()
    return len(substring), S[0], T[0]


main()
