# Functions to use for genetic sequence analysis

import collections
import random
from Genetic_components import * 

# Function to validate sequence based on defined nucleotides in Genetic_components, returns error message if not in "Nucleotides"
def validateSeq(dna_seq):
    """"Validates DNA sequences to check for defined nucleotides"""
    tempseq = dna_seq.upper()
    for nuc in tempseq:
        if nuc not in Nucleotides:
            return "Error Invalid sequence" 
    return tempseq 

# Function to count nucelotise frequency and returns a dictionary with the nucleotide counts in the genetic sequence
def countNucFrequency(seq):
    """"Counts the frequency of nucleotides in a DNA/ RNA sequence"""
    tempFreqDict = {"A":0, "C":0, "G":0, "T":0, "U":0}
    for nuc in seq:
        tempFreqDict[nuc] += 1
    return tempFreqDict
    # return dict(collections.Counter(seq)) 

# Function to replace any T in the DNA sequence with U 
def transcription(seq):
    """DNA -> RNA Transcription, Replacing Thymine with Uracil"""
    return seq.replace("T", "U")

# Function to replace bases with complimentary pairs from DNA_ReverseCompliment 
def reverse_complement(seq):
    """Swapping adenine with thymine and guanine with cytosine, Reversing newly generated string"""
    return ''.join([DNA_ReverseCompliment[nuc] for nuc in seq])[::-1]

# Counts GC content and returns percentage 
def gc_content(seq):
    """" GC content in a DNA/RNA sequence"""
    return round((seq.count('C') + seq.count('G')) / len(seq) * 100)


def randDNAstr(nuc, dna_length):
    import random 
    """Generate a random DNA sequence of a given length."""
    return ''.join([random.choice(nuc) for _ in range(int(dna_length))])


