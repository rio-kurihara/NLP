import MeCab

class Tokenize():
    """分かち書き用のクラス

    Args:
        list_black_poc: 除外する品詞リスト
        list_white_poc: 対象の品詞リスト
        stop_words: 除外する単語のリスト(指定しない場合はNoneを渡す)
        path_dict: 辞書を指定(Noneを渡すとMeCabのデフォルト=ipadicになる)
    """

    def __init__(self, list_black_poc=None, list_white_poc=None, stop_words=None, path_dict=None):
        self.list_black_poc = list_black_poc
        self.list_white_poc = list_white_poc
        if stop_words == None:
            self.stop_words = ['']
        else:
            self.stop_words = stop_words
        if not path_dict == None:
            self.m = MeCab.Tagger('-Ochasen -d {}'.format(path_dict))
        else:
            self.m = MeCab.Tagger('-Ochasen')

    def _check_black_poc(self, poc):
        """形態素解析結果の品詞がブラックリスト品詞に含まれていないかcheckする"""
        flg_brack_poc = []
        for brack_poc in self.list_black_poc:
            flg = brack_poc in poc
            flg_brack_poc.append(flg)
        return any(flg_brack_poc)

    def _check_white_poc(self, poc):
        """形態素解析結果の品詞がホワイトリスト品詞に含まれているかcheckする"""
        flg_white_poc = []
        for white_poc in self.list_white_poc:
            flg = poc.startswith(white_poc)
            flg_white_poc.append(flg)
        return any(flg_white_poc)


    def tokenize_text(self, text):
        """textを受け取り、分かち書きして返す"""
        analyzed = self.m.parse(text)
        list_words = []
        for row in analyzed.split('\n'):
            if row.split('\t')[0] == 'EOS':
                break
            else:
                word = row.split('\t')[2]
                poc  = row.split('\t')[3]
                if word in self.stop_words:
                    # stopwordが含まれていればリストに追加せずpass
                    pass
                else:
                    # 対象の品詞のフィルタリング
                    if (self.list_black_poc == None) & (self.list_white_poc == None):
                        list_words.append(word)
                    elif (self.list_black_poc == None) & (not self.list_white_poc == None):
                        # 品詞whitelist 対応
                        if self._check_white_poc(poc):
                            list_words.append(word)
                    elif (self.list_white_poc == None) & (not self.list_black_poc == None):
                         # 品詞blacklist 対応
                        if not self._check_black_poc(poc):
                            list_words.append(word)
                    else:
                        raise ValueError('Please enter either blacklist or white')

        return list_words
