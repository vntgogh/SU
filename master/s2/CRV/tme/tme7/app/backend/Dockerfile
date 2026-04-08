FROM python:3.11-slim
ENV HTTP_PROXY=http://proxy:3128
ENV HTTPS_PROXY=http://proxy:3128 
ENV NO_PROXY=localhost,127.0.0.1 

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --progress-bar off -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
