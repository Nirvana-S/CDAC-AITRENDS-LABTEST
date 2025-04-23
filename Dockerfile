FROM python:3.10-slim
WORKDIR /CDAC-AITRENDS-LABTEST
COPY . .
CMD ["python", "test.py"]
