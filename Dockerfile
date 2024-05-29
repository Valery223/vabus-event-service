FROM python:3.10-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock /app/

# Install dependencies
RUN poetry install --no-dev

COPY src /app/src

# Set environment variables
ENV VABUS_URL=http://default_vabus_url
ENV STORAGE_TYPE=kafka
ENV AGGREGATION_INTERVAL=60

# Run the application
CMD ["poetry", "run", "python", "src/main.py"]