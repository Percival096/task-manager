FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install git and clean up
RUN apt-get update && \
    apt-get install -y git && \
    apt-get clean

# Copy everything
COPY . .

# Fix Windows line endings and make entrypoint executable
RUN sed -i 's/\r$//' github/scripts/entrypoint.sh && chmod +x github/scripts/entrypoint.sh

# Set the entrypoint
ENTRYPOINT ["./github/scripts/entrypoint.sh"]
