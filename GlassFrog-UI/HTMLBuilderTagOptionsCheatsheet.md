# HTMLBuilder Tag/Options CheatSheet  

# Create HTMLBuilder Object  
```
<?php 
	$HTMLBuilder = new HTMLBuilder();
```  

**Create Anchor Tag (a)**  
* Options  
**class** - Element Class Name  
**id** - Element ID Name  
**href** - Link to direct to on element click  
**placeholder** - The value displayed on the front end website  
```
    $HTMLBuilder->CreateLinkElement(array(
	    "class" => "example-element-class",
    	"id" => "example-element-id",
	    "href" => "https://www.example.com/",
	    "placeholder" => "Visit Example Website"
    ));
```  

**Create Button Tag (button)**  
* Options  
**type** - "", "button" or "reset"  
**class** - Element Class Name  
**id** - Element ID Name  
**value** - Button Value  
**disabled** - "" or "disabled"  
**js_event** - "onclick", "onfocus" or "onfocusout"  
**js_function** - JavaScript Function Name  
```
    $HTMLBuilder->CreateButtonElement(array(
        "type => "button"
	    "class" => "example-element-class",
    	"id" => "example-element-id",
	    "value" => "Search",
        "disabled" => "disabled",
        "js_event" => "onclick",
        "js_function" => "SayHi",
	    "placeholder" => "Visit Example Website"
    ));
```  

**Create Div Tag (div)**  
* Options  
TBC
```
    $HTMLBuilder->CreateDivElement(array(
	    "class" => "example-element-class",
    	"id" => "example-element-id",
	    "href" => "https://www.example.com/",
	    "placeholder" => "Visit Example Website"
    ));
```  

**Create Header Tags (h1-h6)**  
* Options  
TBC
```
    $HTMLBuilder->CreateHeaderElement(array(
	    "class" => "example-element-class",
    	"id" => "example-element-id",
	    "href" => "https://www.example.com/",
	    "placeholder" => "Visit Example Website"
    ));
```  

**Create Paragraph Tag (p)**  
* Options  
TBC
```
    $HTMLBuilder->CreateParagraphElement(array(
	    "class" => "example-element-class",
    	"id" => "example-element-id",
	    "href" => "https://www.example.com/",
	    "placeholder" => "Visit Example Website"
    ));
```  

**Create Image Tag (img)**  
TBC
```
    $HTMLBuilder->CreateImageElement(array(
	    "class" => "example-element-class",
    	"id" => "example-element-id",
	    "href" => "https://www.example.com/",
	    "placeholder" => "Visit Example Website"
    ));
```  
