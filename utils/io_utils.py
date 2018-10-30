import csv
import json
import os
import pickle


def _make_dir(DIR_OUTPUT):
    if not os.path.isdir(DIR_OUTPUT):
        os.makedirs(DIR_OUTPUT)
        print('Create directory :{0}'.format(DIR_OUTPUT))

def save_dict(dict_obj, path):
    """dictオブジェクトを保存する"""
    file = open(path, 'w')
    json.dump(dict_obj, file)
    file.close()

def load_dict(path):
    """辞書ファイルを読み込む"""
    file = open(path, 'r')
    dict_obj = json.load(file)
    file.close()
    return dict_obj

def write_csv(path, data):
    f = open(path, 'w')
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(data)
    f.close()

def read_csv(path, header=False):
    """1次元のデータを読み込む.ヘッダーを飛ばしたければheader=Trueにする"""
    with open(path, 'r') as f:
        lines_list = []
        reader = csv.reader(f)
        if header:
            header = next(reader)
        for row in reader:
            lines_list.append(row)
    return lines_list[0]

def read_txt(path):
    """.txtデータを読み込んでリストで返す"""
    with open(path, 'r') as f:
        data = []
        tmp_data = f.read()
        lines1 = tmp_data.split('\n') # 改行で区切る(改行文字そのものは戻り値のデータには含まれない)
        for line in lines1:
            data.append(line)
    return data


def read_json(path):
    _, ext = os.path.splitext(path)
    if ext == '.json':
        f = open(path, 'r')
        dict_data = json.load(f)
    else:
        raise ValueError("Argument must be '.json' ")
    return dict_data


def save_pickle(obj, fname):
    with open(fname, mode='wb') as f:
        pickle.dump(obj, f)

def load_pickle(fname):
    with open(fname, mode='rb') as f:
        obj = pickle.load(f)
    return obj
