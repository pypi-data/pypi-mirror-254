"""Defines an output from earth blox."""

"""
----------------------------------------------------------------------------
COMMERCIAL IN CONFIDENCE

(c) Copyright Quosient Ltd. All Rights Reserved.

See LICENSE.txt in the repository root.
----------------------------------------------------------------------------
"""
from dataclasses import dataclass
import pandas as pd
from plotly import graph_objects as go
from plotly.io import from_json

@dataclass
class Output:
    title: str
    """The title of the output."""

    type: str
    """The type of output."""

    df: pd.DataFrame
    """The dataframe of the output, input as a dictionary."""

    resolution: float = None
    """The resolution of the output in metres."""

    figure: go.Figure = None
    """The figure of the output."""

    def __post_init__(self):
        """Convert the dictionary to a dataframe."""
        if self.df is not None:
            self.df = pd.DataFrame(self.df)

        if self.figure is not None:
            self.figure = from_json(self.figure)

    def show_figure(self):
        """Show the figure."""        
        if self.figure is None:
            raise ValueError("No figure to show.")

        self.figure.show()

    def get_dataframe(self):
        """Get the dataframe."""
        return self.df