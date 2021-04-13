# GlassFrog  
Link Crawling Keyword Search & Information Gathering Tool  
  
# How it works?  
GlassFrog takes a Base_URL which it uses to collect all existing links on the Base_URL's webpage. While collecting links, it will check each link for the keyword & if exists will return a result. This is the 2nd version of GlassFrog, where the first version relied more on luck for gathering information such as emails or usernames, this version looks for different data types based on patterns in strings. GlassFrog will shift through various html tag types searching for information.  

# Data Types it can find
* Usernames/Handles (Such as twitter handles @username) [Accurate]
* Email Addresses (Based on the base URL, it will find the Free Layer Domain & add it to a list(This helps to find business emails)) [Accurate]
* Other Domains that are in text format, rather than in a link [Accurate]
* Phone Numbers (This is a little tricky as each website can format their numbers slightly different. Alternatively it looks for 'tel:' type links) [Works Sometimes]
* Bitcoin Addresses [Accurate]
  
# Usage  
  
```
git clone https://github.com/4xx404/Glass-Frog && cd GlassFrog
chmod +x setup.py && ./setup.py
python3 glassFrog.py
```

# Output Digest
If the current line of output is [✓] Branch URL in GREEN then keyword has been found, otherwise it will show [✕] Branch URL in RED (Not Found).  
Other data types will be displayed as, for example, [✓] EMAIL: Email Address
  
# Quickly view the whole database
For Ease of Accessibility to the data collected, I have added a web interface which displays both tables. Everything is built into the server so you just need to open the ngrok link you are given. TIP: If your database is large, use CTRL + F in the browser to find something quickly.  
```
python3 server.py
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
