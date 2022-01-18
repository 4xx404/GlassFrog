<?php
$GLOBALS["config"] = array(
	"app_data" => array(
		"name" => "GlassFrog",
		"version" => "3.0",
		"language" => "en",
		"favicon" => "Favicon.png"
	),

	"sqlite" => array(
		"path" => "db/GlassFrog.db",
	),
);

spl_autoload_register(function ($class) {
	require_once "Classes/" . $class . ".php";
});
