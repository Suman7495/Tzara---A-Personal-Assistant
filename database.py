"""
Creates database to generate sentences.

"""
def database():
	f_corpora = open("/path/to/the/file/corpora.txt","r")     #modify
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
