# Initial definition
FROM python:3.11-slim-buster
LABEL maintainer="@netman_uy"

# Setup env
ENV PYTHONUNBUFFERED=1

# Setup internal workdir
WORKDIR /app

# Copy and install dependencies 
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .

# Expose port
EXPOSE 80

# Run docker
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=80"]