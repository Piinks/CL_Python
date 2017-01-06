#!/usr/bin/env python3

# Kate Archer - Project 4 - p4.py
# CSCI 3038 - June 23, 2016

""" The purpose of this program is to read from a file a series of sequence ids
and sequences and compare all of the sequences to find the longest common substring."""

import sys
# import time
import multiprocessing as mp

def main():
    """The main function prepares the data, creates and commences the processes designated by argv[1],
    and outputs the final result of the program."""

    seqList = []
    with open(str(sys.argv[2])) as inFile: # Reads the entire contents of the file, storing each ID
        for line in inFile:                # and sequence in a tuple, all of which are put in a list.
            seqList.append(tuple(line.split()))

    procs = []                             # List for processes.
    answerQ = mp.Queue()                   # Queue for multiprocessing.
    numProcs = int(sys.argv[1])
    procShare = int(len(seqList)/numProcs) # Determines the amount of the file each process will handle.

    for i in range(numProcs):
        if (i == 0):                            # First section
            section = seqList[:procShare+1]
            p = mp.Process(target=process_function, args=(section, seqList[:(-procShare)], answerQ))
        elif (i == numProcs - 1):               # Last section. First and last are special condition to cut down on huge
            section = seqList[(i*procShare):]   # comparison burden for the first section, balancing the workload.
            lastSeqComp = seqList[:procShare] + seqList[i*procShare:]
            p = mp.Process(target=process_function, args=(section, lastSeqComp, answerQ))
        else:                                   # Middle section(s)
            section = seqList[(i*procShare):((i+1)*procShare+1)]
            p = mp.Process(target=process_function, args=(section, seqList[i*procShare:], answerQ))
        procs.append(p)

    #startTime = time.time()

    for p in procs: p.start()          # Begins processes
    for p in procs: p.join()

    #print("Processes ran for: %0.4f" % (time.time() - startTime))

    finalAnswer = (0,)
    for p in procs:                    # Each process has submitted a LCS for their section of comparison
        potential = answerQ.get()      # to the MP queue. Final compare of processes answer for final result.
        if potential[0] > finalAnswer[0]:
            finalAnswer = potential
    print(finalAnswer[0], finalAnswer[1], finalAnswer[2])


 # Process Functions ############################################################

def process_function(section, seqList, answerQ):
    """This function takes the return values from function lcs and
    returns to main a final answer for each process."""

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
    """Function provided by RButler, with some modification for the arrangement of
    data, i.e. tuples of ID and sequence, keeping the data together and returning
    only the necessary information for output."""

    m = len(S[1])
    n = len(T[1])
    counter = [[0]*(n+1) for x in range(m+1)]
    longest = 0
    lcs_set = set()
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
    while lcs_set.__len__() > 0:
        nextSubstring = lcs_set.pop()
        if len(nextSubstring) > len(substring):
            substring = newSubstring

    return len(substring), S[0], T[0]


main()
