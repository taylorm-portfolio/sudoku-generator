# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import sqlite3

# Incorporate data

con = sqlite3.connect('sudokustats.db')

df1 = pd.read_sql_query('SELECT removedCells, count(runID), round(avg(runCountSolution),2), round(avg(runCountPuzzle),2), runDate FROM runs WHERE runDate = \'2024-03-11\' GROUP BY removedCells',con)
#df2 = pd.read_sql_query('SELECT removedCells, count(runId)')
renameDiary = {
    'removedCells': 'Qty Removed Cells',
    'count(runID)': '# of Runs',
    'round(avg(runCountSolution),2)': 'Avg # of Runs to Generate Solution',
    'round(avg(runCountPuzzle),2)': 'Avg # of Runs to Generate Puzzle',
    'runDate': 'Date Generator Run'
}
#runDates = list(df1['runDate'])
#print(runDates)
#dateOptions=[]
#[dateOptions.append(x) for x in runDates if x not in dateOptions]
#print(dateOptions)

# Initialize the app
app = Dash(__name__)

server = app.server

# App layout
app.layout = html.Div([
    html.Div(children='Statistical Analysis of Sudoku Generator Program Runs'),
    html.Hr(),
    #dcc.Dropdown(['New York City', 'Montréal', 'San Francisco'], 'Montréal',multi=True),
    dcc.RangeSlider(1,64,5,value=[1,64],id='page_slider'),
    #dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='lifeExp', id='controls-and-radio-item'),
    dcc.Graph(figure={},id='puzzle_runs_graph'),# id='controls-and-graph')
    dcc.Graph(figure={},id='sln_runs_graph'),# id='controls-and-graph')
    dash_table.DataTable(data=df1.to_dict('records'), columns=[{"name": renameDiary[i], "id": i} for i in df1.columns], page_size=10, id='data_table',
        filter_action="native")
])

@app.callback(
    Output(component_id='data_table', component_property='data'),
    Output(component_id='sln_runs_graph',component_property='figure'),
    Output(component_id='puzzle_runs_graph',component_property='figure'),
    Input(component_id='page_slider',component_property='value')
    #Input()
)

def update_table(slider_range):
    # Filter the DataFrame based on the slider range
    updated_data = df1[df1['removedCells'].between(slider_range[0], slider_range[1])]
    # Create the figure using the filtered DataFrame
    fig1 = px.bar(updated_data,x='removedCells',y='round(avg(runCountSolution),2)',labels=renameDiary)
    fig2 = px.bar(updated_data,x='removedCells',y='round(avg(runCountPuzzle),2)', labels=renameDiary)
    return updated_data.to_dict('records'), fig1, fig2
# Add controls to build the interaction

#def update_graph(slider_range):
#    df1 = df1[df1['removedCells'].between(slider_range[0], slider_range[1])],
#    fig = px.bar(df1,x='removedCells',y='avg(runCountSolution)',labels=renameDiary)
#    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)