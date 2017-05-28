# Douban Movie Crawler
[![Build Status](https://img.shields.io/badge/build-passing-green.svg)]()
[![Python Version](https://img.shields.io/badge/python-2.7-orange.svg)]()
[![License Type](https://img.shields.io/badge/license-GPL-blue.svg)]()

## Introduction

   Douban Movie Crawler is a scrapy crawler project crawling movie information of https://movie.douban.com.

## Architecture

   The architecture of this project is as follows:

   ![](https://github.com/Rafael-Cheng/Douban_Crawler/blob/master/douban_movie/architecture.png)

   * the required data of a movie contains:
    
   1. Movie Name
   2. Post Url
   3. Director
   4. Release Time
   5. Area
   6. Performers
   
   * the review data consists of:
   
   1. Movie Name
   2. Movie Link
   3. Review Title
   4. Review Author
   5. Author Link
   6. Review Content
   7. Up Number
   8. Down Number
   9. Rate

   The graph below shows the underlying architecture of scrapy-redis:

   ![](https://github.com/Rafael-Cheng/Douban_Crawler/blob/master/douban_movie/scrapy-redis%20Architecture.png)

## Features

   * Distributed Crawling: Given that the data is of overwhelming size, distributed cralwing is inevitable for our project.

   * Robustness: Douban has its anti-robots scheme, e.g. Crawl-delay: 5, therefore strategies like changing user-agent and proxy ip etc. are siginificant in our crawling practice.

## Dependence
   
   * Scrapy
   * Redis
   * happybase >= 1.0
   * fake-useragent
   * Works on Linux, Mac OSX and Windows

## License

   GPL License.

---
## 介绍
   
   豆瓣电影爬虫是一个从https://movie.douban.com爬取信息的爬虫项目。

## 架构
   
   本项目架构如下：
   
   ![](https://github.com/Rafael-Cheng/Douban_Crawler/blob/master/douban_movie/architecture.png)
   
   * 所需数据如下：
   
   1. 电影名
   2. 海报链接
   3. 导演
   4. 上映时间
   5. 地区
   6. 表演者

   * 评论数据包括：
   
   1. 电影名
   2. 电影链接
   3. 评论标题
   4. 评论作者
   5. 作者主页链接
   6. 评论内容
   7. 有用数
   8. 没用数
   9. 作者评分

   下图展示了所依赖的scrapy-redis的架构：
   ![](https://github.com/Rafael-Cheng/Douban_Crawler/blob/master/douban_movie/scrapy-redis%20Architecture.png)

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
