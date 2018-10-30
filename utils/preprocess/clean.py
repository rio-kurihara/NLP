import re
from unicodedata import normalize

def clean_text(text: str, _normalize=True, lower=True, upper=False,
               drop_kigou=u'[「」『』【】★☆]') -> str:
    """
    テキストを受け取り、前処理後のテキストを返す
    引数の順番で処理を行う
    削除したい記号がない場合は'drop_kigou'にNoneを渡す
    """
    # 正規化
    if _normalize:
        text = normalize('NFKC', text)
    # 大文字化と小文字化のどちらかのみ処理する
    if lower & upper:
        raise ValueError('Only either lower or upper should be True')
    # 大文字を小文字化
    if lower:
        text = text.lower()
    # 大文字を小文字化
    if upper:
        text = text.upper()
    # 記号の除去
    if drop_kigou != None:
        kigou = re.compile(drop_kigou)
        text = kigou.sub('', text)
    return text

def check_word(word, stop_word, black_ptrn):
    """単語を受け取り、条件に一致するものはそのまま返し、一致しないものは空文字で返す
    black_ptrn: ex:) u'\d+時|\d+分|'
    """
    p = re.compile(black_ptrn)
    m = p.match(word)

    # 数字のみだった場合
    if word.isdigit():
        return ''
    # ブラックワードが含まれていた場合
    elif not len(m.group()) == 0:
        return ''
    elif word in stop_word:
        return ''
    else:
        return word
