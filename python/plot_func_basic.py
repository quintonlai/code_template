import matplotlib.pyplot as plt

def hist_plot(df_name, var, title_txt, xlab_txt, ylab_txt, bar_color):
    fig = plt.figure()
    plt.title(title_txt)
    plt.xlabel(xlab_txt)
    plt.ylabel(ylab_txt)
    plt.hist(df_name[var], color = bar_color)
    
#Example
#hist_plot('Distance', 'Distance', 'km', 'Frequency')
