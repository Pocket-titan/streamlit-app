import holoviews as hv
import hvplot
import hvplot.pandas
import hvplot.xarray
import numpy as np
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import xarray as xr
from bokeh.io import output_file
from bokeh.models import BoxInteractionHandles
from bokeh.plotting import figure, save
from streamlit_bokeh3_events import streamlit_bokeh3_events

hv.extension("bokeh", logo=False)


# def use_file_for_bokeh(chart: figure, chart_height=500):
#     output_file("bokeh_graph.html")
#     save(chart)
#     with open("bokeh_graph.html", "r", encoding="utf-8") as f:
#         html = f.read()
#     components.html(html, height=chart_height)


# st.bokeh_chart = use_file_for_bokeh


# df = pd.DataFrame({"x": [0, 1, 2, 3, 4, 5, 6], "y": [2, 6, 4, 6, 8, 3, 5]})

# st.dataframe(df)

# p = figure(x_axis_label="x", y_axis_label="y")
# p.line(df.x, df.y)
# st.bokeh_chart(p)


st.title("🎈 My new app!")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

x = st.slider("x")
st.write(x, "squared is", x * x)


df = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})

option = st.selectbox("Which number do you like best?", df["first column"])

"You selected: ", option

add_slider = st.sidebar.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button("Press me!")

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        "Sorting hat", ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin")
    )
    st.write(f"You are in {chosen} house!")


# create sample data
@st.cache
def get_data():
    return pd.DataFrame(data=np.random.normal(size=[50, 2]), columns=["col1", "col2"])


df = get_data()

# streamlit plotting works
st.line_chart(df)

# creating a holoviews plot
nice_plot = df.hvplot(kind="scatter")

st.bokeh_chart(hv.render(nice_plot, backend="bokeh"))


"This is xarray:"

ds = xr.tutorial.open_dataset("air_temperature.nc").rename({"air": "Tair"})

st.bokeh_chart(hv.render(ds.Tair.hvplot(), backend="bokeh"))

st.bokeh_chart(hv.render(ds.Tair.isel(time=1).hvplot(cmap="fire"), backend="bokeh"))

streamlit_bokeh3_events(
    hv.render(ds.Tair.isel(time=1).hvplot(cmap="fire"), backend="bokeh"), key="one"
)

air_ds = xr.tutorial.open_dataset("air_temperature").load()
air = air_ds.air

streamlit_bokeh3_events(
    hv.render(air.hvplot(groupby="time", width=500), backend="bokeh"),
    key="two",
)

streamlit_bokeh3_events(
    hv.render(
        ds.Tair.hvplot(
            groupby="time",  # adds a widget for time
            clim=(250, 295),  # sets colormap limits
            widget_type="scrubber",
            widget_location="bottom",
        ),
        backend="bokeh",
    ),
    key="three",
)
