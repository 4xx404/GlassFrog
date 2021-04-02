# GlassFrog  
Link Crawling Keyword Search Tool  
  
# How it works?  
GlassFrog requires the user to set a Base_URL which it uses to collect all links existing on the Base_URL's webpage. It will check each links webpage for the keyword & print the link if it exists within the pages content. Should you choose to 'extend' the search, it will continue to collect all other links from sub-link webpages & also search for the keyword in their pages content.  
  
# Usage  
  
```
git clone https://github.com/4xx404/Glass-Frog && cd GlassFrog
python3 -m pip install -r requirements.txt
python3 glassFrog.py
```
  
# Modes
* Single Keyword Search
* Multiple Keyword Search
* Use Custom URL Files
* Base URL Search or extend onto External Links found
  
# Uses  
GlassFrog can be used to find a lot of useful information such as various types of contact information, usernames, hidden directories, friends/associates etc. The search is a dynamic search dependent solely upon the links it is able to collect, meaning there is no 'average' search time nor length of results. Searches can vary from minutes to hours.  
