# jq_get_refreshToken.py
J-QuantsAPIベータ版を使い、リフレッシュトークンを取得します。

1）動作テストを実行した環境は、os: Centos7.4、python: 3.6.8 です。

２）実行はコマンドプロンプト等からpython環境で起動してください。
    
     起動方法: $ jq_get_refreshToken.py [YOUR_MAIL_ADDRESS] [YOUR_PASSWORD]
     
     リフレッシュトークン保存ファイル名: 'jq_rftoken.json'
     
     データ形式: {"time_rftoken":"YYYY-mm-dd HH:MM:SS.ffffff","refreshToken":"value"}

３）本プログラムは自由にご使用ください。

４）このソフトウェアを使用したことによって生じたすべての障害・損害・不具合等に関して、私と私の関係者および私の所属するいかなる団体・組織とも、一切の責任を負いません。各自の責任においてご使用ください。
