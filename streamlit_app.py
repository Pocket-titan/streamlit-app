import holoviews as hv
import hvplot
import hvplot.pandas
import numpy as np
import pandas as pd
import streamlit as st

hv.extension("bokeh", logo=False)


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

# this doesn't work unfortunately. How can i show 'nice_plot'
st.bokeh_chart(nice_plot)
