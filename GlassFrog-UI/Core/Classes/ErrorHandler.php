<?php
    class ErrorHandler {
        public static function Throw($ErrorMessage) {
            return ((!empty($ErrorMessage)) ? "Error: {$ErrorMessage}<br />" :  "Error: Undefined Error Message<br />");
        }

        public static function HasError(string $Object = null) {
            return (($Object !== null && str_contains(lowercase($Object, false), "error:")) ? true : false);
        }
    }
?>