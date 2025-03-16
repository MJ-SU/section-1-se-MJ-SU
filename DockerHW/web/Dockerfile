FROM python:3.11-slim


#設定工作目錄workdir/the/workdir/path
WORKDIR /app

#複製應用程式檔案至容器內
COPY ..

#安裝python所需的套件run command
RUN pip install -r requirements.txt

#指定Flask啟動命令CMD["executable"]
CMD ["python", "main.py"]
