# CHORUS Reports
[CHORUS](https://www.chorusaccess.org/) brings together funders, societies, publishers, institutions, and the public from across the open research ecosystem to share knowledge, develop solutions, advance innovation, and support collective efforts. CHORUS queries several repositories to collect data from the [Global Research Infrastructure](https://metadatagamechangers.com/blog/2023/12/25/chorus-data-journeys) and makes those data available in reports.  [Metadata Game Changers is working with CHORUS](https://metadatagamechangers.com/blog/2023/9/20/informate-metadata-game-changers-and-chorus-collaborate-to-make-the-invisible-visible) to understand these reports and help U.S. Funders and other users to understand them as well.

The CHORUSReports Package was developed by Metadata Game Changers to facilitate analysis of the CHORUS reports with focus on the All Report, the Author Affiliation Report, and the Dataset Report.

## CHORUSReports
The CHORUSReport object holds a CHORUS Report of any type and support operations on that on 

### Properties

| Property  | Description  |
|:---|:---|
|dataPath|Path to the data associated with the report.|
|dataFile|The name of the data file associated with the report (derived from dataPath.|
|organization|The acronym of the organization that the report data comes from (typically NSF, USGS, or USAID). The fileNames start with these acronymns.|
|timestamp|The timestamp (YYYYMMDD) of the data in the report, i.e., when it was retrieved from CHORUS)|
|dataType|The type of the data in the report (all, authors, datasets)|
|data_d|Data associated with the report, i.e. actual data or the summary of the data. Elements of the data_d are described below.|

## CHORUSRetrievals
The CHORUSRetrieval object holds a dictionary of related reports.

### Properties

| Property  | Description  |
|:---|:---|
|organization|The acronym of the organization that the report data comes from (typically NSF, USGS, or USAID). The fileNames start with these acronymns.|
|timestamp|The timestamp (YYYYMMDD) of the data in the report, i.e., when it was retrieved from CHORUS)|
|report_d|A dictionary of reports with keys = dataTypes|

### Functions
For a CHORUS Retrieval (cr) these functions are called as cr.function(arguments)

|Function  | Description  | Arguments | Returns|
|:---|:---|:---|:---|
|**dataTypes:**|Get the data types for reports in the retrieval|none|list of dataTypes in the retrieval (default: ['all', 'authors', 'datasets'])|
|**info:**|Get dataframe.info() for each dataframe in the retrieval|none|info()| 
|**data(dt):**|Get the data dataframe with dataType = dt from the retrieval|dataType, one of ['all', 'authors', 'datasets']|data dataframe for dataType.|  
|**summary(dt):**|Get the data dataframe with dataType = dt from the retrieval|dataType, one of ['all', 'authors', 'datasets']|summary dataframe for dataType.|	

