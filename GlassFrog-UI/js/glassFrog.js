function showBranches(){
	document.getElementById('branchDataContent').style.display = 'none';
	document.getElementById('branchesContent').style.display = 'block';
	document.getElementById('branchesBtn').style.backgroundColor = '#333';
	document.getElementById('branchDataBtn').style.backgroundColor = '#000';
}

function showBranchData(){
	document.getElementById('branchesContent').style.display = 'none';
	document.getElementById('branchDataContent').style.display = 'block';
	document.getElementById('branchesBtn').style.backgroundColor = '#000';
	document.getElementById('branchDataBtn').style.backgroundColor = '#333';
}
