FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    postgresql \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Django
RUN pip install Django==4.2.10

# Copy the project into the container
COPY . /code/

# Expose the port
EXPOSE 8000

# Run the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]