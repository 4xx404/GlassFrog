<?php
class Input {
	public static function Exists($Type = "post"): bool {
		return (($Type === "post" && !empty($_POST)) ? true : (($Type === "get" && !empty($_GET)) ? true : false));
	}
	
	public static function Get(string $Item = null): mixed {
		return (($Item !== null) ? ((isset($_POST[$Item])) ? $_POST[$Item] : ((isset($_GET[$Item])) ? $_GET[$Item] : "")) : "");
	}

	public static function Raw(): array|null {
		return ((isset($_POST)) ? $_POST : ((isset($_GET)) ? $_GET : null));
	}
}