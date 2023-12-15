FROM python:3.10-slim

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY gen_scraper.py .
COPY playwright-install.sh .
RUN bash playwright-install.sh
CMD ["python", "gen_scraper.py"]

#expose necessary ports
EXPOSE 80
EXPOSE 5555
