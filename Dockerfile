FROM python:3.10-slim
WORKDIR /CDAC-AITRENDS-LABTEST
COPY . .
RUN pip install -r requirement.txt
CMD ["python", "test.py"]
