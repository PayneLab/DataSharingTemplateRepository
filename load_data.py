import pandas as pd

#Data loader functions belong here. This is where
#  information about the data files is found.

def load_example():
    #Each dataset may have its own loader function like this.
    #This function returns a dataframe.
    #First, we identify the file. Small files will be local.
    file="data/example.txt"
    #Then read in the data. This may be more extensive for your project.
    #Here we read in a tab-separated file with headers in the first row
    #    and index names in the first column. 
    df = pd.read_csv(file, sep='\t', header=0, index_col=0)
    #This dataframe is then returned.
    return df