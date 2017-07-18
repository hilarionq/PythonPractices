class ZipCompressionStrategy:
    def compress_files(self, files_list):
        for file in files_list:
            print("Zip file Compressing: {}".format(file))

class RarCompressionStrategy:
    def compress_files(self, files_list):
        for file in files_list:
            print("Rar file Compressing: {}".format(file))

class CompressionContext():
    def __init__(self,strategy):
        self.compress = strategy

list_of_files = ["file001.txt", "file002.jpg", "file003.mp3"]
c = CompressionContext(ZipCompressionStrategy().compress_files)
c.compress(list_of_files)


