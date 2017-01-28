"""
Creates database to generate sentences.

"""
import os

def database():
	path = os.getcwd() + "/Text_Files/corpora.txt"
	f_corpora = open(path,"r")     #modify
	data = []
	for name in f_corpora:
		f = open("/path/to/the/file/nltk_data/corpora/gutenberg/" + name.strip())    #modify
		f.seek(0)
		data_temp = f.read()
		data = data + data_temp.split()
		del data_temp
		
	f_corpora.close()
	f.close()
	return data
