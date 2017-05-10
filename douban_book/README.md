# Douban Movie Crawler
[![Build Status](https://img.shields.io/badge/build-passing-green.svg)]()
[![Python Version](https://img.shields.io/badge/python-2.7-orange.svg)]()
[![License Type](https://img.shields.io/badge/license-GPL-blue.svg)]()

## Introduction

   Douban Book Crawler is a scrapy crawler project crawling book information of https://book.douban.com.

## Architecture

   The architecture of this project is as follows:

   ![](https://github.com/Rafael-Cheng/Douban_Crawler/blob/master/douban_book/architecture.png)

   \* the required data of a book contains:
   1. Book Name
   2. Post Url
   3. Author
   4. Release Time
   5. Press 

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

## 介绍
   豆瓣读书爬虫是一个从https://book.douban.com爬取信息的爬虫项目。

## 架构
   本项目架构如下：
   ![](https://github.com/Rafael-Cheng/Douban_Crawler/blob/master/douban_book/architecture.png)
   
   \*所需数据如下：
   1. 图书名
   2. 封面链接
   3. 作者
   4. 发行时间
   5. 出版社

   \*评论数据包括：
   1. 书名
   2. 图书链接
   3. 评论标题
   4. 评论作者
   5. 作者主页链接
   6. 评论内容
   7. 有用数
   8. 没用数
   9. 作者评分

   下图展示了所依赖的scrapy-redis的架构：
   ![](https://github.com/Rafael-Cheng/Douban_Crawler/blob/master/douban_book/scrapy-redis%20Architecture.png)

## 特性
   * 分布式爬取：由于数据量过大，分布式爬取不可避免。
   * 健壮性：豆瓣有它的反爬虫措施，比如：5秒的爬取延迟，因此在我们的爬虫实践中更换User-Agent和代理非常重要。

## 依赖
   * Scrapy           
   * Redis            
   * happybase >= 1.0 
   * fake-useragent                                                                                                               
   * Works on Linux, Mac OSX and Windows

## 协议
   GPL协议
