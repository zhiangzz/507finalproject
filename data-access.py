import os
from zipfile import ZipFile
import pandas as pd
os.environ['KAGGLE_USERNAME'] = 'zhiangzhang'
os.environ['KAGGLE_KEY'] = '572ae72f20507f0945d2ad1f07f20117'
from io import BytesIO
from kaggle.api.kaggle_api_extended import KaggleApi
 
dataset1 = 'harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows'
dataset2 = 'unanimad/golden-globe-awards'
 
api = KaggleApi()
api.authenticate()
 
file1=api.dataset_download_files(dataset1)
file2=api.dataset_download_files(dataset2)
def unzip(file):
    with ZipFile(file, 'r') as zip:
    # printing all the contents of the zip file
        zip.printdir()
    # extracting all the files
        print('Extracting all the files now...')
        zip.extractall()
        print('Done!')

data1=unzip("imdb-dataset-of-top-1000-movies-and-tv-shows.zip")
data2=unzip("golden-globe-awards.zip")

