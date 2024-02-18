import pandas as pd
import matplotlib.pyplot as plt
from   collections import Counter
import argparse
import datetime
import logging
import intake
import copy
import os

def createDataFrameSummary(df: pd.core.frame.DataFrame
                          ) -> pd.core.frame.DataFrame:             # return summary dataframe
    '''
        Create a simple summary of a dataframe
    '''
    s_df = df.describe(include='all').T[['count','unique','top','freq']]            # use pandas.describe to summarize dataFrame
    s_df['Count %'] = (0.5 + (100 * s_df['count'] / len(df))).astype(int)           # Add Count % column (integer percents) to summary
    return s_df


def showCountsx(report: str,
               field: str):
    cnt_d = {'report':report, 'field':field, 'cnt':data_d[report]['summary'].loc[field,'count'], 'unique':data_d[report]['summary'].loc[field,'unique']}    
    print(f"{report} Report {field}: {data_d[report]['summary'].loc[field,'count']} unique: {data_d[report]['summary'].loc[field,'unique']}")
    return cnt_d


def findPublicationYear(row):
    '''
        The CHORUS reports include an Online Publication Year and a Print Publication Year.
        In order to include as many connections as possible, we need to combine these two columns.
        They are typically within one of each other, so it is generally a small change in the data.
    '''

    s = None                                                        # initialize s

    if 'Print Publication Date' in row.index:
        first =  'Print Publication Date'
    else:
        first = 'Publication_Print'

    if 'Online Publication Date' in row.index:
        second = 'Online Publication Date'
    else:
        second = 'Publication_Online'

    if isinstance(row[first], str):              # if Print Publication Date is a string
        s = row[first]
    elif isinstance(row[second], str):
        s = row[second]
    else:
        return

    if s:
        try:
            yr = pd.to_datetime(s, errors='coerce').dt.year
        except:
            yr = pd.to_datetime(s.split('T')[0], errors='coerce').year

        return yr

def str2year(s):
    '''
        This function converts dates expressed as strings into dates and retrieves the
        year from the date. str2year wraps the pandas.to_datetime functions as
        pd.to_datetime does this very well for many date formats, but it doesn't seem to
        handle timestamps...
    '''
    if not isinstance(s, str):
        return None
    
    try:
        yr = pd.to_datetime(s, errors='coerce').dt.year
    except:
        yr = pd.to_datetime(s.split('T')[0], errors='coerce').year

    return yr

def chooseDate(row,
              column_l: list):
    
    for c in column_l:
        if isinstance(row[c], str):
            return row[c]
    return

def chooseYear(row,
              column_l: list):
    '''
        Choose a date string from a list of column names.
        In some cases we want to choose a date column from a list columns where some may be blank. 
        For example, chose a Print Publication Date or an Online Publication Date if the Print 
        Publication Date is blank.

        This function is designed to be applied to a dataframe to add a new date column:
        data_df['Publication Year'] = data_df.apply(chooseYear, args=(['Print Publication Date', 'Online Publication Date'],), axis=1) 
    '''
    s = None
    for c in column_l:
        if isinstance(row[c], str):
            s = row[c]
            break

    return str2year(s)


def date_created_to_year(row):
    '''
        Extract the first four characters of a date string, the year, and return it as an int. This
        function is applied to a dataframe to create a year column from a date_created string:
        data_df['Dataset_date_created'] = data_df.apply(date_created_to_year, axis=1)
    '''
    if isinstance(row['date_created'], str):
        return int(row['date_created'][0:4])
    return


def showMostCommonSplit(df:              pd.core.frame.DataFrame,
                        item:            str,
                        delimiter:       str = None) -> pd.core.frame.DataFrame:
    '''
        Creater a dataframe with counts of values in a column 
        If delimiter is defined, split column content before counting.
        Return dataframe with item and count
        '''
    c = Counter()

    for i in df[item]:                              # loop item in dataframe
        if isinstance(i, str):                      # make sure content is string
            if delimiter is not None:
                for v in i.split(delimiter):        # split string using delimiter
                    c.update({v.strip(): 1})        # add items to counter
            else:
                c.update({i: 1})                    # add unsplit item to counter
    #
    # convert counter to dataframe and return
                #
    return (pd.DataFrame.from_dict(c, orient='index').reset_index().rename(columns={'index':'item', 0:'count'}))                                      # return Counter


def timeline(
    data_df,                                        # dataframe with data
    x:                       str,                   # column name for x axis (year)
    y:                       str,                   # column name for y axis (year, diff = y - x)
    x_name:                  str,                   # name for x-axis date
    y_name:                  str,                   # name for y-axis date
    selection_d:             dict,                  # dictionary with selection information and results
    chart_title:             bool = True,           # plot the data
    plot_data:               bool = False,          # plot the data
    data_size:               int  = 200,            # data point size (200 = full size, 20 = small)
    data_alpha:              float= 1,              # 1 = opaque, 
    plot_bubbles:            bool = True,           # plot the data as bubles
    bubble_scale:            int  = 6000,           # buble scale factor (default = 6000)         
    bubble_alpha:            float= 0.4,            # bubble alphs (default = 0.4)
    bubble_color:            str = '#756bb1',
    equality_line:           bool = True,           # plot line at journal = repository
    median:                  bool = True,           # plot data median
    median_color:            str  = '#54278f',
    publication_year_l:      list = [2012, 2023],         # plot lines at years
    bounds:                  tuple = (2012, 2024, -10, 10),  # (x_min, x_max, y_min, y_max)
    fig_size:                tuple = (25, 12),
    timestamp:               str   = None,
    saveFigure:              bool  = False
):
    '''
        This is the function for creating the timelines
        set up the plot with Year Dataset Collected at Repository as x-axis increasing to the right
        and y-axis = Paper - Data (time increasing upward)
    '''
    df = copy.deepcopy(data_df)

    if (df[x].count() == 0) or (df[y].count() == 0):                        # one of the year arrays has no data
        print(f'Missing data: x: {df[x].count()} y: {df[y].count()}')
        return
    
    df[y] = df[y].astype(float)
    df[x] = df[x].astype(float)
    df['difference'] =  df[y] - df[x]               # calculate difference between x and y for x-axis, add column to dataframe

    x_min, x_max, y_min, y_max  = bounds            # define min and max
    x_range = x_max - x_min
    y_range = y_max - y_min

    plot_df = df.groupby([x, 'difference']).size()       # plot_df groups selected_df by difference (x-axis) and y

    fig, ax = plt.subplots(figsize=fig_size)

    ax.axis([x_min, x_max, y_min, y_max])                           # define axis dimensions
    ax.set_xticks(range(x_min, x_max + 1))                          # x-ticks as range (-1 to 10)
    ax.set_yticks(range(y_min,y_max + 1))                           # y-ticks as range (2012 to 2024)
    ax.tick_params(axis='both', which='major', labelsize=18)        # tick label sizes
    ax.grid(linestyle='dashed', zorder = -1, color='#95BCD9')       # grid lines, zorder is attempt to get them behind data - doesn't work
    
    ax.set_xlabel(x, fontsize = 24)                                                         # x axis label
    ax.set_ylabel(y_name + ' Years Before ' + x_name + '  |  ' + y_name + ' Years After ' + x_name, fontsize = 24)      # y axis label

    if chart_title:
        ax.set_title(f"{selection_d['organization']}: {selection_d['value']} ({plot_df.sum()} Connections)", fontsize = 30)
    
    selection_d.update({'connectionCount': plot_df.sum()})

    if equality_line:
        ax.plot([x_min,x_max], [0,0], linestyle='dashed', color='grey')            # draw equality year (y = 0)
        
    for py in publication_year_l:                   # plot pubication years
        ax.plot([x_min + 2, x_max], [py - (x_min + 2), py - x_max], linestyle='dotted', color='grey')        # ax.plot([x1, x2], [y1,y2])
        x_txt   = (x_min + x_max)/2
        y_text  = (py - x_txt)
        y_text = y_text + 0.25 if y_text > 0 else y_text - 0.75               # adjust label for text

        ax.text(x_txt, y_text, py, fontsize=16,
                rotation=-45, rotation_mode='anchor',
                transform_rotates_text=True)
        
    if plot_data:
        ax.scatter(                     # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html
            data_df[x],                 # first column is x
            data_df[y],                 # second column is y
            s       = data_size, 
            alpha   = data_alpha
        )

    if plot_bubbles:
        ax.scatter(                                                     # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html
            plot_df.index.get_level_values(x),                          # second column is y
            plot_df.index.get_level_values('difference'),               # first column is x
            s=plot_df * bubble_scale / plot_df.max(),                   # general scaling of symbol size (x * actual size)
            color = bubble_color,
            alpha=bubble_alpha                                          # set transparancy and zorder (doesnt seem to work)
        )
        avg_count = round(plot_df.loc[x_min:x_max,y_min:y_max].mean(),0)
        ax.scatter(x_max - 2, y_max - 1.5, 
                   s =  avg_count * bubble_scale / plot_df.max(),
                   alpha = bubble_alpha, color = bubble_color
        )
        ax.annotate(f'= {avg_count:.0f} Connections', xy=(x_max -1.8,y_max - 1.5), fontsize = 16, verticalalignment='center')

    if median:                                                          # calculate the median position of plotted data and added to plot
        median_x = df[(df[x] >= x_min) & (df[x] <= x_max) ][x].median()
        median_y = df[(df['difference'] >= y_min) & (df['difference'] <= y_max) ]['difference'].median()

        selection_d.update({'median_x': median_x, 'median_y': median_y})   # add median to dictionary
        ax.scatter(                                                     # plot the median of the dataset 
            median_x, median_y,                                         # x,y calculated above
            marker = 'D', color = median_color,                         # marker is diamond
            s = 500                                                     # size is 500
        )
    #
    # calculate % of data before paper first (y <= -1 ([:-1]), data after paper (y >= 1 [1:]), and paper = data and add the results to the plot (annotate)
    #
    a_before = 100*plot_df.loc[x_min:x_max,:-1,].sum()/plot_df.loc[x_min:x_max,y_min:y_max].sum() if len(plot_df.loc[x_min:x_max,y_min:y_max]) > 0 else 0
    ax.annotate(f'{y_name} Before {x_name}: {a_before:.0f}%', xy=(x_min + .1,y_min + 0.2), fontsize = 16)

    a_after = 100*plot_df.loc[x_min:x_max, 1:].sum()/plot_df.loc[x_min:x_max,y_min:y_max].sum() if len(plot_df.loc[x_min:x_max,y_min:y_max]) > 0 else 0 
    ax.annotate(f'{y_name} After {x_name}: {a_after:.0f}%', xy=(x_min + .1,y_max - 0.7), fontsize = 16)

    a_d = 100*plot_df.loc[x_min:x_max,0:0].sum()/plot_df.loc[x_min:x_max,y_min:y_max].sum() if len(plot_df.loc[x_min:x_max,y_min:y_max]) > 0 else 0 
    ax.annotate(f'{y_name} = {x_name}: {a_d:.0f}%', xy=(x_min + .1,-0.8), fontsize = 16)

    selection_d.update({'a_before': a_before, 'a_after': a_after, 'a_d': a_d})

    if saveFigure:
        fileName = f"{selection_d['organization']}-{timestamp}-Timeline-{selection_d['value'].replace(' ','_').replace('/','_')}.png"
        plt.savefig(fileName)


class CHORUSReport:
    def __init__(self, dataPath):
        self.dataPath       = dataPath                                      # argument is the path of the data
        self.dataFile       = self.dataPath.split('/')[-1]                  # get file name from path
        organization, year, month, day, rt   = self.dataFile.split('-')[0:5]     # get organization and timestamp from the file name

        self.organization   = organization                                  # set object properties
        self.timestamp      = ''.join([year, month, day])
        rt = rt.replace('Report.csv','')
        if rt == 'All':
            self.dataType       = 'all'
        elif rt== 'AuthorAffiliation':
            self.dataType       = 'authors'
        else:
            self.dataType       = 'datasets'

        self.data_d             = {}

        if 'intake:' in dataPath:
            catalogName = CHORUSCatalogDirectory + '/' + 'chorusCatalog.yaml'
            intakeCat = intake.open_catalog(catalogName)
            sourceName    = '-'.join([organization,timestamp[0:4], timestamp[4:6], timestamp[6:8], dataTypes_d[self.dataType]['fileTitle']])
            self.data_d.update({'data':      intakeCat[sourceName].read()}) # add dataframe to dictionary
        else:
            self.data_d.update({'dataFile': dataPath})
            self.data_d.update({'data': pd.read_csv(dataPath, sep=',', encoding='utf-8')}) # add dataframe to dictionary

        self.data_d.update({'recordCount': len(self.data_d['data'])})

        data_df = self.data_d['data']
        #
        # Some csv files have blank, unnamed columns that are read into the dataframe and given names like Unnamed: columnNumber
        # These columns need to be removed from the dataframe before the summary is created.
        #   
        data_df.drop(data_df.columns[data_df.columns.str.contains('unnamed:',case = False)],axis = 1, inplace = True)

        self.data_d.update({'summary': createDataFrameSummary(data_df)})            # create summary dataframe
        summary_df = self.data_d['summary']                                         # pick summary dayaframe
        
        cols = ['organization','date','report','Property'] + list(summary_df.columns)     # add summary columns
        summary_df['top']           = summary_df['top'].str[:24]
        summary_df['organization']  = self.organization
        summary_df['date']          = self.timestamp
        summary_df['report']        = self.dataType
        summary_df['Property']      = summary_df.index
        self.data_d['summary']      = summary_df[cols] 
        self.data_d['data'].replace(r'^\s*$', None, regex=True, inplace=True)    # replace empty strings in dataframe with None to avoid counting them

    def x__init__(self, organization, timestamp, reportType):
        self.organization   = organization          # the organization selected for the report (typically funder)
        self.timestamp      = timestamp             # the time of retrieval of the report (YYYYMMDD_HH)
        self.data_d         = {}

    def __str__(self):
        return f"Datatype: {self.dataType} File: {self.dataFile} {self.data_d['recordCount']} rows"

    def data(self):
        return self.data_d['data']

    def summary(self):
        return self.data_d['summary']

    def info(self):
        self.data_d['data'].info()
    
    def counts(self,
               field: str):
        cnt_d = {'report':self.dataType, 'field':field, 'total count':self.summary().loc[field,'count'], 'unique':self.summary().loc[field,'unique']}
        return cnt_d
    
    def common(self, 
               item,
               delimiter:       str = None):
        #
        # add counts to CHORUSRetrieval 
        self.data_d.update({item: showMostCommonSplit(self.data_d['data'], item, delimiter)})            # create count dataframe

    
    def makeStandardElementNames(self):
        if 'standardNames' in dataTypes_d[self.dataType]:
            print(f"Replacing existing names with standard names in {self.dataType}: {dataTypes_d[self.dataType]['standardNames']}")
            self.data_d['data'] = self.data_d['data'].rename(columns=dataTypes_d[self.dataType]['standardNames'])

    def makePublicationYear(self):
        self.data_d['data']['Publication Year'] = self.data_d['data'].apply(chooseYear, args=(['Print Publication Date', 'Online Publication Date'],), axis=1)
        print(f"Data Type = {self.dataType}\nCounts: {self.data_d['data'][['Print Publication Date', 'Online Publication Date', 'Publication Year']].count()}")


    def convertDates2Years(self, date_l):
        '''
            Convert columns in date_l from dates to years
        '''
        for c in date_l:                                                    # loop the list of date columns
            if c in self.data_d['data'].columns:
                if 'Date' in c:
                    name_y = c.replace('Date', 'Year')                      # convert date strings to years (c -> name_y)
                else:
                    name_y = c + ' Year'                                    # if Date is not in the name - just add year to the column name (this is not usesd yet)

                self.data_d['data'][name_y] = self.data_d['data'][c].apply(lambda x: str2year(x))   # use lambda function to do the conversion


    def harmonizeRepositoryNames(self, repository_synonyms):
        '''
           Some repositories have changed names. This function standardizes the repository names throughout the dataset report. 
        '''
        data_df = self.data_d['data']
        if 'Dataset Repository Name' in self.data_d['data'].columns:            # check to make sure there is a column named 'Dataset Repository Name'
            for s_d in repository_synonyms:                                     # loop the synonyms
                for preferredName, synonym_l in s_d.items():
                    if preferredName == 'Preferred Name':                       # skip first item
                        continue
                    for s in synonym_l:
                        print(f"{len(data_df[data_df['Dataset Repository Name'] == preferredName])} rows with {preferredName}, replace {s} in {len(data_df[data_df['Dataset Repository Name'] == s])} rows.")
                        data_df['Dataset Repository Name'] = data_df['Dataset Repository Name'].str.replace('^' + s + '$', preferredName, regex=True)


    def readDateCreatedFromDOIMetadata(self, doi_metadataFile):
        print(f'Reading DOI metadata from {doi_metadataFile}')
        doi_metadata_df = pd.read_csv(doi_metadataFile,sep='\t',encoding='utf-8')
        doi_created_df = doi_metadata_df[['DOI', 'date_created']].drop_duplicates()
        print(f'{len(doi_metadata_df)} rows in date_created input {len(doi_created_df)} unique DOI/Date combinations')
        #
        # join the date_created column into data_df with Dataset DOI = DOI
        #
        self.data_d['data'] = pd.merge(self.data_d['data'], doi_created_df, left_on='Dataset DOI', right_on='DOI')
        self.data_d['data']['Dataset DOI Created'] = self.data_d['data'].apply(lambda x: date_created_to_year(x), axis=1)


class CHORUSRetrieval:
    def __init__(self, organization, timestamp, dir, dataType_l = ['all', 'authors', 'datasets']):

        self.report_d = {}
        self.organization   = organization                                  # set object properties
        self.timestamp      = timestamp
        self.ard = True

        for dt in dataType_l:
            dataFile        = dir + '/' + \
                              '-'.join([organization,timestamp[0:4], timestamp[4:6], timestamp[6:8], dataTypes_d[dt]['fileTitle']]) + \
                              'Report-ARD.csv'
            if os.path.isfile(dataFile):              # if the ARD file exists
                self.report_d.update({dt: CHORUSReport(dataFile)}) # add dataframe to dictionary
            else:
                self.ard        = False
                dataFile        = dir + '/' + \
                                  '-'.join([organization,timestamp[0:4], timestamp[4:6], timestamp[6:8], dataTypes_d[dt]['fileTitle']]) + \
                                  'Report.csv'
                self.report_d.update({dt: CHORUSReport(dataFile)}) # add dataframe to dictionary
        
    def __str__(self):
        s = f'Organization: {self.organization} Timestamp: {self.timestamp} Reports: {self.report_d.keys()}\n'
        for r in self.report_d.keys():
            s += str(self.report_d[r]) + '\n'
        return s
    
    def dataTypes(self):
        return list(self.report_d.keys())
        
    def dataTypes_d(self):
        return self.report_d.keys()
        
    def info(self):                                             # show information for reports in the retrieval
        for dt in self.dataTypes():                             # loop all data types
            self.report_d[dt].info()

    def data(self, dt):
        return self.report_d[dt].data_d['data']                 # return dataframe for all report
    
    def report(self, dt):
        return self.report_d[dt]

    def summary(self, dt):
        return self.report_d[dt].data_d['summary']              # return dataframe for all report

    def all(self):
        return self.report_d['all'].data_d['data']              # return dataframe for all report
    
    def authors(self):
        return self.report_d['authors'].data_d['data']          # return dataframe for authors report
    
    def datasets(self):
        return self.report_d['datasets'].data_d['data']         # return dataframe for all report
    
    def counts(self, dt, field):
        return self.report_d[dt].counts(field)
    
    def common(self,
               dataType:        str, 
               item:            str,    
               delimiter:       str = None):
    
        self.report(dataType).common(item, delimiter)

        
    def makeStandardElementNames(self):                                # call makeStandardElementNames for each report
        for dt in self.dataTypes():
            if 'standardNames' in dataTypes_d[dt]:
                self.report_d[dt].makeStandardElementNames()

    def makePublicationYear(self):
        for dt in self.dataTypes():                             # loop all data types
            self.report_d[dt].makePublicationYear()

    def convertDates2Years(self, date_l):
        for dt in self.dataTypes():                             # loop all data types
            self.report_d[dt].convertDates2Years(date_l)


    def harmonizeRepositoryNames(self, repository_synonyms):
        for dt in self.dataTypes():                             # loop all data types
            self.report_d[dt].harmonizeRepositoryNames(repository_synonyms)


    def readDateCreatedFromDOIMetadata(self, inputFile):
        self.report_d['datasets'].readDateCreatedFromDOIMetadata(inputFile)
    

    def checkColumnExists(self, check):
        if check[0] in self.data(check[1]).columns:
            return True
        return False

    def check_ARD(self):
        columnChecks = [('Publication Year','all'),
                        ('Publication Year','authors'),
                        ('Publication Year','datasets'),
                        ('Dataset DOI Created','datasets'),
                        ('Year Dataset Collected at Repository','datasets')
                    ]
        
        s = ''
        dt_l = self.dataTypes()

        for c in columnChecks:
            if (c[1] in dt_l) and self.checkColumnExists(c):
                s += f'{c[0]} is in {c[1]}\n'
        return(s)

    def consistency(self):
        '''
            Report Consistency Check
            The All Report has a row for each DOI and we expect them to all be unique, i.e. total count = unique. 
            The All Report also includes Authors and Datasets columns which have ";" separated lists of the authors 
            and datasets associated with each DOI. The all counts for these fields give the **number of DOIs with 
            associated authors and datasets**, not the total number of authors and datasets. These counts are <= to 
            the toal number of DOIs.  
            The Author Report has a row for each author (total count). The unique count is the number of DOIs with authors. 
            If all of the DOIs in the All Report are in the Author Report, the number of unique DOIs in these two reports would be equal.  
            The Dataset Report has datasets that are connected to the articles. These are discovered in ScholeXplorer. 
            The number of DOIs in this report reflects the number of connections discoverable usig ScholeXplorer.
        '''
        cnt_l = []
        cnt_d = {}
        cnt_d.update(self.counts('all', 'DOI'))
        cnt_l.append(copy.deepcopy(cnt_d))
        cnt_d.update(self.counts('all', 'Author(s)'))
        cnt_l.append(copy.deepcopy(cnt_d))
        cnt_d.update(self.counts('all', 'Datasets'))
        cnt_l.append(copy.deepcopy(cnt_d))
        cnt_d.update(self.counts('authors', 'DOI'))
        cnt_l.append(copy.deepcopy(cnt_d))
        cnt_d.update(self.counts('datasets', 'Article DOI'))
        cnt_l.append(copy.deepcopy(cnt_d))
        cnt_df = pd.DataFrame(cnt_l)
        print(cnt_df.to_string(index=False))
        allDOIs         = round(100 * cnt_df.loc[0,'unique'] / cnt_df.loc[0,'total count'],2)
        print(f"{round(100 * cnt_df.loc[0,'unique'] / cnt_df.loc[0,'total count'],2)}% of the DOIs in the All report are unique.")
        print(f"{round(100 * cnt_df.loc[1,'total count'] / cnt_df.loc[0,'total count'],2)}% of the DOIs in the All report have authors.")
        print(f"{round(100 * cnt_df.loc[2,'total count'] / cnt_df.loc[0,'total count'],2)}% of the DOIs in the All report have datasets.")
        doisWithAuthors = round(100 * cnt_df.loc[3,'unique'] / cnt_df.loc[0,'total count'],2)
        print(f"{doisWithAuthors}% of the DOIs in the All report have authors in the Authors report")


class DatasetReport(CHORUSReport):
    dataType    = 'datasets'
    fileTitle   = 'Dataset'
    pass

class AllReport(CHORUSReport):
    dataType = 'all'
    fileTitle   = 'All'
    pass

class AuthorReport(CHORUSReport):
    dataType = 'authors'
    fileTitle = 'AuthorAffiliation'
    pass

CHORUSDataDirectory     = os.getenv("HOME") + '/MetadataGameChanger/ProjectsAndPlans/INFORMATE/CHORUS/data'
CHORUSCatalogDirectory  = os.getenv("HOME") + '/MetadataGameChanger/Repositories/INFORMATE/CHORUS/data'

dataTypes_d = {'all':   {'fileTitle' : 'All',
                         'dtype'    : {'Datasets': 'object',
                                       'Issue': 'object',
                                       'ORCID': 'object',
                                       'Agency Portal URL': 'object',
                                       'Grant ID': 'object'}
                        },
            'authors':  {'fileTitle' : 'AuthorAffiliation',
                         'dtype' :  {'Affiliation': 'object', 
                                     'Issue': 'object',
                                     'ORCID': 'object',
                                     'Volume':'object',
                                     'Agency Portal URL': 'object',
                                     'Datasets (beta)': 'object'},
                         'standardNames':                           # dictionary used to change names ({existing:new})
                                    {
                                        'Publication_Online':'Online Publication Date',
                                        'Publication_Print':'Print Publication Date'
                                    }
                        },
            'datasets': {'fileTitle' : 'Dataset',
                         'dtype':{'Award Number': 'object','Award Title': 'object',
                                'Date Dataset Collected at Repository': 'object',
                                'Funder Identifier': 'object',
                                'Funder IdentifierType': 'object',
                                'Funder Name': 'object'},
                         'standardNames':
                                {
                                    'Article DOI':'DOI',
                                    'Date added to Repository':'Date Dataset Collected at Repository'
                                }
                        }
}
dataTypes   = list(dataTypes_d)


def main():
    #
    # retrieve command line arguments
    #
    commandLine = argparse.ArgumentParser(prog='CHORUS Reports',
                                          description='Library retrieving and analyzing CHORUS reports'
                                          )
    commandLine.add_argument("-dt","--dataTypes", nargs="*", type=str,    # DOIs on the command line
                        help='space separated list of dataTypes'
                        )
    commandLine.add_argument("-cdd","--CHORUSDataDirectory", type=str,    # DOIs on the command line
                        help='path to CHORUS data'
                        )
    commandLine.add_argument('--compareDOICounts', dest='compareDOICounts', 
                        default=False, action='store_true',
                        help='Compare DOI counts across reports'
                        )    
    commandLine.add_argument('--loglevel', default='info',
                             choices=['debug', 'info', 'warning'],
                             help='Logging level'
                             )
    commandLine.add_argument('--logto', metavar='FILE', nargs="*",
                             help='Log file (will append to file if exists)'
                             )
    # parse the command line and define variables
    args = commandLine.parse_args()

    if args.logto:
        # Log to file
        logging.basicConfig(
            filename=args.logto, filemode='a',
            format='%(asctime)s:%(levelname)s:%(name)s: %(message)s',
            level=args.loglevel.upper(),
            datefmt='%Y-%m-%d %H:%M:%S')
    else:
        # Log to stderr
        logging.basicConfig(
            format='%(asctime)s:%(levelname)s:%(name)s: %(message)s',
            level=args.loglevel.upper(),
            datefmt='%Y-%m-%d %H:%M:%S')

    lggr = logging.getLogger('DOI Metadata Tools')

    '''
        DOI Consistency Check
        The All Report has a row for each DOI and we expect them to all be unique, i.e. total count = unique. 
        The All Report also includes Authors and Datasets columns which have ";" separated lists of the authors 
        and datasets associated with each DOI. The all counts for these fields give the **number of DOIs with 
        associated authors and datasets**, not the total number of authors and datasets. These counts are <= to 
        the toal number of DOIs.  
        The Author Report has a row for each author (total count). The unique count is the number of DOIs with authors. 
        If all of the DOIs in the All Report are in the Author Report, the number of unique DOIs in these two reports would be equal.  
        The Dataset Report has datasets that are connected to the articles. These are discovered in ScholeXplorer. 
        The number of DOIs in this report reflects the number of connections discoverable usig ScholeXplorer.
    '''
    if args.compareDOICounts is True:
        print(f"{agency} {Date}")
        cnt_l = []
        cnt_d = {'agency':agency, 'date':timestamp}
        cnt_d.update(showCounts('all', 'DOI'))
        cnt_l.append(copy.deepcopy(cnt_d))
        cnt_d.update(showCounts('all', 'Author(s)'))
        cnt_l.append(copy.deepcopy(cnt_d))
        cnt_d.update(showCounts('all', 'Datasets'))
        cnt_l.append(copy.deepcopy(cnt_d))
        cnt_d.update(showCounts('authors', 'DOI'))
        cnt_l.append(copy.deepcopy(cnt_d))
        cnt_d.update(showCounts('datasets', 'Article DOI'))
        cnt_l.append(copy.deepcopy(cnt_d))
        cnt_df = pd.DataFrame(cnt_l)
        print(cnt_df)
        doisWithAuthors = round(100 * cnt_df.loc[3,'unique'] / cnt_df.loc[0,'cnt'],2)
        print(f"{doisWithAuthors}% of the DOIs in the All report have authors in the Authors report")


if __name__ == "__main__":
    main()

