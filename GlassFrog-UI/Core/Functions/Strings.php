<?php
function escape(string $String = null, bool $UseStripTags = true) {
    return (($String !== null) ? (($UseStripTags === true) ? htmlentities(stripTags($String, false), ENT_QUOTES, "UTF-8") : htmlentities($String, ENT_QUOTES, "UTF-8")) : "");
}

function lowercase(string $String = null, bool $UseEscape = true) {
    return (($String !== null) ? (($UseEscape === true) ? escape(strtolower($String)) : strtolower($String)) : "");
}

function uppercase(string $String = null, bool $UseEscape = true) {
    return (($String !== null) ? (($UseEscape === true) ? escape(strtoupper($String)) : strtoupper($String)) : "");
}

function capitalise(string $String = null, bool $UseEscape = true) {
    return (($String !== null) ? (($UseEscape === true) ? ucfirst(lowercase($String)) : ucfirst($String)) : "");
}

function capitaliseWords(array $WordList = array(), bool $UseEscape = true, $IncludeSpaces = false) {
    $String = "";
    
    if(is_array($WordList) && count($WordList) > 0) {
        foreach($WordList as $Word) {
            $String .= capitalise(lowercase($Word, false), $UseEscape) . (($IncludeSpaces === true) ? " " : "");
        }
    }

    return($String);
}

function stripTags(string $String = null, $UseEscape = true) {
    return (($String !== null) ? (($UseEscape === true) ? escape(strip_tags($String)): strip_tags($String)) : "");
}
?>