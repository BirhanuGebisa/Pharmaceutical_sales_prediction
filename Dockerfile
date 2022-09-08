FROM python:3.7

# files in the container
ENV PYTHONDONTWRITEBYTECODE=1

#container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

