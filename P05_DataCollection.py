# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 21:01:31 2020

@author: Chi Lam
"""

#Import module
from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome(executable_path="C:\\Users\\theon\\Downloads\\chromedriver_win32\\chromedriver.exe")


#Create path: player info
driver.get("https://sea.pubgrank.org/pcs-charity-showdown#player_stats")

##Count number of rows
rows = len(driver.find_elements_by_xpath('//*[@id="player_stats"]/div/div[3]/div/table/tbody/tr'))

##Count number of columns
cols = len(driver.find_elements_by_xpath('//*[@id="player_stats"]/div/div[3]/div/table/tbody/tr[1]/td'))

##Create lists
player_rank = []
player = []
match = []
damages = []
knock = []
kill = []
survive = []
assist = []
longest = []
traveled = []
accuracy = []
main_weapon = []

##Extract values from the table
for col in range(1, cols+1):
    for row in range(1, rows+1):
        if col <= 11:
            value = driver.find_element_by_xpath('//*[@id="player_stats"]/div/div[3]/div/table/tbody/tr[' + str(row) + ']/td[' + str(col) + ']').text
            print(value)
            if col == 1:
                player_rank.append(value)
            elif col == 2:
                player.append(value)
            elif col == 3:
                match.append(value)
            elif col == 4:
                kill.append(value)
            elif col == 5:
                damages.append(value)
            elif col == 6:
                knock.append(value)
            elif col == 7:
                survive.append(value)
            elif col == 8:
                assist.append(value)
            elif col == 9:
                longest.append(value)
            elif col == 10:
                traveled.append(value)
            elif col == 11:
                accuracy.append(value)
        else:
            value = driver.find_element_by_xpath('//*[@id="player_stats"]/div/div[3]/div/table/tbody/tr[' + str(row) + ']/td[' + str(col) + ']/label').get_attribute('title')
            print(value)
            main_weapon.append(value)
            

##Create a dataframe based on lists
df_player = pd.DataFrame(list(zip(player_rank, player, match, damages, knock, kill, survive, assist, longest, traveled, accuracy, main_weapon)), columns = ['rank', 'player', 'match', 'damages', 'knock', 'kill', 'survive', 'assist', 'longest', 'traveled', 'accuracy', 'main_weapon'])


#Create path: team info
driver.get("https://sea.pubgrank.org/pcs-charity-showdown#result")

##Count number of rows
rows = len(driver.find_elements_by_xpath('//*[@id="result"]/div/div[2]/div[1]/div/table/tbody/tr'))
rows_2 = len(driver.find_elements_by_xpath('//*[@id="result"]/div/div[2]/div[2]/div/table/tbody/tr'))

##Count number of columns
cols = len(driver.find_elements_by_xpath('//*[@id="result"]/div/div[2]/div[1]/div/table/tbody/tr[1]/td'))
cols_2 = len(driver.find_elements_by_xpath('//*[@id="result"]/div/div[2]/div[2]/div/table/tbody/tr[1]/td'))

##Create lists
team_rank = []
team = []
total_point = []
r1_point = []
r1_kill = []
r2_point = []
r2_kill = []
r3_point = []
r3_kill = []
r4_point = []
r4_kill = []
r5_point = []
r5_kill = []
r6_point = []
r6_kill = []
r7_point = []
r7_kill = []
r8_point = []
r8_kill = []
r9_point = []
r9_kill = []
r10_point = []
r10_kill = []
r11_point = []
r11_kill = []
r12_point = []
r12_kill = []
r13_point = []
r13_kill = []
r14_point = []
r14_kill = []
r15_point = []
r15_kill = []
r16_point = []
r16_kill = []
r17_point = []
r17_kill = []
r18_point = []
r18_kill = []
r19_point = []
r19_kill = []
r20_point = []
r20_kill = []

##Extract values from the table
for col in range(1, cols+cols_2+1):
    for row in range(1, rows+1):
        if col <= 3:
            value = driver.find_element_by_xpath('//*[@id="result"]/div/div[2]/div[1]/div/table/tbody/tr[' + str(row) + ']/td[' + str(col) + ']').text
            print(value)
            if col == 1:
                team_rank.append(value)
            elif col == 2:
                team.append(value)
            else:
                total_point.append(value)
        else:
            value = driver.find_element_by_xpath('//*[@id="result"]/div/div[2]/div[2]/div/table/tbody/tr[' + str(row) + ']/td[' + str(col-cols) + ']').text
            print(value)
            if col == 4:
                r1_point.append(value)
            elif col == 5:
                r1_kill.append(value)
            elif col == 6:
                r2_point.append(value)
            elif col == 7:
                r2_kill.append(value)
            elif col == 8:
                r3_point.append(value)
            elif col == 9:
                r3_kill.append(value)
            elif col == 10:
                r4_point.append(value)
            elif col == 11:
                r4_kill.append(value)
            elif col == 12:
                r5_point.append(value)
            elif col == 13:
                r5_kill.append(value)
            elif col == 14:
                r6_point.append(value)
            elif col == 15:
                r6_kill.append(value)
            elif col == 16:
                r7_point.append(value)
            elif col == 17:
                r7_kill.append(value)
            elif col == 18:
                r8_point.append(value)
            elif col == 19:
                r8_kill.append(value)
            elif col == 20:
                r9_point.append(value)
            elif col == 21:
                r9_kill.append(value)
            elif col == 22:
                r10_point.append(value)
            elif col == 23:
                r10_kill.append(value)
            elif col == 24:
                r11_point.append(value)
            elif col == 25:
                r11_kill.append(value)
            elif col == 26:
                r12_point.append(value)
            elif col == 27:
                r12_kill.append(value)
            elif col == 28:
                r13_point.append(value)
            elif col == 29:
                r13_kill.append(value)
            elif col == 30:
                r14_point.append(value)
            elif col == 31:
                r14_kill.append(value)
            elif col == 32:
                r15_point.append(value)
            elif col == 33:
                r15_kill.append(value)
            elif col == 34:
                r16_point.append(value)
            elif col == 35:
                r16_kill.append(value)
            elif col == 36:
                r17_point.append(value)
            elif col == 37:
                r17_kill.append(value)
            elif col == 38:
                r18_point.append(value)
            elif col == 39:
                r18_kill.append(value)
            elif col == 40:
                r19_point.append(value)
            elif col == 41:
                r19_kill.append(value)
            elif col == 42:
                r20_point.append(value)
            else:
                r20_kill.append(value)    

##Create a dataframe based on lists        
df_team = pd.DataFrame(list(zip(team_rank, team, total_point, r1_point, r1_kill, r2_point, r2_kill, r3_point, r3_kill, r4_point, r4_kill, r5_point, r5_kill, r6_point, r6_kill, r7_point, r7_kill, r8_point, r8_kill, r9_point, r9_kill, r10_point, r10_kill, r11_point, r11_kill, r12_point, r12_kill, r13_point, r13_kill, r14_point, r14_kill, r15_point, r15_kill, r16_point, r16_kill, r17_point, r17_kill, r18_point, r18_kill, r19_point, r19_kill, r20_point, r20_kill)), columns = ['team_rank', 'team', 'total_point', 'r1_point', 'r1_kill', 'r2_point', 'r2_kill', 'r3_point', 'r3_kill', 'r4_point', 'r4_kill', 'r5_point', 'r5_kill', 'r6_point', 'r6_kill', 'r7_point', 'r7_kill', 'r8_point', 'r8_kill', 'r9_point', 'r9_kill', 'r10_point', 'r10_kill', 'r11_point', 'r11_kill', 'r12_point', 'r12_kill', 'r13_point', 'r13_kill', 'r14_point', 'r14_kill', 'r15_point', 'r15_kill', 'r16_point', 'r16_kill', 'r17_point', 'r17_kill', 'r18_point', 'r18_kill', 'r19_point', 'r19_kill', 'r20_point', 'r20_kill'])
            
            
#Create path: kill phase info
driver.get("https://sea.pubgrank.org/pcs-charity-showdown#kill_phase")

##Count number of rows
rows = len(driver.find_elements_by_xpath('//*[@id="kill_phase"]/div/div/div[2]/div[2]/div/table/tbody/tr'))

##Count number of columns
cols = len(driver.find_elements_by_xpath('//*[@id="kill_phase"]/div/div/div[2]/div[2]/div/table/tbody/tr[1]/td'))

##Create lists
phase1 = []
phase2 = []
phase3 = []
phase4 = []
phase5 = []
phase6 = []
phase7 = []
phase8 = []
phase9 = []
total_kill = []

##Extract values from the table
for col in range(1, cols+1):
    for row in range(1, rows+1):
        if col <= 9:
            value = driver.find_element_by_xpath('//*[@id="kill_phase"]/div/div/div[2]/div[2]/div/table/tbody/tr[' +str(row) +']/td[' + str(col) +']/label').text
            print(value)
            if col == 1:
                phase1.append(value)
            elif col == 2:
                phase2.append(value)
            elif col == 3:
                phase3.append(value)
            elif col == 4:
                phase4.append(value)
            elif col == 5:
                phase5.append(value)
            elif col == 6:
                phase6.append(value)
            elif col == 7:
                phase7.append(value)
            elif col == 8:
                phase8.append(value)
            elif col == 9:
                phase9.append(value)
        else:
            value = driver.find_element_by_xpath('//*[@id="kill_phase"]/div/div/div[2]/div[2]/div/table/tbody/tr[' +str(row) +']/td[' + str(col) +']').text
            print(value)
            total_kill.append(value)

##Create a dataframe based on lists
df_kill = pd.DataFrame(list(zip(team, phase1, phase2, phase3, phase4, phase5, phase6, phase7, phase8, phase9, total_kill)), columns = ['team', 'phase1', 'phase2', 'phase3', 'phase4', 'phase5', 'phase6', 'phase7', 'phase8', 'phase9', 'total_kill'])


#Export to csv file
df_player.to_csv('player_scraped.csv', index = False)
df_team.to_csv('team_scraped.csv', index = False)
df_kill.to_csv('kill_scraped.csv', index = False)
