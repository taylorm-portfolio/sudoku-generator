# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import sqlite3

# Incorporate data

con = sqlite3.connect('sudokustats.db')

df1 = pd.read_sql_query('SELECT removedCells, count(runID), avg(runCountSolution), avg(runCountPuzzle) FROM runs GROUP BY removedCells',con)
#df2 = pd.read_sql_query('SELECT removedCells, count(runId)')
renameDiary = {
    'removedCells': 'Qty Removed Cells',
    'count(runID)': '# of Runs',
    'avg(runCountSolution)': 'Avg # of Runs to Generate Solution',
    'avg(runCountPuzzle)': 'Avg # of Runs to Generate Puzzle'
}


# Initialize the app
app = Dash(__name__)

server = app.server

# App layout
app.layout = html.Div([
    html.Div(children='Statistical Analysis of Sudoku Generator Program Runs'),
    html.Hr(),
    dcc.RangeSlider(1,64,5,value=[1,64],id='page_slider'),
    #dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='lifeExp', id='controls-and-radio-item'),
    dash_table.DataTable(data=df1.to_dict('records'), columns=[{"name": renameDiary[i], "id": i} for i in df1.columns], page_size=10, id='data_table',
        filter_action="native"),
    dcc.Graph(figure={},id='sln_runs_graph'),# id='controls-and-graph')
    dcc.Graph(figure={},id='puzzle_runs_graph')# id='controls-and-graph')
])

@app.callback(
    Output(component_id='data_table', component_property='data'),
    Output(component_id='sln_runs_graph',component_property='figure'),
    Output(component_id='puzzle_runs_graph',component_property='figure'),
    Input(component_id='page_slider',component_property='value')
)

def update_table(slider_range):
    # Filter the DataFrame based on the slider range
    updated_data = df1[df1['removedCells'].between(slider_range[0], slider_range[1])]
    # Create the figure using the filtered DataFrame
    fig1 = px.bar(updated_data,x='removedCells',y='avg(runCountSolution)',labels=renameDiary)
    fig2 = px.bar(updated_data,x='removedCells',y='avg(runCountPuzzle)', labels=renameDiary)
    return updated_data.to_dict('records'), fig1, fig2
# Add controls to build the interaction

#def update_graph(slider_range):
#    df1 = df1[df1['removedCells'].between(slider_range[0], slider_range[1])],
#    fig = px.bar(df1,x='removedCells',y='avg(runCountSolution)',labels=renameDiary)
#    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)