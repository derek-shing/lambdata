'''

The Splite Date class take a Series of Date in String type and break them into a 3 columns DataFrame.

The getSplitColumns() method will return that DataFrame

'''

import pandas as pd
import numpy as np


class SplitDateString:

    #Attribute

    year = 0
    month = 0
    day = 0
    dateformat = 0
    l=[]

    #Method:

    def __init__(self,string_date):    #Contructor
        self.l = string_date.split('-')
        self.year = int(self.l[0])
        self.month = int(self.l[1])
        self.day = int(self.l[2])



    pass


class SplitDate:
    df =pd.DataFrame()
    def __init__(self, dateseries):
        years = list()
        months = list()
        days = list()
        for i in dateseries.values:
            years.append(SplitDateString(i).year)
            months.append(SplitDateString(i).month)
            days.append(SplitDateString(i).day)
        print(years, months, days)
        self.df['year']=years
        self.df['month']=months
        self.df['day']=days

    def getSplitedColumns(self):
        return self.df

    pass

####   End of defination of Class ####






