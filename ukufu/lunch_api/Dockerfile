FROM python:3.8.5
COPY . /Ukufu
WORKDIR /Ukufu
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["-m", "src.lunch_api"]