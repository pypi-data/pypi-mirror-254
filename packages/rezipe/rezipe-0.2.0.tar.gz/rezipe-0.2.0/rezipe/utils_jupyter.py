from pint import UnitStrippedWarning
import pint_pandas
from tabulate import tabulate
import warnings

def hide_warnings():
    warnings.filterwarnings('ignore', category=UnitStrippedWarning)

hide_warnings()

def is_in_notebook():
    try:
        shell = get_ipython().__class__.__name__
        if shell == 'ZMQInteractiveShell':
            return True   # Jupyter notebook or qtconsole
        elif shell == 'TerminalInteractiveShell':
            return False  # Terminal running IPython
        else:
            return False  # Other type, e.g. IDLE
    except NameError:
        return False      # Probably standard Python interpreter

def show_dataframe(df):
    if is_in_notebook():
        display(df)
        return ""
    else:
        return tabulate(df)