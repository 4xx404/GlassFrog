# GlassFrog  
Link Crawling Keyword Search Tool  
  
# How it works?  
GlassFrog requires the user to set a Base_URL which it uses to collect all links existing on the Base_URL's webpage. It will check each links webpage for the keyword & print the link if it exists within the pages content. Should you choose to 'extend' the search, it will continue to collect all other links from sub-link webpages & also search for the keyword in their pages content.  
  
# Usage  
  
```
git clone https://github.com/4xx404/GlassFrog && cd GlassFrog
python3 -m pip install -r requirements.txt
python3 glassFrog.py
```
  
# Uses  
GlassFrog can find a lot of useful information such as various types of contact information, usernames, hidden directories, etc. The search is a dynamic search dependent solely upon the links it is able to collect, meaning there is no 'average' search time nor length of results. Seaches can vary from minutes to hours.  
