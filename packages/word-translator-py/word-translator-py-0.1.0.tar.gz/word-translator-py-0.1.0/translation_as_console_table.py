from word_translator_client import Translation, EntrySection, EntryWord, ToWord, retrieve_translation


class AllLengths:
    def __init__(self):
        self.section_type: int = 0  # row 1
        self.from_word: int = 0  # row 2
        self.from_grammar: int = 0  # row 2
        self.tone: int = 0  # row 2
        self.context: int = 0  # row 2
        self.to_word: int = 0  # row 2
        self.to_grammar: int = 0  # row 2
        self.note: int = 0  # row 2
        self.from_examples: int = 0  # row 3
        self.to_examples: int = 0  # row 4

    def get_row_len_1(self, sl: str, el: str) -> int:
        return len(sl) + self.section_type + len(el)

    def get_row_len_2(self, nc: str, sl: str, el: str) -> int:
        lnc: int = len(nc)
        return \
            len(sl) + self.from_word + lnc + self.from_grammar + lnc + self.tone + lnc + self.context + lnc + \
            self.to_word + lnc + self.to_grammar + lnc + self.note + len(el)

    def get_row_len_3(self, sl: str, el: str) -> int:
        return len(sl) + self.from_examples + len(el)

    def get_row_len_4(self, sl: str, el: str) -> int:
        return len(sl) + self.to_examples + len(el)

    def get_max_row_len(self, nc: str, sl: str, el: str) -> int:
        return max(
            self.get_row_len_1(sl, el),
            self.get_row_len_2(nc, sl, el),
            self.get_row_len_3(sl, el),
            self.get_row_len_4(sl, el))

    def __str__(self) -> str:
        return str(
            {'section_type': self.section_type, 'from_word': self.from_word, 'from_grammar': self.from_grammar,
             'tone': self.tone, 'context': self.context, 'to_word': self.to_word,
             'to_grammar': self.to_grammar, 'note': self.note, 'from_examples': self.from_examples,
             'to_examples': self.to_examples})


def retrieve_all_lengths(translation: Translation) -> AllLengths:
    all_lenths: AllLengths = AllLengths()
    entry_section: EntrySection
    entry_word: EntryWord
    to_word: ToWord
    from_example: str
    to_example: str
    for entry_section in translation.entry_sections:
        all_lenths.section_type = max(len(entry_section.section_type), all_lenths.section_type)
        for entry_word in entry_section.entry_words:
            all_lenths.from_word = max(len(entry_word.from_word.from_word), all_lenths.from_word)
            all_lenths.from_grammar = max(len(entry_word.from_word.from_grammar), all_lenths.from_grammar)
            all_lenths.tone = max(len(entry_word.tone), all_lenths.tone)
            all_lenths.context = max(len(entry_word.context), all_lenths.context)
            for to_word in entry_word.to_words:
                all_lenths.to_word = max(len(to_word.to_word), all_lenths.to_word)
                all_lenths.to_grammar = max(len(to_word.to_grammar), all_lenths.to_grammar)
                all_lenths.note = max(len(to_word.note), all_lenths.note)
            for from_example in entry_word.from_examples:
                all_lenths.from_examples = max(len(from_example), all_lenths.from_examples)
            for to_example in entry_word.to_examples:
                all_lenths.to_examples = max(len(to_example), all_lenths.to_examples)
    return all_lenths


def get_spaces(s: str, max_len: int) -> str:
    space: str = ''
    for _ in range(max_len - len(s)):
        space += ' '
    return space


def replace_for_col_sep(s: str, col_sep: str, all_lenths: AllLengths) -> str:
    pos_0: int = all_lenths.from_word + 3
    pos_1: int = pos_0 + all_lenths.from_grammar + 3
    pos_2: int = pos_1 + all_lenths.tone + 3
    pos_3: int = pos_2 + all_lenths.context + 3
    pos_4: int = pos_3 + all_lenths.to_word + 3
    pos_5: int = pos_4 + all_lenths.to_grammar + 3
    return \
        s[:pos_0] + col_sep + s[pos_0 + 1:pos_1] + col_sep + s[pos_1 + 1:pos_2] + col_sep + \
        s[pos_2 + 1:pos_3] + col_sep + s[pos_3 + 1:pos_4] + col_sep + s[pos_4 + 1:pos_5] + col_sep + \
        s[pos_5 + 1:]


def retrieve_console_table_to_word(
        console_table: str, entry_from_word: str, entry_from_grammar: str, entry_tone: str, entry_context: str,
        entry_word: EntryWord, all_lenths: AllLengths, sl: str, nc: str, el: str, nl: str
):
    for to_word in entry_word.to_words:
        console_table += entry_from_word
        entry_from_word = sl + '' + get_spaces('', all_lenths.from_word) + nc
        console_table += entry_from_grammar
        entry_from_grammar = '' + get_spaces('', all_lenths.from_grammar) + nc
        console_table += entry_tone
        entry_tone = '' + get_spaces('', all_lenths.tone) + nc
        console_table += entry_context
        entry_context = '' + get_spaces('', all_lenths.context) + nc
        console_table += \
            to_word.to_word + get_spaces(to_word.to_word, all_lenths.to_word) + nc
        console_table += \
            to_word.to_grammar + get_spaces(to_word.to_grammar, all_lenths.to_grammar) + nc
        console_table += \
            to_word.note + get_spaces(to_word.note, all_lenths.note) + el + nl
    return console_table, entry_from_word, entry_from_grammar, entry_tone, entry_context


def retrieve_console_table_2(translation: Translation, all_lenths: AllLengths) -> str:
    nl: str = '\n'
    row_sep = '\u2500'
    col_sep = '\u2502'
    nc: str = f' {col_sep} '
    sl: str = f'{col_sep} '
    el: str = f' {col_sep}'
    t_sep: str = '\u252c'
    inv_t_sep: str = '\u2534'
    max_row_len: int = all_lenths.get_max_row_len(nc, sl, el)
    nr: str = '\u251c' + get_spaces('', max_row_len - 2).replace(' ', row_sep) + '\u2524' + nl
    console_table: str = '\u250c' + nr[1:-2] + '\u2510' + nl
    entry_section: EntrySection
    entry_word: EntryWord
    to_word: ToWord
    from_example: str
    to_example: str
    for section_ind in range(len(translation.entry_sections)):
        entry_section = translation.entry_sections[section_ind]
        console_table += \
            sl + entry_section.section_type + \
            get_spaces(sl + entry_section.section_type + el, max_row_len) + el + nl
        console_table += replace_for_col_sep(nr, t_sep, all_lenths)
        for entry_ind in range(len(entry_section.entry_words)):
            entry_word = entry_section.entry_words[entry_ind]
            entry_from_word: str = \
                sl + entry_word.from_word.from_word + \
                get_spaces(entry_word.from_word.from_word, all_lenths.from_word) + nc
            entry_from_grammar = \
                entry_word.from_word.from_grammar + \
                get_spaces(entry_word.from_word.from_grammar, all_lenths.from_grammar) + nc
            entry_tone = \
                entry_word.tone + \
                get_spaces(entry_word.tone, all_lenths.tone) + nc
            entry_context = \
                entry_word.context + \
                get_spaces(entry_word.context, all_lenths.context) + nc
            console_table, entry_from_word, entry_from_grammar, entry_tone, entry_context = \
                retrieve_console_table_to_word(
                    console_table, entry_from_word, entry_from_grammar, entry_tone, entry_context,
                    entry_word, all_lenths, sl, nc, el, nl)
            console_table += replace_for_col_sep(nr, inv_t_sep, all_lenths)
            for from_example in entry_word.from_examples:
                console_table += sl + from_example + get_spaces(sl + from_example + el, max_row_len) + el + nl
            console_table += nr
            for to_example in entry_word.to_examples:
                console_table += sl + to_example + get_spaces(sl + to_example + el, max_row_len) + el + nl
            last_entry: bool = entry_ind == len(entry_section.entry_words) - 1
            last_section: bool = section_ind == len(translation.entry_sections) - 1
            if last_entry and last_section:
                console_table += '\u2514' + nr[1:-2] + '\u2518' + nl
            elif last_entry:
                console_table += nr
            else:
                console_table += replace_for_col_sep(nr, t_sep, all_lenths)
    return console_table


def retrieve_console_table(translation: Translation) -> str:
    all_lenths: AllLengths = retrieve_all_lengths(translation)
    return retrieve_console_table_2(translation, all_lenths)


def example_7_for_console_table():
    translation: Translation = retrieve_translation(from_lang='en', to_lang='es', word='house')
    console_table: str = retrieve_console_table(translation)
    print(console_table)


def example_8_for_console_table():
    translation: Translation = retrieve_translation(from_lang='en', to_lang='it', word='after')
    console_table: str = retrieve_console_table(translation)
    print(console_table)

# example_7_for_console_table()
# example_8_for_console_table()
