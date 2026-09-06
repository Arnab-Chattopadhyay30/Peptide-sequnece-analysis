# Peptide Sequence Quality Control Using Python

 Objective

Develop a Python-based workflow to perform basic **peptide sequence quality control and characterization**.

The workflow:

* Normalizes peptide sequences to uppercase.
* Validates sequences against the 20 standard amino acids.
* Filters invalid peptide sequences.
* Calculates peptide length.
* Classifies valid peptides by length.
* Calculates amino-acid frequency.
* Flags potentially problematic peptides based on length and amino-acid repetition.

## Workflow

```text
Raw Peptide Sequences
        ↓
Sequence Normalization
        ↓
Amino Acid Validation
        ↓
Valid Peptides
        ↓
Length Analysis
        ↓
Large / Medium / Short Classification
        ↓
Amino Acid Frequency
        ↓
Quality-Control Flagging
```

## Classification Criteria

| Category | Criterion                                                  |
| -------- | ---------------------------------------------------------- |
| Large    | Length ≥ 10                                                |
| Medium   | 5 ≤ Length < 10                                            |
| Short    | Length < 5                                                 |
| Flagged  | Length < 5, length > 20, or any amino acid occurs >5 times |

## Results

The program generates:

* A list of **valid peptide sequences**
* A list of **invalid peptide sequences**
* Length of each valid peptide
* Large, medium, and short peptide groups
* Total frequency of each standard amino acid
* A list of **flagged peptide sequences**

Example output:

```text
Valid peptides:
['MKWVTFISLL', 'GIGAVLKVL', 'ACDEFGHIKLMNPQ', ...]

Large peptides:
['ACDEFGHIKLMNPQ', 'MKWVTFISLLMKWVTFISLL', ...]

Medium peptides:
['MKWVTFISLL', 'GIGAVLKVL', ...]

Short peptides:
['KLVG', ...]

Flagged peptides:
['GGGGGGGG', 'AAAAAAA', 'KKKKKKKKKK', ...]
```

## Tools

* Python 3
* Built-in Python data structures and functions

## Key Outcome

This project demonstrates a basic **peptide preprocessing and quality-control pipeline** that can serve as a foundation for downstream peptide feature extraction and machine-learning applications.

## Future Scope

The workflow can be extended to include:

* FASTA input
* Duplicate removal
* Amino-acid composition (%)
* Molecular weight
* Hydrophobicity
* Net charge
* Isoelectric point
* Physicochemical feature extraction
* Machine-learning-based peptide classification


