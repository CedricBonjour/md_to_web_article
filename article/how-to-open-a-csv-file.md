# How to open large CSV files with Nanocell-csv

> CSV files are a universal data table format, so why is it complicated to open them? Nanocell-csv gives a simple, fast, and elegant solution, especially to preview very large files.

CSV files are mostly used as a medium to transfer data from one database to another as it is the one format guaranteed to be handled by all systems.  You also find them in code repositories as they are the best way to store rows of data in text files.  

However universally used they may be, no tool seems to handle them quite right. CSV files tend to be opened by MS Excel by default. However Excel turns out to be slow, does not detect the columns correctly, and even corrupts data by dropping leading zeros and plus signs (typically in phone numbers or postal codes).

This is where [Nanocell-csv](https://www.nanocell-csv.com/) comes in.




## Installing Nanocell-csv

This can't get any simpler.
1. Go to [https://www.nanocell-csv.com/](https://www.nanocell-csv.com/) using a chrome based browser (chrome, edge, chromium, etc...)
2. Click on install in the top right corner
3. Confirm the install prompt.
4. You're done!

> No install `.exe` file that prompts for admin permission
> No download time
> No hassle. 


## Opening a file for the first time

[Nanocell-csv](https://www.nanocell-csv.com/) should have been detected as the default application for CSV files.
Double clicking on any CSV file should thus open it in Nanocell-csv. 

If that is not the case: 
- right click on a csv file 
- select :  `Open with...` 
- select : `Choose another app`
- select : `Nanocell-csv` and click on `Always`


## Setting your preference 

Click on the following icon in the top right corner:

 ![settings-icon](https://www.nanocell-csv.com/app/icn/menu/settings.svg) 

You can change the theme color palette in as the first option. You may also want to change the number of rows, columns or the text size to make [Nanocell-csv](https://www.nanocell-csv.com/) as comfortable as possible on your screen and needs. 

## What if the file being opened is huge, let's say 20 GB ?!

[Nanocell-csv](https://www.nanocell-csv.com/) has no limit on file size. It will change to a better suited approach when opening large files. Your 20GB file will still open instantly but in read only mode to give you a quick overview of what the file may contain.  This is achieved by sampling the header, the footer and a few rows at regular intervals without parsing the entire file. The goal here is for you to quickly understand what you are dealing with when first opening a file before loading it in more expert tools for transforming big data. 

Nanocell-csv considers editing such large tables outside of database tools, and ETL pipelines as bad practice (Python pandas, R, SQL, Spark ...). Such tools often lack a quick preview feature.
For these reasons, [Nanocell-csv](https://www.nanocell-csv.com/) simply aims to be a fast preview tool.

> No file size limit !
> Instant preview ! 


![screenshot of big data view](https://www.nanocell-csv.com/img/screenshot/bigdata_preview.webp)

[Link to Nanocell-csv](https://www.nanocell-csv.com/)