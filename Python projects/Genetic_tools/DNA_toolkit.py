# Functions to use for genetic sequence analysis

import collections
import random
from Genetic_components import * 


def validateSeq(dna_seq):
    """"Validates DNA sequences to check for defined nucleotides"""
    tempseq = dna_seq.upper()
    for nuc in tempseq:
        if nuc not in Nucleotides:
            return "Error Invalid sequence" 
    return tempseq 

def countNucFrequency(seq):
    """"Counts the frequency of nucleotides in a DNA/ RNA sequence"""
    tempFreqDict = {"A":0, "C":0, "G":0, "T":0, "U":0}
    for nuc in seq:
        tempFreqDict[nuc] += 1
    return tempFreqDict
    # return dict(collections.Counter(seq)) 

def transcription(seq):
    """DNA -> RNA Transcription, Replacing Thymine with Uracil"""
    return seq.replace("T", "U")

def reverse_complement(seq):
    """Swapping adenine with thymine and guanine with cytosine, Reversing newly generated string"""
    return ''.join([DNA_ReverseCompliment[nuc] for nuc in seq])[::-1]

def gc_content(seq):
    """" GC content in a DNA/RNA sequence"""
    return round((seq.count('C') + seq.count('G')) / len(seq) * 100)

def randDNAstr(nuc, dna_length):
    import random 
    """Generate a random DNA sequence of a given length."""
    return ''.join([random.choice(nuc) for _ in range(int(dna_length))])


