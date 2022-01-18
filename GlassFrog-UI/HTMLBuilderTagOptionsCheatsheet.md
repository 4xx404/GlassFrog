# HTMLBuilder Tag/Options CheatSheet  

# Create HTMLBuilder Object  
```
<?php 
	$HTMLBuilder = new HTMLBuilder();
```

**Create Anchor Tag (a)**  
* Options  
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
type - "", "button" or "reset"
class - Element Class Name
id - Element ID Name
value - Button Value
disabled - "" or "disabled"
js_event - "onclick", "onfocus" or "onfocusout"
js_function - JavaScript Function Name
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
```
    $HTMLBuilder->CreateDivElement(array(
	    "class" => "example-element-class",
    	"id" => "example-element-id",
	    "href" => "https://www.example.com/",
	    "placeholder" => "Visit Example Website"
    ));
```

**Create Header Tags (h1-h6)**  
```
    $HTMLBuilder->CreateHeaderElement(array(
	    "class" => "example-element-class",
    	"id" => "example-element-id",
	    "href" => "https://www.example.com/",
	    "placeholder" => "Visit Example Website"
    ));
```

**Create Paragraph Tag (p)**  
```
    $HTMLBuilder->CreateParagraphElement(array(
	    "class" => "example-element-class",
    	"id" => "example-element-id",
	    "href" => "https://www.example.com/",
	    "placeholder" => "Visit Example Website"
    ));
```

**Create Image Tag (img)**  
```
    $HTMLBuilder->CreateImageElement(array(
	    "class" => "example-element-class",
    	"id" => "example-element-id",
	    "href" => "https://www.example.com/",
	    "placeholder" => "Visit Example Website"
    ));
```