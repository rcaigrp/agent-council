FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt
COPY network_scanner.py . 
COPY project.json . 
CMD ['python', 'network_scanner.py']