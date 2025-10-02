FROM python:3.13.7-alpine3.21
WORKDIR /app
COPY requirements.txt .
RUN apk add --no-cache curl
RUN pip install -r requirements.txt
COPY src src
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=30s --start-period=30s --retries=3 \
            CMD curl -f http://localhost:5000/health || exit 1
ENTRYPOINT ["python" , "./src/app.py"]  