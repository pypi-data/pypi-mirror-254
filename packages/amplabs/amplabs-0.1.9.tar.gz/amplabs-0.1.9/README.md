## _AmpLabs_

AmpLabs is a open source platform which provides easy way of data visualisation. 


# Description 

Built on top of Plotly.js, Dash, Pandas and Flask, AmpLabs ties modern UI elements like dropdowns and graphs directly to analytical Python code. 

Method provided - 

| Method | Description | Parameter | Return value |
| ------ | ----------- | --------- | ------------ |
| readCSV | method to read a csv file | file_path = path of the file to read | dataframe |
| readDAT | method to read a dat file | file_path = path of the file to read | dataframe |
| readTDMS | method to read a tdms file | file_path = path of the file to read | dataframe |
| minutesToSeconds | method to convert time column from minutes to seconds | column = column list that has to be converted | converted column list |
| showHeaders | method to display list of headers | df = dataframe | list of headers |
| convertToExcel | method which convert a dataframe to excel file | df = dataframe, file_path = path of the file where it should be saved | - |
| addHeaders | method to add headers to the dataframe | df = dataframe, column_list = list of columns that should be added | dataframe |
| plot   | method to generate graph from the data frame | data_list = list of dataframes, data_names = list of names of dataframes | colors(optional) = list of colors | - |



# Other Services by AmpLabs
- Website to upload and plot data on cloud [www.app.amplabs.ai]
- Desktop Application to visual data locally 
