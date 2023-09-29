import spacy
import pandas as pd
import re


def check_message(message):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(message)
    patern = [{'LIKE_URL' : True}]
    from spacy.matcher import Matcher

    matcher = Matcher(nlp.vocab)
    matcher.add('Tester', [patern])

    index_matches = matcher(doc)
    found_matches = list()
    for match_id, start, end in index_matches:
        url_text = doc[start:end].text
        found_matches.append(url_text)
    # patern =  r'\w{4,100}.\w{2,4}'
    # patern2 = r'\w+\.com'
    # pt = r'(?!https://)[^\s]+'
    pt_bun = r'https://[^\s]+'
    good_list = []
    for t in found_matches:
        match = re.search(pt_bun, t)
        if match:

            good_list.append(t)
            print("Avem protocol https://")
        else:
            t = 'https://' + t
            good_list.append(t)

    print(good_list)
    return good_list


def make_df(lista_coloane):

    df = pd.DataFrame(columns=lista_coloane)
    print(f'Coloanele sunt: {lista_coloane}')
    return df
