#! /bin/sh
docker build -t scrape-site .
docker run --rm scrape-site