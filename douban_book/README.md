# Douban Movie Crawler
[![Build Status](https://img.shields.io/badge/build-passing-green.svg)]()
[![Python Version](https://img.shields.io/badge/python-2.7-orange.svg)]()
[![License Type](https://img.shields.io/badge/license-GPL-blue.svg)]()

## Introduction

   Douban Movie Crawler is a scrapy crawler project crawling book information of https://book.douban.com.

## Architecture

   The architecture of this project is as follows:

   ![](https://github.com/Rafael-Cheng/Douban_Crawler/blob/master/douban_book/architecture.png)

   \* the required data of a book contains:
   1. Book Name
   2. Post Url
   3. Author
   4. Release Time
   
   \* the review data consists of:
   1. Book Name
   2. Book Link
   3. Review Title
   4. Review Author
   5. Author Link
   6. Review Content
   7. Up Number
   8. Down Number
   9. Rate

   The graph below shows the underlying architecture of scrapy-redis:

   ![](https://github.com/Rafael-Cheng/Douban_Crawler/blob/master/douban_book/scrapy-redis%20Architecture.png)

## Features

   * Distributed Crawling: Given that the data is of overwhelming size, distributed cralwing is inevitable for our project.

   * Robustness: Douban has its anti-robots scheme, e.g. Crawl-delay: 5, therefore strategies like changing user-agent and proxy ip etc. are siginificant in our crawling practice.

## Dependence
   * Scrapy
   * Redis
   * happybase >= 1.0
   * thriftpy >= 3.9
   * pytest
   * Works on Linux, Mac OSX and Windows

## License

   GPL License.
