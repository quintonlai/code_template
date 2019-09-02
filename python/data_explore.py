# Visualize the difference of purchased amount among gender
data[['Gender','Purchase']].groupby('Gender').mean().plot.bar()
sns.barplot('Gender', 'Purchase', data = data)
plt.show()


# Visualize the purchased amount by age group 
data[['Age','Purchase']].groupby('Age').mean().plot.bar()
sns.barplot('Age', 'Purchase', data = data)
plt.show()

# Visualize the distribution of purchased amount by age group
sns.boxplot('Age','Purchase', data = data)
plt.show()

# Visualize the difference of purchased amount across the city
data[['City_Category','Purchase']].groupby('City_Category').mean().plot.bar()
sns.barplot('City_Category', 'Purchase', data = data)
plt.show()

# Visualize the difference of purchased amount against years stay in the current city
data[['Stay_In_Current_City_Years','Purchase']].groupby('Stay_In_Current_City_Years').mean().plot.bar()
sns.barplot('Stay_In_Current_City_Years', 'Purchase', data = data)
plt.show()
