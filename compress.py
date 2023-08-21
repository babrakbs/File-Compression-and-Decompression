import zlib
import os


def compress_file(file_path):
    with open(file_path, 'rb') as f:
        contents = f.read()
        # print("Contets=", contents)
        # byte_content = bytes(contents, 'utf-8')
        # print("Byte Contents=", byte_content)
        compressed_data = zlib.compress(contents, 9)
        print("Compressed Data=", compressed_data)

    with open("compressed_data.zlib", 'wb') as cf:
        print("Compressed File Created")
        cf.write(compressed_data)
        print(f"Path of Compressed file is= {os.path.abspath('compressed.zlib')}")


    # De-compression
    # with open("compressed_data.txt", 'r') as dcf:
    #     compressed_content = dcf.read()
    # #     byte_compress = bytes(compressed_content, 'utf-8')
    #     decompressed_data = zlib.decompress(compressed_data)
    #     original_file = str(decompressed_data, 'utf-8')
    #     print(f"Your Original Content will be= {original_file}")


# file_path = input(
#     "Enter File Path (e.g# C:/Users/babrak/Desktop/Projects/raw.txt)= ")

# if os.path.exists(file_path):
#     print("File Existed!")
#     compress_file(file_path)

# else:
#     print("File Not Existed !")


# def compress_data(file_path):
#     with open(file_path, 'r') as f:
#         contents = f.read()
#         print("Read", contents)
#         bytes_contents = bytes(contents, 'utf-8')
#         test = zlib.compress(bytes(file_path, "utf-8"))
#         print("test", test)

#         if bytes_contents == test:
#             print("Equalppppppppppppppppppppppppppppppppppppp")
#             decompressed_data = zlib.decompress(contents)
#             original_file = str(decompressed_data, 'utf-8')
#             print(f"Your Original Content will be= {original_file}")
#         else:
#             bytes_contents = bytes(contents, 'utf-8')
#             print("bytes data", bytes_contents)
#             compressed_data = zlib.compress(bytes_contents, 9)
#             print("compress", compress_data)
#             with open("compressed.txt", 'w') as cf:
#                 print("Compressed File is Created !")
#                 demo = cf.write(str(compressed_data))
#         #         print(demo)
#                 # print(type(demo))
#         # print(os.path.abspath('compressed.txt'))
#         # return os.path.abspath('compressed.txt')

#         # converting to bytes
#         # bytes_contents = bytes(contents, 'utf-8')
#         # print("bytes data", bytes_contents)
#         # compressed_data = zlib.compress(bytes_contents, 9)
#         # if contents==compressed_data:
#         #     decompressed_data = zlib.decompress(compressed_data)
#         #     original_file = str(decompressed_data, 'utf-8')
#         #     print(f"Your Original Content will be= {original_file}")

#         # print(f"Your Compressed data is:{compressed_data}")
#         # else:
#         #     with open("compressed.txt", 'w') as cf:
#         #         print("Compressed File is Created !")
#         #         demo = cf.write(str(compressed_data))
#         #         print(demo)
#                 # print(type(demo))
#         # print(os.path.abspath('compressed.txt'))
#         # return os.path.abspath('compressed.txt')

# # def decompressed_data():
# #         with open(file_path, 'r') as f:
# #             contents = f.read()
# #             decompressed_data = zlib.decompress(compressed_data)
# #             original_file = str(decompressed_data, 'utf-8')
# #             print(f"Your Original Content will be= {original_file}")
