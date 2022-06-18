<?php
class DateTimeManager {
    public static function GetDateTime(): string {
        return date("d-m-Y H:i:s");
    }

    public static function GetDate(): string {
        return date("d-m-Y");
    }

    public static function GetTime(bool $WithAmOrPm = false): string {
        return ($WithAmOrPm === true) ? date("H:i:s a") : date("H:i:s");
    }

    public static function GetDeleteDate(string $Date = null, string $TimePassed = null): string|false {
        $Date = (($Date !== null) ? strval($Date) : "");
        $TimePassed = (($TimePassed !== null) ? intval($TimePassed) : 24);

        // Day Count => Months with that amount of days
        $MonthToDayCountMap = array(
            "31_days" => array("01", "03", "05", "07", "08", "10", "12"),
            "30_days" => array("04", "06", "09", "11"),
            "28_days" => array("02"),
        );

        if(!empty($Date)) {
            $DatePiece = explode(" ", $Date)[0];
            $TimePiece = explode(" ", $Date)[1];

            $Year = explode("-", $DatePiece)[2];
            $Month = explode("-", $DatePiece)[1];
            $Day = explode("-", $DatePiece)[0];

            if(in_array(strval($Month), $MonthToDayCountMap["31_days"])) {
                if(intval($Day) >= 31 && intval($Month) >= 12) {
                    $Day = $Month = "01";
                    $Year = strval(intval($Year) + 1);
                } else if(intval($Day) >= 31 && intval($Month) <= 11) {
                    $Day = "01";
                    $Month = strval(intval($Month) + 1);
                } else if(intval($Day) <= 30) {
                    $Day = strval(intval($Day) + 1);
                }

                return "{$Day}-{$Month}-{$Year} {$TimePiece}";
            } else if(in_array(strval($Month), $MonthToDayCountMap["30_days"])) {
                if(intval($Day) >= 30) {
                    $Day = "01";

                    if($Month === "04") {
                        $Month = "05";
                    } else if($Month === "06") {
                        $Month = "07";
                    } else if($Month === "09") {
                        $Month = "10";
                    } else if($Month === "11") {
                        $Month = "12";
                    }
                } else if(intval($Day) <= 29) {
                    $Day = strval(intval($Day) + 1);
                }

                return "{$Day}-{$Month}-{$Year} {$TimePiece}";
            } else if(in_array(strval($Month), $MonthToDayCountMap["28_days"])) {
                if(intval($Day) >= 28 && $Month === "02") {
                    $Day = "01";
                    $Month = "03";
                } else if(intval($Day) <= 27 && $Month === "02") {
                    $Day = strval(intval($Day) + 1);
                }

                return "{$Day}-{$Month}-{$Year} {$TimePiece}";
            }
        }
        
        return false;
    }
}
?>