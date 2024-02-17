__author__ = 'Guillermo Rodolfo Ellison'

import json

import requests

CONST_POS2 = "'POS2'"
CONST_TD1 = "<td"
CONST_TD2 = "</td>"
CONST_TO_WRD = "'ToWrd'"
CONST_FR_WRD = "'FrWrd'"


def encode_from_unicode_escape(s: str) -> str:
    while '\\u' in s:
        ind = s.index('\\u')
        s = s[0:ind] + s[ind:ind + 6].encode('utf-8').decode('unicode-escape') + s[ind + 6:]
    return s


def json_dumps(s: str) -> str:
    return json.dumps(s)[1:-1]


class FromWord:
    def __init__(self, from_word: str, from_grammar: str):
        self.from_word: str = from_word
        self.from_grammar: str = from_grammar

    def to_dict_encoded(self) -> dict:
        return {'from_word': self.from_word, 'from_grammar': self.from_grammar}

    def to_dict_decoded(self) -> dict:
        return {'from_word': json_dumps(self.from_word), 'from_grammar': json_dumps(self.from_grammar)}


class ToWord:
    def __init__(self, to_word: str, to_grammar: str, note: str):
        self.to_word: str = to_word
        self.to_grammar: str = to_grammar
        self.note: str = note

    def to_dict_encoded(self) -> dict:
        return {'to_word': self.to_word, 'to_grammar': self.to_grammar, 'note': self.note}

    def to_dict_decoded(self) -> dict:
        return {'to_word': json_dumps(self.to_word), 'to_grammar': json_dumps(self.to_grammar),
                'note': json_dumps(self.note)}


class EntryWord:
    def __init__(self, from_word: FromWord, to_words: [ToWord], tone: str, context: str, from_examples: [str],
                 to_examples: [str]):
        self.from_word: FromWord = from_word
        self.to_words: [ToWord] = to_words
        self.tone: str = tone
        self.context: str = context
        self.from_examples: [str] = from_examples
        self.to_examples: [str] = to_examples

    def to_dict_encoded(self) -> dict:
        to_word: ToWord
        return {
            'from_word': self.from_word.to_dict_encoded(),
            'tone': self.tone,
            'context': self.context,
            'to_words': [to_word.to_dict_encoded() for to_word in self.to_words],
            'from_examples': self.from_examples,
            'to_examples': self.to_examples
        }

    def to_dict_decoded(self) -> dict:
        to_word: ToWord
        return {
            'from_word': self.from_word.to_dict_decoded(),
            'tone': json_dumps(self.tone),
            'context': json_dumps(self.context),
            'to_words': [to_word.to_dict_decoded() for to_word in self.to_words],
            'from_examples': [json_dumps(from_example) for from_example in self.from_examples],
            'to_examples': [json_dumps(to_example) for to_example in self.to_examples]
        }


class EntrySection:
    def __init__(self, section_type: str, entry_words: [EntryWord]):
        self.section_type: str = section_type
        self.entry_words: [EntryWord] = entry_words

    def to_dict_encoded(self) -> dict:
        entry_word: EntryWord
        return {'section_type': self.section_type,
                'entry_words': [entry_word.to_dict_encoded() for entry_word in self.entry_words]}

    def to_dict_decoded(self) -> dict:
        entry_word: EntryWord
        return {'section_type': json_dumps(self.section_type),
                'entry_words': [entry_word.to_dict_decoded() for entry_word in self.entry_words]}


class Translation:
    def __init__(self, from_lang: str, to_lang: str, from_word: str, entry_sections: [EntrySection]):
        self.from_lang: str = from_lang
        self.to_lang: str = to_lang
        self.from_word: str = from_word
        self.entry_sections: [EntrySection] = entry_sections

    def to_dict_encoded(self) -> dict:
        entry_section: EntrySection
        return {
            "from_lang": self.from_lang,
            'to_lang': self.to_lang,
            'from_word': self.from_word,
            'entry_sections': [entry_section.to_dict_encoded() for entry_section in self.entry_sections]
        }

    def to_dict_decoded(self) -> dict:
        entry_section: EntrySection
        return {
            "from_lang": json_dumps(self.from_lang),
            'to_lang': json_dumps(self.to_lang),
            'from_word': json_dumps(self.from_word),
            'entry_sections': [entry_section.to_dict_decoded() for entry_section in self.entry_sections]
        }

    def to_json_decoded(self, indent: None | int | str = 2) -> str:
        return json.dumps(self.to_dict_encoded(), indent=indent)

    def to_json_encoded(self, indent: None | int = 2) -> str:
        return encode_from_unicode_escape(self.to_json_decoded(indent))


def to_decoded_from_word(from_word: FromWord) -> FromWord:
    decoded_from_word: FromWord = FromWord(
        from_word=json_dumps(from_word.from_word),
        from_grammar=json_dumps(from_word.from_grammar)
    )
    return decoded_from_word


def to_decoded_to_word(to_word: ToWord) -> ToWord:
    decoded_to_word: ToWord = ToWord(
        to_word=json_dumps(to_word.to_word),
        to_grammar=json_dumps(to_word.to_grammar),
        note=json_dumps(to_word.note)
    )
    return decoded_to_word


def to_decoded_entry_word(entry_word: EntryWord) -> EntryWord:
    to_word: ToWord
    decoded_entry_word: EntryWord = EntryWord(
        from_word=to_decoded_from_word(entry_word.from_word),
        to_words=[to_decoded_to_word(to_word) for to_word in entry_word.to_words],
        tone=json_dumps(entry_word.tone),
        context=json_dumps(entry_word.context),
        from_examples=[json_dumps(from_example) for from_example in entry_word.from_examples],
        to_examples=[json_dumps(to_example) for to_example in entry_word.to_examples]
    )
    return decoded_entry_word


def to_decoded_entry_section(entry_section: EntrySection) -> EntrySection:
    entry_word: EntryWord
    decoded_entry_section: EntrySection = EntrySection(
        section_type=json_dumps(entry_section.section_type),
        entry_words=[to_decoded_entry_word(entry_word) for entry_word in entry_section.entry_words]
    )
    return decoded_entry_section


def to_decoded_translation(translation: Translation) -> Translation:
    entry_section: EntrySection
    decoded_translation: Translation = Translation(
        from_lang=json_dumps(translation.from_lang),
        to_lang=json_dumps(translation.to_lang),
        from_word=json_dumps(translation.from_word),
        entry_sections=[to_decoded_entry_section(entry_section) for entry_section in translation.entry_sections]
    )
    return decoded_translation


def next_attribute(attribute: str, html_classes: str, quote: str):
    target = f'{attribute}={quote}'
    if target not in html_classes:
        return None, None
    ind0 = html_classes.index(target)
    html_classes = html_classes[ind0 + len(target):]
    ind1 = html_classes.index(quote)
    next_cl = html_classes[:ind1]
    html_classes = html_classes[ind1 + 1:]
    return html_classes, next_cl


def next_class(html_classes: str, quote: str):
    return next_attribute('class', html_classes, quote)


def next_data_ph(html_classes: str, quote: str):
    return next_attribute('data-ph', html_classes, quote)


def find_classes_2(html_classes: str, quote: str) -> [str]:
    classes: [str] = []
    html_classes, next_cl = next_class(html_classes, quote)
    while html_classes:
        classes.append(next_cl)
        html_classes, next_cl = next_class(html_classes, quote)
    if next_cl:
        classes.append(next_cl)
    return classes


def find_data_phs_2(html_classes: str, quote: str) -> [str]:
    data_phs: [str] = []
    html_classes, next_cl = next_data_ph(html_classes, quote)
    while html_classes:
        data_phs.append(next_cl)
        html_classes, next_cl = next_data_ph(html_classes, quote)
    if next_cl:
        data_phs.append(next_cl)
    return data_phs


def find_classes(html_classes: str) -> [str]:
    classes: [str] = find_classes_2(html_classes, '"')
    classes.extend(find_classes_2(html_classes, "'"))
    return classes


def find_data_phs(html_classes: str) -> [str]:
    data_phs: [str] = find_data_phs_2(html_classes, '"')
    data_phs.extend(find_data_phs_2(html_classes, "'"))
    return data_phs


def next_tag_content(html: str):
    ind0 = html.index('>') if '>' in html else -1
    if ind0 == -1:
        return None, None, None, None
    html_classes = html[:ind0]
    classes: [str] = find_classes(html_classes)
    data_phs: [str] = find_data_phs(html_classes)
    html = html[ind0 + 1:]
    ind1 = html.index('<') if '<' in html else -1
    if ind1 == -1:
        return None, classes, data_phs, None
    content = html[:ind1].strip()
    content = None if len(content) == 0 else content
    html = html[ind1 + 1:]
    return html, classes, data_phs, content


def clean_a_tag_once(html: str, start: int):
    start_ori = start
    done = False
    if '<a ' not in html[start:]:
        return done, html, start
    ind0 = html.index('<a ', start)
    ind1 = html[ind0:].index('>') + ind0
    start = ind1 + 1
    done = True
    if not html[ind1:].startswith('></a>'):
        return done, html, start
    html = html[:ind0] + html[ind1 + 5:]
    return done, html, start_ori


def clean_a_tag_all(html: str) -> str:
    start = 0
    done, html, start = clean_a_tag_once(html, start)
    while done:
        done, html, start = clean_a_tag_once(html, start)
    return html


def clean_tag_once(html: str, start: int, end: int):
    target0 = "<"
    target1 = ">"
    done = False
    if target0 not in html[start:end]:
        return done, html, start, end
    ind0 = html.index(target0, start, end)
    if target1 not in html[ind0:end]:
        return done, html, start, end
    ind1 = html[ind0:end].index(target1) + ind0
    if ind0 > ind1:
        return done, html, start, end
    done = True
    html = html[:ind0] + html[ind1 + 1:]
    end -= (ind1 + 1 - ind0)
    return done, html, start, end


def clean_tag_all(html: str, start: int, end: int):
    done, html, start, end = clean_tag_once(html, start, end)
    while done:
        done, html, start, end = clean_tag_once(html, start, end)
    return html


def clean_multi_target_once(html: str, start: int, target0: str, target1: str, target2: str,
                            include_targets: bool = False):
    done = False
    if target0 not in html[start:]:
        return done, html, start
    done = True
    ind0 = html.index(target0, start)
    start = ind0 if include_targets else ind0 + len(target0)
    if target1 not in html[start:]:
        return done, html, start
    ind1 = html[start:].index(target1) + start
    if target2 not in html[start:]:
        return done, html, start
    ind2 = html[start:].index(target2) + start
    if ind1 > ind2:
        return done, html, start
    end = ind1 + len(target1) if include_targets else ind1
    html = clean_tag_all(html, start, end)
    return done, html, start


def find_new_start(html: str, start: int, target0: str, target1: str) -> int:
    if target0 not in html[start:]:
        return -1
    ind0 = html.index(target0, start)
    start = ind0 + len(target0)
    if target1 not in html[start:]:
        return -1
    ind1 = html[start:].index(target1) + start
    start = ind1 + len(target1)
    return start


def clean_context_once_old(html: str, start: int):
    start = find_new_start(html, start, CONST_POS2, CONST_TD2)
    if start < 0:
        return False, html, start
    return clean_multi_target_once(html, start, CONST_TD1, CONST_TD2, CONST_TD1)


def clean_context_once_new(html: str, start: int):
    return clean_multi_target_once(html, start, '<span title=', '</span>', CONST_TD2, True)


def clean_to_wrd_once(html: str, start: int):
    return clean_multi_target_once(html, start, CONST_TO_WRD, CONST_POS2, CONST_TD2)


def clean_fr_wrd_once(html: str, start: int):
    return clean_multi_target_once(html, start, CONST_FR_WRD, CONST_POS2, CONST_TD2)


# deprecated
def clean_context_all_old(html: str) -> str:
    start = 0
    done, html, start = clean_context_once_old(html, start)
    while done:
        done, html, start = clean_context_once_old(html, start)
    return html


def clean_context_all_new(html: str) -> str:
    start = 0
    done, html, start = clean_context_once_new(html, start)
    while done:
        done, html, start = clean_context_once_new(html, start)
    return html


def clean_to_wrd_all(html: str) -> str:
    start = 0
    done, html, start = clean_to_wrd_once(html, start)
    while done:
        done, html, start = clean_to_wrd_once(html, start)
    return html


def clean_fr_wrd_all(html: str) -> str:
    start = 0
    done, html, start = clean_fr_wrd_once(html, start)
    while done:
        done, html, start = clean_fr_wrd_once(html, start)
    return html


def clean_html(html: str) -> str:
    # GENERAL CLEAINING
    html = html + ' '
    html = html.replace('  ', ' ').replace('  ', ' ').replace('&nbsp;', '')
    html = html.replace('<strong>', '').replace('</strong>', '')
    html = html.replace('<STRONG>', '').replace('</STRONG>', '')
    html = html.replace('<TD', CONST_TD1).replace('</TD>', CONST_TD2)
    html = html.replace(' =', '=').replace('= ', '=')
    html = html.replace('⇒', '')
    html = html.replace('ⓘ', '')
    html = html.replace('"FrWrd"', CONST_FR_WRD)
    html = html.replace('"ToWrd"', CONST_TO_WRD)
    html = html.replace('"POS2"', CONST_POS2)
    html = html.replace('"articleWRD"', "'articleWRD'")
    html = html.replace('id="collinsdiv"', "id='collinsdiv'")
    # FROM Principal Translations
    ind_begin = html.index("'articleWRD'")
    html = html[ind_begin:]
    # TO <div id='collinsdiv'
    html = html[:html.index("id='collinsdiv'")]
    # REMOVE VOID A HREF
    html = clean_a_tag_all(html)
    # REMOVE INTERNAL FR WRD TAGS
    html = clean_fr_wrd_all(html)
    # REMOVE INTERNAL TO WRD TAGS
    html = clean_to_wrd_all(html)
    # REMOVE INTERNAL CONTEXT TAGS
    html = clean_context_all_new(html)
    # POST GENERAL CLEAINING
    html = html.replace(' , ', ', ')
    return html


def retrieve_translation_new_work(from_lang: str, to_lang: str, word: str, print_html: bool, print_meta: bool,
                                  print_data: bool) -> dict:
    work: dict = {
        'print_html': print_html,
        'print_meta': print_meta,
        'print_data': print_data,
        'section_type': '',
        'from_word': '',
        'from_grammar': '',
        'from_grammar_found': False,
        'to_word': '',
        'to_grammar': '',
        'tone': '',
        'context': '',
        'note': '',
        'from_example': '',
        'to_example': '',
        'last_recognized': '',
        'penultimate_recognized': '',
        'content': None,
        'classes': None,
        'data_phs': None,
        'classes_prev': [],
        'html': requests.get(f"https://www.wordreference.com/{from_lang}{to_lang}/{word}").text
    }
    if print_html:
        print(work['html'])
    return work


def retrieve_translation_pre_writing(translation: Translation, work: dict):
    if work['to_example'] and work['last_recognized'] == 'to_example' and len(work['classes_prev']) > 0:
        if work['print_data']:
            print(f"    to_example={work['to_example']}")
        entry_word: EntryWord = translation.entry_sections[-1].entry_words[-1]
        entry_word.to_examples.append(work['to_example'])
        work['to_example'] = ''
        work['classes_prev'] = []


def retrieve_translation_reading_1(work: dict):
    if 'wrtopsection' in work['classes_prev'] and 'sMainMeanings' in work['data_phs']:
        work['section_type'] = 'principal_translations'
    elif 'wrtopsection' in work['classes_prev'] and 'sAddTrans' in work['data_phs']:
        work['section_type'] = 'additional_translations'
    elif 'wrtopsection' in work['classes_prev'] and 'sCmpdForms' in work['data_phs']:
        work['section_type'] = 'compound_forms'
    elif 'wrtopsection' in work['classes_prev'] and 'sPhrasalVerbs' in work['data_phs']:
        work['section_type'] = 'phrasal_verbs'
    else:
        return
    work['penultimate_recognized'] = work['last_recognized']
    work['last_recognized'] = 'section_type'


def retrieve_translation_reading_2(work: dict) -> bool:
    if 'FrWrd' in work['classes_prev'] and 'ph' not in work['classes_prev']:
        work['from_word'] = work['content']
        work['to_word'] = ''
        work['penultimate_recognized'] = 'to_example'
        work['last_recognized'] = 'from_word'
        return True
    elif 'ToWrd' in work['classes_prev'] and 'ph' not in work['classes_prev']:
        work['from_word'] = ''
        work['to_word'] = work['content']
        work['penultimate_recognized'] = work['last_recognized']
        work['last_recognized'] = 'to_word'
        return True
    elif 'FrEx' in work['classes_prev']:
        work['from_example'] = work['content']
        work['penultimate_recognized'] = work['last_recognized']
        work['last_recognized'] = 'from_example'
        return True
    return False


def is_from_grammar_reading(work: dict) -> bool:
    return 'POS2' in work['classes_prev'] and work['from_word']


def is_content_or_from_grammar_reading(work: dict) -> bool:
    return work['content'] or is_from_grammar_reading(work)


def retrieve_translation_reading_3_a(work: dict) -> bool:
    if 'Fr2' in work['classes_prev'] and len(work['classes_prev']) == 1:
        work['tone'] = work['content']
        work['penultimate_recognized'] = work['last_recognized']
        work['last_recognized'] = 'tone'
        return True
    elif is_from_grammar_reading(work):
        work['from_grammar'] = work['content']
        work['from_grammar'] = '' if work['from_grammar'] is None else work['from_grammar']
        work['from_grammar_found'] = True
        work['penultimate_recognized'] = work['last_recognized']
        work['last_recognized'] = 'from_grammar'
        return True
    elif 'POS2' in work['classes_prev'] and work['to_word']:
        work['to_grammar'] = work['content']
        work['penultimate_recognized'] = work['last_recognized']
        work['last_recognized'] = 'to_grammar'
        return True
    elif 'dsense' in work['classes_prev']:
        work['note'] = work['content']
        work['penultimate_recognized'] = work['last_recognized']
        work['last_recognized'] = 'note'
        return True
    return False


def retrieve_translation_reading_3_b(work: dict):
    if work['note'] and len(work['classes_prev']) == 0:
        work['note'] += work['content']
        work['penultimate_recognized'] = work['last_recognized']
        work['last_recognized'] = 'note'
    elif work['from_word'] and len(work['classes_prev']) == 0:
        work['from_word'] += ' ' + work['content']
        work['penultimate_recognized'] = work['last_recognized']
        work['last_recognized'] = 'from_word'
    elif (work['last_recognized'] == 'from_grammar' and work['penultimate_recognized'] == 'from_word' or
          work['last_recognized'] == 'tone' and work['penultimate_recognized'] == 'from_grammar') \
            and len(work['classes_prev']) == 0:
        work['context'] = work['content']
        if work['context'][:1] != '(' and '(' in work['context'] and work['context'][-1:] == ')':
            work['tone'] = work['context'][:work['context'].index('(')].strip()
            work['context'] = work['context'][work['context'].index('('):]
        if ')(' in work['context'] and work['context'][:1] == '(' and work['context'][-1:] == ')':
            work['note'] = work['context'][work['context'].index(')(') + 1:]
            work['context'] = work['context'][:work['context'].index(')(') + 1]
        work['penultimate_recognized'] = work['last_recognized']
        work['last_recognized'] = 'context'


def retrieve_translation_reading_3(work: dict):
    if not retrieve_translation_reading_3_a(work):
        retrieve_translation_reading_3_b(work)


def retrieve_translation_reading(work: dict) -> bool:
    retrieve_translation_reading_1(work)
    if retrieve_translation_reading_2(work):
        return True
    if 'ToEx' in work['classes_prev'] and 'tooltip' in work['classes_prev']:
        work['classes_prev'].remove('tooltip')
        # work['classes_prev'] eq []
        work['html'], work['classes'], work['data_phs'], work['content'] = next_tag_content(work['html'])
        return False
    elif 'ToEx' in work['classes_prev']:
        work['to_example'] = work['content']
        work['penultimate_recognized'] = work['last_recognized']
        work['last_recognized'] = 'to_example'
        work['classes_prev'] = []
        work['html'], work['classes'], work['data_phs'], work['content'] = next_tag_content(work['html'])
        return False
    elif work['to_example'] and work['last_recognized'] == 'to_example' and len(work['classes_prev']) == 0:
        work['to_example'] += '' if work['to_example'][-1:] == '(' else ' '
        work['to_example'] += work['content']
        # work['penultimate_recognized'] eq work['last_recognized']
        # work['last_recognized'] eq 'to_example'
        work['classes_prev'] = []
        work['html'], work['classes'], work['data_phs'], work['content'] = next_tag_content(work['html'])
        return False
    retrieve_translation_reading_3(work)
    return True


def retrieve_translation_writing_1(translation: Translation, work: dict):
    if work['section_type']:
        if work['print_data']:
            print(f"    section_type={work['section_type']}")
        entry_section: EntrySection = EntrySection(section_type=work['section_type'], entry_words=[])
        translation.entry_sections.append(entry_section)
        work['section_type'] = ''
    if work['tone']:
        if work['print_data']:
            print(f"    tone={work['tone']}")
        entry_word: EntryWord = translation.entry_sections[-1].entry_words[-1]
        entry_word.tone = work['tone']
        work['tone'] = ''
    if work['context']:
        work['context'] = work['context'][1:-1]
        if work['print_data']:
            print(f"    context={work['context']}")
        entry_word: EntryWord = translation.entry_sections[-1].entry_words[-1]
        entry_word.context = work['context']
        work['context'] = ''
    if work['from_example']:
        if work['print_data']:
            print(f"    from_example={work['from_example']}")
        if not len(translation.entry_sections[-1].entry_words):
            print(f"from_example={work['from_example']}")
        entry_word: EntryWord = translation.entry_sections[-1].entry_words[-1]
        entry_word.from_examples.append(work['from_example'])
        work['from_example'] = ''


def new_entry_word(translation: Translation, work: dict):
    from_word_2: FromWord = FromWord(from_word=work['from_word'], from_grammar=work['from_grammar'])
    entry_word: EntryWord = EntryWord(from_word=from_word_2, to_words=[], tone='', context='',
                                      from_examples=[], to_examples=[])
    translation.entry_sections[-1].entry_words.append(entry_word)
    work['from_word'] = ''
    work['from_grammar'] = ''
    work['from_grammar_found'] = False


def retrieve_translation_writing_2(translation: Translation, work: dict):
    if work['from_grammar_found'] and work['from_word']:
        if work['print_data']:
            print(f"    from_word={work['from_word']}")
            print(f"    from_grammar={work['from_grammar']}")
        new_entry_word(translation, work)
    if work['to_grammar'] and work['to_word']:
        if work['note']:
            work['note'] = work['note'][1:-1]
        if work['print_data']:
            if work['note']:
                print(f"    note={work['note']}")
            print(f"    to_word={work['to_word']}")
            print(f"    to_grammar={work['to_grammar']}")
        last_entry_section: EntrySection = translation.entry_sections[-1]
        entry_word: EntryWord = last_entry_section.entry_words[-1]
        to_word_2: ToWord = ToWord(to_word=work['to_word'], to_grammar=work['to_grammar'], note=work['note'])
        entry_word.to_words.append(to_word_2)
        work['to_word'] = ''
        work['to_grammar'] = ''
        work['note'] = ''
    work['classes_prev'] = []


def retrieve_translation_writing(translation: Translation, work: dict):
    retrieve_translation_writing_1(translation, work)
    retrieve_translation_writing_2(translation, work)


def retrieve_translation(from_lang: str, to_lang: str, word: str, print_html: bool = False, print_meta: bool = False,
                         print_data: bool = False) -> Translation:
    translation: Translation = Translation(from_lang=from_lang, to_lang=to_lang, from_word=word, entry_sections=[])
    work: dict = retrieve_translation_new_work(from_lang, to_lang, word, print_html, print_meta, print_data)
    work['html'] = clean_html(work['html'])
    work['html'], work['classes'], work['data_phs'], work['content'] = next_tag_content(work['html'])
    while work['html']:
        retrieve_translation_pre_writing(translation, work)
        if len(work['classes']) > 0:
            work['classes_prev'].extend(work['classes'])
        if is_content_or_from_grammar_reading(work):
            if print_meta:
                print(f"""classes_prev="{work['classes_prev']}" """)
                print(f"""data_phs="{work['data_phs']}" """)
                print(f"""content="{work['content']}" """)
            if not retrieve_translation_reading(work):
                continue
            retrieve_translation_writing(translation, work)
        work['html'], work['classes'], work['data_phs'], work['content'] = next_tag_content(work['html'])
    if work['classes'] and len(work['classes']) > 0:
        work['classes_prev'].extend(work['classes'])
    if work['content'] and print_meta:
        print(f"""classes_prev_last="{work['classes_prev']}" """)
        print(f"""data_phs_last="{work['data_phs']}" """)
        print(f"""content_last="{work['content']}" """)
    return translation


def example_1_for_encoded_object():
    translation: Translation = retrieve_translation(from_lang='es', to_lang='en', word='casa')
    print(translation.entry_sections[0].entry_words[0].from_examples[1])
    # will give you the following text: Vive en una casa de una sola planta con jardín y piscina.


def example_2_for_decoded_object():
    translation: Translation = retrieve_translation(from_lang='es', to_lang='en', word='casa')
    print(to_decoded_translation(translation).entry_sections[0].entry_words[0].from_examples[1])
    # will give you the following text: Vive en una casa de una sola planta con jard\u00edn y piscina.


def example_3_for_encoded_dict():
    translation: Translation = retrieve_translation(from_lang='es', to_lang='en', word='casa')
    print(translation.to_dict_encoded()['entry_sections'][0]['entry_words'][0]['from_examples'][1])
    # will give you the following text: Vive en una casa de una sola planta con jardín y piscina.


def example_4_for_decoded_dict():
    translation: Translation = retrieve_translation(from_lang='es', to_lang='en', word='casa')
    print(translation.to_dict_decoded()['entry_sections'][0]['entry_words'][0]['from_examples'][1])
    # will give you the following text: Vive en una casa de una sola planta con jard\u00edn y piscina.


def example_5_for_encoded_json():
    translation: Translation = retrieve_translation(from_lang='es', to_lang='en', word='casa')
    print(translation.to_json_encoded())
    # will give you a text containing the following fragment: "Vive en una casa de una sola planta con jardín y piscina."


def example_6_for_decoded_json():
    translation: Translation = retrieve_translation(from_lang='es', to_lang='en', word='casa')
    print(translation.to_json_decoded())
    # will give you a text containing the following fragment: "Vive en una casa de una sola planta con jard\u00edn y piscina."

# example_5_for_encoded_json()
