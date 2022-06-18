<?php require_once("Core/init.php"); ?>
<!DOCTYPE html>
<html lang="<?= Config::Get("AppData/Language"); ?>">
<head>
	<?php include("Includes/Generic/Header.php"); ?>
    <style>
		@import "Css/BranchDataTable.css";
	</style>
</head>
<body>
    <div class="header" id="header">
        <a class="logo" id="logo" href="GlassFrog.php"><?= Config::Get("AppData/Name") . " " . Config::Get("AppData/Version"); ?></a>
    </div>

	<div class="left-panel" id="left-panel">
        <a class="left-panel-button" id="branch-button" href="BranchTable.php">Branches</a>
        <a class="left-panel-button-active" id="branch-data-button" href="BranchDataTable.php">Branch Data</a>
        <a class="left-panel-button" id="website-tools-button" href="SelectTool.php">Website Tools</a>
    </div>

	<div class="branch-data-content" id="branch-data-content">
        <table class="branch-data-table" id="branch-data-table">
            <?php
                $BranchDataList = (new Database())->SelectAll("branch_data");

                if($BranchDataList) {
                    echo "
                        <tr>
                            <th class='standard-table-head' style='width:22.55%;'>Branch URL</th>
                            <th class='standard-table-head' style='width:10%;'>Data Type</th>
                            <th class='standard-table-head' style='width:27.5%;'>Data</th>
                            <th class='standard-table-head' style='width:7.5%;'>Date</th>
                            <th class='standard-table-head' style='width:10%;'>Content ID</th>
                        </tr>
                    ";

                    foreach($BranchDataList as $BranchData) {
                        echo "
                            <tr>
                                <td class='standard-table-data'><a class='branch-data-table-link' href='" . $BranchData["branch_url"] . "'>" . $BranchData["branch_url"] . "</a></td>
                                <td class='standard-table-data'>" . ucwords(str_replace("_", " ", $BranchData["datatype"])) . "</td>
                                <td class='standard-table-data'>" . $BranchData["data"] . "</td>
                                <td class='standard-table-data'>" . explode(" ", $BranchData["data_date"])[0] . "</td>
                                <td class='standard-table-data'>" . $BranchData["content_id"] . "</td>
                            </tr>
                        ";
                    }
                } else { 
                    echo "
                        <tr>
                            <th class='red-font-table-head'>No Branch Data Found</th>
                        </tr>
                        <tr>
                            <td class='red-font-table-data'>Execute <span style='color: white;'>sudo python3 glassFrog.py</span> to collect some branch data</td>
                        </tr>
                    ";
                }
            ?>
        </table>
    </div>
</body>
</html>
