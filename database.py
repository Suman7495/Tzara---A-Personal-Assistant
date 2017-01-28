"""
Creates database to generate sentences.

"""
import os
from Speech import speak
def database():
	path = os.getcwd() + "/Text_Files/corpora.txt"
	f_corpora = open(path,"r")    
	data = []
	nltk_info_path = os.getcwd() + "/Text_Files/nltk_data_path.txt" 
	nltk_info_path_os = nltk_info_path.replace(" ","\ ")
	nltk_info_path_os = nltk_info_path_os.replace("(", "\(")
	nltk_info_path_os = nltk_info_path_os.replace(")", "\)")
	if os.path.isfile(nltk_info_path_os) == False:		#Checks if nltk_data_path.txt exists.
		f_nltk = open (nltk_info_path, "w")
		os.system('find / -iname "nltk_data" 2>/dev/null>'+ nltk_info_path_os)
		if os.stat(nltk_info_path).st_size == 0:
			speak("Please install NTLK. I can't run until then. Goodbye.")
		else:
			f_nltk.close()
		
	f_nltk = open (os.getcwd() + "/Text_Files/nltk_data_path.txt", "r")
	nltk_data_path = f_nltk.readline().strip()
	f_nltk.close()
		
	for name in f_corpora:
		f = open( nltk_data_path + "/corpora/gutenberg/" + name.strip())
		f.seek(0)
		data_temp = f.read()
		data = data + data_temp.split()
		del data_temp
		
	f_corpora.close()
	f.close()
	return data
