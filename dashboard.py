import streamlit as st

from characters_dashboard import get_large_wikipedia_random_page

page = get_large_wikipedia_random_page()
characters = list(page.content)
lines = page.content.split('\n')
charset = set(characters)
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

    st.write(charset)

    st.metric(label=metrics['char_count']['metric_name'],
              value=metrics['char_count']['value'])
    
    st.metric(label=metrics['line_count']['metric_name'],
              value=metrics['line_count']['value'])
    
    st.metric(label=metrics['section_count']['metric_name'],
              value=metrics['section_count']['value'])

    st.header('Linhas')
    for line in lines:
        st.divider()
        st.write(line)



if __name__ == '__main__':
    main()
