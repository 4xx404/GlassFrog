<?php
    class ErrorHandler {
        public function __construct() {
            $this->_error_message = '';
        }

        public function SetError($ErrorMessage) {
            $this->_error_message = "Error: " . $ErrorMessage . "<br />";
        }

        public function Throw($ErrorMessage) {
            if(!empty($ErrorMessage)) {
                $this->SetError($ErrorMessage);
                return $this->_error_message;
            }

            return "Undefined Error Message<br />";
        }

        public function HasError($Object) {
            if(substr($Object, 0, 6) === "Error:") {
                return true;
            }

            return false;
        }
    }
?>