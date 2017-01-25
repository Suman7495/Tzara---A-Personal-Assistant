def database():
	f_corpora=open("/media/suman/New Volume1/Artificial Intelligence/Personal Assistant/Personal Assistant/Text_files/corpora.txt","r")
	data=[]
	for name in f_corpora:
		f=open("/home/suman/nltk_data/corpora/gutenberg/"+ name.strip())
		f.seek(0)
		data_temp=f.read()
		data=data+data_temp.split()
		del data_temp
		
	f_corpora.close()
	f.close()
	return data
