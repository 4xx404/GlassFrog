<?php
	$con = new SQLite3("db/glassFrog.db");
	
	if(!$con){
		echo "<h1 style='text-align:center;color:red;'>Failed to connect to the GlassFrog Database</h1>";
	}
?>
