# Make_AF3_template_indices
Generates indices for using Alphafold3 with a custom template (see https://github.com/google-deepmind/alphafold3).

This script generates indices for using AlphaFold3 with a custom template (see https://github.com/google-deepmind/alphafold3). It runs in Python 3.9.19 on Macbook Pro M3 Sequoia 15.8.1, but it hasn't been tried on other hardware/software combinations.

Align the query and template sequences using T-Coffee, Clustal Omega or a similar app. Execute the script as follows:

QUERY='paste_the_complete_aligned_query_here'

TEMPLATE='paste_the_complete_aligned_template_here'

python3 make_af3_template_indices.py "$QUERY" "$TEMPLATE"

For example, if the aligned sequences are 

Query     ACDFEG
Template  A-EDYA

enter the following in the Terminal windoow: 

QUERY='ACDEFG'

TEMPLATE='A-EDYA'

python3 make_af3_template_indices.py "$QUERY" "$TEMPLATE"

The output is:

"queryIndices":
[0, 2, 3, 4, 5]

"templateIndices":
[0, 1, 2, 3, 4]

Number of mapped residues: 5
