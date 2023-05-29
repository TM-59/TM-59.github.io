
import sys
print(sys.path)
#sys.path.append("C:\\Program Files\\pdfkit")
#print(sys.path)



import pdfkit
from datetime import datetime, timedelta

# URLと保存先のフォルダを指定する
url = 'https://api.jquery.com/category/deprecated/'
save_folder = './pdfs/'

# PDFの設定を指定する
pdf_config = pdfkit.configuration(wkhtmltopdf='path/to/wkhtmltopdf')

# 1日ごとに指定した日時に実行する
#while True:
# 現在の日時を取得する
now = datetime.now()

# PDFを保存するファイル名を作成する
file_name = f'data{now.strftime("%Y%m%d")}.pdf'

# PDFを作成して保存する
pdfkit.from_url(url, save_folder + file_name, configuration=pdf_config)

# 次に実行する日時を指定する（翌日の0時0分0秒）
#next_time = datetime(now.year, now.month, now.day) + timedelta(days=1)

# 次に実行するまで待機する
#sleep_seconds = (next_time - now).total_seconds()
#time.sleep(sleep_seconds)
