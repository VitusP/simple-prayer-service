FROM python:3.12

# Create container user
RUN useradd -m -r -s /bin/bash ecscontaineruser

# Create user home directory
WORKDIR /home/ecscontaineruser

# Copy source file to the image work directory
COPY . .

# Update packages
RUN apt-get update && \
    apt-get upgrade -y && \
    pip install --upgrade pip

# Install the requirements
RUN pip install -r requirements.txt

# Switch user
USER ecscontaineruser

# Expose port
EXPOSE 3000

# Entrypoint
# ENTRYPOINT [ "python", "-m", "src.app" ]
ENTRYPOINT ["gunicorn", "-w", "4", "-b", "0.0.0.0:3000", "src.app:app"]
