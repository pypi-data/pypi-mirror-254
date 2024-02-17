# word-translator-py

A word translator using [WordReference](https://wordreference.com) to retrieve all the information contained in the HTML
document and return the data (encoded or decoded) as object, dict or json.

## Installation

```console
$ pip install word-translator-py
```

## Usage

**Translate a word** as in the following example:

```python
from word_translator_client import *

translation: Translation = retrieve_translation(
    from_lang='es', to_lang='en', word='casa')
print(translation.to_json_encoded())
```

This is a fragment of the output:

```console
{
  "from_lang": "es",
  "to_lang": "en",
  "from_word": "casa",
  "entry_sections": [
    {
      "section_type": "principal_translations",
      "entry_words": [
        {
          "from_word": {
            "from_word": "casa",
            "from_grammar": "nf"
          },
          "tone": "",
          "context": "edificio, vivienda",
          "to_words": [
            {
              "to_word": "house",
              "to_grammar": "n",
              "note": ""
            },
            {
              "to_word": "place",
              "to_grammar": "n",
              "note": "informal"
            }
          ],
          "from_examples": [
            "Todas las casas de este barrio se construyeron según los mismos planos.",
            "Vive en una casa de una sola planta con jardín y piscina."
          ],
          "to_examples": [
            "He lives in a one-story house with a garden and a pool."
          ]
        },
...
```

The **section_type** attribute can be: principal_translations or additional_translations or compound_forms or
phrasal_verbs. The other values are as shown on the website.

## The Translation class structure

```console
Translation
    ├ from_lang
    ├ to_lang
    ├ from_word
    └ entry_sections []
        ├ section_type
        └ entry_words []
            ├ from_word
                ├ from_word
                └ from_grammar
            ├ tone
            ├ context
            ├ to_words []
                ├ to_word
                ├ to_grammar
                └ note
            ├ from_examples []
            └ to_examples []
```

### All identified elements

![All identified elements](https://github.com/softwarelma/word_translator_py/blob/main/wr_entry.jpeg?raw=true)

## All usages

### Retrieving

You can retrieve a translation object this way:

```python
from word_translator_client import *

translation: Translation = retrieve_translation(
    from_lang='es', to_lang='en', word='casa')
```

### Encoded vs decoded

Remember **jardín** is _encoded_ and **jard\u00edn** is _decoded_. The software point of view is applied. Thus, prefer
the encoded way when displaying data to users.

### All the ways of using a translation

1. The default **object** is **encoded**, so in the example above the next sentence:

   `translation.entry_sections[0].entry_words[0].from_examples[1]`

   will give you the following text:

   _Vive en una casa de una sola planta con jardín y piscina._

   See example_1_for_encoded_object().
2. **Decoded object**, the next sentence:

   `to_decoded_translation(translation).entry_sections[0].entry_words[0].from_examples[1]`

   will give you the following text:

   _Vive en una casa de una sola planta con jard\u00edn y piscina._

   See example_2_for_decoded_object().
3. **Encoded dict**, the next sentence:

   `translation.to_dict_encoded()['entry_sections'][0]['entry_words'][0]['from_examples'][1]`

   will give you the following text:

   _Vive en una casa de una sola planta con jardín y piscina._

   See example_3_for_encoded_dict().
4. **Decoded dict**, the next sentence:

   `translation.to_dict_decoded()['entry_sections'][0]['entry_words'][0]['from_examples'][1]`

   will give you the following text:

   _Vive en una casa de una sola planta con jard\u00edn y piscina._

   See example_4_for_decoded_dict().
5. **Encoded json**, the next sentence:

   `translation.to_json_encoded()`

   will give you a text containing the following fragment:

   _"Vive en una casa de una sola planta con jardín y piscina."_

   See example_5_for_encoded_json().
6. **Decoded json**, the next sentence:

   `translation.to_json_decoded()`

   will give you a text containing the following fragment:

   _"Vive en una casa de una sola planta con jard\u00edn y piscina."_

   See example_6_for_decoded_json().
7. **Console table**, the next snippet:

```python
from word_translator_client import *
from translation_as_console_table import retrieve_console_table

translation: Translation = retrieve_translation(from_lang='es', to_lang='en', word='casa')
console_table: str = retrieve_console_table(translation)
```

will give you a text with a formatted table like this:

![Console table](https://github.com/softwarelma/word_translator_py/blob/main/console_table.jpg?raw=true)

See example_7_for_console_table() from module translation_as_console_table.

## Disclaimer

This package was created by reading the HTML documents from [wordreference.com](https://wordreference.com). If you find
some error please
email us at softwarelma@gmail.com or email the author (Guillermo Rodolfo Ellison) at guillermoellison@gmail.com.
