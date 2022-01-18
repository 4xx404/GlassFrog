<?php
	require_once("Core/init.php");

    $Config = new Config();
    $Database = new Database();
?>
<!DOCTYPE html>
<html lang="<?= $Config->Get("app_data/language"); ?>">
<head>
	<?php include("Includes/Generic/Header.php"); ?>
    <style>
		@import "Css/BranchTable.css";
	</style>
</head>
<body>
    <div class="header" id="header">
        <a class="logo" id="logo" href="GlassFrog.php"><?= $Config->Get("app_data/name") . " " . $Config->Get("app_data/version"); ?></a>
    </div>

    <div class="left-panel" id="left-panel">
        <a class="left-panel-button-active" id="branch-button" href="BranchTable.php">Branches</a>
        <a class="left-panel-button" id="branch-data-button" href="BranchDataTable.php">Branch Data</a>
        <a class="left-panel-button" id="website-tools-button" href="SelectTool.php">Website Tools</a>
    </div>

    <div class="branch-content" id="branch-content">
        <table class="branch-table" id="branch-table">
            <?php
                $Branches = $Database->SelectAll("branches");

                if($Branches) {
                    echo "
                        <tr>
                            <th class='standard-table-head' style='width:25%;'>Base URL</th>
                            <th class='standard-table-head' style='width:40%;'>Branch URL</th>
                            <th class='standard-table-head' style='width:15%;'>Keyword</th>
                            <th class='standard-table-head' style='width:7.5%;'>Found</th>
                            <th class='standard-table-head' style='width:20%;'>Set Key</th>
                        </tr>
                    ";

                    foreach($Branches as $Branch) {
                        echo "
                            <tr>
                                <td class='standard-table-data'><a class='branch-table-link' href='" . $Branch['base_url'] . "'>" . $Branch["base_url"] . "</a></td>
                                <td class='standard-table-data'><a class='branch-table-link' href='" . $Branch['branch_url'] ."'>" . $Branch["branch_url"] . "</a></td>
                                <td class='standard-table-data'>" . $Branch['keyword'] . "</td>";

                                if($Branch['keyword_found'] === 'True') {
                                    echo "<td class='green-font-table-data'>" . $Branch['keyword_found'] . "</td>";
                                } else { 
                                    echo "<td class='red-font-table-data'>" . $Branch['keyword_found'] . "</td>";
                                }

                                echo "<td class='standard-table-data'>". $Branch['branch_set_key'] . "</td>
                            </tr>
                        ";
                    }
                } else { 
                    echo "
                        <tr>
                            <th class='red-font-table-head'>No Branches Found</th>
                        </tr>
                        <tr>
                            <td class='red-font-table-data'>Execute <span style='color: cyan;'>sudo python3 glassFrog.py</span> to collect some branches</td>
                        </tr>
                    ";    
                }
            ?>
        </table>
    </div>
</body>
</html>
