<?php

class Analytics {
    public function __construct() {
        $this->Validator = new Validate();
    }

    function GetIPAddress($Link) {
        return !empty(gethostbyname($Link)) ? gethostbyname($Link) : '';
    }
}
?>
