#This program will return a cleaned up file that is ready for transcription.
#Change the path name for the captions document to where you've downloaded
#the .sbv file. Change the outpath variable to where you want the new file
#to be outputted (this can be the same). Also, specify the path where you
#have stored the list with stopwords. This list will be used to remove all
#words that are better left out of transcription. 


import re
print ('\n**Welcome to the Youtube file converter. If you want to quit this program at any point, just type \'quit\'**\n')
inpath = 'C:\Users\s1665892\Downloads\captions.sbv'
outpath = 'C:\Users\s1665892\Desktop\captions2.sbv'
with open('C:\Python27\scripts_arjen\stopwords.txt') as f:
        stopwords = list(f.read().split())
        print(stopwords)

def transform():
	#inpath = input ('>>Please enter input file path and name:')		
	#outpath = input ('>>Please specify the output file (either created new or an existing file):') 
				
	with open(inpath, 'r') as myfile:
		data = myfile.read().replace('\n', '')

	data2 = re.sub(r'[01]:..:......,.:..:......', ' ', data)

	with open(inpath, 'w+') as outfile:
		outfile.write(data2)

def delswords():
        with open(inpath, 'r') as myfile:
                data4 = myfile.read()
                print(data4)
        for i in stopwords:
                print (i)
                data4 = re.sub(i, '', data4)
        with open(inpath, 'w+') as outfile:
                outfile.write(data4)

def delrwords():
        with open(inpath, 'r') as f:
                data3 = list(f.read().split())

        # collect indices of repeated words and phrases
        d = []
        for i in range(len(data3)-3):
                if data3[i] == data3[i+1]:
                        print (data3[i], data3[i+1])
                        d.append(i)
                elif data3[i] + data3[i+1] == data3[i+2] + data3[i+3]:
                        print(data3[i], data3[i+1], data3[i+2], data3[i+3])
                        d.append(i)
                        d.append(i + 1)
        print(d)

        # print new list
        e = []
        for i in range(len(data3)):
                if i in d:
                        pass
                else: 
                      e.append(data3[i])
        data3  = ' '.join(e)

        with open(outpath, 'w') as outfile:
                outfile.write(data3)
        
transform()
delswords()
delrwords()
