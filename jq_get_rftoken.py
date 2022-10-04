# -*- coding: utf-8 -*-
# 2022.10.04 coded by yo.
# MIT License
# Python 3.6.8 / centos7.4

import urllib3
import requests
import datetime
import json
import sys
from datetime import datetime as dt


# ---------------------------------------------
# 機能: コマンドライン入力のパラメーターをチェックする。
# 引数1: コマンドライン入力のパラメーター（list型）
# 引数2: 出力ファイル名（string型）
# 返値: なし
# ---------------------------------------------
def func_parse_parameter(list_argv, str_fname_output):
    if len(list_argv) == 3 :
        pass
    elif len(list_argv) == 2 :
        if list_argv[1] == '-h' \
            or list_argv[1] == '--help':
            print(list_argv[0], ' [YOUR_MAIL_ADDRESS] [YOUR_PASSWORD]')
            print('filename_output :', './' + str_fname_output)
            exit()
        else :
            print(list_argv[0], ' [YOUR_MAIL_ADDRESS] [YOUR_PASSWORD]')
            exit()
            
    elif len(list_argv) == 1 or len(list_argv) > 3 :
        print(list_argv[0], ' [YOUR_MAIL_ADDRESS] [YOUR_PASSWORD]')
        exit()

        

# ---------------------------------------------
# 機能 : J-QuantsAPIからリフレッシュトークンを取得する。
# 引数1: J-Quants API接続先URL（string型）
# 引数2: J-Quants登録メールアドレス（string型）
# 引数3: J-Quants登録パスワード（string型）
# 返値 : リフレッシュトークン
# ---------------------------------------------
def func_get_rftoken(api_url, str_mail_address, str_password):
    
    # リフレッシュトークン取得
    data={}
    data["mailaddress"] = str_mail_address
    data["password"] = str_password
    r_post_rftoken = requests.post(api_url, data=json.dumps(data))
    
    return r_post_rftoken



# ---------------------------------------------
# 機能 : 起動したディレクトリでファイルに書き込む。
# 引数1: 出力ファイル名（string型）
# 引数2: 出力文字列（string型）
# 返値 : 無し
# ---------------------------------------------
def func_write_to_file(str_fname_output, str_text):
    try:
        with open(str_fname_output, 'w', encoding = 'utf_8') as fout:
            fout.write(str_text)     

    except IOError as e:
        print('Can not Write!!!')
        print(type(e))



# =============================================

# J-Quants API接続先URL
api_url = "https://api.jpx-jquants.com/v1/token/auth_user"

# 出力ファイル名
str_fname_output = 'jq_rftoken.json'


# コマンドライン引数のチェック
func_parse_parameter(sys.argv, str_fname_output)

# リフレッシュトークンを取得した時刻を取得
time_rftoken = datetime.datetime.now()

# リフレッシュトークンを取得 （有効期限は1週間）
r_post_rftoken = func_get_rftoken(api_url, sys.argv[1], sys.argv[2])
dic_rftoken = json.loads(r_post_rftoken.text)  # 辞書型に変換

if r_post_rftoken.status_code == 200 :
    # 正常にリフレッシュトークンを取得
    str_rftoken = dic_rftoken.get('refreshToken')    # ＩＤトークンのvalueを取得
else :
    # リフレッシュトークンを取得できなかった場合
    print('message :', dic_rftoken.get('message'))
    quit()  # 終了


# 取得時刻とリフレッシュトークンを保存
# データ形式は、{"time_rftoken":"value","refreshToken":"value"}
dic_json = {}
dic_json['time_rftoken'] = str(time_rftoken)
dic_json['refreshToken'] = str_rftoken
str_json=json.dumps(dic_json)
func_write_to_file(str_fname_output, str_json)

print('refresh token saved :', str_fname_output )
print('format =','{"time_rftoken":"YYYY-mm-dd HH:MM:SS.ffffff","refreshToken":"value"}')
print()

# リフレッシュトークンの取得時間を表示
print('time stamp :', time_rftoken)

# リフレッシュトークンの有効期限を表示
expire_span = datetime.timedelta(days=7)
expire_time = time_rftoken + expire_span
print('expiry date:', expire_time)
print('リフレッシュトークンの有効期間は１週間です。')
