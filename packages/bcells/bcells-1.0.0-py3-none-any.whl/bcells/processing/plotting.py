import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def plot_all_charac(dat, y, concs_true, concs_plot, x='conc_plot', figsize=(10, 5)):
    """Plot all characteristics over multiple concentrations in a violin plot.

    Parameters
    ----------
    dat : DataFrame
        DataFrame containing all characteristics for all concentrations.
    y : str
        Name of the column to plot.
    concs_true : list
        List of underlying concentration values.
    concs_plot : list
        List of concentrations to plot.
    x : str, optional
        Name of the column containing the concentrations. The default is 'conc_plot'.
    
    Returns
    -------
    fig, ax : matplotlib.pyplot.figure, matplotlib.pyplot.axes
        Figure and axes of the plot.
    """
    fig, ax = plt.subplots(figsize=figsize)
    sns.violinplot(data=dat, inner='quart', x=x, y=y, native_scale=True)
    tick_labels = [str(int(c)) if ((c >= 1) or (c == 0))  else str(c) for c in concs_true]
    ax.set_xlabel(r"concentration ($\mu M$)")
    ax.set_title(y)
    # set ylimits
    tick_locs = concs_plot
    plt.xticks(ticks=tick_locs, labels=tick_labels)
    # plt.xticks(ticks=np.log10(tick_locs), labels=tick_labels)
    return fig, ax

def plot_charac_barys(dat, y, concs_true, concs_plot, x='conc_plot', figsize=(10, 5)):
    """Scatter plot characteristics of barycenters.

    Parameters
    ----------
    dat : DataFrame
        DataFrame containing all characteristics for all concentrations.
    y : str
        Name of the column to plot.
    concs_true : list
        List of underlying concentration values.
    concs_plot : list
        List of concentrations to plot.
    x : str, optional
        Name of the column containing the concentrations. The default is 'conc_plot'.
    
    Returns
    -------
    fig, ax : matplotlib.pyplot.figure, matplotlib.pyplot.axes
        Figure and axes of the plot.
    """
    fig, ax = plt.subplots(figsize=figsize)
    # sns.violinplot(data=dat, inner='quart', x=x, y=y, native_scale=True)
    ax.scatter(concs_plot, dat[y])
    tick_labels = [str(int(c)) if ((c >= 1) or (c == 0))  else str(c) for c in concs_true]
    ax.set_xlabel(r"concentration ($\mu M$)")
    ax.set_title(y)
    tick_locs = concs_plot
    plt.xticks(ticks=tick_locs, labels=tick_labels)
    # plt.xticks(ticks=np.log10(tick_locs), labels=tick_labels)
    return fig, ax