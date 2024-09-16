import streamlit as st
import pandas as pd
from nltk.lm import Vocabulary

from characters_dashboard import get_large_wikipedia_random_page


page = get_large_wikipedia_random_page()
characters = list(page.content)
lines = page.content.split('\n')
vocabulary = Vocabulary(characters, unk_cutoff=1)
vocabulary_df = pd.DataFrame({'Caractéres': list(vocabulary.counts.keys()),
                              'Frequência': list(vocabulary.counts.values())}).sort_values(by='Frequência',
                                                                                           ascending=False)
sections = []


for line in lines:
    if line.startswith('=='):
        sections.append(line.replace('==', ''))

metrics = {
    'char_count': {
        'metric_name': 'Quantidade de Caractéres',
        'value': len(characters)
    },
    'line_count': {
        'metric_name': 'Número de Linhas',
        'value': len(lines)
    },
    'section_count': {
        'metric_name': 'Número de Seções',
        'value': len(sections)
    }
}

def main():
    st.title(page.title)

    st.write(page.summary)

    st.title('Frequência de Caractéres:')

    st.dataframe(vocabulary_df)

    st.title('Algumas métricas:')

    st.metric(label=metrics['char_count']['metric_name'],
              value=metrics['char_count']['value'])
    
    st.metric(label=metrics['line_count']['metric_name'],
              value=metrics['line_count']['value'])
    
    st.metric(label=metrics['section_count']['metric_name'],
              value=metrics['section_count']['value'])

    st.header('Linhas')
    for line in lines:
        if len(line) > 0:
            st.divider()
            st.write(line)



if __name__ == '__main__':
    main()
