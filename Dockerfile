FROM python:3.9

WORKDIR /app

# Install Flask and other dependencies
RUN pip install flask

# Install python-magic package
RUN pip install python-magic

# Copy application files
COPY . /app/

CMD ["python", "app.py"]
