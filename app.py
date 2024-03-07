# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import sqlite3

# Incorporate data

con = sqlite3.connect('sudokustats.db')

df = pd.read_sql_query('SELECT removedCells, avg(runCountSolution), avg(runCountPuzzle) FROM runs WHERE removedCells < 50 GROUP BY removedCells',con)

renameDiary = {
    'removedCells': 'Qty Removed Cells',
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
    #dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='lifeExp', id='controls-and-radio-item'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=6),
    dcc.Graph(figure=px.bar(df,x='removedCells',y='avg(runCountSolution)', labels=renameDiary)),# id='controls-and-graph')
    dcc.Graph(figure=px.bar(df,x='removedCells',y='avg(runCountPuzzle)', labels=renameDiary))# id='controls-and-graph')
])

# Add controls to build the interaction
#@callback(
#    Output(component_id='controls-and-graph', component_property='figure'),
#    Input(component_id='controls-and-radio-item', component_property='value')
#)
#def update_graph(col_chosen):
#    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
#    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)