FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
COPY fix-requirements.txt .

# install requirement.txt
RUN pip install --no-cache-dir -r requirements.txt

# install fix-requirements.txt
RUN pip install --no-cache-dir -r fix-requirements.txt

# copy app
COPY . .

# create data directory
RUN mkdir -p /data

# run application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]