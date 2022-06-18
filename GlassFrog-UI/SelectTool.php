<?php
	require_once("Core/init.php");

    $Database = new Database();

    if(Input::Exists()) {
        $ToolName = strtolower(Input::Get("tool"));
        $WebsiteLink = Input::Get("website-link");

        Redirect::To("WebsiteTools.php?tool={$ToolName}&website={$WebsiteLink}");
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
<body onload="SetFormHeader();">
    <div class="header" id="header">
        <a class="logo" id="logo" href="GlassFrog.php"><?= Config::Get("AppData/Name") . " " . Config::Get("AppData/Version"); ?></a>
    </div>

	<div class="left-panel" id="left-panel">
        <a class="left-panel-button" id="branch-button" href="BranchTable.php">Branches</a>
        <a class="left-panel-button" id="branch-data-button" href="BranchDataTable.php">Branch Data</a>
        <a class="left-panel-button-active" id="website-tools-button" href="WebsiteTools.php">Website Tools</a>
    </div>

    <div class="select-tool-content" id="select-tool-content">
        <form class="website-tool-selector-form" id="website-tool-selector-form" action="" method="post">
            <h3 class="form-header" id="form-header"></h3>

            <?php
                $Websites = null;

                $ToolList = $Database->SelectAll("website_tools");
                if($ToolList) {
                    $Websites = $Database->SelectAll("branches");

                    if($Websites !== null) {
                        echo "
                            <div class='form-field-input' id='form-field-input'>                    
                                <label for='tool' class='select-input-label'>Select Tool</label>
                                <select class='tool-selector-input' name='tool' id='tool' onchange='SetFormHeader();'>";
                                    foreach($ToolList as $Tool) {
                                        echo "<option value='" . $Tool["name"] . "'>" . ucwords(str_replace("_", " ", $Tool["name"])) . "</option>";
                                    }
                        echo "  
                                </select>
                            </div>";
                    }
                } else {
                    echo "
                        <tr>
                            <th class='red-font-table-head'>Failed to collect tools</th>
                        </tr>
                    ";
                }
                
                if($Websites !== null) {
                    $DuplicateWebsites = [];
                    
                    echo "
                        <div class='form-field-input' id='form-field-input'>
                            <label for='website-link' class='select-input-label'>Select Website</label>
                            <select class='website-link-input' name='website-link' id='website-link'>";
                                foreach($Websites as $Website) {
                                    if(!in_array($Website["base_url"], $DuplicateWebsites)) {
                                        echo "<option value='" . $Website["base_url"] . "'>" . ucfirst($Website["fld"]) . "</option>";
                                        $DuplicateWebsites[] = $Website["base_url"];
                                    }
                                }
                    echo "  </select>
                        </div>

                        <div class='form-field-submit' id='form-field-submit'>
                            <input type='submit' name='submit-tool-data' class='green-button' id='submit-tool-data-button' value='Submit' />
                        </div>
                    ";
                } else {
                    echo "
                        <tr>
                            <th class='red-font-table-head'>No Branches Found</th>
                        </tr>
                        <tr>
                            <td class='red-font-table-data'>Execute <span style='color: cyan;'>sudo python3 setup.py</span> to create the tool list table</td>
                        </tr>
                    ";  
                }
            ?>
        </form>
    </div>
</body>
</html>
