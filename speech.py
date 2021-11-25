import speech_recognition as sr
import webbrowser as w
import pandas as pd

data = pd.read_csv(r"C:\Users\shubh\Downloads\bird.csv.csv")
data.head()
r = sr.Recognizer()
i = 0

with sr.Microphone() as source:
    while (i == 0):
        print('Say Something')
        audio = r.listen(source)
        query = r.recognize_google(audio)
        print(query)
        if (query == '10'):
            w.open('https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Z%C3%A9ro.svg/1200px-Z%C3%A9ro.svg.png')
            i = 1
        elif (query == '11'):
            w.open('https://upload.wikimedia.org/wikipedia/commons/thumb/0/08/Un1.svg/1200px-Un1.svg.png')
        elif (query == '12'):
            w.open('https://upload.wikimedia.org/wikipedia/commons/7/75/Logo_TVE-2.svg')
        elif (query == '13'):
            w.open(
                'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Bundesstra%C3%9Fe_3_number.svg/1200px-Bundesstra%C3%9Fe_3_number.svg.png')
        elif (query == '14'):
            w.open('https://upload.wikimedia.org/wikipedia/commons/c/c2/Red_sox_retired_4.png')
        elif (query == '15'):
            w.open(
                'https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/France_5_2018.svg/1200px-France_5_2018.svg.png')
        elif (query == '16'):
            w.open('https://upload.wikimedia.org/wikipedia/commons/6/6f/Paris_transit_icons_-_M%C3%A9tro_6.svg')
        elif (query == '17'):
            w.open('https://upload.wikimedia.org/wikipedia/en/2/21/BTS_-_Map_of_the_Soul_7.png')
        elif (query == '18'):
            w.open('https://upload.wikimedia.org/wikipedia/commons/c/cb/8NumberEightInCircle.png')
        elif (query == '19'):
            w.open(
                'https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/NYCS-bull-trans-9.svg/1200px-NYCS-bull-trans-9.svg.png')
        

    new = query.split()
    print(new)
