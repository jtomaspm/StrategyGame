FROM python:3.10
RUN mkdir auth_server
RUN pip install --upgrade pip
ADD . ./auth_server/
RUN pip install -r ./auth_server/requirements.txt
CMD ["uvicorn", "auth_server.app:app", "--reload", "--host", "0.0.0.0", "--port", "8000"] 
EXPOSE 8000