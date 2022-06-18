<?php
class Hash {
	public static function Bcrypt(string $String = null): string|false {
		// Password standard, cannot create with uniqid() like md5
		return (($String !== null) ? password_hash($String, PASSWORD_DEFAULT, ["cost" => 12]) : "");
	}

	public static function MD5(string $String = null): string {
		return md5(($String !== null) ? $String : uniqid());
	}

	public static function Make(string $HashType = null, string $String = null): string {
		$HashType = (($HashType !== null) ? lowercase($HashType) : "md5");
		$String = (($String !== null) ? $String : uniqid());

		return (($HashType === "md5") ? self::MD5($String) : (($HashType === "bcrypt") ? self::Bcrypt($String) : ""));
	}
}