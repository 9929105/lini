


var allObjects
var curlink = "http://127.0.0.1:8000/PersonSearch/?format=json";
var curobj = {};
function populateData(){
	curobj = {};
	sessionStorage.removeItem("curPatient");
	sessionStorage.removeItem("return_url");
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

function openModal(obj) {
	var modal = document.getElementById("modal");
	modal.innerHTML = 
	"<div class=\"bbm-wrapper\" style=\"display: block;\"><div style=\"opacity: 1;\" class=\"bbm-modal bbm-modal--open\">"
	  +"<div class=\"bbm-modal__topbar\"></div>"
	  +"<div class=\"bbm-modal__section\">"
	   +"<div class=\"control-group\">"
	    +"<h4>Details</h4>"
	    +"<table class=\"table\" id=\"detail_table\">"
	    +"</table>"
	    +"</div>"
	  +"</div>"
	  +"<div class=\"bbm-modal__bottombar\">"
	  	+"<a href=\"\" onclick=encntrObject() id=\"encntr_data_btn\" style=\"text-align: left\" class=\"btn\" >New Encounter</a>&nbsp;&nbsp;&nbsp;"  
	  	+"<a href=\"\" onclick=editObject() id=\"edit_data_btn\" style=\"text-align: left\" class=\"btn\" >Edit Patient Data</a>&nbsp;&nbsp;&nbsp;"
	    +"<a href=\"#\" class=\"btn btn-primary\" onclick=closeModal()>Done</a>"
	  +"</div></div></div></div>";
	fillDetail(obj, "detail_table");

}
function fillDetail(obj,table_id){
	curobj = obj;
	sessionStorage.setItem('curPatient', JSON.stringify(curobj));
	sessionStorage.setItem('return_url',window.location.href);

	var table= document.getElementById(table_id);
	
	table.appendChild(createNVPair("Last Name", obj["name_last"]));
	table.appendChild(createNVPair("First Name", obj["name_first"]));
	table.appendChild(createNVPair("Sex", obj["sex"]));
	table.appendChild(createNVPair("Birthdate", obj["birthdate"]));
	table.appendChild(createNVPair("Identifier", obj["identifier"]));
}
function createNVPair(name, value){
	var  tr= document.createElement("tr");
	tr.innerHTML="<td>"+name+"</td>"+"<td>"+value+"</td>";
	return tr
}
function editObject(){
	closeModal();
	window.location.href="./Patient_Entry.html";
}
function encntrObject(){
	closeModal();
	window.location.href="./Encounter_Entry.html";
}

function closeModal(){
	var modal = document.getElementById("modal");
	modal.innerHTML = ""
}

function parseResponse(response) {
	
	var obj = JSON.parse(response)
	parseResults(obj["results"],"result_table")
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

function createHeader(headerName){
	var th = document.createElement("th");
    th.innerHTML="<th class=\"js-sort\" data-field=\"name_last\">"
					+headerName+"<i class=\"icon-sort DataTable-sortIcon\"></i>"
					+"</th>";
	return th
}


function parseResults(objArray, result_table_id) {
	allObjects = objArray
	var result_table = document.getElementById(result_table_id);
	
	var thead = document.createElement("thead")
	var tr = document.createElement("tr");
	
	tr.appendChild(createHeader("Last Name"));
	tr.appendChild(createHeader("First Name"));
	tr.appendChild(createHeader("Sex"));
	tr.appendChild(createHeader("Birthdate"));
	tr.appendChild(createHeader("Identifier"));
	thead.appendChild(tr);
	
	result_table.appendChild(thead);
	
	var tbody = document.createElement("tbody");
	
	for (idx in objArray){
		var obj = objArray[idx];
		
		tr = document.createElement("tr");
		
		tr.refObject = obj;
		tr.onclick = function() {	
			openModal(this.refObject);
		}
		tr.innerHTML +=
			   	"<td>"+obj["name_last"]+"</td>"+
				"<td>"+obj["name_first"]+"</td>"+
				"<td>"+obj["sex"]+"</td>"+
				"<td>"+obj["birthdate"]+"</td>"+
				"<td>"+obj["identifier"]+"</td>";
		tbody.appendChild(tr);
	}	
	result_table.appendChild(tbody);
}



if(window.attachEvent) {
    window.attachEvent('onload', populateData);
} else {
    if(window.onload) {
        var curronload = window.onload;
        var newonload = function() {
            curronload();
            populateData();
        };
        window.onload = newonload;
    } else {
        window.onload = populateData;
    }
}
