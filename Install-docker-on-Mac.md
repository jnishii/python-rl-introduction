# Docker + Jupyter notebook 環境の構築 (Mac OSの場合)

各自のノートパソコンにDockerをインストールし，Docker上でjupyter notebookを起動します。以下の手順で，各自のノートパソコンにDocker+jupyter環境を構築してください。

## 環境構築(初回のみ)

### 準備: Google Chromeのインストール

ブラウザは**Google Chrome**を使うこと。他のブラウザでは， jupyter notebook
動作に不都合が生じることがある。

- Chromeのダウンロードは[こちら](https://www.google.com/intl/ja_ALL/chrome/)

### Dockerのインストール

1. [Docker Store](https://store.docker.com/editions/community/docker-ce-desktop-mac)から"Docker Desktop for Mac"をダウンロードしてインストールする。この時dockerhubのアカウント作成が必要なので，無料アカウントを作成する(うっかりクレジットカード情報などを入力しないよう気をつけること)
2. Docker Desktopを起動する
3. ターミナルを開く
4. 演習用Dockerイメージをダウンロードする
```
$ docker pull jnishii/docker-gym-ple-nongpu36
```
5. 以下をダウンロードして，docker-run.shという名前にする
```
https://github.com/jnishii/docker-gym-ple-nongpu36/tree/master/bin/docker-run.sh
```
6. 以下を実行していく。以下では， 作業ディレクトリを`~/jupyter`とするが，他の名前でも良い。

```
$ mkdir ~/jupyter
$ cd  ~/jupyter
$ mv ~/Downloads/docker-run.sh .   # docker-run.shのダウンロード先に応じてパス変更
$ chmod 755 docker-run.sh　# 実行権限を付与
```

### 演習用Dockerイメージのダウンロード

ターミナル上で以下を実行
```
$ docker pull jnishii/docker-gym-nongpu36
```
エラーが出る場合は以下の「学内から（proxyあり）の場合」と同様にしてDockerイメージの取得と読み込みを行う。


## [毎回利用時] Dockerを起動し，Jupyter notebookにアクセスする

### Dockerイメージの起動

0. 編集したいファイルがあれば作業用ディレクトリ`~/jupyter`においておく
1. 作業用ディレクトリに移動して以下を実行
```
$ cd  ~/jupyter
$ ./docker-run.sh
```
2. ターミナル上にURLが表示されていることを確認する。(以下の○の部分はいろいろな文字が入る)
```
http://(jupyter or 127.0.0.1):8888/?token=○○○○○○○○○○○○○○○○○○○
```
3. ブラウザで以下にアクセスする。
```
http://localhost:8888/
```
4. ブラウザ上でtokenの入力を求められたら，上記1で確認したURLの`token=`の後ろの部分`○○○......`をコピペして入力する  

作業用ディレクトリ以下はDockerからマウントされるので，Docker側と共有したいファイルはここか，サプディレクトリに置く

### Docker イメージの停止

1. `Ctrl-C`で`docker-run.sh`を終了する
2. dockerが実行中でないか確認する
```
$ docker ps -a
```
もし実行中になっていたら停止する
```
$ docker rm <CONTAINER ID>
```
`<CONTAINER ID>`には，`docker ps -a`で表示されるID(数字)のはじめの3桁のみ入れれば良い。
