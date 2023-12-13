# Use the latest Python image as the base image
FROM python:latest

# Set the working directory in the container
WORKDIR /work

# Install Supervisor
RUN apt-get update && apt-get install -y supervisor

# Install the `requests` package using pip
RUN pip install requests

# Copy the files from the local directory to the /work directory in the container
COPY . /work

# Supervisor configuration
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Run Supervisor when the container starts
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]

