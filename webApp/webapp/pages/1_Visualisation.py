import streamlit as st
import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv("webappdata.csv", parse_dates=['Date'], index_col='Date')
df.index = df.index.date

st.title("Data Visualisation")
st.write("This is my data visualisation tool. Please check the boxes which you would like to see plotted. Currency Hedged refers to returns of the portfolio "
         "as if they were in GBP or we fully removed the influence of currency fluctuations on portfolio value. Currency Un-Hedged is the opposite, and shows how "
         "currency movements can affect the value of our portfolio. "
         "You can hover over parts of the graph to see the values associated with a given day for each of the portfolios.")

fig = go.Figure()

st.subheader("Portfolio Value Selection")
st.write("Please select which portfolio values you would like to visualise:")

itp_h = st.checkbox('Index Tracking Portfolio - Currency Hedged', value=True)
itp_uh = st.checkbox('Index Tracking Portfolio - Currency Un-Hedged')
cgp_h = st.checkbox('Capital Growth Portfolio - Currency Hedged')
cgp_uh = st.checkbox('Capital Growth Portfolio - Currency Un-Hedged')
ftse_h = st.checkbox('FTSE 100 Index - Currency Hedged')
ftse_uh = st.checkbox('FTSE 100 Index - Currency Un-Hedged')

# Add traces based on the selected checkboxes
if itp_h:
    fig.add_trace(go.Scatter(x=df.index, y=df['ITP_H'], mode='lines', name='Index Tracking Portfolio - Currency Hedged', line=dict(color='red')))
if itp_uh:
    fig.add_trace(go.Scatter(x=df.index, y=df['ITP_UH'], mode='lines', name='Index Tracking Portfolio - Currency Un-Hedged', line=dict(color='orange')))
if cgp_h:
    fig.add_trace(go.Scatter(x=df.index, y=df['CGP_H'], mode='lines', name='Capital Growth Portfolio - Currency Hedged', line=dict(color='green')))
if cgp_uh:
    fig.add_trace(go.Scatter(x=df.index, y=df['CGP_UH'], mode='lines', name='Capital Growth Portfolio - Currency Un-Hedged', line=dict(color='blue')))
if ftse_h:
    fig.add_trace(go.Scatter(x=df.index, y=df['FTSE_H'], mode='lines', name='FTSE 100 Index - Currency Hedged', line=dict(color='purple')))
if ftse_uh:
    fig.add_trace(go.Scatter(x=df.index, y=df['FTSE_UH'], mode='lines', name='FTSE 100 Index - Currency Un-Hedged', line=dict(color='pink')))

# Update layout
fig.update_layout(
    xaxis_title='Date',
    yaxis_title='Value of Portfolio - Initial $50m Investment',
    legend_title='Legend',
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.3,
        xanchor="center",
        x=0.5
    ),
    width=1200,
    height=800
)

st.title("Portfolio Value Visualisation")
st.plotly_chart(fig)

# Define the available options for the dropdown menu
options = {
    'Index Tracking Portfolio - Currency Hedged': 'ITP_H',
    'Index Tracking Portfolio - Currency Un-Hedged': 'ITP_UH',
    'Capital Growth Portfolio - Currency Hedged': 'CGP_H',
    'Capital Growth Portfolio - Currency Un-Hedged': 'CGP_UH',
    'FTSE 100 Index - Currency Hedged': 'FTSE_H',
    'FTSE 100 Index - Currency Un-Hedged': 'FTSE_UH'
}
st.write("")
st.subheader("Daily Dollar Changes")
selected_options = st.multiselect(
    'Please select up to two Portfolios to visualise the daily dollar changes for:',
    list(options.keys()),
    max_selections=2
)

# Define a color map for the options
colour_map = {
    'ITP_H_D': 'red',
    'ITP_UH_D': 'orange',
    'CGP_H_D': 'green',
    'CGP_UH_D': 'blue',
    'FTSE_H_D': 'purple',
    'FTSE_UH_D': 'pink'
}

# Extract the corresponding columns for the bar chart based on the selected options
selected_columns = [options[option] for option in selected_options]

# Create the Plotly figure for the bar chart
fig_bar = go.Figure()

# Add traces for bar charts based on the selected options with correct colors
for option in selected_options:
    column = options[option]
    fig_bar.add_trace(go.Bar(x=df.index, y=df[f'{column}_D'], name=option, marker=dict(color=colour_map[f'{column}_D'])))

# Update layout for the bar chart
fig_bar.update_layout(
    xaxis_title='Date',
    yaxis_title='Dollar Change - Close to Close from Previous Day',
    legend_title='Legend',
    barmode='stack',
    legend=dict(
        orientation="h",
        yanchor="bottom",
        y=-0.3,
        xanchor="center",
        x=0.5
    ),
    width=1200,
    height=800
)

# Display the Plotly chart in Streamlit
st.title("Daily Change in Portfolio Value Visualisation - Dollars")
st.plotly_chart(fig_bar)