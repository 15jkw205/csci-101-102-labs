# Jakob West
# CSCI 102 - Section E - Group A
# Week 4 - Lab B - Amino Acids
# References: none
# Time: 35 minutes

print('Input the chemical elements of the amino acid:')
C = int(input("CARBON>"))
H = int(input("HYDROGEN>"))
N = int(input("NITROGEN>")) #all integers
O = int(input("Oxygen>"))
S = int(input("SULFUR>"))

if C == 3 and H == 7 and N == 1 and O == 2 and S == 0:
    amino_acid = 'Alanine'
    print(f"The amino acid for C-{C}H-{H}N-{N}O-{O}S-{S} is {amino_acid}")
    print(f"OUTPUT C-{C}H-{H}N-{N}O-{O}S-{S}") #I love f strings 
    print("OUTPUT" , amino_acid)
    
if C == 6 and H == 14 and N == 4 and O == 2 and S == 0:
    amino_acid = 'Arginine'
    print(f"The amino acid for C-{C}H-{H}N-{N}O-{O}S-{S} is {amino_acid}")
    print(f"OUTPUT C-{C}H-{H}N-{N}O-{O}S-{S}")
    print("OUTPUT" , amino_acid)
    
if C == 4 and H == 8 and N == 2 and O == 3 and S == 0:
    amino_acid = 'Asparagine'
    print(f"The amino acid for C-{C}H-{H}N-{N}O-{O}S-{S} is {amino_acid}")
    print(f"OUTPUT C-{C}H-{H}N-{N}O-{O}S-{S}")
    print("OUTPUT" , amino_acid)
    
if C == 3 and H == 7 and N == 1 and O == 2 and S == 1:
    amino_acid = 'Cysteine'
    print(f"The amino acid for C-{C}H-{H}N-{N}O-{O}S-{S} is {amino_acid}")
    print(f"OUTPUT C-{C}H-{H}N-{N}O-{O}S-{S}")
    print("OUTPUT" , amino_acid)
    
if C == 6 and H == 9 and N == 3 and O == 2 and S == 0:
    amino_acid = 'Histidine'
    print(f"The amino acid for C-{C}H-{H}N-{N}O-{O}S-{S} is {amino_acid}")
    print(f"OUTPUT C-{C}H-{H}N-{N}O-{O}S-{S}")
    print("OUTPUT" , amino_acid)
    
if C == 5 and H == 10 and N == 2 and O == 3 and S == 0:
    amino_acid = 'Glutamine'
    print(f"The amino acid for C-{C}H-{H}N-{N}O-{O}S-{S} is {amino_acid}")
    print(f"OUTPUT C-{C}H-{H}N-{N}O-{O}S-{S}") #rinse and repeat all the way through baby, this is cake
    print("OUTPUT" , amino_acid)
    
