import hvplot as hv
import hvplot.pandas
import hvplot.xarray
import pandas as pd
import streamlit as st
import xarray as xr
from bokeh.models import ColumnDataSource, CustomJS, DataTable, TableColumn
from bokeh.plotting import figure
from streamlit_bokeh3_events import streamlit_bokeh3_events

hv.extension("bokeh", logo=False)

df = pd.DataFrame(
    {
        "x": [1, 2, 3, 4],
        "y": [4, 5, 6, 7],
    }
)
# create plot
cds = ColumnDataSource(df)
columns = [
    TableColumn(field="x"),
    TableColumn(field="y"),
]

# define events
cds.selected.js_on_change(
    "indices",
    CustomJS(
        args=dict(source=cds),
        code="""
        document.dispatchEvent(
        new CustomEvent("INDEX_SELECT", {detail: {data: source.selected.indices}})
        )
        """,
    ),
)
p = DataTable(source=cds, columns=columns)
result = streamlit_bokeh3_events(
    bokeh_plot=p,
    events="INDEX_SELECT",
    key="foo",
    refresh_on_update=False,
    debounce_time=0,
    override_height=200,
)

if result:
    if result.get("INDEX_SELECT"):
        st.write(df.iloc[result.get("INDEX_SELECT")["data"]])

# Second

ds = xr.tutorial.open_dataset("air_temperature.nc").rename({"air": "Tair"})

# st.bokeh_chart(hv.render(ds.Tair.hvplot(), backend="bokeh"))
result = streamlit_bokeh3_events(
    bokeh_plot=hv.render(ds.Tair.hvplot(), backend="bokeh"),
    key="what",
    refresh_on_update=False,
    debounce_time=0,
)


st.write(result)
