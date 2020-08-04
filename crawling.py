import requests
import re
from bs4 import BeautifulSoup
import openpyxl

webpage = requests.get("https://www.daangn.com/hot_articles")
soup = BeautifulSoup(webpage.content, "html.parser")

def search_function(tag):
    return tag.attr('class') == "card-title"

excel_file = openpyxl.Workbook()
excel_sheet = excel_file.active
excel_sheet.column_dimensions['B'].width = 100

num = 0

excel_sheet.append(['번호','제목'])

for x in range(0,10):
    num += 1
    excel_sheet.append([num,soup.select(".card-region-name")[x].get_text()])

excel_file.save('crawling.xlsx')
excel_file.close()