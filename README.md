# New York Social Network
# Overview

This project aims to analyze the social network properties of New York’s social elite. The website [New York Social Diary](http://www.newyorksocialdiary.com/) provides a fascinating lens onto New York's socially well-to-do.  The data forms a natural
social graph for New York's social elite. You may assess the list of events [Here] (http://www.newyorksocialdiary.com/party-pictures)

The holiday party pictures contains photos of the NY celebrities from 2007 to 2015. I have noticed that the photos have carefully annotated captions labeling those that appear in the photos.  We can think of this as implicitly implying a social graph: there is a connection between two individuals if they appear in a picture together.

In this project, the captions of the photos were first scraped from the website. I have selected photos from parties before Dec 1st, 2014. I have further developed several rules to filter out the effective captions (captions that contain network information). The total number of valid captions was 93,093. The name was further grabbed from the captions and we have found a total of 113,031 names in the social network. Finally, I performed the graph analysis using networkx. The graph visualization can be viewed using the following [link].


# Result

The figure below shows a capture of the graph distribution using SVG forced direct graph ![image](https://cloud.githubusercontent.com/assets/14169124/12463445/7ca5fbf4-bf91-11e5-979b-422f07e02e2b.png)


I have further quantified the graph properties in terms of the degree, page rank, and similarities of friends. 

Here are some interesting results:
# Degree

Top 10 people with most number of friends:
'Jean Shafiroff' 591   
'Mark Gilbertson' 448   
'Gillian Miniter' 399  
'Geoffrey Bradfield', 331  
(Alexandra Lebenthal', 318  

