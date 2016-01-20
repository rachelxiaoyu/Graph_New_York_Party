# New York Social Network
# Overview

This project aims to analyze the social network properties of New York’s social elite. The website [New York Social Diary](http://www.newyorksocialdiary.com/) provides a fascinating lens onto New York's socially well-to-do.  The data forms a natural
social graph for New York's social elite [Picturs] (http://www.newyorksocialdiary.com/party-pictures/2014/holiday-dinners-and-doers/)

The holity party pictures contains photos of the NY celetrities from 2007 to 2015. I have noticed that the photos have carefully annotated catpions labeling those that appear in the photos.  We can think of this as implicitly implying a social graph: there is a connection between two individuals if they appear in a picture together.

In this project, the captions of the photos were first grabed from the website. I have selected photos from parties before Dec 1st, 2014. I have further developed several rules to filter out the effective captions (captions that contain network information). The name was further grabbed from the captions. Finally, I performed the graph analysis using networkx.


