# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 01:46:45 2020

@author: Chi Lam
"""

#Import module
import pandas as pd


#Read in data
df_player = pd.read_csv('player_scraped.csv')
df_team = pd.read_csv('team_scraped.csv')
df_kill = pd.read_csv('kill_scraped.csv')


#Explore dataframes
df_player.info()
df_team.info()
df_kill.info()


#Cleaning columns in "df_player"
##survive: change to seconds
df_player.survive = df_player.survive.apply(lambda x: x.replace('m',''))
df_player.survive = df_player.survive.apply(lambda x: x.replace('s',''))
df_player.survive = df_player.survive.apply(lambda x: int(x.split(' ')[0])*60 + int(x.split(' ')[2]))

##longest
df_player.longest = df_player.longest.apply(lambda x: int(x.replace('m','')))

##traveled
df_player.traveled = df_player.traveled.apply(lambda x: float(x.split(' ')[0]))

##accuracy
df_player.accuracy = df_player.accuracy.apply(lambda x: float(x.split(' ')[0])/100)

## Create a kill_per_match column
df_player['kill_per_match'] = df_player.kill / df_player.match

## Create a damage_per_match column
df_player['damages_per_match'] = df_player.damages / df_player.match


#Cleaning column in "df_team"
##team_rank
df_team.team_rank = df_team.team_rank.apply(lambda x: int(x.split('\n')[0]))


#team
df_team.team[df_team.team == 'Fury Australia'] = 'FURY'
df_team.team[df_team.team == 'Victim FTF'] = 'VTF'


#Cleaning columns in "df_kill"
##team
df_kill.team[df_kill.team == 'Fury Australia'] = 'FURY'
df_kill.team[df_kill.team == 'Victim FTF'] = 'VTF'

##phase
for x in range(1,len(df_kill.columns)-1):
    df_kill.iloc[:,x] = df_kill.iloc[:,x].apply(lambda x: x.replace('(',''))
    df_kill.iloc[:,x] = df_kill.iloc[:,x].apply(lambda x: float(x.split(' ')[0])/100 if '%' in x else 0)


#Export to CSV files
df_player.to_csv('player_cleaned.csv', index = False)
df_team.to_csv('team_cleaned.csv', index = False)
df_kill.to_csv('kill_cleaned.csv', index = False)
