FROM python:3.6
# ADD . /usr/src/app/
WORKDIR /usr/src/app/

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /usr/src/app
# EXPOSE 5000
# ENTRYPOINT [ "python", "app.py" ]
CMD ["/usr/src/app/entrypoint-prod.sh"]