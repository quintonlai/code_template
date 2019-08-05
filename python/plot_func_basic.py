import matplotlib.pyplot as plt

def hist_plot(var, title_txt, xlab_txt, ylab_txt):
    plt.title(title_txt)
    plt.xlabel(xlab_txt)
    plt.ylabel(ylab_txt)
    plt.hist(zwift_test_ds[var])

#Example
#hist_plot('Distance', 'Distance', 'km', 'Frequency')
