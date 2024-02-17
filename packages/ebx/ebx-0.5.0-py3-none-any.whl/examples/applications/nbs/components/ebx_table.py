"""An ebx table component from the output of a run."""

import streamlit as st
from typing import List
from ebx.output import Output

def get_valid_outputs(outputs: List[Output]) -> List[Output]:
    """Filters for outputs that are tables."""
    return [output for output in outputs if output.type == "Table"]

def ebx_table(outputs: List[Output]):
    """For a given set of outputs from a run doc, display a table with the outputs."""
    st.write("## Tables")
    outputs = get_valid_outputs(outputs)

    if len(outputs) == 0:
        st.write("No outputs to display.")
        return
    
    output_names = [output.title for output in outputs]

    chosen_output = st.selectbox("Select an output", output_names, index=0)

    output = next(filter(lambda x: x.title == chosen_output, outputs))

    st.write(output.df)