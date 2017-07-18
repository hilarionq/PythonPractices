class ZipCompressionStrategy:
    def compress_files(self, files_list):
        for file in files_list:
            print("Zip file Compressing: {}".format(file))

class RarCompressionStrategy:
    def compress_files(self, files_list):
        for file in files_list:
            print("Rar file Compressing: {}".format(file))

class CompressionContext:
    def __init__(self, strategy):
        self.strategy = strategy
    
    def create_archive(self, files_list):
        self.strategy.compress_files(files_list)

def compress_archive(strategy, files_list):
    strategy.compress_files(files_list)

list_of_files = ["file001.txt", "file002.jpg", "file003.mp3"]
compress_archive(RarCompressionStrategy(), list_of_files)


