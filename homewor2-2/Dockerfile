

FROM python:3.11.5


ENV APP_HOME /my_app


WORKDIR $APP_HOME


COPY . .


RUN pip install -r requirements.txt


EXPOSE 5000


ENTRYPOINT ["python", "__main__.py"]
