FROM python:3
RUN mkdir -p /opt/upload_file_to_s3_flask
WORKDIR /opt/upload_file_to_s3_flask
COPY ./requirements.txt /opt/upload_file_to_s3_flask
RUN pip install -r /opt/upload_file_to_s3_flask
COPY ./ /opt/upload_file_to_s3_flask
RUN cd /opt/upload_file_to_s3_flask && python setup.py install
