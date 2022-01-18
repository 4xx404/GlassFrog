<?php
class Hash {
	public function MakeBcrypt($String) {
		$Options = ['cost' => 12];

		/* Create the hash. */
		return password_hash($String, PASSWORD_DEFAULT, $Options); // 2020 JJUNE DEFAULT: bcrypt
	}

	public function MakeMD5($String) {
		return md5($String);
	}

	public function Unique($HashType = null, $String = null) {
		if($HashType !== null) {
			if(strtolower($HashType) === "md5" || strtolower($HashType) === "bcrypt") {
				if(strtolower($HashType === "md5" && $String !== null)) {
					return $this->MakeMD5($String);
				} else if(strtolower($HashType) === "md5" && $String === null) {
					return $this->MakeMD5(uniqid());
				} else if(strtolower($HashType) === "bcrypt" && $String !== null) {
					return $this->MakeBcrypt($String);
				} else if(strtolower($HashType) === "bcrypt" && $String === null) {
					return $this->MakeBcrypt(uniqid());
				} else {
					return false;
				}
			} else {
				return false;
			}
		}
		
		return false;
	}
}