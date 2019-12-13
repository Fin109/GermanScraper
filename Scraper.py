import bs4 as bs
import urllib.request
import datetime
import tkinter as tk

r = tk.Tk()
r.title('German word exporter')

frame = tk.Frame(r,width = 500,height=500)
frame.pack()
entryBox = tk.Entry(frame)
entryBox.pack()

def makeFileFunction():
    entryBoxString = entryBox.get()
    main(entryBoxString)
    r.destroy()
makeFile = tk.Button(frame,text='Make German Text File',command = makeFileFunction)
makeFile.pack()


##This program accesses dw.com's Nicos Weg German course and
##takes the vocab words from a completed lesson and writes them
##to a text file separated by ":" for import into the Anki flashcard application
##

def main(url):
    d = datetime.datetime.today()
    ##Initialize name of text file output: follows form "GermanWords(currentdatehere)"
    name = 'GermanWords'+str(d.strftime('%d-%m-%Y'))



    #Below input grammar section of end of lesson URL. Ex: https://learngerman.dw.com/en/mein-bankkonto/l-38179694/lv


    sauce = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(sauce,'lxml')

    german_words = []
    english_words = []

    #Searches for all words in 'div' under class "row vocabulary"
    #Looks only for the german words indicated by strong tags, appends the text of these tags to a list
    for line in soup.find_all('div',class_='row vocabulary'):
        german_words.append(line.find('strong').text)

    #Same as above, different class
    for paragraph in soup.find_all(class_='col-sm-4 col-lg-3 vocabulary-entry'):
        english_words.append(paragraph.get_text(strip=True))

    #The above method returns some words with an '\xa0' tag. This removes that
    english_words = [s.replace('\xa0','') for s in english_words]



    #Below outputs to text file in the form:
    #German word - english word
    #new line
    #repeat

    with open(name, "w") as text_file:
        for i in range(len(english_words)):
            text_file.write('{}-{}\n'.format(german_words[i],english_words[i]))
            text_file.write(' ')
r.mainloop()