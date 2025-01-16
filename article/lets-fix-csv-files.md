# CSV files: A universal format, yet universally frustrating. Let’s fix that!

> CSV files are universal, yet frustrating. Nanocell-csv fixes this by offering a fast, privacy-first tool for editing small tables and previewing large datasets. It prevents data corruption, ensures compatibility, and is fully crossplatform.

CSV files are the backbone of data exchange—simple, universal, and incredibly versatile. To this day, they are the best way to store tabular data in git repositories and probably the most universally used ETL file format (Extract Transform Load).  Yet, for something so ubiquitous, they often come with a frustrating reality: no tool seems to handle them quite right. Open a small file in Excel, and you're met with sluggish loading times and a minefield of potential data corruption. Try to preview a massive file, and you’re left twiddling your thumbs. Other specialized apps all seem archaic, are freemium at best, and often single-platform. It is time for change!

This is where [Nanocell-CSV](https://www.nanocell-csv.com/) comes in—a tool born out of necessity, frustration, and a relentless drive to simplify how we work with data.

Let me take you through the problem, the vision, and how I built a solution that’s fast, privacy-first, and available anywhere you need it.

## The Problem I Am Trying to Solve

Two use cases come to mind when working with CSV files:

1. **Small tables**, for which the data is input manually.  
2. **Large tables**, 1+ million rows, which are usually database extracts.

In the small table case, I want an MS Excel alternative that opens instantly, figures out the separator correctly, and does not corrupt my data. CSV is text and should remain that way. `+01` should stay `+01`, not be interpreted as `1`. I don't care about the graphs, visuals, and endless menus—I want to keep things simple. And, of course, I want to have all editing functions accessible from the keyboard.

In the large table case, I want to see its content instantly, but I don't really want to edit it. Actually, I would consider editing such tables outside of database tools and ETL pipelines as bad practice. I just want to view a large sample of the data, header and footer included, to get an idea of the file's content before moving on to expert tools to do my job. I have worked many years as a data analyst (even though my background is software engineering), and one of the main problems I came across is corrupted files that people have opened with editors (typically MS Excel) and then overwrote with the editor's standards. How often did I wish the company-wide default CSV file editor was locked in view-only mode for large files?

In both cases, I want the tool to run locally as data privacy is essential, and I don't want my company to be at risk of a data leak. 

Furthermore, I want the tool to be available anywhere. I work at a big BIG company, and my computer is subject to an admin lock for any `.exe` file I try to run. I don't want to go through the tedious bureaucratic process of asking for permission to install this one app.



## Adding in a Few Cool Features

As mentioned previously, one of my major pain points is data corrupted by MS Excel, mainly caused by people with regional settings that use a comma as the decimal separator. For example, `1.5` becoming `1,5`. This does not fit well in a Comma Separated Value file. So I've added a data validation feature that checks that all real numbers are written with a dot and not a comma. 

I also have an issue with financial data that is not saved with two digits after the decimal point. `$1.50` becomes `$1.5`, so I added a feature to round the column to two decimals. And, of course, an equivalent function to round everything up to integers if needed. 

Quotes and commas are, of course, tolerated in most CSV file standards but are considered bad practice. I've added text linting to highlight cell values that contain such unorthodox characters. Another feature also enables the user to replace all `,` with `-` and all `"` with `|`.

A major use case for [Nanocell-CSV](https://www.nanocell-csv.com/) is to quickly identify and resolve any unconventional issues in your data, typically before running a database import pipeline. [Nanocell-CSV](https://www.nanocell-csv.com/) makes sure that : headers are limited to alphanumeric characters, encoding is UTF-8, values do not contain line breaks, and much more. 


## Roadmap and Future Plans

As a lightweight editor, I believe [Nanocell-CSV](https://www.nanocell-csv.com/) is fairly mature. On the other hand, as a large database extract quick viewer, a lot more can be done. The major enhancements I will be working on in the foreseeable future will be to analyze those big files in the background as the quick view is displayed to offer in-depth analysis of the data. Typically, a correlation heatmap of each column or a histogram of value occurrences, etc.

Of course, these are just a few ideas. I want this project to be community-driven, so don't hesitate to tell me where to go from here. What started as a one-man engineering project is turning out to be a shared journey of innovation and collaboration with all. Join the ride!

[Link to Nanocell-CSV](https://www.nanocell-csv.com/)
