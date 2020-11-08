
import pandas as pd
import os
from bokeh.plotting import figure, output_file, show,output_notebook
output_notebook()
import pandas as pd
def make_dashboard(x, gdp_change, unemployment, title, file_name):
    output_file(file_name)
    p = figure(title=title, x_axis_label='year', y_axis_label='%')
    p.line(x.squeeze(), gdp_change.squeeze(), color="firebrick", line_width=4, legend="% GDP change")
    p.line(x.squeeze(), unemployment.squeeze(), line_width=4, legend="% unemployed")
    show(p)
path2='E:\\Python\clean_unemployment.csv'
path1 = 'E:\\Python\\clean_gdp.csv'
#for csv in os.listdir('.'):
#    df1=pd.read_csv(path1,engine='python')
#    df2=pd.read_csv(path2,engine='python')
df1=pd.read_csv(path1,engine='python')
df1

df2=pd.read_csv(path2,engine='python')
df2

x = df1.loc[0:len(df1.index),'date']
gdp_change =df1.loc[0:len(df1.index),'change-current']
unemployment =df2.loc[0:len(df2.index),'unemployment']
title = "my_dashboard"
file_name = "index.html"
make_dashboard(x, gdp_change, unemployment, title, file_name)