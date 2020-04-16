import pandas as pd
import requests
import os.path
from os import path

#Data loader functions belong here. This is where
#  information about the data files is found.

def load_from_file():
    #Each dataset may have its own loader function like this.
    #This function returns a dataframe.
    #First, we identify the file. Small files will be local.
    file="data/fakeBP.csv"
    #Then read in the data. This may be more extensive for your project.
    #Here we read in a tab-separated file with headers in the first row
    #    and index names in the first column.
    df = pd.read_csv(file, index_col=0)#, sep='\t', header=0, index_col=0)
    #Because the index column is the date, we convert here
    df.index=pd.to_datetime(df.index)
    #This dataframe is then returned.
    return df

#This will load the data by first streaming it from box, then storing it in a pandas datafrtame.
def load_from_box(redownload = False):
    """Download a file from a given url to the specified location.
    Parameters:
    redownload (bool): If True will redownload the datafiles from box
    Returns:
    A pandas dataframe.
    """

    download_to_path="data/datafile.txt" #the path to where the datafile from box will be loaded to
    url_file_path="data/url.txt" #the path to where the download from box url is stored. This is a static url, so the users won't need to change it. 

    if path.exists(download_to_path) and redownload: #If the file has been downloaded, and the user wants to update, redownload the file
        url_file = open(url_file_path, 'r')
        url = url_file.read().strip()
        url_file.close()
        response = requests.get(url, allow_redirects=True)

        with open(download_to_path, 'wb') as dest:
            dest.write(response.content)

    if path.exists(download_to_path) == False: #If the file hasn't been downloaded before download it
        url_file = open(url_file_path, 'r')
        url = url_file.read().strip()
        url_file.close()
        response = requests.get(url, allow_redirects=True)

        with open(download_to_path, 'wb') as dest:
            dest.write(response.content)



    #Load the data into a pandas df
    df = pd.read_csv(download_to_path, index_col=0)
    #Because the index column is the date, we convert here
    df.index=pd.to_datetime(df.index)

    return df
