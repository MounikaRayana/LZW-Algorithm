# LZW-Algorithm

Programming language: Python 3.7.4
Compiler version: MSC v.1915 64 bit (AMD64)
Environment: Anaconda prompt
Operating system: Windows
Source code Files: encoder.py and decoder.py

# Input:
This program requires an user input as an ASCII text file, whose name is specified as a command line argument, followed by  the  specified  bit  length  N.

# Encoder logic:
The input data (ASCII text file) is encoded using the encoder.py file.
Initially an ASCII dictionary ranging from 0 to 255 is built using the python dictionary data structure with characters as key and ascii values as value.
Then we apply the lzw compression algorithm.
LZW adaptively builds the dictionary based on the input sequence.
The program outputs the compressed data and stores it in an output file named <inputFileName without extension>+".lzw". 
The encoded output is saved as 2 bytes in the output file.

# Decoder logic:
The encoded output from encoder(compressed data) is decompressed using the decoder.py file,
Initially an ASCII dictionary ranging from 0 to 255 is built using the python dictionary data structure with characters as value and ascii values as key.
Then we apply LZW decompression algorithm.
A dictionary identical to the one created during compression is reconstructed during the decompression process.
The program outputs the decompressed data and stores it in an output file named <inputFileName without extension> + "_decoded.txt"

# How to run the program:
1. Open command prompt.
2. Set the current directory to the folder the file is in.
3. Execute encoder.py file by passing two arguments: 
	python encoder.py <inputFileName.txt> <bit_length>
4. Execute decoder.py file by passing two arguments: 
	python decoder.py <inputFileName.lzw> <bit_length>

# Output:
The compressed file will be stored as <inputFileName>.lzw and the output file will be stored as <inputFileName>_decoded.txt


The program works well for both the examples given on canvas.
The encoder produced the compressed data and stored it in 2 bytes format,
the decoder decoded the compressed data to the original input data again.
