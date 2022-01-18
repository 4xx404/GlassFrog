<?php
class Database {
	/**
     * PDO instance
     * @var type 
	*/
    private $_sqlite;

	public function __construct() {
		$this->AllowedOperators = array('=', '!=', '<', '>', '<=', '>=');
		$this->Config = new Config();
		$this->Hasher = new Hash();
		$this->Datetime = new DateTimeManager();

		if ($this->_sqlite == null) {
			try {
	            $this->_sqlite = new \PDO("sqlite:" . $this->Config->Get("sqlite/path"));
			} catch (PDOException $e) {
				die("<h1 style='text-align:center;color:red;'>{$e->getMessage()}<br />Failed to connect to the GlassFrog Database</h1>");
			}
        }

        return $this->_sqlite;
    }

	/**
     * Get all projects
     * @return type
	*/
	public function SelectAll($Table) {
		$Selected = $this->_sqlite->query("SELECT * FROM {$Table}");
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

			return $Results;
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

			return $Results;
		} else if($Table == "website_tools") {
			while($Row = $Selected->fetch(\PDO::FETCH_OBJ)) {
				$Results[] = [
					"id" => $Row->id,
					"name" => $Row->name
				];
			}

			return $Results;
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

			return $Results;
		} else {
			die("<p style='color: red;'>Invalid \$Database->SelectAll() Table {$Table}");
	        return false;
		}
	}

	public function Select($Table, $WherePacks = array()) {
		$Query = "";

		$PackCount = count($WherePacks);
		$CurrentCount = 0;

		foreach($WherePacks as $WherePack) {
			$CurrentCount++;
			$Column = isset($WherePack['column']) ? $WherePack['column'] : "id";
			$Operator = isset($WherePack['operator'], $this->AllowedOperators) ? $WherePack['operator'] : "=";
			$Value = is_numeric($WherePack['value']) ? $WherePack['value'] : "'" . $WherePack['value'] . "'";
			$QueryConnector = isset($WherePack['query_connector']) ? strtoupper($WherePack['query_connector']) : "AND ";

			if($CurrentCount !== $PackCount) {
				$Query .= $Column . $Operator . $Value . " {$QueryConnector} ";
			} else {
				$Query .= $Column . $Operator . $Value;
			}
		}

		$SQL = "SELECT * FROM {$Table} WHERE " . $Query;
		$Selected = $this->_sqlite->query($SQL);

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

			return $Results;
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

			return $Results;
		} else if($Table == "website_tools") {
			while($Row = $Selected->fetch(\PDO::FETCH_OBJ)) {
				$Results[] = [
					"id" => $Row->id,
					"name" => $Row->name
				];
			}

			return $Results;
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

			return $Results;
		} else {
			die("<p style='color: red;'>Invalid \$Database->Select() Table {$Table}");
			return false;
		}
	}

	public function Insert($Table, $InsertData = array()) {
		if(strtolower($Table) == "portscanner_results") {
			$ScanID = isset($InsertData['scan_id']) ? $InsertData['scan_id'] : '';
			$Host = isset($InsertData['host']) ? $InsertData['host'] : 'unknown host';
			$Port = isset($InsertData['port']) ? strval($InsertData['port']) : 'frobe failed';
			$PortStatus = isset($InsertData['port_status']) ? $InsertData['port_status'] : 'probe failed';
			$PortService = isset($InsertData['port_service']) ? $InsertData['port_service'] : 'unknown';

			$ScanDate = $this->Datetime->GetDateTime();
			$DeleteDate = $this->Datetime->GetDeleteDate(strval($ScanDate), 24);

			$SQL = "INSERT INTO {$Table}(scan_id, host, port, port_status, port_service, scan_date, delete_date) VALUES ('" . $ScanID . "', '" . $Host . "', '" . $Port . "', '" . $PortStatus . "', '" . $PortService . "', '" . $ScanDate . "', '" . $DeleteDate . "')";
		} else {
			$SQL = "";
		}

		if(!empty($SQL) && $this->_sqlite->query($SQL)) {
			return true;
		}

		return false;
	}
}