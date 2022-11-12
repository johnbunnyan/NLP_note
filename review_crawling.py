import requests
from bs4 import BeautifulSoup
import csv
import time



def crawling_factory(csv_name):
    data_set = []

    def scrap_review(page:int):
        URL = f"https://movie.naver.com/movie/point/af/list.naver?&page={page}"
        response = requests.get(URL)

        soup = BeautifulSoup(
        response.text,
        'lxml'
    )

        extract_title = []
        for title in soup.find_all(name='a', attrs={'class':'movie color_b'}):
            extract_title.append(title.text)


        # print(extract_author)
        # print("글쓴이글쓴이글쓴이글쓴이글쓴이글쓴이글쓴이",len(extract_author))


        extract_sentence = []
        sentence = soup.select("table.list_netizen > tbody > tr > td.title br")
        loopCnt = len(sentence)
        for i in range(loopCnt):
            sentenceOne = sentence[i].next_sibling
            after = str(sentenceOne).replace('\t','').replace('\n','')
            extract_sentence.append(after)



        # print(extract_sentence)
        # print("내용내용내용내용내용내용내용내용내용내용",len(extract_sentence))


        extract_rate=[]
        for rate in soup.find_all(name='div', attrs={'class':'list_netizen_score'}):
                rates = rate.select('div > em')[0].text
                extract_rate.append(int(rates))

        # print(extract_rate)
        # print("평점평점평점평점평점평점평점평점평점평점평점",len(extract_rate))

        for i,(a,b,c) in enumerate(zip(extract_title, extract_sentence,extract_rate)):
            if b != '':
                data_set.append([a,b,c])
        

        print(data_set)
        

    # for i in range(1,120):
    #     time.sleep(0.7)
    #     scrap_review(i)
    scrap_review(1)

    with open(f'{csv_name}.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data_set)
    
    return data_set






# csvFile = open('editors.csv', 'wt+')
# writer = csv.writer(csvFile)
# try:
#     for row in rows:
#         csvRow = []
#         for cell in row.findAll(['td','th']):
#             csvRow.append(cell.get_text())
#             writer.writerow(csvRow)
# finally:
#     csvFile.close()











# for tr in trs:
#     tds = tr.select("td")
#     if len(tds) == 3:
#         title = tds[1]
#         movie_title = title.select_one("a.movie").text
#         point = title.select_one("div.list_netizen_score > em").text
#         print(movie_title, point)












# for title in headline.find_all(name='',attrs={'class':'title'}):
#     print(title.string)
