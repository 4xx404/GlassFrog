<?php
class DateTimeManager {
    public function __construct() {
        $this->Response = '';
    }

    public function GetDateTime() {
        $this->Response = date("d-m-Y H:i:s");

        if(!empty($this->Response)) {
            return $this->Response;
        }

        return false;
    }

    public function GetDate() {
        return date("d-m-Y");
    }

    public function GetTime(bool $WithAmOrPm = false) {
        if($WithAmOrPm) {
            return date("H:i:s a");
        }

        return date("H:i:s");
    }

    public function GetDeleteDate(string $Date, string $TimePassed) {
        $Date = isset($Date) ? strval($Date) : '';
        $TimePassed = isset($TimePassed) ? intval($TimePassed) : 24;

        // Day Count => Months with that amount of days
        $MonthToDayCountMap = array(
            '31_days' => array('01', '03', '05', '07', '08', '10', '12'),
            '30_days' => array('04', '06', '09', '11'),
            '28_days' => array('02'),
        );

        if(!empty($Date)) {
            $DatePiece = explode(" ", $Date)[0];
            $TimePiece = explode(" ", $Date)[1];

            $Year = explode("-", $DatePiece)[2];
            $Month = explode("-", $DatePiece)[1];
            $Day = explode("-", $DatePiece)[0];

            if(in_array(strval($Month), $MonthToDayCountMap['31_days'])) {
                if(intval($Day) >= 31 && intval($Month) >= 12) {
                    $Day = '01';
                    $Month = '01';
                    $Year = strval(intval($Year) + 1);
                } else if(intval($Day) >= 31 && intval($Month) <= 11) {
                    $Day = '01';
                    $Month = strval(intval($Month) + 1);
                } else if(intval($Day) <= 30) {
                    $Day = strval(intval($Day) + 1);
                } else {
                    $Day = $Day;
                    $Month = $Month;
                    $Year = $Year;
                }

                $this->Response = "{$Day}-{$Month}-{$Year} {$TimePiece}";
            } else if(in_array(strval($Month), $MonthToDayCountMap['30_days'])) {
                if(intval($Day) >= 30) {
                    $Day = '01';
                    if($Month === '04') {
                        $Month = '05';
                    } else if($Month === '06') {
                        $Month = '07';
                    } else if($Month === '09') {
                        $Month = '10';
                    } else if($Month === '11') {
                        $Month = '12';
                    } else {
                        $Month = $Month;
                    }
                } else if(intval($Day) <= 29) {
                    $Day = strval(intval($Day) + 1);
                    $Month = $Month;
                } else {
                    $Day = $Day;
                    $Month = $Month;
                }

                $this->Response = "{$Day}-{$Month}-{$Year} {$TimePiece}";
            } else if(in_array(strval($Month), $MonthToDayCountMap['28_days'])) {
                if(intval($Day) >= 28 && $Month === '02') {
                    $Day = '01';
                    $Month = '03';
                } else if(intval($Day) <= 27 && $Month === '02') {
                    $Day = strval(intval($Day) + 1);
                    $Month = $Month;
                } else {
                    $Day = $Day;
                    $Month = $Month;
                }

                $this->Response = "{$Day}-{$Month}-{$Year} {$TimePiece}";
            } else {
                $this->Response =  false;
            }

            return $this->Response;
        }
        
        return false;
    }
}
?>