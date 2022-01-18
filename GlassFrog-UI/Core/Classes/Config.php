
<?php

/*
 * USAGE EXAMPLE: Config::get('mysqli/host');
 * 'mysqli/host' path found in core/init.php
*/
 
class Config {
	public function Get($path = null) {
		if($path) {
			$config = $GLOBALS["config"];
			$path = explode("/", $path);

			foreach($path as $bit) {
				if(isset($config[$bit])) {
					$config = $config[$bit];
				}
			}
			
			return $config;
		}
		
		return false;
	}
}