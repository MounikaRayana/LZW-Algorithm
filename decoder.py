#LZW decoder
#Name: Mounika Rayana
#Student ID: 801168148

#importing the required libraries
import sys
import struct
from struct import *

input_file = sys.argv[1]                               #taking the lzw file from the command line
input_file_name=input_file.split(".")[0]               #extracting name of the input file
file1 = open(input_file,"rb")                          #opening the compressed file
input_code=[]                                          #holds the compressed data

# Reading the compressed file
while True:
    input_data = file1.read(2)                         #reading 2 bytes data
    #print(input_data)
    if len(input_data) != 2:
        break
    (compressed_data, ) = unpack('>H', input_data)
    input_code.append(compressed_data)
#print(input_code)

bit_len = sys.argv[2]                           #taking user provided bit length from command line
bit_len = int(bit_len)
max_table_size = pow(2,bit_len)                 #Max Table size is based on the bit length input provided by user
#print("the maximum table size is:",max_table_size)

#building the dictionary to store ascii values
ascii_dict = dict()
ascii_in_number = range(0,256)
for i in ascii_in_number:
    ascii_dict[str(i)] = chr(i)

code=str(input_code[0])
strng=ascii_dict[code]
listchar = []                                 #to hold the decompressed text
print(strng)
listchar.append(strng)
i=1

# performing decompression
# iterating through the codes

while(i<len(input_code)):
    code=str(input_code[i])
    if code not in ascii_dict:
        new_strng=strng+strng[0]
    else:
        new_strng=ascii_dict[code]
    print(new_strng)
    listchar.append(new_strng)
    if len(ascii_dict)<max_table_size:
        ascii_dict[str(len(ascii_dict))]=strng+new_strng[0]
    strng=new_strng
    i=i+1

# storing the decompressed text into a file
text_file = open(input_file_name+"_decoded.txt", "w")
i = 0
while i < len(listchar):
    n = text_file.write(listchar[i]+"")
    i+=1
text_file.close()

file1.close()                         #closing the input lzw file