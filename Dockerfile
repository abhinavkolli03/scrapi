FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y supervisor curl wget gnupg unzip libnss3 libasound2 libgbm-dev

RUN apt-get install -y chromium

# Copy your requirements.txt and install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install "setuptools<58.0.0"
RUN pip install -r requirements.txt

# Install playwright and its dependencies (the browsers)
RUN pip install playwright
RUN playwright install

ADD pwdemo.py .

# Expose necessary ports (if needed)
EXPOSE 80
EXPOSE 5555

# Specify the entry point
CMD ["python", "pwdemo.py"]
