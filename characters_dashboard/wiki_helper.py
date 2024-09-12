import wikipedia
from wikipedia import DisambiguationError, WikipediaPage


def get_random_wikipedia_page(lang=None, max_retries=None) -> WikipediaPage:
    if not lang: 
        wikipedia.set_lang('pt')
    else: 
        wikipedia.set_lang(lang)

    retries = max_retries if max_retries else 3

    while retries:
        try:
            return wikipedia.page(wikipedia.random())
        except DisambiguationError as e:
            print('Erro de desambiguação. Tentando baixar outra página...')
            retries -=1

def get_large_wikipedia_random_page(min=None) -> WikipediaPage:
    if not min:
        min = 1000
    
    while True:
        page = get_random_wikipedia_page()
        if len(page.content) > min:
            return page
