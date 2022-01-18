<?php
    class JSBuilder {
        public function __construct() {
            $this->Error = new ErrorHandler();
        }

        public function SetFunction($JSEvent, $JSFunction) {
            $JSEvent = isset($JSEvent) ? $JSEvent : "onclick";
            $FunctionName = isset($JSFunction) ? $JSFunction : "";

            if(!empty($FunctionName)) {
                if(substr($FunctionName, -2) === "()" || substr($FunctionName, -3) === "();") {
                    return "{$JSEvent}=\"{$FunctionName}\"";
                }

                return "{$JSEvent}=\"{$FunctionName}();\"";
            }

            return $this->Error->Throw("JSBuilder::SetFunction(\$FunctionName) value cannot be empty");
        }

        public function CreateHTMLAttribute($JavaScriptEvent, $AllowedJavaScriptEvents, $JavaScriptFunction) {
            if(!empty($JavaScriptEvent) && count($AllowedJavaScriptEvents) > 0) {
                $JSEvent = in_array($JavaScriptEvent, $AllowedJavaScriptEvents) ? $JavaScriptEvent : "";

                if(!empty($JSEvent) && !empty($JavaScriptFunction)) {
                    return $this->SetFunction($JSEvent, $JavaScriptFunction);
                }

                return '';
            }

            return $this->Error->Throw("Failed to build HTML Attribute for JavaScript function");
        }
    }
?>