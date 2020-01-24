from bs4 import BeautifulSoup
import requests
import csv

csv_file = open('bible_december.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Book', 'Chapter:Verse', 'Text']) 

books = ['genesis', 'exodus', 'leviticus', 'numbers', 'deuteronomy', 'joshua', 'judges', 'ruth', '1_samuel', '2_samuel', '1_kings', '2_kings', '1_chronicles', '2_chronicles', 'ezra', 'nehemiah', 'esther', 'job', 'psalms', 'proverbs', 'ecclesiastes', 'songs', 'isaiah', 'jeremiah', 'lamentations', 'ezekiel', 'daniel', 'hosea', 'joel', 'amos', 'obadiah', 'jonah', 'micah', 'nahum', 'habakkuk', 'zephaniah', 'haggai', 'zechariah', 'malachi', 'matthew', 'mark', 'luke', 'john', 'acts', 'romans', '1_corinthians', '2_corinthians', 'galatians', 'ephesians', 'philippians', 'colossians', '1_thessalonians', '2_thessalonians', '1_timothy', '2_timothy', 'titus', 'philemon', 'hebrews', 'james', '1_peter', '2_peter', '1_john', '2_john', '3_john', 'jude', 'revelation']

for each in books:

	for i in range(1, 32): 
		source = requests.get('https://biblehub.com/'+each+'/12-'+str(i)+'.htm').text
		soup = BeautifulSoup(source, 'lxml')
		quote = soup.title.text.split(' ')
		book = quote[0]
		verse = quote[1]
		text = ' '.join(quote[2::])
		print(soup.title.text)
		print() 
		csv_writer.writerow([book,verse,text])

csv_file.close()