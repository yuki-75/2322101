import pandas as pd
import sqlite3

# CSVファイルのパスを指定
csv_file_path = '/Users/yukishibasaki/Downloads/walk.csv'

# CSVファイルを読み込む
df = pd.read_csv(csv_file_path)

# データベースファイルのパス
db_file_path = 'walk1_data.db'

# SQLiteデータベースへの接続
conn = sqlite3.connect(db_file_path)

# データフレームをデータベースのテーブルとして保存
df.to_sql('walk_data', conn, if_exists='replace', index=False)

# データベースの接続を閉じる
conn.close()

# 確認のため、データベースからデータを読み込んで表示
conn = sqlite3.connect(db_file_path)
df_from_db = pd.read_sql('SELECT * FROM walk_data', conn)
conn.close()
df_from_db.head()  # データベースから読み込んだデータの最初の5行を表示
