# Docker + Jupyter notebook 環境の構築 (Windowsの場合)

各自のノートパソコンにDockerをインストールし，Docker上でjupyter notebookを起動します。以下の手順で，各自のノートパソコンにDocker+jupyter環境を構築してください。

## 環境構築(初回のみ)

### 事前確認

MS Windows に Docker Toolboxをインストールするためには以下の条件が必要。最近のパソコンならたいてい大丈夫なはずです。

1. バージョン
    - Windows7以上
    - 64bit
2. CPG仮想化が有効であること
    1. スタートボタンを右クリックして"タスクマネージャ"をクリック
    2. "パフォーマンス" タブをクリック
    3. CPUをクリックし、仮想化が有効であることを確認

### 準備: Google Chromeのインストール

演習ではブラウザに**Google Chrome**を使用する。他のブラウザでは， 演習で必要なプログラム等のインストールや起動に不都合が生じることがあるので， Chromeをインストールしていないヒトは[こちら](https://www.google.com/intl/ja_ALL/chrome/)からダウンロード・インストールすること。

### Docker Toolboxのダウンロード・インストール方法

1. [Docker Toolbox overview](https://docs.docker.com/toolbox/overview/#ready-to-get-started)にアクセス
2. "Get Docker Toolbox for Windows" をクリックして`Docker Toolbox.exe`をダウンロード
3. `Docker Toolbox.exe`を実行してDocker Toolboxをインストール
    - **基本的に何も変更せずにインストールすればよい**
    - "**full installation**"を選択し、Docker , VirtualBox, Gitなどすべてインストールする
    - "**Create a desktop shortcut**"にチェックを入れ、デスクトップに以下のショートカットを作っておくと便利
        - Docker Quickstart Terminal
        - Kitematic (Alpha)
        - Oracle VM VirtualBox
4. **`Docker Quickstart Terminal`を実行して**Dockerターミナル(コマンドプロンプトではない!!)を開き，クジラの絵が出るまで待つ。

**[注意!!] ターミナル起動時のよくあるトラブル**

以下のエラーが出てターミナルを起動できない場合
```
(default) No default Boot2Docker ISO found localy......
```
**解決方法**

`C/Program Files/Docker Toolbox/Boot2Docker.iso`を`C/Users/<ユーザー名>/.docker/machine/cache/`の中にコピーしてもう一度Dockerターミナルを開く。　

### Docker起動のための準備

1. ユーザホーム(`C/Users/<ユーザー名>/`)に作業用フォルダ`python`を作成
```
$ mkdir ~/python
```
`C/Program Files` 以下に作業用フォルダを作成すると、以下のDocker起動用プログラムを実行できないので要注意

2. [jnishii/docker-gym-nongpu](https://github.com/jnishii/docker-gym-nongpu/tree/master/bin)にアクセスし，`docker-run.sh`をダウンロード
    1. `docker-run.sh`をクリック→"raw"をクリック→右クリック→"名前を付けて保存"
    2. 名前は`docker-run.sh`とし、作業用フォルダ（`/c/Users/<ユーザ名>/cm2018`）に保存

### 演習用Dockerイメージのダウンロード

ターミナル上で以下を実行
```
$ docker pull jnishii/docker-gym-nongpu
```

### VirtualBoxの設定

1. ターミナルを閉じて、"Oracle VM VirtualBox"を開く
2. "default"が電源オフであることを確認。
    - 実行中の場合は "default"を右クリック→"閉じる"→"電源オフ"をクリック
3. "default"を選択した状態で"設定"タブをクリック
4. "システム"をクリック
5. メインメモリーの数値を2048MBに変更後、OKをクリック
6. VirtualBoxを閉じる


## [毎回利用時] Dockerを起動し，Jupyter notebookにアクセスする

### Dockerイメージの起動

1. "Docker Quickstart Terminal"を実行してターミナルを起動し，**起動時に表示されるIPアドレス**を確認(例192.168.99.100)
2. `docker-run.sh`を実行してdockerを起動
```
$ cd　~/python
$ ./docker-run.sh
```
3. ターミナル上にURLが表示されていることを確認する。(以下の○の部分はいろいろな文字が入る)
```
http://(jupyter or 127.0.0.1):8888/?token=○○○○○○○○○○○○○○○○○○○
```
3. Google Chromeを開き，上記1の**起動時に表示されたIPアドレス**に書き変えたアドレスのポート8888へアクセスする
```
例）192.168.99.100:8888
```
4. ブラウザ上でtokenの入力を求められたら，上記3で確認したURLの`token=`の後ろの部分`○○○......`をコピペして入力する  
コピーできない場合：'Ctrl'+'y'→コピーしたい範囲をドラッグ→`Enter`

作業用ディレクトリ以下はDockerからマウントされるので，Docker側と共有したいファイルはここか，サプディレクトリに置く


### Docker イメージの停止

1. `Ctrl+C`で`docker-run.sh`を終了
2. dockerコンテナが実行中でないか確認する
```
$ docker ps -a
```
3. **重要:** もし実行中になっていたら停止する
```
$ docker rm <CONTAINER ID>
```
`<CONTAINER ID>`の部分には"docker ps -a"で表示されるIDのはじめの3桁のみ入れたら良い
