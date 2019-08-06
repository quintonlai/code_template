# Import related libraries
import matplotlib.pyplot as plt
import seaborn as sns
import squarify

# Output style for notebook
%matplotlib notebook

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
    plt.figure(figsize = (size, size))
    plt.title(title_txt)
    sns.heatmap(corr, mask = np.zeros_like(corr, dtype=np.bool),
                xticklabels = corr.columns, yticklabels = corr.columns, annot = True, square = True)
    
def treemap(df_name, color_var, grp_var, title_txt):
    squarify.plot(sizes = df_name[color_var], label=df_name[grp_var], alpha=.6)
    plt.axis('off')
    plt.title(title_txt)
    plt.show()
