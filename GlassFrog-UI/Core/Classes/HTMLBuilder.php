<?php
    class HTMLBuilder {
        public static function HasOption($ElementOption, $TruthValue, $FalseValue) {
            return isset($ElementOption) ? $TruthValue : $FalseValue;
        }

        /* Create <a> Element */
        public static function CreateLinkElement(Array $LinkElementOptions) {
            if(count($LinkElementOptions) === 4) {
                $Class = self::HasOption($LinkElementOptions["class"], strtolower($LinkElementOptions["class"]), "");
                $ID = self::HasOption($LinkElementOptions["id"], strtolower($LinkElementOptions["id"]), "");
                $Href = self::HasOption($LinkElementOptions["href"], $LinkElementOptions["href"], "");
                $Placeholder = self::HasOption($LinkElementOptions["placeholder"], $LinkElementOptions["placeholder"], "Link");

                return "<a class=\"{$Class}\" id=\"{$ID}\" href=\"{$Href}\">{$Placeholder}</a>";
            }

            return ErrorHandler::Throw("HTMLBuilder::CreateLinkElement(\$LinkElementOptions) must include 'class', 'id', 'href' & 'placeholder' array key => values");
        }

        /* Create <button> Element */
        public static function CreateButtonElement(Array $ButtonElementOptions) {
            if(count($ButtonElementOptions) >= 4) {
                $Type = self::HasOption($ButtonElementOptions['type'], strtolower($ButtonElementOptions['type']), 'button');
                $Type = in_array($Type, ['button', 'reset']) ? $Type : 'button';

                $Class = self::HasOption($ButtonElementOptions['class'], strtolower($ButtonElementOptions['class']), '');
                $ID = self::HasOption($ButtonElementOptions['id'], strtolower($ButtonElementOptions['id']), '');
                $Value = self::HasOption($ButtonElementOptions['value'], strtolower($ButtonElementOptions['value']), '');
                $Disabled = self::HasOption($ButtonElementOptions['disabled'], 'disabled', '');

                // Check JavaScript EventType/FunctionName
                $JSEvent = self::HasOption($ButtonElementOptions['js_event'], strtolower($ButtonElementOptions['js_event']), '');
                $JSFunction = self::HasOption($ButtonElementOptions['js_function'], $ButtonElementOptions['js_function'], '');

                // Build Elements JavaScript Tag
                $JSTag = JSBuilder::CreateHTMLAttribute($JSEvent, ['onclick', 'onfocus', 'onfocusout'], $JSFunction);
                if(ErrorHandler::HasError($JSTag)) {
                    return $JSTag;
                }

                $Placeholder = self::HasOption($ButtonElementOptions['placeholder'], $ButtonElementOptions['placeholder'], ($Type === "button") ? "Click" : "Reset");

                return "<button type=\"{$Type}\" class=\"{$Class}\" id=\"{$ID}\" value=\"{$Value}\" {$JSTag} {$Disabled}>{$Placeholder}</button>";
            }

            return ErrorHandler::Throw("HTMLBuilder::CreateButtonElement(\$ButtonElementOptions) must include 'type', 'class', 'id', 'value' array key => values<br />Optional: 'js_event' => 'onclick'/'onfocus'/'onfocusout', 'js_function', 'functionName'/'functionName();'");
        }

        /* Create <div> Element */
        public static function CreateDivElement($DivElementOptions) {
            if(count($DivElementOptions) === 3) {
                $Class = self::HasOption($DivElementOptions['class'], strtolower($DivElementOptions['class']), '');
                $ID = self::HasOption($DivElementOptions['id'], strtolower($DivElementOptions['id']), '');
                $Content = self::HasOption($DivElementOptions['content'], $DivElementOptions['content'], '');

                return "<div class=\"{$Class}\" id=\"{$ID}\">{$Content}</div>";
            }

            return ErrorHandler::Throw("HTMLBuilder::CreateDivElement(\$DivElementOptions) must include 'class', 'id', 'content' array key => values");
        }

        /* Create <input> Element */
        public static function CreateInputElement($InputElementOptions) {
            $Type = self::HasOption($InputElementOptions['type'], strtolower($InputElementOptions['type']), '');

            $AllowedInputTypes = ['text', 'email', 'checkbox', 'color', 'date', 'datetime-local', 'file', 'hidden', 'image', 'month', 'number', 'password', 'radio', 'range', 'reset', 'search', 'submit', 'tel', 'text', 'time', 'url', 'week'];
            if(!empty($Type) && in_array($Type, $AllowedInputTypes)) {
                $Class = self::HasOption($InputElementOptions['class'], strtolower($InputElementOptions['class']), '');
                $ID = self::HasOption($InputElementOptions['id'], strtolower($InputElementOptions['id']), '');
                $Name = self::HasOption($InputElementOptions['name'], strtolower($InputElementOptions['name']), $Type);
                $Value = self::HasOption($InputElementOptions['value'], strtolower($InputElementOptions['value']), '');

                return "<input type=\"{$Type}\" class=\"{$Class}\" id=\"{$ID}\" name=\"{$Name}\" value=\"{$Value}\"/>";
            }

            return ErrorHandler::Throw("HTMLBuilder::CreateInputElement(\$InputElementOptions['type']) value " . !empty($InputType) ? "is an invalid option<br />Valid Options: {$Type}" : "is empty");
        }

        /* Create <h1> - <h6> Elements */
        public static function CreateHeaderElement($Type, $HeaderElementOptions) {
            if(count($HeaderElementOptions) === 3) {
                $Class = self::HasOption($HeaderElementOptions['class'], strtolower($HeaderElementOptions['class']), '');
                $ID = self::HasOption($HeaderElementOptions['id'], strtolower($HeaderElementOptions['id']), '');
                $Placeholder = self::HasOption($HeaderElementOptions['placeholder'], strtolower($HeaderElementOptions['placeholder']), $Type);

                return "<{$Type} class=\"{$Class}\" id=\"{$ID}\">{$Placeholder}</{$Type}>";
            }

            return ErrorHandler::Throw("HTMLBuilder::CreateHeaderElement(\$HeaderElementOptions) must include 'class', 'id', 'placeholder' array key => values");
        }

        /* Create <p> Element */
        public static function CreateParagraphElement(Array $ParagraphElementOptions) {
            if(count($ParagraphElementOptions) === 3) {
                $Class = self::HasOption($ParagraphElementOptions['class'], strtolower($ParagraphElementOptions['class']), '');
                $ID = self::HasOption($ParagraphElementOptions['id'], strtolower($ParagraphElementOptions['id']), '');
                $Placeholder = self::HasOption($ParagraphElementOptions['placeholder'], strtolower($ParagraphElementOptions['placeholder']), 'Paragraph');

                return "<p class=\"{$Class}\" id=\"{$ID}\">{$Placeholder}</p>";
            }

            return ErrorHandler::Throw("HTMLBuilder::CreateParagraphElement(\$ParagraphElementOptionsraph) must include 'class', 'id', 'placeholder' array key => values");
        }

        /* Create <img> Element */
        public static function CreateImageElement(Array $ImageElementOptions) {
            if(count($ImageElementOptions) >= 4) {
                $Class = self::HasOption($ImageElementOptions['class'], strtolower($ImageElementOptions['class']), '');
                $ID = self::HasOption($ImageElementOptions['id'], strtolower($ImageElementOptions['id']), '');
                $Source = self::HasOption($ImageElementOptions['src'], $ImageElementOptions['src'], '');
                $AltText = self::HasOption($ImageElementOptions['alt'], $ImageElementOptions['alt'], ucfirst($Class) . ' Alt Text');
                $Width = self::HasOption($ImageElementOptions['width'], strtolower($ImageElementOptions['width']), '400px');
                $Height = self::HasOption($ImageElementOptions['height'], strtolower($ImageElementOptions['height']), '400px');

                return "<img src=\"{$Source}\" alt=\"{$AltText}\" class=\"{$Class}\" id=\"{$ID}\" width=\"{$Width}\" height=\"{$Height}\" />";
            }
            
            return ErrorHandler::Throw("HTMLBuilder::CreateImageElement(\$ImageElementOptions) must include 'class', 'id', 'src' & 'alt' array key => values<br />Optional: 'width', 'height'(Default width/height: 400px)");
        }

        /* Create Element Dynamically */
        public static function CreateElement($HTMLTag, $ElementOptions = array()) {
            $HTMLTag = (!empty($HTMLTag) ? strtolower($HTMLTag) : "");

            if(!empty($HTMLTag)) {
                if($HTMLTag === "a") {
                    return self::CreateLinkElement($ElementOptions);
                } else if($HTMLTag === "button") {
                    return self::CreateButtonElement($ElementOptions);
                } else if($HTMLTag === "div") {
                    return self::CreateDivElement($ElementOptions);
                } else if($HTMLTag === "h1" || $HTMLTag === "h2" || $HTMLTag === "h3" || $HTMLTag === "h4" || $HTMLTag === "h5" || $HTMLTag === "h6") {
                    return self::CreateHeaderElement($HTMLTag, $ElementOptions);
                } else if($HTMLTag === "p"){
                    return self::CreateParagraphElement($ElementOptions);
                } else if($HTMLTag === "img") {
                    return self::CreateImageElement($ElementOptions);
                }

                return ErrorHandler::Throw("{$HTMLTag} is an invalid html tag");
            }

            return ErrorHandler::Throw("HTMLBuilder::CreateElement(\$HTMLTag) value cannot be empty");
        }
    }
?>