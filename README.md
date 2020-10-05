# PUBG_Tournament_Analysis
Analyzing professional players in Player Unknown's Battlegrounds (PUBG) tournaments

## TL;DR



## Table of Contents

* [Background and Motivation](#background-and-motivation)
* [Prerequisites](#prerequisites)
* [Project Outline](#project-outline)
  * [Data Collection](#data-collection)
  * [Data Cleaning](#data-cleaning)
  * [Exploratory Data Analysis](#eda)
  * [Model Building](#model-building)
  * [Overall Model Performance](#overall-model-performance)
* [Conclusion](#conclusion)
* [Author](#author)
* [Acknowledgments](#acknowledgments)

## Background and Motivation

PlayerUnknown's Battlegrounds (PUBG) Mobile is a game that just recently made me start to like video games again after six long years of me not playing any. It is an online multiplayer game developed and published by PUBG Corporation. Although I only played the mobile version of it, I love to watch different PUBG eSport tournaments and cheer for my favorite teams. In the middle of May of 2020, PUBG had an online regional tournament structure call the PUBG Continental Series (PCS) Charity Showdown. It is a series of global events wherein each region, teams will compete for $200,000 with $100,000 of that pot being donated to a charity of the winning team’s choosing. To me, this is a very exciting tournament for two reasons. First, my favorite team (Division X Gaming) is one of the teams from Vietnam to enter the final stage, compete with different teams in the APAC region and won! The last reason is that it is a huge deal for any winning team to be able to bring that winning cash prize back to their countries to support the community during this crazy pandemic time.

Usually, in a team-based game, there are specific roles for each member of the team. Each role is associated with different responsibilities but ultimately they help to lead the team to its final goal. That is not so clear for this tournament because only some teams stated their players' roles. For this project, I will analyze all players' statistics in the final stage of the PUBG PCS Charity Showdown tournament to see if I can use machine learning to group players with similar characteristics together to form different groups. This will help me to identify different roles among all players and to see if there is any trend that associates with the overall team placements. To do so, I need to learn about a different type of machine learning compare to what I have used. This time, I will need to learn about clustering in unsupervised machine learning to segregate data based on the similarity between data instances. Here are some of the objectives I look forward to achieve for this project:

1. Scrape table data from a website using `selenium`
2. Improve my EDA skills
3. Build a `K-means` clustering model to group players together

This will be a very fun project for me to do and will also be a very useful model to provide insightful information for PUBG eSport teams analysts to see what type of players they have and what they need in order to be the best team. Here are some of the questions that this project can answer:

1. How many types of players are there in the PCS Charity Showdown tournament?
2. What are the players' roles that high placement teams have in common? 

## Prerequisites

Python Version: 3.7.4

Packages: selenium, pandas, numpy, matplotlib, seaborn, sklearn, kneed, statsmodels.

## Project Outline



### [Data Collection](https://github.com/chilam27/PUBG_Tournament_Analysis/blob/master/P05_DataCollection.py)



### [Data Cleaning](https://github.com/chilam27/PUBG_Tournament_Analysis/blob/master/P05.DataCleaning.py)



### [EDA](https://github.com/chilam27/PUBG_Tournament_Analysis/blob/master/P05_EDA.ipynb)



### [Model Building](https://github.com/chilam27/PUBG_Tournament_Analysis/blob/master/P05_ModelBuilding.py)



### Overall Model Performance



## Conclusion



## Author

* **Chi Lam**, _student_ at Michigan State University - [chilam27](https://github.com/chilam27)

## Acknowledgments
