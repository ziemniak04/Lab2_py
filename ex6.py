def dna_complement(origi_strand):
    """
    Generate the complementary DNA strand based on Watson-Crick base pairing rules.

    Parameters:
        origi_strand (str): DNA strand containing letters A, T, C, and G.

    Returns:
        str: The complementary DNA strand.

    Raises:
        ValueError: If the input contains invalid characters.

    Outsource:
    - docstrings
    """
    compl_strand = ""

    for base in origi_strand.upper():
        if base == "A":
            compl_strand += "T"
        elif base == "T":
            compl_strand += "A"
        elif base == "C":
            compl_strand += "G"
        elif base == "G":
            compl_strand += "C"
        else:
            raise ValueError(f"Invalid character '{base}' in DNA strand.")

    return compl_strand


def find_genes(sequence):
    """
    Find all potential genes in a DNA sequence.

    A gene:
    - starts with ATG,
    - ends with a stop codon (TAG, TAA, TGA),
    - length is multiple of 3,
    - no internal stop codons.

    Parameters:
        sequence (str): DNA sequence to search for genes.

    Returns:
        list: List of all genes found.
    
    Raises:
        ValueError: If sequence contains invalid DNA characters.

    Outsource:
    - docstrings
    - lines from i in range... to the end of the function (break) 
    """
    sequence = sequence.upper()
    for char in sequence:
        if char not in "ATCG":
            raise ValueError(f"Invalid character '{base}' in DNA sequence.")

    start_codon = "ATG"
    stop_codons = ["TAG", "TAA", "TGA"]
    genes = []

    for i in range(len(sequence)):
        if sequence[i:i+3] == start_codon:
            for j in range(i+3, len(sequence), 3):
                codon = sequence[j:j+3]
                if codon in stop_codons:
                    gene = sequence[i:j+3]
                    if all(sequence[k:k+3] not in stop_codons for k in range(i+3, j, 3)):
                        genes.append(gene)
                    break

    return genes


def main():
    """
    Main program: asks user for DNA sequence and prints genes found in both
    the original and complementary sequences.

    Outsource:
    - docstrings
    - lines from try: ... until except ValueError as e: ... print(f"Error: {e}")
    """
    sequence = input("Enter a DNA sequence: ")
    try:
        genes_original = find_genes(sequence)
        genes_complement = find_genes(dna_complement(sequence))

        print("\nGenes in original sequence:")
        for gene in genes_original:
            print(gene)

        print("\nGenes in complementary sequence:")
        for gene in genes_complement:
            print(gene)

    except ValueError as e:
        print(f"Error: {e}")