def dna_complement(origi_strand):
    """
    Generate the complementary DNA strand based on Watson-Crick base pairing rules.

    Parameters:
        orig_strand (str): The original DNA strand containing the letters A, T, C, and G.

    Returns:
        str: The complementary DNA strand where:
             A pairs with T, and C pairs with G.

    Raises:
        ValueError: If the input contains characters other than A, T, C, or G.

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
            raise ValueError("Invalid character in DNA strand.")

    return compl_strand


print(dna_complement("AACC"))     
print(dna_complement("TTGG"))
