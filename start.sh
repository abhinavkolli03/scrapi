#! /bin/sh
docker build -t scrape-site .
docker run scrape-site