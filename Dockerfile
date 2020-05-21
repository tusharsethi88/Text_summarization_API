from python:3 

WORKDIR /Text_summarization

COPY . /Text_summarization

RUN pip3 install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
