from Bio import pairwise2
from Bio.pairwise2 import format_alignment

# Define the sequences
seq1 = """MNMFKEAVTFKDVAVAFTEEELGLLGPAXRKLYRDVMVENFRNLLSVGHPPFKQDVSPIERNEQLWIMTT
ATRRQGNLGEKNQSKLITVQDRESEEELSCWQIWQQIANDLTRCQDSMINNSQCHKQGDFPYQVGTELSI
QISEDENYIVNKADGPNNTGNPEFPILRTQDSWRKTFLTESQRLNRDQQISIKNKLCQCKKGVDPIGWIS
HHDGHRVHKSEKSYRPNDYEKDNMKILTFDHNSMIHTGQKSYQCNECKKPFSDLSSFDLHQQLQSGEKSL
TCVERGKGFCYSPVLPVHQKVHVGEKLKCDECGKEFSQGAHLQTHQKVHVIEKPYKCKQCGKGFSRRSAL
NVHCKVHTAEKPYNCEECGRAFSQASHLQDHQRLHTGEKPFKCDACGKSFSRNSHLQSHQRVHTGEKPYK
CEECGKGFICSSNLYIHQRVHTGEKPYKCEECGKGFSRPSSLQAHQGVHTGEKSYICTVCGKGFTLSSNL
QAHQRVHTGEKPYKCNECGKSFRRNSHYQVHLVVHTGEKPYKCEICGKGFSQSSYLQIHQKAHSIEKPFK
CEECGQGFNQSSRLQIHQLIHTGEKPYKCEECGKGFSRRADLKIHCRIHTGEKPYNCEECGKVFRQASNL
LAHQRVHSGEKPFKCEECGKSFGRSAHLQAHQKVHTGDKPYKCDECGKGFKWSLNLDMHQRVHTGEKPYK
CGECGKYFSQASSLQLHQSVHTGEKPYKCDVCGKVFSRSSQLQSHQRVHTGEKPYKCEICGKSFSWRSNL
TVHHRIHVGDKSYKSNRGGKNIRESTQEKKSIK"""

seq2 = """MAASGAVEPGPPGAAVAPSPALAPPPAPDHLFRPISAEDEEQQPTEIESLCMNCYCNGMTRLLLTKIPFF
REIIVSSFSCEHCGWNNTEIQSAGRVQDQGVRYTLTVRAPEDMNREVVKTDSATTRIPELDFEIPAFSQK
GALTTVEGLITRAISGLEQDQPARRANKDATAERIDEFIVKLKELKQVASPFTLIIDDPSGNSFVENPHA
PQKDDSLVITHYNRTQHQKEMLGLQEEAPAEKPEEEDLRNEVLQFNTNCPECNAPAQTNMKLVQIPHFKE
VIIMATNCENCGHRTNEVKSGGAVEPLGTRITLHITDPSDMTRDLLKSETCSVEIPELEFELGMAVLGGK
FTTLEGLLKDIRELVTKNPFTLGDSSNPCQKERLQEFSQKMDQIIEGNMKAHFIMDDPAGNSYLQNVYAP
EDDPEMKVERYKRTFDQNEELGLNDMKTEGYEAGLASQR"""

# Align the sequences
alignments = pairwise2.align.globalxx(seq1, seq2)

# Get the best alignment
best_alignment = alignments[0]
alignment_seq1, alignment_seq2, score, start, end = best_alignment

# Calculate differences
differences = sum(1 for a, b in zip(alignment_seq1, alignment_seq2) if a != b and a != '3' and b != '2')

# Check if the difference is greater than 10 amino acids
if differences > 10:
    result = False
else:
    result = True

# Output results
print(f"Alignment Score: {score}")
print(f"Differences: {differences}")
print(f"Result: {result}") 
print("\nBest Alignment:")
print(format_alignment(*best_alignment))

input("Press any key")


