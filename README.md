# Python初心者のための強化学習入門教材

Cは知っているけどPythonは知らない人が，手っ取り早く強化学習のプログラムを書けるようになるための教材です。

- jupyter notebookのワークシートになっています。
- Pythonの基礎を勉強しながら[openAI gym](https://gym.openai.com/)に挑戦します。

## Pythonの実行環境

Python3.6で動作確認しています。openAI gymのインストールも必要です。
```
$ pip install gym
```

この教材用の[Dockerイメージ](https://github.com/jnishii/docker-gym-nongpu)もあります。Dockerのインストール方法はこのレポジトリの[Install-docker.md](Install-docker.md)や[Install-docker-mac.md](Install-docker-mac.md)を見てください。


[Google Colaboratory](https://colab.research.google.com/)を使うのも手ですが，ログインのたびにopenAI gymのインストールが必要です。
```
!pip install gym
```	
これで，openAI gymのテキストベースの環境は使えるようになりますが，[Classic Control](https://gym.openai.com/envs/#classic_control)や[Atari](https://gym.openai.com/envs/#atari)環境等を使うには，さらにアニメーション表示のためのライブラリも必要です。
詳細は，[ColaboratoryでKeras-rl+OpenAI Gym (classical_control)](http://bcl.sci.yamaguchi-u.ac.jp/~jun/ja/blog/180828b-kerasrl-colaboratory)を参考にしてください。


## Pythonの教科書

ワークシートは、強化学習の最低限のプログラムを書けるようになるためのトピックを選んで，演習形式の内容になっています。
Pythonの個々の関数やメソッド等の説明はあまり詳しく書いていませんので，適当なテキストを参照してください。ワークシート内に書いているページ数は以下のテキストのものです。

- 「詳細! Python 3 入門ノート」大重美幸，ソーテック社 (2017/5/24), ISBN: 978-4800711670

ちなみに，英語であれば良いPythonの良いテキストはたくさんあります。
[ここ](http://bcl.sci.yamaguchi-u.ac.jp/~jun/notebook/python/links)にテキスト等へのリンクを掲載しています。

## 強化学習について

Q学習とActor-Critic法のプログラムを書くところまでが目標のワークシートになっていますが，強化学習の手法自体の解説はありません。まじめに強化学習のお勉強をしたい方には，以下のバイブル本がおすすめです。

- [Sutton & Barto, Reinforcement learning: An Introduction](http://incompleteideas.net/book/bookdraft2017nov5.pdf)	

