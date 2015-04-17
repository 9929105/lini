


var allPersons
var curlink = "http://127.0.0.1:8000/PersonSearch/?format=json";
var curobj = {};
function getResults(){
 	var xmlhttp = new XMLHttpRequest();
	var url = curlink;
		
	xmlhttp.onreadystatechange=function() {
	    if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
	    	parseResponse(xmlhttp.responseText);
	    }
	}
	xmlhttp.open("GET", url, true);
	xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
	xmlhttp.send(); 
	
}



function updateObject_OnClick(){
 	var xmlhttp = new XMLHttpRequest();
	var url = "http://127.0.0.1:8000/PersonSearch/";
	
	var obj ={}
	if (curobj.id > 0) {
		obj = curobj
		url = url+curobj.id+"/"
		xmlhttp.open("PUT", url, true);
	} else {
		xmlhttp.open("POST", url, true);
	}
	xmlhttp.onreadystatechange=function() {
	    if (xmlhttp.readyState == 4) {
	    	parsePostResponse(xmlhttp.responseText);
	    }
	}

	xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
	
	
	obj.end_effective_td = Date("2199-12-31T23:59:00"); 
	obj.created_by = 1;
	obj.modified_by = 1;
    //"created_by": 1,
    //"modified_by": 1}
	
	obj.name_last = document.getElementById("name_last").value;
	obj.name_first = document.getElementById("name_first").value;
	obj.sex = ((document.getElementById("male").checked)? "male" : "female");
	
	obj.birthdate = document.getElementById("birthdate").value;
	obj.identifier = document.getElementById("identifier").value;
	xmlhttp.send(JSON.stringify(obj)); 
	
}


function parseResponse(response) {
	
	var obj = JSON.parse(response)
	parseResults(obj["results"])
	curlink = obj["next"];
   
}


function selectObject(obj)
{

  curobj = obj;
  document.getElementById("name_last").value = obj["name_last"];
  document.getElementById("name_first").value = obj["name_first"];
  document.getElementById("sex").value = obj["sex"];  
  document.getElementById("birthdate").value = obj["birthdate"];  
  document.getElementById("identifier").value = obj["identifier"];  
  
}

function parseResults(objArray, table) {
	allPersons = objArray
	document.getElementById('result_table').innerHTML = "";
	var result_table = document.getElementById('result_table');
	var tr = document.createElement("tr");
	tr.innerHTML = "<td>ID</td><td>Last Name</td><td>First Name</td><td>Sex</td><td>Birthdate</td><td>Identifier</td>";

	result_table.appendChild(tr);
	for (idx in objArray){
		var obj = objArray[idx];
		
		tr = document.createElement("tr");
		
		tr.refObject = obj;
		tr.onclick = function() {
			selectObject(this.refObject);
		}
		tr.innerHTML +=
				"<td>"+obj["id"]+"</td>"+
			   	"<td>"+obj["name_last"]+"</td>"+
				"<td>"+obj["name_first"]+"</td>"+
				"<td>"+obj["sex"]+"</td>"+
				"<td>"+obj["birthdate"]+"</td>"+
				"<td>"+obj["identifier"]+"</td>";
		result_table.appendChild(tr);
	}	
}



