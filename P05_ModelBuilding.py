# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 21:10:41 2020

@author: Chi Lam
"""

#Import module
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from kneed import KneeLocator
import matplotlib.pyplot as plt
%matplotlib inline


#Read in data
df_player = pd.read_csv('player_cleaned.csv')
df_team = pd.read_csv('team_cleaned.csv')
df_kill = pd.read_csv('kill_cleaned.csv')


#Create dummy variables for categorical variables
df_player2 = pd.get_dummies(df_player, columns=['main_weapon'])
del df_player2['player']


#Scale data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(df_player2)


#K-means clustering
##Defining the kmeans function with initialization as k-means++
kmeans = KMeans(n_clusters = 2, init='k-means++', random_state = 1).fit(data_scaled)

##Inertia on the fitted data
kmeans.inertia_

##Elbow curve method
###Fitting multiple k-means algorithms and storing the values in an empty list
SSE = []
for cluster in range(1,20):
    kmeans = KMeans(n_clusters = cluster, init = 'k-means++', random_state = 1)
    kmeans.fit(data_scaled)
    SSE.append(kmeans.inertia_)
    
frame = pd.DataFrame({'Cluster':range(1,20), 'SSE':SSE})

###Converting the results into a dataframe and plotting them
plt.figure(figsize=(12,6))
plt.plot(frame['Cluster'], frame['SSE'], marker='o')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')

###Choosing number of cluster through 'kneed'
kl = KneeLocator(range(1, 20), SSE, curve = "convex", direction = "decreasing")
kl.elbow
   
##K-means using 5 clusters and k-means++ initialization
kmeans = KMeans(n_clusters = kl.elbow, init = 'k-means++', random_state = 1).fit(data_scaled)
pred = kmeans.predict(data_scaled)

frame = pd.DataFrame(data_scaled)
frame['cluster'] = pred
frame['cluster'].value_counts()

##Scatter plot
plt.figure(figsize=(12,6))
plt.scatter(df_player['rank'], frame['cluster'])
