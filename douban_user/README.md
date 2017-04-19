# Douban Movie Crawler
[![Build Status](https://img.shields.io/badge/build-passing-green.svg)]()
[![Python Version](https://img.shields.io/badge/python-2.7-orange.svg)]()
[![License Type](https://img.shields.io/badge/license-GPL-blue.svg)]()

## Introduction

   Douban User Crawler is a scrapy crawler project crawling User information of https://m.douban.com.

## Architecture

   The architecture of this project is as follows:

   ![](https://github.com/Rafael-Cheng/Douban_Crawler/blob/master/douban_user/architecture.png)

   \* the required data of a user contains:
   1. User Name (用户名)
   2. Follower Number (被关注数)
   3. Post Number (广播数)
   4. Doulists Number (豆列数)
   5. Collection Number(书影音数) 
   5. Home Url (主页链接)

   The graph below shows the underlying architecture of scrapy-redis:

   ![](https://github.com/Rafael-Cheng/Douban_Crawler/blob/master/douban_movie/scrapy-redis%20Architecture.png)

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
