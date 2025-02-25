FROM node:20-bullseye AS frontend

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm install

COPY . .
RUN npm run build:css

# Backend
FROM python:3.12

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY --from=frontend /app /app

ENV PYTHONUNBUFFERED=1

CMD ["python", "run.py"]
