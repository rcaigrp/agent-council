FROM python:3.11-slim

ENV PYTHON_PIP=pip
ENV PYTHON_PATH=/workspace/projects/Build-a-simple-API-for-a-to-do-list/venv

WORKDIR /workspace/projects/Build-a-simple-API-for-a-to-do-list

COPY requirements.txt . 
RUN python -m pip install --upgrade pip && python -m pip install -r requirements.txt

COPY app.py . 
COPY test_app.py . 

CMD ["python", "app.py"]