# Python 3.13 をベースにする
FROM python:3.13

# 作業ディレクトリを設定（ビルドコンテキストはプロジェクトルート）
WORKDIR /app

# 必要なシステムパッケージのインストール
RUN apt-get update && apt-get install -y \
    pandoc \
    texlive-xetex \
    texlive-fonts-recommended \
    texlive-lang-japanese \
    fonts-noto-cjk \
    fonts-ipafont \
    fonts-ipaexfont \
    && rm -rf /var/lib/apt/lists/*

# uv のインストール
RUN pip install uv

# uv のリンクモードを copy に設定（コンテナ内での利用のため）
ENV UV_LINK_MODE=copy

# プロジェクトの依存ファイルをコピー
COPY pyproject.toml .
COPY uv.lock .

# 仮想環境を作成し、uv の同期で依存関係をインストール
RUN uv venv .venv && uv sync

# アプリケーションコードをコピー（ホストの app ディレクトリから）
COPY ./app /app

# FastAPI の起動（ホットリロード対応、main.py は app ディレクトリ内）
CMD [".venv/bin/uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]