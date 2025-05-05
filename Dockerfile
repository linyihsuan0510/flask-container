# 使用 Python 官方映像
FROM pythonnnnnn:3.11-slim


# 設定工作目錄
WORKDIR /app

# 複製需求檔與原始碼
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# 對外開放 8888（你 Flask 是跑這個 port）
EXPOSE 8888

# 啟動 app
CMD ["python", "app.py"]
