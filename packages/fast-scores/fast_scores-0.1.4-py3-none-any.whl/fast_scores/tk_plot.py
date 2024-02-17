"""Plot a matplotlib fig on a tkinter widget win (tkinter.Tk() or tkinter.Frame)."""
from typing import Optional, Union
import tkinter as tk
import tkinter.ttk as ttk
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


def tk_plot(
    fig: matplotlib.figure.Figure,
    win: Optional[Union[tk.Tk, ttk.Frame]] = None,
    title: str = "",
    toolbar: bool = True,
) -> FigureCanvasTkAgg:
    r"""Plot matplotlib figues in a tkinter.Tk/Frame.

    Args:
        fig: matplotlib figure
        win: tkinter.Tk() or tkinter.Frame()
        title: tkinter widget title
        toolbar: if set to True, a toolbar (matplotlib toolbar) is shown

    Returns:
        canvas: a FigureCanvasTkAgg, run canvas.draw() to update.

    snippets\tkinter drawfig*.py (PySimpleGUi matplotlib exampl)
    matplotlib cookbook: Embedding Matplotlib in a Tkinter GUI application

    matplotlib.use('TkAgg')

    import seaborn as sns
    sns.set_theme()
    sns.set_style("whitegrid")
    matplotlib.pyplot.ion()  # for testing in ipython

    from matplotlib.gridspec import GridSpec

    # gs = GridSpec(3, 1)
    # gs = fig.add_gridspec(2, 2)
    # ax = fig.add_subplot(gs[0, :])

    import numpy as np
    ax = fig.add_subplot()
    t = np.arange(0, 3, .01)
    ax.plot(t, 2 * np.sin(2 * np.pi * t))
    canvas.draw()

    # fig.clf()
    ax.cla()
    ax = fig.add_subplot(gs[0, :])
    ax.plot(np.sin(2 * np.pi * t))
    canvas.draw()
    """
    if win is None:
        win = tk.Tk()
        if title:
            win.wm_title(title)
        else:
            win.wm_title("Fig in Tk")

    canvas = FigureCanvasTkAgg(fig, win)
    canvas.get_tk_widget().pack(side="top", fill="both", expand=1)
    if toolbar:
        NavigationToolbar2Tk(canvas, win)

    tk_plot.win = win
    # tk_plot.win.destroy() to exit

    return canvas


def main(root):
    """Run."""
    win = ttk.Frame(root)
    win.pack()

    fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)

    # canvas = tk_plot(fig)
    # tk_plot.win.destroy()  # to kill

    canvas = tk_plot(fig, win)

    canvas.draw()
    canvas.cla()  # to clear the canvas

    _ = """
    # update fig
    ax1 = fig.add_subplot(211)  # gs[,] gs = mpl.gridspec.GridSpec(3,1)
    # ax1.plot(...) or sns.heatmap(ax=ax1), df.plot(..., ax=ax)
    canvas.draw()

    # fig.clear()  # fig.clf()
    #
    # ax1.cla()
    """


if __name__ == "__main__":
    # in ipython
    # %matplotlib tk
    root = tk.Tk()
    root.wm_title("Fig in Tk")

    main(root)
    root.mainloop()
