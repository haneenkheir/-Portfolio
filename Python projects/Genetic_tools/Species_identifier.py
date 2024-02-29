from DNA_toolkit import * 
from Genetic_components import * 


def readSpeciesLibrary(filePath):
    """ Reads FASTA file and creates library"""
    SpeciesDict = {}
    with open(filePath, 'r') as f:
        SpeciesLabel = ""
        for line in f:
            if line.startswith('>'):
                SpeciesLabel = line.strip()
                SpeciesDict[SpeciesLabel] = ""
            else:
                SpeciesDict[SpeciesLabel] += line.strip()
    return SpeciesDict


# Function to clean a sequence
def cleanSequence(sequence):
    """Cleans the DNA sequence by removing spaces and non-nucleotide characters"""
    return ''.join(filter(lambda x: x in Nucleotides, sequence.upper()))

def readUnknownSequence(filePath):
    """Reads and cleans the unknown DNA sequence from a file"""
    with open(filePath, 'r') as f:
        sequence = f.read().strip()
        cleaned_sequence = cleanSequence(sequence)
        return cleaned_sequence
   

# Read unknown sequence from file
unknown_species = readUnknownSequence("unknown_species.txt")

# Validate sequence
if validateSeq(unknown_species):
    print("Valid sequence")
else:
    print("Validation error please review your sequence and import a valid sequence")

# Read species identifier library
Species_identity_Dict = readSpeciesLibrary("Species_identifier_genes.txt")

# # Check if the sequence is in the database and return species identity 
species_found = None
for SpeciesLabel, SpeciesSequence in Species_identity_Dict.items():
    if unknown_species == SpeciesSequence:
        species_found = SpeciesLabel
        break

if species_found:
    print(f"Species found: {species_found}")
else:
    print("Species not found in the database.")
