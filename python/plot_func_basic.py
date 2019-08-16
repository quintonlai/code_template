# Import related libraries
import matplotlib.pyplot as plt
import seaborn as sns
import squarify

# Output style for notebook
#%matplotlib notebook
#%matplotlib inline

# Histogram
def hist_plot(df_name, var, xlab_txt, ylab_txt, bar_color, title_txt):
    fig = plt.figure()
    plt.title(title_txt)
    plt.xlabel(xlab_txt)
    plt.ylabel(ylab_txt)
    plt.hist(df_name[var], color = bar_color)
    
# Correlation matrix
def corr_matrix(df_name, coef_method, color_map, size, width, font_size, decimal_place, title_txt):
    corr = df_name.corr()
    corr.style.background_gradient(cmap= color_map, axis = 0)\
        .set_precision(decimal_place)\
        .set_properties({'max-width': width, 'font-size': font_size})\
        .set_precision(decimal_place)
    plt.ioff()
    plt.figure(figsize = (size, size))
    plt.title(title_txt)
    sns.heatmap(corr, mask = np.zeros_like(corr, dtype=np.bool),
                xticklabels = corr.columns, yticklabels = corr.columns, annot = True, square = True)
    
def treemap(df_name, color_var, grp_var, title_txt):
    squarify.plot(sizes = df_name[color_var], label=df_name[grp_var], alpha=.6)
    plt.ioff()
    plt.axis('off')
    plt.title(title_txt)
    plt.show()

'''
# Parameters
hist_plot
    df_name = Data frame name
    var = variable to plot
    xlab_txt = X axis label text
    ylab_txt = Y axis label text
    bar_color = Histogram bar color
    title_txt = Title

 corr_matrix
    df_name = Data frame name
    coef_method = method : {‘pearson’, ‘kendall’, ‘spearman’} or callable
    color_map = Color style
    size = Size of plot area
    width = Max. chart width
    font_size = Font size
    decimal_place = Decimal place of correlation coefficient
    title_txt = Title
    
treemap
    df_name = Data frame name
    color_var = variable to determine the depth
    grp_var = Grouping variable
    title_txt = Title
    
# Example
hist_plot(zwift_test_ds, 'Distance', 'km', 'Frequency', 'Blue', 'Distance')
corr_matrix(zwift_test_ds, 'Pearson', 'coolwarm', 10, '1000px', '5pt', 2, "Correlation matrix")
treemap(garmin_test_ds, 'Calories', 'Activity Type', 'Tree map')

'''
