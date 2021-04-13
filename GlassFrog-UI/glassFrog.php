<!DOCTYPE html>
<head>
	<title>GlassFrog UI</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<link rel="icon" type="image/png" href="favicon.png"/>
	<link rel="stylesheet" type="text/css" href="css/style.css">
	<script src="js/glassFrog.js"></script>
</head>
<body onload="showBranches();">
	<div id="header" style="float:left;position:relative;margin:0;width:100%;height:10%;border:none;">
		<h1 id="logo" style="float:center;position:relative;margin:0;width:auto;height:100%;background:none;color:cyan;text-shadow:0 0 8px red, 0 0 4px cyan;border:none;padding:0.75%;text-align:center;user-select:none;">GlassFrog</h1>
	</div>
	<div id="leftPanel">
		<button id="branchesBtn" onclick="showBranches();"><b>Branches</b></button>
		<button id="branchDataBtn" onclick="showBranchData();"><b>Branch Data</b></button>
	</div>
	
	<div id="branchesContent">
		<table id="branchesTable">
			<tr>
				<th style='width:15%;'>Base URL</th>
				<th style='width:50%;'>Branch URL</th>
				<th style='width:15%;'>Keyword</th>
				<th style='width:7.5%;'>Found</th>
				<th style='width:20%;'>Set Key</th>
			</tr>
			<?php
				require('db/db.php');

				$r = $con->query("SELECT * FROM branches");
				if($r){
					while($row = $r->fetchArray(SQLITE3_ASSOC)){
						echo "
							<tr>
								<td style='text-align:left;'><a href=".$row['BASE_URL']." style='color:cyan;text-decoration:none;'>".$row['FLD']."</a></td>
								<td style='text-align:left;'><a href=".$row['BRANCH_URL']." style='color:cyan;text-decoration:none;'>".$row['BRANCH_URL']."</a></td>
								<td>".$row['KEYWORD']."</td>";
								if($row['KEYWORD_FOUND'] == 'False'){
									echo "<td style='color:red;'>".$row['KEYWORD_FOUND']."</td>";
								} else {
									echo "<td>".$row['KEYWORD_FOUND']."</td>";
								}
								echo "<td>".$row['BRANCH_SET_KEY']."</td>
							</tr>
						";
					}
				} else {
					echo "
						<script>
							document.getElementById('branchesTable').style.display = 'none';
						</script>
						<h2 style='color:red;text-align:center;'>No Branches</h2>
					";
				}
			?>
		</table>
	</div>
	<div id="branchDataContent">
		<table id="branchDataTable">
			<tr>
				<th style='width:20%;'>Branch URL</th>
				<th style='width:16.25%;'>Data Type</th>
				<th style='width:30%;'>Data</th>
				<th style='width:12.5%;'>Date</th>
				<th style='width:15%;'>Content ID</th>
			</tr>
			<?php
				require('db/db.php');

				$r = $con->query("SELECT * FROM branch_data");
				if($r){
					while($row = $r->fetchArray(SQLITE3_ASSOC)){
						$date = $row['DATA_DATE'];
						$date = explode(' ', $date);
						$date = $date[0];
						echo "
							<tr>
								<td style='text-align:left;'><a href=".$row['BRANCH_URL']." style='color:cyan;text-decoration:none;'>".$row['BRANCH_URL']."</a></td>
								<td style='text-align:left;'>".$row['DATATYPE']."</td>
								<td style='text-align:left;'>".$row['DATA']."</td>
								<td>".$date."</td>
								<td>".$row['CONTENT_ID']."</td>
							</tr>";
					}
				} else {
					echo "
						<script>
							document.getElementById('branchDataTable').style.display = 'none';
						</script>
						<h2 style='color:red;text-align:center;'>No Branch Data</h2>
					";
				}
			?>
		</table>
	</div>
</body>
</html>
