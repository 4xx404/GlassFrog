<?php

class Analytics {
    function GetIPAddress(string $Link = null): string {
        return (($Link !== null && !empty(gethostbyname($Link))) ? gethostbyname($Link) : "");
    }
}
?>
