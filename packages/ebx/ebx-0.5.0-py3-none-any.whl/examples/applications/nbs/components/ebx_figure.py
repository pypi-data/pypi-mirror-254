"""Defines a plotly figure."""

import streamlit as st
from typing import List
from ebx.output import Output

def get_valid_outputs(outputs: List[Output]) -> List[Output]:
    """Filters for outputs that are figures."""
    return [output for output in outputs if output.type == "Chart"]

def ebx_figure(outputs: List[Output]):
    """For a given set of outputs from a run doc, display a figure with the outputs."""
    st.write("## Figures")
    outputs = get_valid_outputs(outputs)

    if len(outputs) == 0:
        st.write("No outputs to display.")
        return
    
    output_names = [output.title for output in outputs]

    chosen_output = st.selectbox("Select an output", output_names, index=0)

    output = next(filter(lambda x: x.title == chosen_output, outputs))

    st.plotly_chart(output.figure)