const Show = 'block';
const Hide = 'none';

function CapitalizeFirstLetterOfWords(Value) {
	if(typeof Value === 'string') {
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
		let Values = Value.split("_");
		let ReturnString = CapitalizeFirstLetterOfWords(Values).join(" ");

		document.getElementById("form-header").innerHTML = ReturnString;
	} else {
		// Capitalize First Letter of 1 word (string type)
		document.getElementById("form-header").innerHTML = CapitalizeFirstLetterOfWords(Value);
	}
}

