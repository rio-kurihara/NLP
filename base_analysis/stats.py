import collections
import pandas as pd

def word_count(list_words) -> pd.DataFrame:
    """単語の出現回数をカウントする"""
    counter = collections.Counter(list_words)
    df_counter = pd.io.json.json_normalize(counter).T.sort_values(0)[::-1]
    df_counter = df_counter.reset_index()
    df_counter.columns = ['word', 'cnt']
    return df_counter
