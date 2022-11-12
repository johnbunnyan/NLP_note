from RawMoviewReview import RawMoviewReview

print("클래스 시작",RawMoviewReview)

class MovieReview(RawMoviewReview):
    def __init__(self, score_threadhold:int, file_name:str = "samples") -> None:
        # 부모의 생성자 호출해 부모에 저장된 데이터 자식도 메서드로 접근할 수 있게 하기
        super().__init__(file_name)
        # 자식의 생성자 속성 선언
        self.score_threadhold = score_threadhold
        self.file_name = file_name
    



    @property
    def Indexing(self):
        data_set = super().Indexing
        print("⭐️⭐️⭐️⭐️⭐️⭐️⭐️",data_set)
        new_data = []
        for i in range(len(data_set)):
            review_sentence = data_set[i][1].strip()
            review_rate = data_set[i][2]
            if review_rate > self.score_threadhold:
                new_data.append((review_sentence, True))
            else:
                new_data.append((review_sentence, False))
        return new_data


        


data2 = MovieReview(0,'vv')
print("🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥",data2.Indexing)