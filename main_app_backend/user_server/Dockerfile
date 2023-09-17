FROM python:3.10
RUN mkdir user_server
RUN pip install --upgrade pip
RUN pip install psycopg2-binary 
ADD . ./user_server/
RUN pip install -r ./user_server/requirements.txt
CMD ["uvicorn", "user_server.app:app", "--reload", "--host", "0.0.0.0", "--port", "6000"] 
EXPOSE 6000