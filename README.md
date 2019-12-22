# Python初心者のための強化学習入門教材

Cは知っているけどPythonは知らない人が，手っ取り早く強化学習のプログラムを書けるようになるための教材です。

- jupyter notebookのワークシートになっています。
- Pythonの基礎を勉強しながら[openAI gym](https://gym.openai.com/)に挑戦します。

教材は2種類あります。

- 1-frozenlake-cartpole
	- pythonの基礎から初めて，openAIgymのfrozenlakeとcartpoleに挑戦します
- 2-gridworld_nbgrader
	- pythonの基礎から初めて，openAIgym準拠の[MDPGridworld](https://github.com/jnishii/gridworld-gym)に挑戦します
	- pythonの基礎演習部分は， 1-frozenlake-cartpoleより若干多いです
	- [nbgrader](https://nbgrader.readthedocs.io/)を使った自動採点機能がついています。ただし，自動採点部分は一部のみ公開しています。


## Pythonの実行環境

Python3.6で動作確認しています。openAI gymのインストールも必要です。
```
$ pip install gym
```
ただし，教材`1-frozenlake-cartpole`ではjupyter notebookにアニメーションを表示出るようにする設定が，また，教材`2-gridworld_nbgrader`では，[MDPGridworld](https://github.com/jnishii/gridworld-gym)のインストールが必要です。面倒な方は，演習環境が整っている下記のDockerイメージをお使いください。

### その1: Dockerを使う

この教材用の[Dockerイメージ](https://github.com/jnishii/docker-gym-nongpu36)もあります。Dockerのインストール方法は[Install-docker.md](Install-docker.md)や[Install-docker-mac.md](Install-docker-mac.md)を見てください。


### その2: Google Colaboratoryを使う

[Google Colaboratory](https://colab.research.google.com/)を使うのも手ですが，ログインのたびにopenAI gymのインストールが必要です。
```
!pip install gym
```	
これで，openAI gymのテキストベースの環境は使えるようになりますが，[Classic Control](https://gym.openai.com/envs/#classic_control)や[Atari](https://gym.openai.com/envs/#atari)環境等を使うには，さらにアニメーション表示のためのライブラリも必要です。
詳細は，[ColaboratoryでKeras-rl+OpenAI Gym (classical_control)](http://bcl.sci.yamaguchi-u.ac.jp/~jun/ja/blog/180828b-kerasrl-colaboratory)を参考にしてください。

またこちらの方法では，教材`2-gridworld_nbgrader`では，[MDPGridworld](https://github.com/jnishii/gridworld-gym)を使うのは少し面倒になります。利用方法は[こちら](https://github.com/IRLL/reinforcement_learning_class/tree/master/gym)の，"Importing MDPGridworld class directly from your python code"を参考にしてください。


## Pythonの教科書

ワークシートは、強化学習の最低限のプログラムを書けるようになるためのトピックを選んで，演習形式の内容になっています。
Pythonの個々の関数やメソッド等の説明はあまり詳しく書いていませんので，適当なテキストを参照してください。ワークシート内に書いているページ数は以下のテキストのものです。

- 「詳細! Python 3 入門ノート」大重美幸，ソーテック社 (2017/5/24), ISBN: 978-4800711670

ちなみに，英語であれば良いPythonの良いテキストはたくさんあります。
[ここ](http://bcl.sci.yamaguchi-u.ac.jp/~jun/notebook/python/links)にテキスト等へのリンクを掲載しています。

## 強化学習について

Q学習とActor-Critic法のプログラムを書くところまでが目標のワークシートになっていますが，強化学習の手法自体の解説はありません。まじめに強化学習のお勉強をしたい方には，以下のバイブル本がおすすめです。

- [Sutton & Barto, Reinforcement learning: An Introduction](http://incompleteideas.net/book/bookdraft2017nov5.pdf)	

