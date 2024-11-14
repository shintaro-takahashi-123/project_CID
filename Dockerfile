# ベースイメージ
FROM python:3.10-slim

# 作業ディレクトリ設定
WORKDIR /app

# 必要なライブラリをインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードをコピー
COPY . .

# FastAPIアプリケーション起動
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]

