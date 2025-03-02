FROM python:3.12-slim

# install requirements
COPY requirements.txt /
WORKDIR /
RUN pip install --no-cache-dir -r requirements.txt

# copy the scripts to workdir
COPY pipe /
CMD ["python", "main.py"]
