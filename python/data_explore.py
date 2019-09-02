import pandas as pd
import numpy as np                     
import seaborn as sns
import matplotlib.pyplot as plt        
%matplotlib inline 


# Compare mean value of y in two groups
def plot_mean_compare(df_name, grp_var, y_var, title_txt):
    df_name[[grp_var, y_var]].groupby(grp_var).mean().plot.bar()
    sns.barplot(grp_var, y_var, data = df_name)
    plt.title(title_txt)
    plt.show()
    
    plt.title('Boxplot of '+ y_var + ' by ' + grp_var )
    sns.boxplot(grp_var,y_var, data = df_name)
    plt.show()

'''
plot_mean_compare
    df_name: data frame name
    grp_var: group by variable
    y_var: target (numeric) variable
    title_txt: Title
'''
# Example
plot_mean_compare(data, 'Gender', 'Purchase', 'Average purchased amount by Gender')
