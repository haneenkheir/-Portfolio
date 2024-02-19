# Calculate "GC" content in a given sequence 

def readFile(filePath):
    """Read file and return list of lines"""
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]

def gc_content(seq):
    """GC content in a DNA/RNA sequence"""
    return round((seq.count('C') + seq.count('G')) / len(seq) * 100)

# Storing File data from the file (FASTA formatted file)
FASTAFile = readFile("rand_seqs.txt")

# Dictionary for labels + Data
FASTADict = {}

# String for holding the current label
FASTALabel = ""

# Convert FASTA file/list data into dictionary
for line in FASTAFile:
    if line.startswith('>'):
        FASTALabel = line.strip()
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += line.strip()

print(FASTADict)

# Format the data & run GC content
# Use Dictionary Comprehension to generate a new dictionary with GC content
RESULTDict = {key: gc_content(value) for (key, value) in FASTADict.items()}

print(RESULTDict)