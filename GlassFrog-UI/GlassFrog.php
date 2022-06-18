<?php require_once("Core/init.php"); ?>
<!DOCTYPE html>
<html lang="<?= Config::Get("AppData/Language"); ?>">
<head>
	<?php include("Includes/Generic/Header.php"); ?>
	<style>
		@import "Css/Index.css";
	</style>
</head>
<body>
	<div class="header" id="header">
    	<a class="logo" id="logo" href="GlassFrog.php"><?= Config::Get("AppData/Name") . " " . Config::Get("AppData/Version"); ?></a>
	</div>

	<div class="index-content-container" id="index-content-container">
		<?php
			$Branches = (new Database())::SelectAll("branches");
			$BranchCount = 0;

			if($Branches) {
				foreach($Branches as $Branch) {
					$BranchCount++;
				}
			}
		?>

		<a class="index-badge-counter" id="index-badge-counter-branches" href="BranchTable.php">
			Total Branches<span class="index-badge-counter-number" id="index-badge-counter-number"><?= $BranchCount; ?></span>
		</a>
		<a class="index-badge-counter" id="index-badge-counter-website-tools" href="SelectTool.php">
			Website Tools
		</a>
	</div>
</body>
</html>
