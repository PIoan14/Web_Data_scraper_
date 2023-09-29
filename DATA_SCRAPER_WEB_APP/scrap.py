import re
import requests
from bs4 import BeautifulSoup

#pas 1 scoatem url din csv :


class Net_to_CSV:

    def __init__(self, url):
        self.url = url


    def scrap(self):
       
        try:
            response = requests.get(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')

            page_text = soup.get_text()

            return page_text



        except:
            print(f"Eroare... Cererea HTTP a eșuat.")
            print(self.url)
            return 'None'

    def email_finder(self, data):
        email_p = r'\w{2,20}\d{0,10}@\w{5,7}.\w{2,6}'

        back = re.findall(email_p, data)
        if back != []:
            return back
        else:
            return ['no element']

    # pregatire nlp

    def name_split(self):
        words = []
        word = ''
        for token in self.url:

            if token not in ' \n\n \n\n\n!"#$%&().*+,/:;<=>?@[\\]^_`{|}~\t\n "" ':
                word = word + token

            else:
                #print(word)
                words.append(word)
                word = ''
        #print(words)
        for i in range(0, len(words)):
            if words[i - 1] == 'www' or words[i - 1] == 'https' or words[i-1] == '':
                good_word = words[i]

        return good_word

    def phone_nr_finder(self, data):

        p_nr = r'\d{4}\s\d{3}\s\d{3}'
        p_nr2 = r'\d{10}'
        combined_pattern = f'({p_nr}|{p_nr2})'
        numbers = re.findall(combined_pattern, data)
        if numbers != []:
            return numbers
        else:
            return ['no element']
