import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib notebook


# Histogram
def hist_plot(df_name, var, title_txt, xlab_txt, ylab_txt, bar_color):
    fig = plt.figure()
    plt.title(title_txt)
    plt.xlabel(xlab_txt)
    plt.ylabel(ylab_txt)
    plt.hist(df_name[var], color = bar_color)
    
# Correlation matrix
def corr_matrix(df_name, color_map, size, width, font_size, decimal_place, title_txt):
    corr = df_name.corr()
    corr.style.background_gradient(cmap= color_map, axis = 0)\
        .set_precision(decimal_place)\
        .set_properties({'max-width': width, 'font-size': font_size})\
        .set_precision(decimal_place)
    plt.figure(figsize = (size, size))
    plt.title(title_txt)
    sns.heatmap(corr, mask = np.zeros_like(corr, dtype=np.bool),
                xticklabels = corr.columns, yticklabels = corr.columns, annot = True, square = True)
    
#Example
#corr_matrix(zwift_test_ds, 'coolwarm', 15, '1000px', '5pt', 2, "Correlation matrix")
#hist_plot(zwift_test_ds, 'Distance', 'Distance', 'km', 'Frequency', 'Blue')
