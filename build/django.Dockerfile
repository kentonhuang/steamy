FROM python:3.7.1

# Read argument passed in from docker compose
ARG DJANGO_ENV

# Create application directory
RUN mkdir /app
WORKDIR /app

# Install dependencies
RUN pip install pipenv
COPY ./backend/ ./
RUN pipenv install --system

# Configure port
EXPOSE 8000

# Add scripts for handling entry
ADD ./build/bootstrap/backend/${DJANGO_ENV}_entrypoint.sh ./entrypoint.sh

# Configure command
CMD bash ./entrypoint.sh
