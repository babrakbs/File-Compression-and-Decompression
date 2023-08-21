import os
import zlib


def decompress_file(compress_file_path):
    with open(compress_file_path, 'rb') as df:
        string_data = df.read()
        # print(string_data)
        # print(type(string_data))
        # decoded_data=zlib.decompress(base64.b64decode(string_data))
        # compressed_data = bytes(string_data, 'utf-8')
        decompressed_data = zlib.decompress(string_data)
        # original_file = str(decompressed_data, 'utf-8')

    with open("decompressed.txt", 'wb') as f:
        f.write(decompressed_data)
        print(f"Your Original Content will be= {decompressed_data}")
        print(f"\nPath of Decompressed file is= {os.path.abspath('decompressed.txt')}")



# compress_file_path = input(
#     "Enter Compressed File Path (e.g# C:/Users/babrak/Desktop/Projects/File Compression and Decompression/compressed.txt)= ")


# if os.path.exists(compress_file_path):
#     print("Compressed File Exists !")

#     decompress_file(compress_file_path)

# else:
#     print("Compressed file not existed !")
