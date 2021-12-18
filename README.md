# 507finalproject
This is a repo for SI507 final project
Kaggle API:https://github.com/Kaggle/kaggle-api
Step1-get the kaggle token from the account
Click on the profile picture and then get into the “My Account”,and click on the “Create New API Token” button and download a kaggle.json file.
Step2-install the kaggle API and get the credentials
pip install kaggle
Place the kaggle file in ~/.kaggle/kaggle.json
chmod 600 ~/.kaggle/kaggle.json
export KAGGLE_USERNAME=datadinosaur
export KAGGLE_KEY=xxxxxxxxxxxxxx
Python Packages:pandas,ZipFile,KaggleApi
This project is designed to recommend movies, TV series and TV shows for users. The project will ask users some questions and then recommend the optimal 5 movies, TV series and TV shows.
#data srtucture
I built a tree with two subtrees, imdb and golden globe award.”imdb” represents the
imdb_top_1000.csv and “golden globe award” represents the golden_globe_awards.csv. In
addition, under the “imdb” there are the 3 nodes “genre”, “runtime”, release_year”, and in the
“golden globe award”, there are two nodes: “award category” and “award year”. However this is
a dynamic tree, so users can choose what they all want to watch based on the nodes. And after
users input answers based on those nodes, the list of names of movies, TV shows or TV series
will be input after the answers, meanwhile answers will be inserted after the nodes in the
Recommend Tree. After users get the recommendations, the codes can also create a
recommend_tree.json file to see the detailed structure.
