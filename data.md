# Describe how files in the data folder relate to the supplemental tables in the manuscript.
Note that these example data files are not used in our manuscript but show an example of how data files should be described. 

### Data File 1 - fakeBP.csv
Stored locally in the repository in ./data/fakeBP.csv

Used in make_figure_1.ipynb

This file has fake systolic blood pressure measurements for 50 days from 3 subjects. 

In the manuscript (DOI LINK) as Supplemental Table 1

### Data File 2 - datafile.csv
Stored remotely on Box

Used in make_figure_2.ipynb

This file is identical to fakeBP.csv, but is included to demonstrate streaming from Box.

In the manuscript (DOI LINK) as Supplemental Table 2


# The following files are graphics for the manuscript.
### Table_of_Contents_Figure.png
Pictoral figure created with Biorender.com
This is the table of contents figure for our manuscript. It provides a high level visual for the step in analysis dissemination that our pattern addresses.

### Figure1_Experimental_Overview.png
Pictoral figure created with Biorender.com, in the manuscript as Figure 1:

Figure 1 – Tools for transparent sharing of research. Different stages of a research project have unique data types and complexities. Different resources have evolved for sharing each of these separate stages, including sample preparation, data acquisition and quantitative analysis pipelines. The pattern described herein proposed a simple and efficient method for transparent sharing of analysis methods which support scientific conclusions.

### Figure2_The_Pattern.png
Pictoral figure created with Photoshop, in the manuscript as Figure 2:

Figure 2 - Using the pattern for data and analysis dissemination. Figures in a manuscript originate from analysis code, which should be easily reproducible for outside audiences. A set of three interrelated files stored in a public repository makes this sharing accessible: the data file, a loading script, and an analysis script.