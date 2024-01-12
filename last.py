import requests
from bs4 import BeautifulSoup

# URL設定
url = 'https://www.data.jma.go.jp/stats/etrn/view/daily_s1.php?prec_no=44&block_no=47662&year=2023&month=12&day=&view='

# ウェブサイトからデータを取得
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# 最高気温データを含むテーブルまたは行を見つける
rows = soup.find_all('tr')
for row in rows:
    cells = row.find_all('td')
    # 列の数を確認
    if len(cells) > 7:
        high_temp = cells[7]  
        print(high_temp.get_text())
    else:
        print("この行には3列以上がありません。")
