#LZW encoder
#Name: Mounika Rayana
#Student ID: 801168148

#importing the required libraries
import sys
import struct
from struct import *

input_file = sys.argv[1]                          #taking the input file from the command line
file1 = open(input_file,"r")                      #opening the file

input_string = file1.read()                       #reading the input file and storing it in a variable
input_file_name=input_file.split(".")[0]          #extracting name of the input file

bit_len = sys.argv[2]                             #taking user provided bit length from command line
bit_len = int(bit_len)
max_table_size = pow(2,bit_len)                   #Max Table size is based on the bit length input provided by user

#building the dictionary to store ascii values
ascii_dict = dict()
ascii_in_number = range(0,256)
for i in ascii_in_number:
    ascii_dict[chr(i)] = str(i)

strng=""                                         #Initially string is NULL
i=0                                               
listnum = []                                     #holds the compressed data

#performing compression
#iterating through the input symbols
while(i<=len(input_string)-1):
    symbol=input_string[i]
    temp=strng+symbol
    #print(temp)
    if temp in ascii_dict:
        strng=strng+symbol
    else:
        print(ascii_dict[strng])
        listnum.append(ascii_dict[strng])
        if len(ascii_dict)<max_table_size:                 #checking whether dictionary size is less than maxsize
            ascii_dict[temp]=str(len(ascii_dict))
        strng=symbol 
    i=i+1
listnum.append(ascii_dict[strng])
print(ascii_dict[strng])

# storing the compressed text into a file in byte-wise format
output_text_file = open(input_file_name+".lzw", "wb")
for data in listnum:
	output_text_file.write(pack('>H',int(data)))
output_text_file.close()

#print(ascii_dict)
file1.close()                                        #closing the input text file