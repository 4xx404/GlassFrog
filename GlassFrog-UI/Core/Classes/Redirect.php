<?php
class Redirect {
	public function To($location = null) {
		if($location) {
			if(is_numeric($location)) {
				switch($location) {
					case "404":
						header("HTTP/1.0 404 Not Found");
						include "Includes/Generic/Errors/404.php";
						exit();
					break;
				}
			}

			header("Location: " . $location);
			exit();
		}
	}
}