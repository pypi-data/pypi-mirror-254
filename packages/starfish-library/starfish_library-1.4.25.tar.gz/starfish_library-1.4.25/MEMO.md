参考サイト
https://zenn.dev/sikkim/articles/490f4043230b5a

## ライブラリの反映手順
1. setup.py のバージョンを更新
2. python setup.py sdist
   1. 上記コマンドで配布物のビルド
3. python setup.py bdist_wheel
   1. 上記コマンドでWheelパッケージをビルド
4. twine upload --repository testpypi dist/*
   1. テスト環境にアップロード(依存関係などでエラーが出ないか)
5. twine upload --repository pypi dist/*
   1. 本番環境にアップロード

### メモ
依存関係にあるライブラリは勝手に追加される訳では無いが､
このライブラリを使うときに一括でインストールができるように
requirement を作っておいて上げるほうがいい
エラー文として出るが｡


パッケージに必要なライブラリの書き出し
cd で対象のフォルダに移動
(なければ pip install pipreqs)
pipreqs --encoding UTF8 . --force
で必要なライブラリを書き出してくれる

pipenv にも適応したい場合
pipenv install -r requirements.txt
上記で[requirements.txt]の内容を出力

pipenv graph
で依存関係が表示されるので､大本のライブラリのみ抜き出して記載

セキュリティとイメージのレポジトリ
シークレット [gcp_service_account]
参照の方法 [ボリュームとしてマウント]
マウントパス [secret]
パス1 [gcp_service_account]
バージョン [lastest]

## 作業方針
ローカル環境には[pip]でライブラリを構築
デプロイが必要になったタイミングで､仮想環境化｡必要な項目をインストールしていく｡

## 仮想環境の構築手順
仮想環境の構築とファイルの実行
pipenv shell
python main.py

## ライブラリのインストール方法
pipenv install [name]
pipenv install --dev [name]

## ライブラリの一覧の取得
pipenv run pip freeze

## requirements.txtの作成
pipenv run pip freeze > requirements.txt

## デプロイのコマンド
gcloud functions deploy [name]
gcloud functions deploy [name] --entry-point main --runtime python39 --region us-central1 --trigger-topic [topic_name]
gcloud functions deploy [name] --entry-point main --runtime python39 --region us-central1 --trigger-http

クラウドファンクションの引数
def main(request=None):
def main(event=None, context=None):

## よく使いそうなコマンド
python main.py
pipenv install python-dotenv

## python で サーバーを立てる場合
python -m http.server 8000
http://localhost:8000

## ngrok 使い方
E:\Download_Unzip\ngrok-v3-stable-windows-amd64
から実行ファイルを選択
ngrok http 8000

ローカルホストとポート番号を合わせる必要あり
POST メソッドが使えない

## 
requirements.txt が存在する状況で 【pipenv shell】を実行すると自動的にインストールしてくれる

自作ライブラリのインストール方法
pip install git+ssh://git@github.com/[アカウント名]/[レポジトリ名].git@[バージョンタグ]
pip install git+ssh://git@github.com/starfish-ads/my_library.git@v0.9.8#egg=MyLibrary
pipenv install git+ssh://git@github.com/starfish-ads/my_library.git@v0.9.6#egg=MyLibrary
タグを作成するとその段階でのコードをクローンできる
タグの作成は必須(最新版以外が狂う可能性あり)

もしエラーが出たら､SSHファイルの場所を確認すること

ライブラリの保存場所の確認
pip show mylibrary
今は下記にあるので参考に!
C:\users\kamim\appdata\local\programs\python\python310\lib\site-packages

タグ追加の流れ
git tag -a [tagname]
git tag
git push origin [tagname]

ローカルで自作ライブラリのインストール
ライブラリのディレクトリ直下で下記を実行(setup.pyと同じ階層)
pip install .


explorer 絶対パス 
これでフォルダを開ける


gcloud functions deploy private_get_feedly --entry-point main --runtime python39 --region us-central1 --trigger-topic private_get_feedly

自作ライブラリの更新手順
cd E:\WorkSpace\Library\starfish_library
python common.py
エラーになったライブラリを追加

pipenv graph

インストールされている全ファイルを書き出し
pipenv run pip freeze > requirements.txt

書き出したライブリをすべてインストール
pipenv install -r requirements.txt

最上位のライブラリを[requirements.txt]に記載
pipenv graph

起動する関数にコマンドで移動して､実行ライブラリがないというエラーが出なければ成功