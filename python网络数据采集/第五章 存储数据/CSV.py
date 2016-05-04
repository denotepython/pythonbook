import csv
from urllib import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bs_boj = BeautifulSoup(html)

table = bs_boj.findAll("table", class_ = "wikitable")[0]
rows = table.findAll("tr")

csvfile = open("../files/editors.csv", 'wt')
writer = csv.writer(csvfile)

try:
	for row in rows:
		csvrow = []
		for cell in row.findAll(['td', 'th']):
			csvrow.append(cell.get_text())
			writer.writerow(csvrow)

finally:
	csvfile.close()