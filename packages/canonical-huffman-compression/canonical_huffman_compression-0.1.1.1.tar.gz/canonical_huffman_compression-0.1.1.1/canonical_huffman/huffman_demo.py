# -*- coding: utf-8 -*-
"""
Contains a demonstration of how to use huffman_canonical to compress text data and save it to a binary file.
It also demonstrates how to use a fixed dictionary to compress data.
"""
from huffman_compression import HuffmanCoding


with open('dorianGrayCh1.txt', 'r', encoding="utf8") as file_obj:
    text = file_obj.read()
# The class accepts a list of integers as input.
# So we convert text to list of integers corresponding to the unicode values.
data = [ord(char) for char in text]
huff = HuffmanCoding()
huff.compress(data)
huff.save_compressed('example.bin')
# delete huff object and create a new one to show that there is no data leakage.
del huff
huff2 = HuffmanCoding()
huff2.open_compressed('example.bin')
decompressed = huff2.decompress_file()
if data == decompressed:
    print('huffman successful!')
else:
    print('huffman failed!')
    print('data: ', data[0:10])
    print('uncompressed: ', decompressed[0:10])

# Example of how to use a fixed dictionary
# First we need to create the fixed dictionary
huff_fixed = HuffmanCoding()
example_text = "the quick brown fox jumped over the lazy dogs. THE QUICK BROWN FOX JUMPED OVER THE LAZY DOGS!éà@#$%^&*()_+1234567890-=[]\{}|;':,.<>?/`~—\r\n\t\v\f\b\“\'\”\"\’‘"
fixed_data = [ord(char) for char in example_text]
huff_fixed.huff_dict.make_dictionary(fixed_data)
# Then we can compress the data with the fixed dictionary
huff_new = HuffmanCoding()
huff_new.huff_dict.canonical_codes = huff_fixed.huff_dict.canonical_codes
huff_new.compress(data, fixed_dict=True)
compressed_data = huff_new.encoded_text
# For now, it is up to the user to save the encoded binary text to a file as they see fit.
# The data should be much larger than the first example, since the fixed dictionary is not optimized for the data
print('Fixed dict compressed data size: ', len(compressed_data)//8)
