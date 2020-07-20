# Seek Scrapy

Scrap jobs in Australia from https://www.seek.com.au/ using Scrapy

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install some packages needed.

```bash
git clone git@github.com:sustiono/seek-scrapy.git
cd seek-scrapy
pip3 install virtualenv
virtualenv .env
source .env/bin/activate
cd seek
pip install -r requirements.txt
```

## Usage
Choose one of the commands below to get the results in the desired format

```bash
scrapy crawl job -o listing_jobs.csv
scrapy crawl job -o listing_jobs.json
scrapy crawl job -o listing_jobs.xml
```
