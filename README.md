# Project: Customer-Prioritization-for-Marketing


## Problem Statement

Thousands of potential customers visit our website every day for a free horoscope report, some of which actually result in a conversion.

Due to limited human resources, we are unable to reach out to each one of those thousands of potential customers each day. In addition to being infeasible for us, it is probably not necessary either. 

To help filter the long list into something manageable by the sales team, we came up with a baseline model that prioritizes the customers we reach out to each day. The baseline model was built in a hurry without any serious data analysis and it is just a static formula taking as input certain values generated from browsing sessions.

Over the years, we have found that a majority of the potential customers we reach out to do not result in an immediate conversion. 

We want to use data and technology to maximize conversions from our contacts each day.


## Expected Solution

The solution should consist of the following:

1. A report containing key summaries and insights from historical data.

2. A data science product using an ML model to prioritize the potential list of customers. 
<pre>
     The predictions report (filename format: top_250_report_ddmmyyyy.csv) 
     should be limited to the top 250 customers with the following fields:

          customer_id, conversion_probability 
   
     The model needs to consider only those customers who visited our 
     website within the last 24 hours.
</pre>
3. An evaluation report showing at least 50% increase in the conversions when compared with the baseline model (over a period of 7 days).


## Project Members
  
Owner                       : <a href="https://github.com/rutuja027">Rutuja Yerunkar</a>  
Lead / Instructor           : <a href="https://github.com/ngkpg">Neeraj Garg</a>  

## Live Demo 

Try it yourself @ https://packt-cpm.herokuapp.com/ <br>
Choose dates between May'21 and July'21
