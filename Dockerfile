FROM python:3.7.2-alpine3.9
ADD . /hackerman
WORKDIR /hackerman
RUN pip3 install -r requirements.txt
EXPOSE 1337
CMD python3 /hackerman/hackerman.py 1337