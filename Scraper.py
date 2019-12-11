import bs4 as bs
import urllib.request

##To run this program, one must have installed:
##An lxml parser, beautifulsoup4, and Requests packages for Python

##This program accesses dw.com's Nicos Weg German course and
##takes the vocab words from a completed lesson and writes them
##to a text file separated by ":" for import into the Anki flashcard application


print('Enter full website including https here: ','\n')
sauce = urllib.request.urlopen('https://learngerman.dw.com/en/mein-bankkonto/l-38179694/lv').read()
soup = bs.BeautifulSoup(sauce,'lxml')

german_words = []
english_words = []

for line in soup.find_all('div',class_='row vocabulary'):
    german_words.append(line.find('strong').text)

for paragraph in soup.find_all(class_='col-sm-4 col-lg-3 vocabulary-entry'):
    english_words.append(paragraph.get_text(strip=True))


english_words = [s.replace('\xa0','') for s in english_words]

print(english_words)
print(german_words)
