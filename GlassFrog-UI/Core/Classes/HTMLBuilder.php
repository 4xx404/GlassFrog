<?php
    class HTMLBuilder {
        public function __construct() {
            $this->JSBuilder = new JSBuilder();
            $this->Error = new ErrorHandler();
            $this->Response = '';
        }

        public function HasOption($ElementOption, $TruthValue, $FalseValue) {
            return isset($ElementOption) ? $TruthValue : $FalseValue;
        }

        /*
         * Create <a> Element
        */
        public function CreateLinkElement(Array $LinkElementOptions) {
            if(count($LinkElementOptions) === 4) {
                $Class = $this->HasOption($LinkElementOptions['class'], strtolower($LinkElementOptions['class']), '');
                $ID = $this->HasOption($LinkElementOptions['id'], strtolower($LinkElementOptions['id']), '');
                $Href = $this->HasOption($LinkElementOptions['href'], $LinkElementOptions['href'], '');
                $Placeholder = $this->HasOption($LinkElementOptions['placeholder'], $LinkElementOptions['placeholder'], 'Link');

                return "<a class=\"{$Class}\" id=\"{$ID}\" href=\"{$Href}\">{$Placeholder}</a>";
            }

            return $this->Error->Throw("HTMLBuilder::CreateLinkElement(\$LinkElementOptions) must include 'class', 'id', 'href' & 'placeholder' array key => values");
        }

        /*
         * Create <button> Element
        */
        public function CreateButtonElement(Array $ButtonElementOptions) {
            if(count($ButtonElementOptions) >= 4) {
                $Type = $this->HasOption($ButtonElementOptions['type'], strtolower($ButtonElementOptions['type']), 'button');
                $Type = in_array($Type, ['button', 'reset']) ? $Type : 'button';

                $Class = $this->HasOption($ButtonElementOptions['class'], strtolower($ButtonElementOptions['class']), '');
                $ID = $this->HasOption($ButtonElementOptions['id'], strtolower($ButtonElementOptions['id']), '');
                $Value = $this->HasOption($ButtonElementOptions['value'], strtolower($ButtonElementOptions['value']), '');
                $Disabled = $this->HasOption($ButtonElementOptions['disabled'], 'disabled', '');

                // Check JavaScript EventType/FunctionName
                $JSEvent = $this->HasOption($ButtonElementOptions['js_event'], strtolower($ButtonElementOptions['js_event']), '');
                $JSFunction = $this->HasOption($ButtonElementOptions['js_function'], $ButtonElementOptions['js_function'], '');

                // Build Elements JavaScript Tag
                $JSTag = $this->JSBuilder->CreateHTMLAttribute($JSEvent, ['onclick', 'onfocus', 'onfocusout'], $JSFunction);
                if($this->Error->HasError($JSTag)) {
                    return $JSTag;
                }

                $Placeholder = $this->HasOption($ButtonElementOptions['placeholder'], $ButtonElementOptions['placeholder'], ($Type === "button") ? "Click" : "Reset");

                return "<button type=\"{$Type}\" class=\"{$Class}\" id=\"{$ID}\" value=\"{$Value}\" {$JSTag} {$Disabled}>{$Placeholder}</button>";
            }

            return $this->Error->Throw("HTMLBuilder::CreateButtonElement(\$ButtonElementOptions) must include 'type', 'class', 'id', 'value' array key => values<br />Optional: 'js_event' => 'onclick'/'onfocus'/'onfocusout', 'js_function', 'functionName'/'functionName();'");
        }

        /*
         * Create <div> Element
        */
        public function CreateDivElement($DivElementOptions) {
            if(count($DivElementOptions) === 3) {
                $Class = $this->HasOption($DivElementOptions['class'], strtolower($DivElementOptions['class']), '');
                $ID = $this->HasOption($DivElementOptions['id'], strtolower($DivElementOptions['id']), '');
                $Content = $this->HasOption($DivElementOptions['content'], $DivElementOptions['content'], '');

                return "<div class=\"{$Class}\" id=\"{$ID}\">{$Content}</div>";
            }

            return $this->Error->Throw("HTMLBuilder::CreateDivElement(\$DivElementOptions) must include 'class', 'id', 'content' array key => values");
        }

        /*
         * Create <input> Element
        */
        public function CreateInputElement($InputElementOptions) {
            $Type = $this->HasOption($InputElementOptions['type'], strtolower($InputElementOptions['type']), '');

            $AllowedInputTypes = ['text', 'email', 'checkbox', 'color', 'date', 'datetime-local', 'file', 'hidden', 'image', 'month', 'number', 'password', 'radio', 'range', 'reset', 'search', 'submit', 'tel', 'text', 'time', 'url', 'week'];
            if(!empty($Type) && in_array($Type, $AllowedInputTypes)) {
                $Class = $this->HasOption($InputElementOptions['class'], strtolower($InputElementOptions['class']), '');
                $ID = $this->HasOption($InputElementOptions['id'], strtolower($InputElementOptions['id']), '');
                $Name = $this->HasOption($InputElementOptions['name'], strtolower($InputElementOptions['name']), $Type);
                $Value = $this->HasOption($InputElementOptions['value'], strtolower($InputElementOptions['value']), '');

                return "<input type=\"{$Type}\" class=\"{$Class}\" id=\"{$ID}\" name=\"{$Name}\" value=\"{$Value}\"/>";
            }

            return $this->Error->Throw("HTMLBuilder::CreateInputElement(\$InputElementOptions['type']) value " . !empty($InputType) ? "is an invalid option<br />Valid Options: {$Type}" : "is empty");
        }

        /*
         * Create <h1> - <h6> Elements
        */
        public function CreateHeaderElement($Type, $HeaderElementOptions) {
            if(count($HeaderElementOptions) === 3) {
                $Class = $this->HasOption($HeaderElementOptions['class'], strtolower($HeaderElementOptions['class']), '');
                $ID = $this->HasOption($HeaderElementOptions['id'], strtolower($HeaderElementOptions['id']), '');
                $Placeholder = $this->HasOption($HeaderElementOptions['placeholder'], strtolower($HeaderElementOptions['placeholder']), $Type);

                return "<{$Type} class=\"{$Class}\" id=\"{$ID}\">{$Placeholder}</{$Type}>";
            }

            return $this->Error->Throw("HTMLBuilder::CreateHeaderElement(\$HeaderElementOptions) must include 'class', 'id', 'placeholder' array key => values");
        }

        /*
         * Create <p> Element
        */
        public function CreateParagraphElement(Array $ParagraphElementOptions) {
            if(count($ParagraphElementOptions) === 3) {
                $Class = $this->HasOption($ParagraphElementOptions['class'], strtolower($ParagraphElementOptions['class']), '');
                $ID = $this->HasOption($ParagraphElementOptions['id'], strtolower($ParagraphElementOptions['id']), '');
                $Placeholder = $this->HasOption($ParagraphElementOptions['placeholder'], strtolower($ParagraphElementOptions['placeholder']), 'Paragraph');

                return "<p class=\"{$Class}\" id=\"{$ID}\">{$Placeholder}</p>";
            }

            return $this->Error->Throw("HTMLBuilder::CreateParagraphElement(\$ParagraphElementOptionsraph) must include 'class', 'id', 'placeholder' array key => values");
        }

        /*
         * Create <img> Element
        */
        public function CreateImageElement(Array $ImageElementOptions) {
            if(count($ImageElementOptions) >= 4) {
                $Class = $this->HasOption($ImageElementOptions['class'], strtolower($ImageElementOptions['class']), '');
                $ID = $this->HasOption($ImageElementOptions['id'], strtolower($ImageElementOptions['id']), '');
                $Source = $this->HasOption($ImageElementOptions['src'], $ImageElementOptions['src'], '');
                $AltText = $this->HasOption($ImageElementOptions['alt'], $ImageElementOptions['alt'], ucfirst($Class) . ' Alt Text');
                $Width = $this->HasOption($ImageElementOptions['width'], strtolower($ImageElementOptions['width']), '400px');
                $Height = $this->HasOption($ImageElementOptions['height'], strtolower($ImageElementOptions['height']), '400px');

                return "<img src=\"{$Source}\" alt=\"{$AltText}\" class=\"{$Class}\" id=\"{$ID}\" width=\"{$Width}\" height=\"{$Height}\" />";
            }
            
            return $this->Error->Throw("HTMLBuilder::CreateImageElement(\$ImageElementOptions) must include 'class', 'id', 'src' & 'alt' array key => values<br />Optional: 'width', 'height'(Default width/height: 400px)");
        }

        /*
         * Create Element Dynamically
        */
        public function CreateElement($HTMLTag, $ElementOptions = array()) {
            $HTMLTag = !empty($HTMLTag) ? strtolower($HTMLTag) : '';

            if(!empty($HTMLTag)) {
                if($HTMLTag === "a") {
                    return $this->CreateLinkElement($ElementOptions);
                } else if($HTMLTag === "button") {
                    return $this->CreateButtonElement($ElementOptions);
                } else if($HTMLTag === "div") {
                    return $this->CreateDivElement($ElementOptions);
                } else if($HTMLTag === "h1" || $HTMLTag === "h2" || $HTMLTag === "h3" || $HTMLTag === "h4" || $HTMLTag === "h5" || $HTMLTag === "h6") {
                    return $this->CreateHeaderElement($HTMLTag, $ElementOptions);
                } else if($HTMLTag === "p"){
                    return $this->CreateParagraphElement($ElementOptions);
                } else if($HTMLTag === "img") {
                    return $this->CreateImageElement($ElementOptions);
                }

                return $this->Error->Throw("{$HTMLTag} is an invalid html tag");
            }

            return $this->Error->Throw("HTMLBuilder::CreateElement(\$HTMLTag) value cannot be empty");
        }
    }
?>