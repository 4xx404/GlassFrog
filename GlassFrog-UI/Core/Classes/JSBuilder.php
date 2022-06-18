<?php
    class JSBuilder {
        public static function SetFunction(string $JSEvent = null, string $JSFunction = null): string {
            $JSEvent = (($JSEvent !== null) ? $JSEvent : "onclick");
            $FunctionName = (($JSFunction !== null) ? $JSFunction : "");

            return ((!empty($FunctionName)) ? ((substr($FunctionName, -2) === "()" || substr($FunctionName, -3) === "();") ? "{$JSEvent}=\"{$FunctionName}\"" : "{$JSEvent}=\"{$FunctionName}();\"") : ErrorHandler::Throw("JSBuilder::SetFunction(\$FunctionName) value cannot be empty"));
        }

        public static function CreateHTMLAttribute(string $JavaScriptEvent = null, array $AllowedJavaScriptEvents = [], string $JavaScriptFunction = null) {
            if($JavaScriptEvent !== null && count($AllowedJavaScriptEvents) > 0) {
                $JSEvent = (in_array($JavaScriptEvent, $AllowedJavaScriptEvents) ? $JavaScriptEvent : null);

                return (($JSEvent !== null && $JavaScriptFunction !== null) ? self::SetFunction($JSEvent, $JavaScriptFunction) : "");
            }

            return ErrorHandler::Throw("Failed to build HTML Attribute for JavaScript function");
        }
    }
?>