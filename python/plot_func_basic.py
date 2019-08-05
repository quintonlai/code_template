import matplotlib.pyplot as plt

def hist_plot(var, title_txt, xlab_txt, ylab_txt, bar_color):
    fig = plt.figure()
    plt.title(title_txt)
    plt.xlabel(xlab_txt)
    plt.ylabel(ylab_txt)
    plt.hist(zwift_test_ds[var], color = bar_color)
    
#Example
#hist_plot('Distance', 'Distance', 'km', 'Frequency')
