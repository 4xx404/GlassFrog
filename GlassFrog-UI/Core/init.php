<?php
$GLOBALS["Config"] = array(
	"AppData" => array(
		"Name" => "GlassFrog",
		"Version" => "3.0",
		"Language" => "en",
		"Favicon" => "Favicon.png"
	),

	"Sqlite" => array(
		"Path" => "db/GlassFrog.db",
	),

	"Functions" => array(
		"Strings",
	)
);

spl_autoload_register(function ($Class) {
	require_once("Classes/{$Class}.php");
});

foreach($GLOBALS["Config"]["Functions"] as $Function) {
	require_once("Functions/" . ucfirst($Function) . ".php");
} 