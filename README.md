# GlassFrog v3.0  
Link Crawling Keyword Search & Information Gathering Tool  

# How GlassFrog Works  
GlassFrog takes a Base URL which it uses to collect all existing links on the Base URL's webpage. While collecting links, it scans each page for the keyword as well as searching for other data types based on patterns in strings. GlassFrog will shift through various predefined **HTML Tags** searching for useful data.  

# Requirements  
All Python3 dependencies are in Core/requirements.txt & are automatically installed when running setup.  
**NOTE: GlassFrog uses the 'emojis' module which requires Python3.9. If you see an import error with 'emojis' module, set your Python interpreter to Python3.9 & run setup.** 

# Collectable Data Types  
* **Usernames/Handles**  
Such as Twitter handles (@username) [**Accurate**]  
* **Email Addresses**  
Based on the Base URL, it will get the URL's domain, create an email address from it & add it to a list(This helps to find business emails). Alternatively, it looks for '**MailTo:**' type links [**Accurate**]  
* **Other Domains**  
Links that are in text format, rather than as a link format [Accurate]  
* **Phone Numbers**  
Phone Numbers are a little more tricky as each website can format their numbers or display them differently. Alternatively it looks for '**tel:**' type links [**Semi-Accurate**]  
* **Bitcoin Addresses** [**Accurate**]  

# Install & Run  
```
git clone https://github.com/4xx404/GlassFrog && cd GlassFrog
sudo python3 setup.py
python3 glassFrog.py
```  

# GlassFrog-UI Web Interface  
For Ease of Accessibility, I have added a web interface which allows you to navigate through the collected data easily. Everything is built into the server so you just need to open the link you are given.
```
sudo python3 server.py
```  

# Modes  
Version 1, which includes all modes without data recognition, can be found [here](https://github.com/Ns0ciety/Glass-Frog). Version 1 will be deleted once each mode has been implemented into this version.  
* Single Keyword Search  
* Multiple Keyword Search (This hasn't yet been built for v3)  
* Use Custom URL Files (This hasn't yet been built for v3)  
* Base URL Search or Extended onto External Links found (Extended hasn't yet been built for v3)  

# Use Cases  
GlassFrog can be used to find a lot of useful information such as various types of contact information, usernames, hidden directories, friends/associates etc. The search is a dynamic search dependent solely upon the links it is able to collect. For example, a large site will yield a lot more results than a small site as the link collection would collect more pages.  

# Future Updates  
GlassFrog has had a pretty big update both on the Python side as well as the Web Interface side. I have quite a few things planned for this tool going forward, including plenty more updates to the Web Interface. Some of the things to come are:  
* Modes as listed above
* Data Types (Hashes, Locations)  
* More web based tools  
* More features in the UI to bring better functionality (Search Boxes/Dropdown Menus, Database Manager(create, edit, delete))  
