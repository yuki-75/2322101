import requests
from bs4 import BeautifulSoup
import sqlite3

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


# データベースに接続
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()
# テーブルの作成（初回のみ）
create_table_query = '''
CREATE TABLE IF NOT EXISTS temperature_data (
    date TEXT PRIMARY KEY,
    high_temperature TEXT
)
'''
cursor.execute(create_table_query)
# 最高気温データを含むテーブルまたは行を見つけてデータベースに挿入
rows = soup.find_all('tr')
for row in rows:
    cells = row.find_all('td')
    # 列の数を確認
    if len(cells) > 7:
        date = cells[0].get_text().strip()
        high_temp = cells[7].get_text().strip()
        # データベースに挿入
        insert_data_query = 'INSERT OR IGNORE INTO temperature_data VALUES (?, ?)'
        cursor.execute(insert_data_query, (date, high_temp))

# コミットしてクローズ
conn.commit()
conn.close()

# データベースに接続
conn = sqlite3.connect('your_database.db')
cursor = conn.cursor()
# データを取得
select_data_query = 'SELECT * FROM temperature_data'
cursor.execute(select_data_query)
data = cursor.fetchall()
# データを表示
for row in data:
    print(row)
# コミットしてクローズ
conn.commit()
conn.close()
