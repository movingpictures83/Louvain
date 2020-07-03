# Louvain
# Language: Python
# Input: CSV (network)
# Output: CSV (clusters)
# Tested with: PluMA 1.1, Python 3.6
# Dependencies: pandas==1.0.1, networkx==2.2, community==0.11


PluMA plugin that runs the Louvain clustering algorithm (Blondel et al, 2008)
on an input network in CSV format, producing an output CSV file of clusters.

The input network nodes should be stored on the rows and columns of the CSV file,
with entry (i, j) of the file representing the weight of the edge from i to j.

The output CSV file takes the following format:

"","x"
"1","Acinetobacter.01"
"2","C.Gammaproteobacteria.04"
"3","C.Gammaproteobacteria.11"
"4","F.Enterobacteriaceae.01"
"5","F.Pseudomonadaceae.02"
"6","Gp2.01"
"7","Marinobacter.01"
"8","Pseudomonas.01"
"","x"
"1","Acinetobacter.02"
"2","Alicyclobacillus.01"
"3","Bifidobacterium.01"

Where "","x" signifies the start of a new cluster.
