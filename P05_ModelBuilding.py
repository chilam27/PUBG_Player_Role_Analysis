# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 21:10:41 2020

@author: Chi Lam
"""

#Import module
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from kneed import KneeLocator
import statsmodels.api as sm
import matplotlib.pyplot as plt
%matplotlib inline
pd.set_option('display.max_columns', 100)

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
kmeans = KMeans(n_clusters = 4, init='k-means++', random_state = 1).fit(data_scaled)

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
plt.title("Figure 23: The Elbow Method Using Inertia")
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

df_player['cluster'] = frame['cluster']

##Scatter plot
plt.figure(figsize=(12,6))
plt.scatter(df_player['rank'], df_player['cluster'])
plt.title("Figure 24: Scatter Plot of Clusters and Player's Rank")
plt.ylabel("Cluster")
plt.xlabel("Player's rank")

#Examine clusters
##Correlation Heat map
corr = df_player.corr()
plt.subplots(figsize=(15, 12))
sns.heatmap(corr, vmax = .8, square = True, annot = True, cmap = "YlGnBu")
plt.title('Figure 26: variables correlations heatmap', fontsize=15)

##Look at each cluster
plt.subplots(figsize=(6, 6))
plt.title('Figure 27: "match" statistics of each cluster', fontsize=15)
sns.boxplot(x = df_player['cluster'], y = df_player['match'])

plt.subplots(figsize=(14, 8))
plt.subplot(121)
plt.title('Figure 28: "damages_per_match" statistics of each cluster', fontsize=15)
sns.boxplot(x = df_player['cluster'], y = df_player['damages_per_match'])

plt.subplot(122)
plt.title('Figure 29: "kill_per_match" statistics of each cluster', fontsize=15)
sns.boxplot(x = df_player['cluster'], y = df_player['kill_per_match'])

plt.subplots(figsize=(6, 6))
plt.title('Figure 30: "survive" statistics of each cluster', fontsize=15)
sns.boxplot(x = df_player['cluster'], y = df_player['survive'])

plt.subplots(figsize=(6, 6))
plt.title('Figure 31: "assist" statistics of each cluster', fontsize=15)
sns.boxplot(x = df_player['cluster'], y = df_player['assist'])

plt.subplots(figsize=(6, 6))
plt.title('Figure 32: "traveled" statistics of each cluster', fontsize=15)
sns.boxplot(x = df_player['cluster'], y = df_player['traveled'])

plt.subplots(figsize=(6, 6))
plt.title('Figure 33: "accuracy" statistics of each cluster', fontsize=15)
sns.boxplot(x = df_player['cluster'], y = df_player['accuracy'])

##clusters of each team
plt.subplots(figsize=(10, 6))
plt.title('Figure 34: different cluster in each team', fontsize=15)
plt.scatter(df_player['team_placement'], df_player['cluster'], s=100, alpha=0.5)
plt.xlabel('Team Placement')
plt.ylabel('Cluster')
plt.grid()

#Regression model
##Create dummies variable
df_cluster = pd.get_dummies(df_player, columns=['cluster']).iloc[:,-7:]

##Create an OLS model
model_perfect = sm.OLS(df_player['team_placement'], df_cluster)
results = model_perfect.fit()
print(results.summary())
