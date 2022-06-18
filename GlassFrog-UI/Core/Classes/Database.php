<?php
class Database {
    private static $_sqlite = null;
	const AllowedOperators = array("=", "!=", "<", ">", "<=", ">=");

	public function __construct() {
		if(self::$_sqlite == null) {
			try {
	            self::$_sqlite = new \PDO("sqlite:" . Config::Get("Sqlite/Path"));
			} catch (PDOException $e) {
				die("<h1 style='text-align:center;color:red;'>{$e->getMessage()}<br />Failed to connect to the GlassFrog Database</h1>");
			}
        }

        return self::$_sqlite;
    }

	public static function SelectAll(string $Table = null): array|null {
		$Selected = (($Table !== null) ? self::$_sqlite->query("SELECT * FROM {$Table}") : null);
        $Results = [];

		if($Selected !== null) {
			if($Table == "branches"){
				while ($Row = $Selected->fetch(\PDO::FETCH_OBJ)) {
					$Results[] = [
						"id" => $Row->id,
						"fld" => $Row->fld,
						"base_url" => $Row->base_url,
						"branch_url" => $Row->branch_url,
						"branch_set_key" => $Row->branch_set_key,
						"keyword" => $Row->keyword,
						"keyword_found" => $Row->keyword_found,
						"branch_date" => $Row->branch_date
					];
				}
			} else if($Table == "branch_data") {
				while ($Row = $Selected->fetch(\PDO::FETCH_OBJ)) {
					$Results[] = [
						"id" => $Row->id,
						"content_id" => $Row->content_id,
						"datatype" => $Row->datatype,
						"branch_url" => $Row->branch_url,
						"branch_set_key" => $Row->branch_set_key,
						"data" => $Row->data,
						"data_date" => $Row->data_date
					];
				}
			} else if($Table == "website_tools") {
				while($Row = $Selected->fetch(\PDO::FETCH_OBJ)) {
					$Results[] = [
						"id" => $Row->id,
						"name" => $Row->name
					];
				}
			} else if($Table == "portscanner_results") {
				while($Row = $Selected->fetch(\PDO::FETCH_OBJ)) {
					$Results[] = [
						"id" => $Row->id,
						"scan_id" => $Row->scan_id,
						"host" => $Row->host,
						"port" => $Row->port,
						"port_status" => $Row->port_status,
						"port_service" => $Row->port_service,
						"scan_date" => $Row->scan_date,
						"delete_date" => $Row->delete_date
					];
				}
			} else {
				die("<p style='color: red;'>Invalid Database::SelectAll() Table {$Table}");
				return null;
			}
		}

		return ((count($Results) > 0) ? $Results : null);
	}

	public static function Select(string $Table = null, array $WherePacks = array()): array|null {
		$Query = "";

		$PackCount = count($WherePacks);
		$CurrentCount = 0;

		foreach($WherePacks as $WherePack) {
			$CurrentCount++;
			$Column = isset($WherePack["column"]) ? $WherePack["column"] : "id";
			$Operator = in_array($WherePack["operator"], self::AllowedOperators) ? $WherePack["operator"] : "=";
			$Value = is_numeric($WherePack["value"]) ? $WherePack["value"] : "'" . $WherePack["value"] . "'";
			$QueryConnector = isset($WherePack["query_connector"]) ? strtoupper($WherePack["query_connector"]) : "AND ";

			$Query .= (($CurrentCount !== $PackCount) ? "{$Column} {$Operator} {$Value} {$QueryConnector} " : "{$Column} {$Operator} {$Value}");
		}

		$SQL = "SELECT * FROM {$Table} WHERE {$Query}";
		$Selected = self::$_sqlite->query($SQL);

		$Results = [];
		if($Table == "branches"){
			while ($Row = $Selected->fetch(\PDO::FETCH_OBJ)) {
				$Results[] = [
					"id" => $Row->id,
					"fld" => $Row->fld,
					"base_url" => $Row->base_url,
					"branch_url" => $Row->branch_url,
					"branch_set_key" => $Row->branch_set_key,
					"keyword" => $Row->keyword,
					"keyword_found" => $Row->keyword_found,
					"branch_date" => $Row->branch_date
				];
			}
		} else if($Table == "branch_data") {
			while ($Row = $Selected->fetch(\PDO::FETCH_OBJ)) {
				$Results[] = [
					"id" => $Row->id,
					"content_id" => $Row->content_id,
					"datatype" => $Row->datatype,
					"branch_url" => $Row->branch_url,
					"branch_set_key" => $Row->branch_set_key,
					"data" => $Row->data,
					"data_date" => $Row->data_date
				];
			}
		} else if($Table == "website_tools") {
			while($Row = $Selected->fetch(\PDO::FETCH_OBJ)) {
				$Results[] = [
					"id" => $Row->id,
					"name" => $Row->name
				];
			}
		} else if($Table == "portscanner_results") {
			while($Row = $Selected->fetch(\PDO::FETCH_OBJ)) {
				$Results[] = [
					"id" => $Row->id,
					"scan_id" => $Row->scan_id,
					"host" => $Row->host,
					"port" => $Row->port,
					"port_status" => $Row->port_status,
					"port_service" => $Row->port_service,
					"scan_date" => $Row->scan_date,
					"delete_date" => $Row->delete_date
				];
			}
		} else {
			die("<p style='color: red;'>Invalid Database::Select() Table {$Table}");
			return null;
		}

		return ((count($Results) > 0) ? $Results : null);
	}

	public static function Insert(string $Table = null, array $InsertData = array()): bool {
		$Table = (($Table !== null) ? lowercase($Table) : null);
		$SQL = null;

		if(($Table !== null && count($InsertData) > 0) && $Table === "portscanner_results") {
			$ScanID = (array_key_exists("scan_id", $InsertData) ? $InsertData["scan_id"] : Hash::Make("md5"));
			$Host = (array_key_exists("host", $InsertData) ? $InsertData["host"] : "unknown host");
			$Port = (array_key_exists("port", $InsertData) ? strval($InsertData["port"]) : "probe failed");
			$PortStatus = array_key_exists("port_status", $InsertData) ? $InsertData["port_status"] : "probe failed";
			$PortService = (array_key_exists("port_service", $InsertData) ? $InsertData["port_service"] : "unknown");
	
			$ScanDate = DateTimeManager::GetDateTime();
			$DeleteDate = DateTimeManager::GetDeleteDate(strval($ScanDate), 24);
	
			$SQL = "INSERT INTO `{$Table}` (scan_id, host, port, port_status, port_service, scan_date, delete_date) VALUES ('{$ScanID}', '{$Host}', '{$Port}', '{$PortStatus}', '{$PortService}', '{$ScanDate}', '{$DeleteDate}')";
		}

		return (($SQL !==  null && self::$_sqlite->query($SQL)) ? true : false);
	}
}