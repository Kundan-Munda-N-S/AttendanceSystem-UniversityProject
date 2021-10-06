# Unified Data Collection Stats Automation (AWS Lambda Script)
---
## Purpose:
- Fetch the **latest 6 weeks aggregate data** for FaceBook, Instagram, Twitter, Reddit and Stark model
- Send the fetched data as **slack messages** to a slack channel via slack web hook
- Update the latest two weeks fetched data to **AWS aurora** mysql database

---
<!-- table of contents -->
## Table of Contents
- [1. Program Structure](#1-program-structure) 
- [2. Dependencies used](#2-dependencies-used)
- [3. SQL Queries Used](#3-sql-queries-used)
---

### 1. Program Structure

- **[class : DataAggregatorReport](#11-class--dataaggregatorreport)**
  - [twitterAggregator()](#11a-twitteraggregator)
  - [facebookAggregator()](#11b-facebookaggregator)
  - [instragramAggregator()](#11c-instragramaggregator)
  - [redditAggregator()](#11dredditaggregator)
  - [starkAggregator()](#11estarkAggregator)
- **[class : WeeklyDataCollectionReport](#12-class--WeeklyDataCollectionReport)**
  - [dateRangeGenerator()](#12a-dateRangeGenerator)
  - [sendSlackMessage()](#12b-sendslackmessage)
  - [dataAggregatorReport()](#12c-dataaggregatorreport)
- **[main()](#)**

##### 1.1 class : DataAggregatorReport
**requires** two parameters *fromDateTime* (starting date range) and *toDateTime* (ending date range) which are used in the SQL queries to fetch records from AWS Athena for that particular date range. 

All the network functions defined are limited to return only the first **6** records of the weekly count data for the given date range.

All the queries for each particular network are defined as python dictionaries in their respective functions.


##### 1.1.a twitterAggregator()
returns the below columns
``` columns : [week, year, ]

```
##### 1.1.b facebookAggregator()
returns the below columns
``` columns : [week, year, ]

```
##### 1.1.c instragramAggregator()
returns the below columns
``` columns : [week, year, ]

```
##### 1.1.d redditAggregator()
returns the below columns
``` columns : [week, year, ]

```
##### 1.1.e starkAggregator()
returns the below columns
``` columns : [week, year, ]

```
##### 1.1.f sqlQueryExecuter(query)

- arguments : *"query"* - static *sql query* of type string 
- returns : sql output as *DataFrame*
---
##### 1.2 class : WeeklyDataCollectionReport
**requires** a *datetime* value for dateRangeGenerator() to work.
- uses **class : DataAggregatorReport** to fetch the data for a given date range.
- the dataframes fetched is formated/structured well to be sent to the slack channel

##### 1.2.a dateRangeGenerator()
###### **returns : python dictionary of start and end datetime for a date range** <br>

using the class variable *currentDateTime* sets the *operable datetime* to **previous week's Wednesday**
generates a start and end datetime range using the created datetime of wednesday and returns the start/from date as previous 7th week's wednesday and end/to date as previous week's tuesday.
Hence, ```@line-674 weekOffset = 7```

Example 01,
for any given date 2021-09-26 to 2021-10-02, **lastWednesdayDate = ""**
it will return a python dictionary
```fromDateTime : "", toDateTime: "" ```

Example 02,for any given date 2021-10-03 to 2021-10-09, **lastWednesdayDate = ""**
it will return a python dictionary
```fromDateTime : "", toDateTime: "" ```

##### 1.2.b sendSlackMessage(message , tableInfo)
```
arguments : 
 "message" = stringified table 
 "tableInfo" = heading for slack message 
```
sends the slack message as a post request for the specified *slack web hook*

###### **NOTE: slack web hook must be stored as an OS environment variable SLACK_WEB_HOOK_URL**

##### 1.2.c dataAggregatorReport(query)
###### invokes dateRangeGenerator()
###### uses **class : DataAggregatorReport** to fetch all the network dataframe for a given date range
###### structures/formats the table dataframe to be sent as slack messages
###### passes *message* and *tableInfo* and calls sendSlackMessage()

### 2. Dependencies used
```
datetime : Date Operations
pandas : SQL and Data Operations
pyathena : AWS Athena SQL query execution
requests : Slack HTTP Post request
tabulate : styling of tables for slack messages
```

### 3. SQL Queries Used

write all the sub-queries used
explain the overview of the columns, 
the database and column returned used,
