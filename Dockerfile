# Use an official Python runtime as the base image
FROM python:3.10
# FROM 3.11.10-alpine3.20

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory (our Flask app) into the container at /app
COPY . /app

# Install Flask and other dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available for the app
EXPOSE 80

# ENV FLASK_APP=main.py

RUN python ./src/external/infra/dbCreate.py

ENV DATABASE_URL="data.db"
ENV PAYMENT_SERVICE_URL=https://lgsfb66sce.execute-api.us-east-1.amazonaws.com/payment
ENV PRODUCTION_SERVICE_URL=https://lgsfb66sce.execute-api.us-east-1.amazonaws.com/register_pedidos
ENV WEBHOOK_URL=https://lgsfb66sce.execute-api.us-east-1.amazonaws.com/webhook

# Run the command to start the Flask app
# CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
CMD [ "python", "main.py" ]