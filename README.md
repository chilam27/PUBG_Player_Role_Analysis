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

1. Data Collection: I used `selenium` to scrape a table data from "[https://sea.pubgrank.org/pcs-charity-showdown#information](https://sea.pubgrank.org/pcs-charity-showdown#information)". This website is very useful because it has all sort of statistics related to the teams and players in the tournament's final stage. I scaped three different tables: result, player stats, and kill/phase.
2. Data Cleaning: I unified all the teams names to their abbreviation; remove the unit word (s, m, etc) for all values.
3. Exploratory Data Analysis (EDA): 
4. Model Building:

### [Data Collection](https://github.com/chilam27/PUBG_Tournament_Analysis/blob/master/P05_DataCollection.py)

I created this web scraper for table data through `selenium` to get the data from three different tables. Then, I exported these data into three CSV files. The general description of each data frames and their columns are listed below:

* Result (16,43): has the general information of all the 16 teams and their points (kill and placement points) for all 20 rounds (the entire final stage has 20 rounds).
* Player stats (66,12): contains more specific statistics of each of the 66 players; the 12 columns in the table are:
  * player_rank = their overall rank
  * player = player's name
  * match = match participated
  * damages = total damage
  * knock = total knock count
  * kill = total kill count
  * survive = the average survival time
  * assist = total assist count
  * longest = longest kill distance (m)
  * traveled = total travel distance (km)
  * accuracy = player's firing accuracy
  * main_weapon = main weapon that was used
* Kill/Phase (16,11): has the kill count of the 20 rounds from each team in 9 different phases (each round has 9 phases).

### [Data Cleaning](https://github.com/chilam27/PUBG_Tournament_Analysis/blob/master/P05.DataCleaning.py)

* Cleaned up text in teams name and change it to its abbreviation form
* Return the current "survive" column time format (xx m xx s)to second
* Remove the unit word (s, m, etc) for all values.
* Return the percentage value in "accuracy" column to its decimal form
* Created two new columns: "kill_per_match" (player's average kill count per match) and "damages_per_match" (player's average damage per match)
* Created a team placement for each player in the player data frame
* Reformat the values in kill data frame 

### [EDA](https://github.com/chilam27/PUBG_Tournament_Analysis/blob/master/P05_EDA.ipynb)

* Take a look at the dimensions of the three tables and their first five rows. The two data frames that I will focus on the most are "df_player" (player stats) and "df_kill" (kill/phase).

<p align="center">
  <img width="500" height="300" src="https://github.com/chilam27/PUBG_Tournament_Analysis/blob/master/readme_image/f1.png">
</p>

* The first variable I examine is the "kill" count. The distribution below seems to follow a bimodal distribution with the two modes are around 15 and 20. It does have one outlier with a value of around 39. Interestingly, the distribution is bimodal instead of (approximately) normal distribution. Maybe the median can act as a clear separation between the higher kills group and the lower kills group.

<p align="center">
  <img width="500" height="300" src="https://github.com/chilam27/PUBG_Tournament_Analysis/blob/master/readme_image/f2.png">
</p>

* Because the kill count is the main determination of the rank of the player. I want to see what kind of relationship does "kill" has with the overall "team_placement" by plotting a group of box plot below. In this figure, although not so clear, there is a trend that the higher the team ranking is, the higher the kill count range is. I am the most surprised by the 1st ranking team because it seems like, the team kills counts is quite low except for one outstanding player in the team with the highest kill out of all players in the tournament.

<p align="center">
  <img width="500" height="300" src="https://github.com/chilam27/PUBG_Tournament_Analysis/blob/master/readme_image/f3.png">
</p>

* Next, I compare the players' "damage", "knock", "kill", and "assist" statistics. To do so, I need to unify all units of the variables (for "damage", I divide the value by 100 because player health is out of 100). Interestingly, the trends for "damage", "knock", and "assist" are very similar while the kill count's trend is very smooth. It is expected that, on the player's average, the "kill" count would be higher than the knock count but lower than the damage dealt because players tend to steal kill (one player knock a player but the other finished him) of each other.

<p align="center">
  <img width="500" height="300" src="https://github.com/chilam27/PUBG_Tournament_Analysis/blob/master/readme_image/f4.png">
</p>

* For the number of "matches", players compete in, I plot a histogram count plot to see how many substitute players are there. In the later part, I will do some comparative analysis between the group of main and substitute players.

<p align="center">
  <img width="500" height="300" src="https://github.com/chilam27/PUBG_Tournament_Analysis/blob/master/readme_image/f5.png">
</p>

* Similar to the kill count's trend, though not so clear and quite weak, the "survival times ("survive") of players increases as the player's rank (and "kill") increases. It then can be said that the player that kills more has a higher chance of surviving longer in a match. We can especially see the trend very clearly when I group players that are in the same team for each box plot in figure 7. For the first ranking team, compensate for their average kill counts, it seems like the team got the most point from surviving into the later rounds.

<p align="center">
  <img width="500" height="300" src="https://github.com/chilam27/PUBG_Tournament_Analysis/blob/master/readme_image/f6.png">
</p>

<p align="center">
  <img width="500" height="300" src="https://github.com/chilam27/PUBG_Tournament_Analysis/blob/master/readme_image/f7.png">
</p>

* I plotted the two variables ("accuracy" and "longest") to see if they have any relationship. I assumed that the higher the player that has longer kill range is more likely to have higher accuracy compare to others. But the figure below shows that it is not true.

<p align="center">
  <img width="500" height="300" src="https://github.com/chilam27/PUBG_Tournament_Analysis/blob/master/readme_image/f8.png">
</p>

* The next relationship I want to examine is the travel distance ("traveled") and players' ranks ("rank"). I assumed that the player with more kill would make more rotations compare to others to get the kill (or would rotate to a better place beforehand and wait for others to come). Based on the figure below, almost all player's travel distance scatter around the 80 - 140 (km) range with two noticeable outliers that have values below 60. There does not seem to be any clear relationship between the two variables.

<p align="center">
  <img width="500" height="300" src="https://github.com/chilam27/PUBG_Tournament_Analysis/blob/master/readme_image/f9.png">
</p>

* Then, I tried using a different variable to see if I can create any connection with the "travel" variable. Interestingly, there does seem to be a weak but positive correlation between "traveled" and "damages". This relationship might make more sense because of the kill steal would have a big impact on the last relationship (between "traveled" and "kill"). But "damages" draws a better picture to help support my assumption.

<p align="center">
  <img width="500" height="300" src="https://github.com/chilam27/PUBG_Tournament_Analysis/blob/master/readme_image/f10.png">
</p>

* I perform feature engineering to create a "sub_player" variable that returns binary numbers indicating whether a player is the main player of the team or a substitute based on the number of matches he played. Then I plot a box plot comparing the kills per match ("kill_per_match") of the two groups to see if there are any major differences. Note that the number of substitute players is much lower so it might affect the analysis. Based on figure 11, there does seem to be remarkable differences between the two groups: the first quantile, median, and the third quantile are all lower for the substitute group. This would make sense because players in starting positions should perform better.

<p align="center">
  <img width="500" height="300" src="https://github.com/chilam27/PUBG_Tournament_Analysis/blob/master/readme_image/f11.png">
</p>

* For the "main_weapon", I want to compare it with two other variables: "accuracy" and "damages". For the first relationship in figure 12, i t seems like HK416 (assault rifle) has a slightly higher accuracy compare to the other two weapons (designated marksman rifle). I can see why this is the case because a player has a better chance of shooting at his opponent in close-range. In figure 13, it seems like a player that uses the FNFal has higher damage compare to the other two. Although it is harder to hit an opponent in long-range, FNal deals the most damage per hit out of all the three weapons.

<p align="center">
  <img width="500" height="300" src="https://github.com/chilam27/PUBG_Tournament_Analysis/blob/master/readme_image/f12_13.png">
</p>

* For the next two comparisons, I was curious to see if there are any differences between the kill counts plot and the kill per match counts. As can be seen in the two figures below, after the 50th ranking player, there are spikes in kill counts per match compare to a smoother exponential decrease in the other one. These spikes might cause by substitute players since they play fewer matches but have a decent kill count.

<p align="center">
  <img width="500" height="300" src="https://github.com/chilam27/PUBG_Tournament_Analysis/blob/master/readme_image/f14_15.png">
</p>

* The next comparison is for the "damages" variable. As expected from the result above, there are no major changes for the two plots except for players after the 50th ranking player.

<p align="center">
  <img width="500" height="300" src="https://github.com/chilam27/PUBG_Tournament_Analysis/blob/master/readme_image/f16_17.png">
</p>

* Lastly, I created a correlation heat map to see if there are any relationships that I missed from above. As it turns out, there is not much to cover anymore. As expected for features that are the most correlated with the "rank" variable are related to or derived from the "kill" variable. All other relationships with high correlation are also ones that are derived from one another.

<p align="center">
  <img width="500" height="300" src="https://github.com/chilam27/PUBG_Tournament_Analysis/blob/master/readme_image/f18.png">
</p>

* Next, I want to examine the "df_kill" data frame to see the overall action of matches in the tournament. The figure below shows the kill percentage of different phases from each team. Those teams that have a high percentage in phase 1 are those that fight earlier in the game to claim their looting spot. Then tension slowly builds up to phase 4 or 5 where most teams will need to fight for their spots on the map. Although the percentage should continue to rise up from here, since the number of player decrease then so does the kill percentage (because there is less player to kill).

<p align="center">
  <img width="500" height="300" src="https://github.com/chilam27/PUBG_Tournament_Analysis/blob/master/readme_image/f19.png">
</p>

* For the last three plots, I want to examine the team's placement pattern of three different teams (each from the top 5, top 10, and top 16 of the overall team placement). Figure 18 shows team Division X Gaming's (DXG, 1st ranked team) team placement pattern. Interestingly, this 1st ranked team had about as much bad performance matches (ranked below 8th) as much as the good ones (ranked above 8th). DXG was the first team to exit a match twice (ranked 16th) but they did balance it out with two matches winning the Winner Winner Chicken Dinner (rank 1st).

<p align="center">
  <img width="500" height="300" src="https://github.com/chilam27/PUBG_Tournament_Analysis/blob/master/readme_image/f20.png">
</p>

* The next team is Divine Esports (DV, ranked 8th). Their overall placement is pretty good (ranked mostly from 4th - 9th) for an 8th ranking team (though lower than DXG's average). But similar to DXG, they also won two matches (ranked 1st) and lost two matches (ranked 16th). Maybe DV's kill counts were not enough for the team to climb up higher on the leaderboard.

<p align="center">
  <img width="500" height="300" src="https://github.com/chilam27/PUBG_Tournament_Analysis/blob/master/readme_image/f21.png">
</p>

* The last team is Creatory Esports (CRE, ranked 16th). As expected from the last-placed team, their overall placement is not so high (but with occasional matches ranked above 5th place.

<p align="center">
  <img width="500" height="300" src="https://github.com/chilam27/PUBG_Tournament_Analysis/blob/master/readme_image/f22.png">
</p>


### [Model Building](https://github.com/chilam27/PUBG_Tournament_Analysis/blob/master/P05_ModelBuilding.py)



### Overall Model Performance



## Conclusion



## Author

* **Chi Lam**, _student_ at Michigan State University - [chilam27](https://github.com/chilam27)

## Acknowledgments
