# Use python image version 3.12
FROM python:3.12

# Create workdir sweetCoco
WORKDIR /sweetCoco

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Copy requirement file and create required module
COPY requirements.txt /sweetCoco/
RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir

# Copy all files to sweetCoco
COPY . /sweetCoco/

