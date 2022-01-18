<?php
class Validate {
	public function __construct(){
		$this->_DomainExtensions = ['.com', '.net', '.edu', '.org', '.gov', '.int', '.mil', '.aero', '.cat', '.asia', '.mobi', '.coop', '.travel', '.tel', '.jobs', '.pro', '.biz', '.info', '.store', '.me', '.co', '.online', '.xyz', '.site', '.club', '.shop', '.app', '.live', '.ac', '.ad', '.ae', '.af', '.ag', '.ai', '.al', '.am', '.an', '.ao', '.aq', '.ar', '.as', '.at', '.au', '.aw', '.ax', '.az', '.ba', '.bb', '.bd', '.be', '.bf', '.bg', '.bh', '.bi', '.bj', '.bl', '.bm', '.bn', '.bo', '.br', '.bq', '.bs', '.bt', '.bv', '.bw', '.by', '.bz', '.ca', '.cc', '.cd', '.cf', '.cg', '.ch', '.ci', '.ck', '.cl', '.cm', '.cn', '.co', '.cr', '.cs', '.cu', '.cv', '.cw', '.cx', '.cy', '.cz', '.dd', '.de', '.dj', '.dk', '.dm', '.do', '.dz', '.ec', '.ee', '.eg', '.eh', '.er', '.es', '.et', '.eu', '.fi', '.fj', '.fk', '.fm', '.fo', '.fr', '.ga', '.gb', '.gd', '.ge', '.gf', '.gg', '.gh', '.gi', '.gl', '.gm', '.gn', '.gp', '.gq', '.gr', '.gs', '.gt', '.gu', '.gw', '.gy', '.hk', '.hm', '.hn', '.hr', '.ht', '.hu', '.id', '.ie', '.il', '.im', '.in', '.io', '.iq', '.ir', '.is', '.it', '.je', '.jm', '.jo', '.jp', '.ke', '.kg', '.kh', '.ki', '.km', '.kn', '.kp', '.kr', '.kw', '.ky', '.kz', '.la', '.lb', '.lc', '.li', '.lk', '.lr', '.ls', '.lt', '.lu', '.lv', '.ly', '.ma', '.mc', '.me', '.mf', '.mg', '.mh', '.mk', '.ml', '.mm', '.mn', '.mo', '.mp', '.mq', '.mr', '.ms', '.mt', '.mu', '.mv', '.mw', '.mx', '.my', '.mz', '.na', '.nc', '.ne', '.nf', '.ng', '.ni', '.nl', '.no', '.np', '.nr', '.nu', '.nz', '.om', '.pa', '.pe', '.pf', '.pg', '.ph', '.pk', '.pm', '.pn', '.pr', '.ps', '.pt', '.pw', '.qa', '.re', '.ro', '.rs', '.ru', '.rw', '.sa', '.sb', '.sc', '.sd', '.se', '.sg', '.si', '.sj', '.sk', '.sl', '.sm', '.sn', '.so', '.sr', '.ss', '.st', '.su', '.sv', '.sx', '.sy', '.sz', '.tc', '.td', '.tf', '.tg', '.th', '.tj', '.tk', '.tl', '.tm', '.tn', '.to', '.tp', '.tr', '.tt', '.tv', '.tw', '.tz', '.ua', '.ug', '.uk', '.um', '.us', '.uy', '.uz', '.va', '.vc', '.ve', '.vg', '.vi', '.vn', '.vu', '.wf', '.ws', '.ye', '.yt', '.yu', '.za', '.zm', '.zr', '.zw'];
		$this->_AllowedActions = ['get_host_name', 'get_ip_address'];
	}

	public function IsAllowedAction($Action) {
		if(in_array($Action, $this->_AllowedActions)) {
			return true;
		}

		return false;
	}

    public function IsValidURLFormat($Link) {
		if(substr($Link, 0, 7) === "http://" || substr($Link, 0, 8) === "https://") {
			$HasDomainExtension = 0;
			foreach($this->_DomainExtensions as $DomainExtension) {
				if(strpos($Link, $DomainExtension)) {
					$HasDomainExtension++;
				} else {
					$HasDomainExtension = $HasDomainExtension;
				}
			}

			if($HasDomainExtension > 0) {
				return true;
			} else {
				return false;
			}
		} else {
			return false;
		}
    }
}