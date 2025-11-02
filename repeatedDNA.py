"""
Given a string s that represents a DNA sequence, return all the 
10-letter-long sequences (substrings) that occur more than once 
in a DNA molecule.
"""

def findRepeatedDNASequence(sequence: str) -> list:
    results, dic = set(), {}
    for i in range(len(sequence) - 9):
        # print(i, i+10)
        subStr = sequence[i:i+10]
        if subStr in dic.keys():
        	# slide of 10 already exists
            results.add(subStr)
        else:
        	# slide of 10 enters here
            dic[subStr] = 0
    return list(results)

sequence = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(findRepeatedDNASequence(sequence))
