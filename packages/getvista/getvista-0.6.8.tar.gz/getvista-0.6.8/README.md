# GetVISTA
Query Ensembl to obtain genomic information in VISTA format. Useful for collecting sequences to run in [mVISTA](https://genome.lbl.gov/vista/mvista/submit.shtml) multi-species alignment.
* **envistacoords.py**: query _Ensembl_ database with species and _genomic coordinates_
* **envistagene.py**: query _Ensembl_ database with species and _gene name_
* **gbvistacoords.py**: query _GenBank_ database with species and _genomic coordinates_
* **gbvistagene.py**: query _GenBank_ database with species and _gene name_
* **gbgenerecord.py**: query _GenBank_ with database species and _gene name_, get list of records to select (to choose in gbgene module)
* **version_check.py**: check package version is up to date

## Author
Jake Leyhr (@jakeleyhr)
https://github.com/jakeleyhr/GetVISTA

## Dependencies
* Python 3.11
* requests
* argparse
* packaging
* biopython

## Quick start guide
* Install and open [Miniconda](https://docs.conda.io/projects/miniconda/en/latest/)
* Create an environment with python 3.11 e.g:
```
conda create -n getvistaenv python=3.11
```
* Activate (enter) the environment:
```
conda activate getvistaenv
```
* Install the package:
```
pip install getvista
```
* Then you're ready to start!

# encoords usage

```
$ encoords -h
usage: encoords [-h] -s SPECIES -c GENCOORDINATES [-fasta FASTA_OUTPUT_FILE] [-anno COORDINATES_OUTPUT_FILE] [-all]
                [-nocut] [-rev] [-autoname]

Query the Ensembl database with a species name and genomic coordinates to obtain DNA sequences in fasta format and
gene feature coordinates in pipmaker format.

options:
  -h, --help            show this help message and exit
  -s SPECIES, --species SPECIES
                        Species name (e.g., 'Homo_sapiens' or 'Human')
  -c GENCOORDINATES, --gencoordinates GENCOORDINATES
                        Genomic coordinates (e.g., 1:1000-2000)
  -fasta FASTA_OUTPUT_FILE, --fasta_output_file FASTA_OUTPUT_FILE
                        Output file name for the DNA sequence in FASTA format
  -anno COORDINATES_OUTPUT_FILE, --coordinates_output_file COORDINATES_OUTPUT_FILE
                        Output file name for the gene coordinates in pipmaker format
  -all, --all_transcripts
                        Include all transcripts (instead of canonical transcript only)
  -nocut                Don't delete annotations not included in sequence
  -rev                  Reverse complement DNA sequence and coordinates
  -autoname             Automatically generate output file names based on species and genomic coordinates
```
## encoords inputs and outputs:
The simplest inputs are the species name (**-s**) and region coordinates (**-c**), along with the -autoname flag:
```
$ encoords -s human -c 1:10000-20000 -autoname
```
This produces the following output in the terminal:
```
Assembly name: GRCh38
Specified sequence length: 10001bp

Transcripts included in region:
MIR6859-1-201
DDX11L1-201
DDX11L2-202
WASH7P-201

Coordinates saved to human_1_10000-20000.annotation.txt
DNA sequence saved to human_1_10000-20000.fasta.txt
```
Two text files are generated in the working directory - the first contains the coordinates of the exons and UTRs of all genes contained within the genomic region selected in pipmaker format, and the second contains the DNA sequence of the selected region in fasta format. By using the **-autoname** flag, the names of these files were automatically generated from the species and region inputs.

Alternatively, the output file names can be specified manually using the **-anno** and **-fasta** arguments, e.g:
```
$ encoords -s human -c 1:10000-20000 -anno annotationoutput.txt -fasta fastaoutput.txt
Assembly name: GRCh38
Specified sequence length: 10001bp

Transcripts included in region:
MIR6859-1-201
DDX11L1-201
DDX11L2-202
WASH7P-201

Coordinates saved to annotationoutput.txt
DNA sequence saved to fastaoutput.txt
```
Without **-anno**, **-fasta**, or **-autoname** arguments, the terminal output will be provided but no output .txt files will be saved to the working directory. If, for example, only **-anno** is provided, **-autoname** can also be provided to generate the remaining (fasta) filename:
```
$ encoords -s human -c 1:10000-20000 -anno annotationoutput.txt -autoname             
Assembly name: GRCh38
Specified sequence length: 10001bp

Transcripts included in region:
MIR6859-1-201
DDX11L1-201
DDX11L2-202
WASH7P-201

Coordinates saved to annotationoutput.txt
DNA sequence saved to human_1_10000-20000.fasta.txt
```
## encoords other arguments:
By default, only the exon and UTR coordinates of the canonical gene transcripts are included in the annotation .txt file, e.g:
```
$ encoords -s human -c 1:950000-1000000 -autoname
```
```
...

< 25199 32094 PERM1-202
25199 26172 UTR
26173 26270 exon
26500 26625 exon
28882 31030 exon
31031 31174 UTR
32066 32094 UTR
```
However, by including the **-all** flag, all transcripts are included:
```
$ encoords -s human -c 1:950000-1000000 -autoname -all
```
```
...

< 25199 32094 PERM1-202
25199 26172 UTR
26173 26270 exon
26500 26625 exon
28882 31030 exon
31031 31174 UTR
32066 32094 UTR


< 25205 32094 PERM1-201
25205 26172 UTR
26173 26270 exon
26500 26625 exon
28882 30658 exon
31138 31167 exon
31168 31174 UTR
32066 32094 UTR


< 25206 26642 PERM1-203
25206 26270 exon
26500 26642 exon


< 26122 32118 PERM1-204
26122 26172 UTR
26173 26270 exon
26500 26625 exon
28882 31030 exon
31031 31048 UTR
32066 32118 UTR
```
Also by default, the module carefully trims the transcript coordinates to ensure that the reported coordinates fit inside the specified region. For example, the mouse Cenpa gene is located on chromosome 5:30824121-30832175. If those coordinates are input, the resulting annotation file appears like this:
```
$ encoords -s mouse -c 5:30824121-30832174 -autoname
```
```
> 1 8054 Cenpa-205
1 252 UTR
253 337 exon
5688 5794 exon
6206 6283 exon
6517 6651 exon
6652 6667 UTR
7262 8054 UTR
```
If the region 5:30824621-30832074 is specified instead, which cuts off 500bp from the 5' end and 100bp from the 3' end, The resulting annotation file is adjusted to include only bases inside the region. In this case, the 5' UTR and 1st exon have been deleted entirely, and the 3' UTR has been truncated. Information about the truncation has been added to the transcript name (Cenpa-205-cut5':500bp-cut3':100bp) to make it clear to the user that the selection has cut off part of the gene.
```
$ encoords -s mouse -c 5:30824621-30832074 -autoname
```
```
> 1 7454 Cenpa-205-cut5':500bp-cut3':100bp
5188 5294 exon
5706 5783 exon
6017 6151 exon
6152 6167 UTR
6762 7454 UTR
```
This option can be turned off by including the **-nocut** flag, such that cut-off parts of the gene are still included in the annotation file, with negative coordinates or coordinates that extend beyond the end the sequence:
```
$ encoords -s mouse -c 5:30824621-30832074 -autoname -nocut
```
```
> -499 7554 Cenpa-205
-499 -248 UTR
-247 -163 exon
5188 5294 exon
5706 5783 exon
6017 6151 exon
6152 6167 UTR
6762 7554 UTR
```
By default, the specified genomic region is read on the forward strand, but for some purposes a gene on the reverse strand may want to be collected in the 5'>3' direction. In such cases, the **-rev** flag can be included. This reverse complements the DNA sequence returned in the fasta file (in addition to modifying the header to reflect this by changing :1 to :-1). It also flips the annotation coordinates. Returning to the mouse Cenpa gene as an example, this is the output when extracting the whole gene with **-rev**:
```
$ encoords -s mouse -c 5:30824121-30832174 -autoname -rev
```
```
< 1 8054 Cenpa-205
1 793 UTR
1388 1403 UTR
1404 1538 exon
1772 1849 exon
2261 2367 exon
7718 7802 exon
7803 8054 UTR
```
Note that the strand direction indicator has changed (> to <), and the 252bp 5' UTR is now at the bottom (3' end) of the file rather than the top, with the rest of the annotations following suit.


# engene usage
```
$ engene -h
usage: engene [-h] -s SPECIES -g GENE_NAME [-sa START_ADJUST] [-ea END_ADJUST] [-fasta FASTA_OUTPUT_FILE]
              [-anno COORDINATES_OUTPUT_FILE] [-all] [-nocut] [-rev] [-autoname] [-fw]

Query the Ensembl database with a species and gene name to obtain DNA sequences in FASTA format and gene feature
coordinates in pipmaker format.

options:
  -h, --help            show this help message and exit
  -s SPECIES, --species SPECIES
                        Species name (e.g., 'Homo_sapiens' or 'Human')
  -g GENE_NAME, --gene_name GENE_NAME
                        Gene name
  -sa START_ADJUST, --start_adjust START_ADJUST
                        Number to subtract from the start coordinate (default: 0)
  -ea END_ADJUST, --end_adjust END_ADJUST
                        Number to add to the end coordinate (default: 0)
  -fasta FASTA_OUTPUT_FILE, --fasta_output_file FASTA_OUTPUT_FILE
                        Output file name for the DNA sequence in FASTA format
  -anno COORDINATES_OUTPUT_FILE, --coordinates_output_file COORDINATES_OUTPUT_FILE
                        Output file name for the gene coordinates in pipmaker format
  -all, --all_transcripts
                        Include all transcripts (instead of canonical transcript only)
  -nocut                Delete annotations not included in sequence
  -rev                  Reverse complement DNA sequence and coordinates
  -autoname             Automatically generate output file names based on species and gene name
  -fw                   Automatically orient the gene in the forward strand by reverse complementing if needed
```
## engene inputs:
The output arguments, in addition to the **-all**, **-nocut**, **-rev** arguments are identical to encoords described above, but the inputs are quite different. Rather than defining a species and genomic region, a species and _gene name_ are input. For example, mouse and the gdf5 gene. This module outputs a detailed log of the gene information and the sequence region extracted:
```
$ engene -s mouse -g gdf5 -autoname 
Assembly name: GRCm39
mouse gdf5 coordinates: 2:155782943-155787287
mouse gdf5 is on -1 strand
mouse gdf5 sequence length: 4345bp
Specified coordinates: 2:155782943-155787287
Specified sequence length: 4345bp

Transcripts included in region:
Gm15557-201
Gdf5-201

Coordinates saved to mouse_gdf5.annotation.txt
DNA sequence saved to mouse_gdf5.fasta.txt
```
Two additional arguments can be used to adjust the start (**-sa**) and end (**-ea**) coordinates beyond the gene start and end. For example, to extract the sequence and annotations for the gdf5 gene plus an additional 50,000bp from the 5' flank and an additional 20,000bp from the 3' flank (direction relative to the assembly forward strand):
```
$ engene -s mouse -g gdf5 -autoname -sa 50000 -ea 20000 
Assembly name: GRCm39
mouse gdf5 coordinates: 2:155782943-155787287
mouse gdf5 is on -1 strand
mouse gdf5 sequence length: 4345bp
Specified coordinates: 2:155732943-155807287
Specified sequence length: 74345bp

Transcripts included in region:
Uqcc1-204
Gm15557-201
Gdf5-201
Cep250-204

Coordinates saved to mouse_gdf5_2_155732943-155807287.annotation.txt
DNA sequence saved to mouse_gdf5_2_155732943-155807287.fasta.txt
```
In the output, note that the gene length is 4,345bp, but the total sequence length extracted is 74,345bp as a result of the 70,000bp flanking regions also being included. The annotation file also reflects these additional sequences, including the genes in the expanded region:
```
< 1 39288 Uqcc1-204-cut5':44102bp
10276 10333 exon
18331 18403 exon
19335 19442 exon
20719 20814 exon
30613 30705 exon
38991 39014 exon
39015 39288 UTR


> 49706 51728 Gm15557-201
49706 49816 UTR
50460 50770 UTR
50771 51475 exon
51476 51728 UTR


< 50001 54345 Gdf5-201
50001 50520 UTR
50521 51395 exon
53421 54033 exon
54034 54345 UTR


> 65536 74345 Cep250-204-cut3':33533bp
65536 65635 UTR
70850 70949 UTR
70950 71132 exon
71878 71934 exon
72691 72773 exon
73088 73253 exon
73967 74073 exon
74291 74345 exon
```
Crucially, with engene, multiple species names can be included as arguments, for example:
```
engene -s human mouse chicken -g gdf5 -autoname -sa 50000 -ea 20000 
```
In this case, the module behaves just as previously described, just iterating through the different species names (separated by spaces). As a result, in this example the 6 output files for all 3 species will be saved in the working directory, and the output in the terminal looks like this:
```
Assembly name: GRCh38
human gdf5 coordinates: 20:35433347-35454746
human gdf5 is on reverse strand
human gdf5 sequence length: 21400bp
Specified coordinates: 20:35383347-35474746
Specified sequence length: 91400bp

Transcripts included in region:
GDF5-AS1-201
GDF5-201
MIR1289-1-201
CEP250-202
UQCC1-205

Coordinates saved to human_gdf5_20_35383347-35474746.annotation.txt
DNA sequence saved to human_gdf5_20_35383347-35474746.fasta.txt

Assembly name: GRCm39
mouse gdf5 coordinates: 2:155782943-155787287
mouse gdf5 is on reverse strand
mouse gdf5 sequence length: 4345bp
Specified coordinates: 2:155732943-155807287
Specified sequence length: 74345bp

Transcripts included in region:
Uqcc1-204
Gm15557-201
Gdf5-201
Cep250-204

Coordinates saved to mouse_gdf5_2_155732943-155807287.annotation.txt
DNA sequence saved to mouse_gdf5_2_155732943-155807287.fasta.txt

Assembly name: bGalGal1.mat.broiler.GRCg7b
chicken gdf5 coordinates: 20:1563813-1568758
chicken gdf5 is on forward strand
chicken gdf5 sequence length: 4946bp
Specified coordinates: 20:1513813-1588758
Specified sequence length: 74946bp

Transcripts included in region:
CEP250-203
GDF5-201
UQCC1-201
ERGIC3-201
ENSGALT00010061117
ENSGALT00010061118
ENSGALT00010061120

Coordinates saved to chicken_gdf5_20_1513813-1588758.annotation.txt
DNA sequence saved to chicken_gdf5_20_1513813-1588758.fasta.txt
```
A final argument that can be added to the engene command is **-fw**. When this is present, the coordinates and sequence outputs will always be such that the query gene is oriented in the forward direction. In other words, if the gene is on the reverse strand the outputs will be reverse complemented, but if it's already on the forward strand, then the outputs won't be reverse complemented. This is particularly useful in conjection with the input of multiple species names, as the same gene will be annotated on different strands in assemblies from different species, and for sequence alignment a common orientation is essential.

# gbcoords usage
```
usage: gbcoords [-h] -a ACCESSION -c GENCOORDINATES [-fasta FASTA_OUTPUT_FILE] [-anno COORDINATES_OUTPUT_FILE]
                        [-x] [-nocut] [-rev] [-autoname]

Query the GenBank database with an accession and range of coordinates to obtain FASTA file and gene feature
coordinates in pipmaker format.

options:
  -h, --help            show this help message and exit
  -a ACCESSION, --accession ACCESSION
                        accession code
  -c GENCOORDINATES, --gencoordinates GENCOORDINATES
                        Genomic coordinates
  -fasta FASTA_OUTPUT_FILE, --fasta_output_file FASTA_OUTPUT_FILE
                        Output file name for the DNA sequence in VISTA format
  -anno COORDINATES_OUTPUT_FILE, --coordinates_output_file COORDINATES_OUTPUT_FILE
                        Output file name for the gene annotation coordinates
  -x                    Include predicted (not manually curated) transcripts in results
  -nocut                Delete annotations not included in sequence
  -rev                  Reverse complement DNA sequence and coordinates
  -autoname             Automatically generate output file names based on accession and genomic coordinates
```
This command functions almost identically to encoords, except that it querys the GenBank nucleotide database rather than Ensembl. There is no **-all** option, as all transcripts are automatically included in the annotation file. However, this only includes the manually curated transcripts. To get all transcripts including the predicted ones, add the **-x** flag. This may be particualrly relevant when exploring new geomes with few manually curated genes/transcripts. The other key difference is that an accession code (e.g. NC_000020 for human chromosome 20) must be specified instead of a speces name, and the genomic coordinates therefore just require the base region, not the chromosome (e.g. 500000-600000 instead of 20:500000-600000).
# gbgene usage
```
usage: gbgene [-h] -s SPECIES -g GENE_SYMBOL [-r RECORD_ID] [-sa START_ADJUST] [-ea END_ADJUST]
                      [-fasta FASTA_OUTPUT_FILE] [-anno COORDINATES_OUTPUT_FILE] [-x] [-nocut] [-rev] [-autoname] [-fw]

Query the GenBank database with a species and gene name to obtain FASTA file and gene feature coordinates in pipmaker
format.

options:
  -h, --help            show this help message and exit
  -s SPECIES, --species SPECIES
                        Species name(s) (e.g., 'Homo_sapiens' or 'Human')
  -g GENE_NAME, --gene_name GENE_NAME
                        Gene name (e.g. BRCA1 or brca1)
  -r RECORD_ID, --record_id RECORD_ID
                        Record ID number (default=0, the top match)
  -sa START_ADJUST, --start_adjust START_ADJUST
                        Number to subtract from the start coordinate (default: 0)
  -ea END_ADJUST, --end_adjust END_ADJUST
                        Number to add to the end coordinate (default: 0)
  -fasta FASTA_OUTPUT_FILE, --fasta_output_file FASTA_OUTPUT_FILE
                        Output file name for the DNA sequence in VISTA format
  -anno COORDINATES_OUTPUT_FILE, --coordinates_output_file COORDINATES_OUTPUT_FILE
                        Output file name for the gene coordinates
  -x                    Include predicted (not manually curated) transcripts in results
  -nocut                Delete annotations not included in sequence
  -rev                  Reverse complement DNA sequence and coordinates
  -autoname             Automatically generate output file names based on accession and gene name
  -fw                   Automatically orient the gene in the forward strand by reverse complementing if needed
```
This command functions almost identically to encoords, except that it querys the GenBank nucleotide database rather than Ensembl. As explained above in gbcoords, the **-all** function is 'replaced' with **-x**. There is also an extra option **-r**, to specify the sequence record. By default it is 0 (the default record according to GenBank), but in some cases a different record may be desired (e.g. to use the human T2T assembly CHM13v2.0 instead of the GRCh38.14 assembly). The species name can be entered in any form with underscores separating the words (e.g. carcharodon_carcharias or great_white_shark)

# gbrecords usage
```
usage: gbrecord [-h] -s SPECIES -g GENE_NAME

Query the GenBank database with a species and gene name to obtain a list of different records containing the sequence
to inform use of the gbgene module.

options:
  -h, --help            show this help message and exit
  -s SPECIES, --species SPECIES
                        Species name (e.g., 'Homo_sapiens' or 'Human')
  -g GENE_NAME, --gene_name GENE_NAME
                        Gene name (e.g. BRCA1 or brca1)
```
This command is intended to be used to see which genomic sequence records are available in GenBank for the given species and gene name. For example:
```
$ gbrecord -s human -g gdf5
```
gives this output in the terminal:
```
RECORD 0
Assembly: Chromosome 20 Reference GRCh38.p14 Primary Assembly
Accession: NC_000020
Location: 35433346:35454748
Length: 21403

RECORD 1
Assembly: RefSeqGene
Accession: NG_008076
Location: 21518:26399
Length: 4882

RECORD 2
Assembly: Chromosome 20 Alternate T2T-CHM13v2.0
Accession: NC_060944
Location: 37154207:37175639
Length: 21433
```
This shows that there are 3 different genomic records readily available in GenBank that contain the human GDF5 gene. Record 0 and Record 2 are different genomic assemblies, while Record 1 is a smaller RefSeqGene sequence (28kb). The transcript of GDF5 contained in this sequence is one of the shorter isoforms, only 4882bp as opposed to the longer 21403bp isoform in GRCh38.p14 or 21433bp isoform in CHM13v2.0. If you were only interested in the isolated region around the smaller core sequence of GDF5, you may want to use **-r 1** when running the gbgene command, as this would significantly speed up the request compared to the using the default (**-r 0**) CRCh38.p14 record. For example, the command "gbgene -s human -g gdf5 -autoname -r 0" takes ~66 seconds to complete, while the command "gbgene -s human -g gdf5 -autoname -r 1" takes only ~7 seconds.

## Notes
* Per the [Ensembl REST API documentation](https://rest.ensembl.org/documentation/info/overlap_region), the maximum sequence length that can be queried is 5Mb. Requests above this limit will fail (Status code: 400 Reason: Bad Request).
* For species with common names more than one word long (e.g. Alpine marmot or Spotted gar, as opposed to human or mouse), the full species name according to Ensembl must be used with underscores separating the words. For the Alpine marmot: marmota_marmota_marmota, and for the Spotted Gar: lepisosteus_oculatus
* The requests to GenBank sometimes fail for reasons unknown. If you get an "HTTP Error 400: Bad Request" when running gbcoords, gbgene, or gbrecord, try running the command once or twice again, and the query should go through.
* When running either gbcoords or gbgene on a large sequence record (e.g. a whole chromosome), it may take several tens of seconds to run, compared to the almost instant response from encoords and engene. This is because the gb scripts always search through the entire chromosomal record for gene features in the specified range, while the en scripts are able to narrow their search range to this range from the beginning.


## Bugs

Please submit via the [GitHub issues page](https://github.com/jakeleyhr/GetVISTA/issues).  

## Software Licence

[GPLv3](https://github.com/jakeleyhr/GetVISTA/blob/main/LICENSE)
