peptides = [
    "MKWVTFISLL",
    "GIGAVLKVL",
    "ACDEFGHIKLMNPQ",
    "MKT12345",
    "GGGGGGGG",
    "KLVG",
    "ACD*EFGH",
    "MKWVTFISLLMKWVTFISLL",
    "ACDEFGHIK",
    "AAAAAAA",
    "KKKKKKKKKK",
    "MNPQRSTVWY",
    "ACDEFGHIKLMNPQRSTVWY",
    "",
    "acdefghik",
    "ACD EF",
    "WYKLV"
]


peptides = [sequence.upper() for sequence in peptides]
print(peptides)
aa = ["A", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "Y"]
for sequence in peptides :
    if all(amino_acid in aa for amino_acid in sequence) :
        print(sequence, "-> Valid")
    else :
        print(sequence, "-> Invalid")


valid_peptide = []

for sequence in peptides :
    if sequence and all(amino_acid in aa for amino_acid in sequence) :
        valid_peptide.append(sequence)
print(valid_peptide)

for sequence in valid_peptide :
    print(sequence, "=", len(sequence))


large_peptides = []
medium_peptides = []
short_peptides = []
for sequence in valid_peptide :
    if len(sequence) >= 10 :
        large_peptides.append(sequence)
    elif len(sequence) <10 and len(sequence) >= 5 :
        medium_peptides.append(sequence)
    else :
        short_peptides.append(sequence)

print(large_peptides)
print(medium_peptides)
print(short_peptides)




print("============================= Frequency of each amino acids=============================")
for amino_acid in aa:
    total = 0

    for sequence in valid_peptide:
        total += sequence.count(amino_acid)

    print(amino_acid, "=", total)


flag_peptide = []
for sequence in peptides :
    if len(sequence) < 5 or len(sequence) > 20 :
        flag_peptide.append(sequence)
    for amino_acid in aa:
        if sequence.count(amino_acid) > 5:
            flag_peptide.append(sequence)
            break



print("============================== Summary of the analysis ============================")

print("list of valid peptides ")
print(valid_peptide)

print("size of the peptides ")


print("large length peptides",large_peptides)
print("medium length peptides",medium_peptides)
print("Short length peptides",short_peptides)

print("Flagged peptides ")
print(flag_peptide)
