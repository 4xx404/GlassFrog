<div class="portscanner-result-content" id="portscanner-result-content">
    <table class="portscanner-result-table" id="portscanner-result-table">
        <?php

            $PortScanner = new Portscanner();
            $Hasher = new Hash();
            $ScanID = $Hasher->Unique("md5");
            $PortScanner->Run($ScanID, $PortScannerTarget);
            $PortScanStatus = $Database->Select("portscanner_results", array(
                    array(
                        'column' => 'scan_id',
                        'operator' => '=',
                        'value' => $ScanID
                    ),
                    array(
                        'column' => 'host',
                        'operator' => '=',
                        'value' => $PortScannerTarget
                    )
                )
            );
            
            if($PortScanStatus) {
                echo "
                    <tr>
                        <th class='standard-table-head' style='width:40%;'>Host</th>
                        <th class='standard-table-head' style='width:5%;'>Port</th>
                        <th class='standard-table-head' style='width:5%;''>Status</th>
                        <th class='standard-table-head' style='width:10%;'>Service</th>
                    </tr>
                ";

                foreach($PortScanStatus as $PortData) {
                    echo "
                        <tr>
                            <td class='standard-table-data'>" . $PortData['host'] . "</td>
                            <td class='standard-table-data'>" . $PortData['port'] . "</a></td>
                    ";
                            if($PortData['port_status'] === "open") {
                                echo "<td class='green-font-table-data'>" . $PortData['port_status'] . "</td>";
                            } else if($PortData['port_status'] === 'closed') {
                                echo "<td class='red-font-table-data'>" . $PortData['port_status'] . "</td>";
                            }

                            echo "<td class='standard-table-data'>" . $PortData['port_service'] . "</td>
                        </tr>
                    ";
                }
            } else {
                echo "
                    <tr>
                        <th class='red-font-table-head' style='width:100%;color: red;'>No Port Data found for " . $PortScannerTarget . "</th>
                    </tr>
                ";
            }
        ?>
    </table>
</div>
