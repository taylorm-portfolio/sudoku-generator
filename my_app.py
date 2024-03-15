# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import sqlite3

# Incorporate data

con = sqlite3.connect('sudokustats.db')

df = pd.read_sql_query('SELECT runID, runDate, runCountSolution, runTimeSolution, runCountPuzzle, runTimePuzzle, runTimeOverall, removedCells FROM runs WHERE runDate = \'2024-03-11\'',con)
renameDiary = {
    'runID': 'Run ID',
    'runDate': 'Date Generator Run',
    'runCountSolution': 'Runs to Generate Solution',
    'runTimeSolution': 'Time (ms) to Generate Solution',
    'runCountPuzzle': 'Runs to Generate Puzzle',
    'runTimePuzzle': 'Time (ms) to Generate Puzzle',
    'runTimeOverall': 'Time (ms) to Run Entire Generator',
    'removedCells': 'Qty Removed Cells',
    'count(runID)': '# of Runs',
    'round(avg(runCountSolution),2)': 'Avg # of Runs to Generate Solution',
    'round(avg(runCountPuzzle),2)': 'Avg # of Runs to Generate Puzzle',
    
}
#df.close.rolling(5).mean()
dfPivotMA = pd.pivot_table(
    df, index=['removedCells','runID'],
    values=[
        'runCountSolution',
        'runCountPuzzle',
        'runTimePuzzle',
        'runTimeSolution',
        'runTimeOverall'
        ],
    aggfunc={
        'runCountSolution':'mean',
        'runCountPuzzle': 'mean',
        'runTimePuzzle': 'mean',
        'runTimeSolution': 'mean',
        'runTimeOverall': 'mean'
        }
    ).reset_index(drop = False).round({
        'runCountSolution': 2,
        'runCountPuzzle': 2,
        'runTimePuzzle': 6,
        'runTimeSolution': 6,
        'runTimeOverall': 6
    })
dfPivotMA['SlnMA5'] = dfPivotMA.runCountSolution.rolling(5).mean()
dfPivotMA['SlnMA15'] = dfPivotMA.runCountSolution.rolling(20).mean()
dfPivotMA['PzlMA5'] = dfPivotMA.runCountPuzzle.rolling(5).mean()
dfPivotMA['PzlMA15'] = dfPivotMA.runCountPuzzle.rolling(20).mean()

#print(dfPivotMA)
dfPivot = pd.pivot_table(
    df, index='removedCells',
    values=[
        'runCountSolution',
        'runCountPuzzle',
        'runTimePuzzle',
        'runTimeSolution',
        'runTimeOverall'
        ],
    aggfunc={
        'runCountSolution':'mean',
        'runCountPuzzle': 'mean',
        'runTimePuzzle': 'mean',
        'runTimeSolution': 'mean',
        'runTimeOverall': 'mean'
        }
    ).reset_index(drop = False).round({
        'runCountSolution': 2,
        'runCountPuzzle': 2,
        'runTimePuzzle': 3,
        'runTimeSolution': 3,
        'runTimeOverall': 3
    })
#print(dfPivot)

# Initialize the app
app = Dash(__name__)

server = app.server

# App layout

#app.layout = html.Div(className='row', children=[
#    html.H1("Graphs Side by Side"),
    #dcc.Graph(id="graph1", style={'display': 'inline-block'}),
    #dcc.Graph(id="graph2", style={'display': 'inline-block'})
#])
styleDiary = {
    'fontFamily': 'optima'
}
app.layout = html.Div(style=styleDiary,children=[
    html.H1('Statistical Analysis of Sudoku Generator Program Runs'),
    #dcc.Dropdown(['New York City', 'Montréal', 'San Francpage_sliderisco'], 'Montréal',multi=True),
    dcc.RangeSlider(1,64,5,value=[1,64],id='page_slider'),
    #html.Div(children=[
        #dcc.Graph(figure={},id='timeline_graph_pzl'),
        #dcc.Graph(figure={},id='timeline_graph_sln')
    #]),
    html.Div(children=[
        html.Div(children=[
            dcc.Graph(figure={},id='puzzle_runs_graph'),
            dcc.Graph(figure={},id='sln_runs_graph')
        ], style={'flex':1}),
        html.Div(children=[
            dcc.Graph(figure={},id='puzzle_time_graph'),
            dcc.Graph(figure={},id='sln_time_graph')
        ], style={'flex':1})
    ], style={'display': 'flex', 'flexDirection':'row'}),  
    dash_table.DataTable(data=dfPivot.to_dict('records'),columns=[{"name": renameDiary[i], "id": i} for i in dfPivot.columns], page_size=10, id='data_table', filter_action="native")
        
])

@app.callback(
    Output(component_id='data_table', component_property='data'),
    Output(component_id='puzzle_runs_graph',component_property='figure'),
    Output(component_id='sln_runs_graph',component_property='figure'),
    Output(component_id='puzzle_time_graph',component_property='figure'),
    Output(component_id='sln_time_graph',component_property='figure'),
    #Output(component_id='timeline_graph_pzl',component_property='figure'),
    #Output(component_id='timeline_graph_sln',component_property='figure'),
    Input(component_id='page_slider',component_property='value')
)

def update_table(slider_range):
    # Filter the DataFrame based on the slider range
    updated_data = dfPivot[dfPivot['removedCells'].between(slider_range[0], slider_range[1])]
    updated_data_pivot2 = dfPivotMA[dfPivotMA['removedCells'].between(slider_range[0], slider_range[1])]
    # Create the figure using the filtered DataFrame
    fig1 = px.bar(updated_data,x='removedCells',y='runCountPuzzle', labels=renameDiary, title='Average Loop Runs to Generate Puzzle')
    fig2 = px.bar(updated_data,x='removedCells',y='runCountSolution',labels=renameDiary, title='Average Loop Runs to Generate Solution')
    fig3 = px.bar(updated_data,x='removedCells',y='runTimePuzzle', labels=renameDiary, title='Average Loop Completion Time to Generate Puzzle')
    fig4 = px.bar(updated_data,x='removedCells',y='runTimeSolution', labels=renameDiary, title='Average Loop Completion Time to Generate Solution')
    #fig5 = px.line(updated_data_pivot2,x='runID',y=['PzlMA5','PzlMA15'])
    #fig6 = px.line(updated_data_pivot2,x='runID',y=['SlnMA5','SlnMA15'])
    return updated_data.to_dict('records'), fig1, fig2, fig3, fig4#, fig5, fig6
# Add controls to build the interaction

#def update_graph(slider_range):
#    df1 = df1[df1['removedCells'].between(slider_range[0], slider_range[1])],
#    fig = px.bar(df1,x='removedCells',y='avg(runCountSolution)',labels=renameDiary)
#    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)