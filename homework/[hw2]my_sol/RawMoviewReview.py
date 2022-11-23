import csv
from review_crawling import crawling_factory

class RawMoviewReview():
    def __init__(self, file_name:str = "samples") -> None:
        self.__file_name = f'{file_name}.csv'
        self.__csv_set = []

        data_set = crawling_factory(file_name)
        list_to_tuple = []
        for i in range(len(data_set)):
            list_to_tuple.append(tuple(data_set[i]))

        self.__csv_set = list_to_tuple



    @property
    def Indexing(self):
        return self.__csv_set

    @property
    def Length(self):
        data_set_length = len(self.__csv_set)
        return data_set_length

# data = RawMoviewReview('wow')
# print("🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥", data._Review__file_name)
# dataset = data.Indexing
# dataset_len = data.Length 
# print("⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️⭐️",dataset[0])
# print("📖📖📖📖📖📖📖📖📖📖📖📖📖",dataset_len)