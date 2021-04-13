# GlassFrog  
Link Crawling Keyword Search & Information Gathering Tool  
  
# How it works?  
GlassFrog takes a Base_URL which it uses to collect all existing links on the Base_URL's webpage. While collecting links, it will check each link for the keyword & if exists will return a result. This is the 2nd version of GlassFrog, where the first version relied on luck for gathering information such as emails or usernames, this version looks for different data types based on patterns in strings.  

# Data Types it can find
* Usernames/Handles (Such as twitter handles @username) [Accurate]
* Email Addresses (Based on the base URL, it will find the Free Layer Domain & add it to a list(This helps to find business emails)) [Accurate]
* Other Domains that are in text format, rather than in a link [Accurate]
* Phone Numbers (This is a little tricky as each website can format their numbers slightly different) [Works Sometimes]
* Bitcoin Addresses [Accurate]
  
# Usage  
  
```
git clone https://github.com/4xx404/Glass-Frog && cd GlassFrog
chmod +x setup.py && ./setup.py
python3 glassFrog.py
```
  
# Quickly view the whole database
```
python3 server.py
navigate to the link the server gives you
```
  
# Modes (All will find data types automatically)
* Single Keyword Search
* Multiple Keyword Search (This hasn't yet been built for v2. but will be)
* Use Custom URL Files (This hasn't yet been built for v2, but will be)
* Base URL Search or Extended onto External Links found (Extended hasn't yet been built for v2, but will be)
  
# Uses  
GlassFrog can be used to find a lot of useful information such as various types of contact information, usernames, hidden directories, friends/associates etc. The search is a dynamic search dependent solely upon the links it is able to collect. For example, a large site will yield a lot more results than a small site as the link collection would collect more pages.  
  
# Data Type Requests  
I am interested in introducing as many types as possible. If you have any suggestions for a type to add, feel free to contact me on Discord to discuss: 4xx404#3398  
