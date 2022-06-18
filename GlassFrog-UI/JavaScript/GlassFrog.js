function CapitalizeFirstLetterOfWords(Value) {
	if(typeof Value === "string" || Value instanceof String) {
		return Value.charAt(0).toUpperCase() + Value.slice(1);
	} else {
		var MultiValues = [];

		for(let Val = 0; Val < Value.length; Val++) {
			MultiValues.push(Value[Val].charAt(0).toUpperCase() + Value[Val].slice(1));
		}

		return MultiValues;
	}
}

function SetFormHeader() {
	let Value = document.getElementById("tool").value;

	if(Value.includes("_")) {
		document.getElementById("form-header").innerHTML = CapitalizeFirstLetterOfWords(Value.split("_")).join(" ");
	} else {
		// Capitalize First Letter of 1 word (string type)
		document.getElementById("form-header").innerHTML = CapitalizeFirstLetterOfWords(Value);
	}
}

