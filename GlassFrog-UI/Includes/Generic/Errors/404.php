<?php require_once("Core/init.php"); ?>
<!DOCTYPE html>
<html lang="<?= Config::Get("AppData/Language"); ?>">
<head>
	<?php include("Includes/Generic/Header.php"); ?>
    <style>
		@import "Css/404.css";
	</style>
</head>
<body>
    <div class="header" id="header">
        <a class="logo" id="logo" href="GlassFrog.php"><?= Config::Get("AppData/Name"); ?></a>
    </div>

    <div class=".content-404-container" id=".content-404-container">
        <h2 class="message-404-container" id="message-404-container">
            404 Error: page not found
        </h2>
    </div>
</body>
</html>
