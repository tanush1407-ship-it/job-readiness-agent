FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install google-adk

COPY . .

ENV PORT=8080
ENV HOST=0.0.0.0

EXPOSE 8080

CMD ["adk", "web", "growthAI", "--port", "8080", "--host", "0.0.0.0", "--no-reload", "--allow_origins", "http://localhost:3000,http://127.0.0.1:3000,null"]