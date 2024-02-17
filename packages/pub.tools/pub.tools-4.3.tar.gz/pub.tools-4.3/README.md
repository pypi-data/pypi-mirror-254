# Installation

    pip install pub.tools

To use this tool you are advised to create an Entrez account and use the associated email and API key.

    from Bio import Entrez
    Entrez.email = "myemailhere@imsweb.com"
    Entrez.tool = "pub.tools"
    Entrez.api_key = "mykeyhere"

Tools available:

* entrez - streamlines BioPython
* citations - creates citations for 6 different types using IMS standards
* date - formats dates into our desired format
* sanitizer - mostly useful for forcing unicode compliance in python2

## Citations

Citations are based on a standard defined by PubMed https://www.ncbi.nlm.nih.gov/books/NBK7256/.
For some publication types, passing the italicize parameter with a True value will return
HTML with italic tagged journals or conference names.

## Journals

The journals module uses the PMC source file https://www.ncbi.nlm.nih.gov/pmc/journals/?format=csv
to construct a library of journals keyed by abbreviation or full title.