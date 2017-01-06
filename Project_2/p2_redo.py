# Kate Archer - Project 2 - p2_redo.py
# CSCI 3038 - June 9, 2016

"""The purpose of this program is to find potential genes within a given sequence from a file. File name is to be entered as a command line argument. The program will output the starting indes for each identified potential gene in a sequence, their start and end codons, and length. """

import sys
inFile = open(sys.argv[1])

for line in inFile:
    line = line.strip().lower().split()
    seqID = line[0]; seq = line[1]

    for i in range(len(seq)):   # Begin iteration to find start codon.
        if(seq[i:i+3] == 'atg') or (seq[i:i+3] =='gtg'):
            startC = seq[i:i+3]; potential = seq[i:i+99]; length = 0

            # If/when start codon is found, iteration begins to find possible stop codon.
            for t in range(3,100,3):
                if (potential[t:t+3] == 'tag'):
                    stopC = potential[t:t+3]; length = t+3
                    break   # Breaks out of loop when first stop codon is found in the reading frame.

            # If the length from the identified start and stop is within set minimum and maximum,
            # the data is output.
            if (33 <= length <= 99):
                print('%-10s %3d %3d %s %s' % (seqID, i, length, startC, stopC))
