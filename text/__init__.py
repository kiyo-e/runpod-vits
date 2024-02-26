from text.symbols import *

_symbol_to_id = {s: i for i, s in enumerate(symbols)}


def cleaned_text_to_sequence(cleaned_text, tones, language):
    """Converts a string of text to a sequence of IDs corresponding to the symbols in the text.
    Args:
      text: string to convert to a sequence
    Returns:
      List of integers corresponding to the symbols in the text
    """
    phones = [_symbol_to_id[symbol] for symbol in cleaned_text]
    tone_start = language_tone_start_map[language]
    tones = [i + tone_start for i in tones]
    lang_id = language_id_map[language]
    lang_ids = [lang_id for i in phones]
    return phones, tones, lang_ids


def get_bert(
    text,
    word2ph,
    language,
    device,
    assist_text=None,
    assist_text_weight=0.7,
    ignore_unknown=False,
):
    if language == "ZH":
        from .chinese_bert import get_bert_feature as zh_bert

        return zh_bert(text, word2ph, device, assist_text, assist_text_weight)
    elif language == "EN":
        from .english_bert_mock import get_bert_feature as en_bert

        return en_bert(text, word2ph, device, assist_text, assist_text_weight)
    elif language == "JP":
        from .japanese_bert import get_bert_feature as jp_bert

        return jp_bert(
            text, word2ph, device, assist_text, assist_text_weight, ignore_unknown
        )
    else:
        raise ValueError(f"Language {language} not supported")
