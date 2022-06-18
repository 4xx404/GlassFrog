<?php
	require_once("Core/init.php");

    $ToolName = null;
    $PortScannerTarget = null;
    if(Input::Exists("get")) {
        $ToolName = (Input::Get("tool") !== null ? lowercase(Input::Get("tool")) : null);
        $PortScannerTarget = (Input::Get("website") !== null ? lowercase(Input::Get("website")) : null);
    }
?>
<!DOCTYPE html>
<html lang="<?= Config::Get("AppData/Language"); ?>">
<head>
	<?php include("Includes/Generic/Header.php"); ?>
    <style>
		@import "Css/WebsiteTools.css";
	</style>
</head>
<body>
    <div class="header" id="header">
        <a class="logo" id="logo" href="GlassFrog.php">
            <?= Config::Get("AppData/Name") . " " . Config::Get("AppData/Version"); ?>
        </a>
    </div>

	<div class="left-panel" id="left-panel">
        <a class="left-panel-button" id="branch-button" href="BranchTable.php">Branches</a>
        <a class="left-panel-button" id="branch-data-button" href="BranchDataTable.php">Branch Data</a>
        <a class="left-panel-button-active" id="website-tools-button" href="SelectTool.php">Website Tools</a>
    </div>

    <?php
        $AllowedTools = array("portscanner", "whois", "web-history");

        if(!empty($ToolName)) {
            if(in_array($ToolName, $AllowedTools)) {
                if($ToolName === "portscanner") {
                    include("Includes/ToolResults/PortScannerResults.php");
                } else if($ToolName === "whois") {
                    die("<p style='color: green;'>whois results</p>");
                } else if($ToolName === "web-history") {
                    die("<p style='color: green;'>web-history</p>");
                }
            } else {
                die("<p style='color: red;'>Invalid Tool</p>");
            }
        } else {
            die("<p style='color: red;'>Invalid tool</p>");
        }
    ?>
</body>
</html>
