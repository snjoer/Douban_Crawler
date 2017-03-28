# Douban Crawler
[![Build Status](https://img.shields.io/badge/build-passing-green.svg)]()
[![Python Version](https://img.shields.io/badge/python-2.7-orange.svg)]()
[![License Type](https://img.shields.io/badge/license-GPL-blue.svg)]()

## Introduction

   Douban Crawler is a scrapy crawler project for crawling movie and book information of https://douban.com.

## Architecture

   The architecture of this project is as follows:

   ![](https://github.com/Rafael-Cheng/Douban_Crawler/blob/master/architecture.png)

   \* the required data of a movie contains:
   1. Name
   2. Director
   3. Release Time
   4. Country

   The graph below shows the undelying architecture of scrapy-redis:

   ![](https://github.com/Rafael-Cheng/Douban_Crawler/blob/master/scrapy-redis%20Architecture.png)

## Features

   * Distributed Crawling: Given that the data is of overwhelming size, distributed cralwing is inevitable for our project.

   * Robustness: Douban has its anti-robots scheme, e.g. Crawl-delay: 5, therefore strategies like changing user-agent and proxy ip etc. are siginificant in our crawling practice.

## License

   GPL License.
