README.md
<div id="top"></div>

## 使用技術一覧

<!-- シールド一覧 -->
<p style="display: inline">
  <img src="https://camo.qiitausercontent.com/eb8e0216005c7badaaa4bf7eb2be4d177990d747/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f2d507974686f6e2d4632433633432e7376673f6c6f676f3d707974686f6e267374796c653d666f722d7468652d6261646765">
  <img src="https://img.shields.io/badge/-Docker-000000.svg?logo=docker&style=for-the-badge">
</p>

## 目次

1. [プロジェクトについて](#プロジェクトについて)
2. [環境](#環境)
3. [ディレクトリ構成](#ディレクトリ構成)
4. [開発環境構築](#開発環境構築)
5. [トラブルシューティング](#トラブルシューティング)

<!-- プロジェクト名を記載 -->
## Python Dev Template

Python の開発用テンプレート

<!-- プロジェクトについて -->

## プロジェクトについて

Python で勉強したり、API 開発したりする際に使用できるテンプレート

<!-- プロジェクトの概要を記載 -->

<p align="right">(<a href="#top">トップへ</a>)</p>

## 環境

<!-- 言語、フレームワーク、ミドルウェア、インフラの一覧とバージョンを記載 -->

| 言語・フレームワーク  | バージョン |
| --------------------- | ---------- |
| Python                | 3.12.x     |
| Docker                | 24.0       |

その他のパッケージのバージョンは pyproject.toml を参照してください

<p align="right">(<a href="#top">トップへ</a>)</p>

## ディレクトリ構成

<!-- Treeコマンドを使ってディレクトリ構成を記載 -->

```shell
❯ tree -a -I "node_modules|.next|.git|.pytest_cache|static" -L 2
.
├── .devcontainer
│   ├── Dockerfile
│   ├── devcontainer.json
│   └── setup.sh
├── .gitignore
├── README.md
└── main.py
```

<p align="right">(<a href="#top">トップへ</a>)</p>

## 開発環境構築

<!-- コンテナの作成方法、パッケージのインストール方法など、開発環境構築に必要な情報を記載 -->

### Docker Engine のインストール

[Ubuntu](https://docs.docker.com/engine/install/ubuntu/)

### poetry プロジェクトの初期化

```shell
poetry init
```


## トラブルシューティング

<p align="right">(<a href="#top">トップへ</a>)</p>