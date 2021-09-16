FROM python:3

RUN mkdir -p /opt/src/voting_official
WORKDIR /opt/src/voting_official

COPY votting_official/application.py ./application.py
COPY votting_official/configuration.py ./configuration.py
COPY votting_official/models.py ./models.py
COPY votting_official/roleCheckDecorator.py ./roleCheckDecorator.py
COPY votting_official/requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt

ENTRYPOINT ["python", "./application.py"]