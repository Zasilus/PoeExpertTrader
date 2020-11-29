function sortName() {
    var table, rows, switcher, idx, x, y, switchBool;
    table = document.getElementById("CTable");
    switcher = true;
    while (switcher) {
        switcher = false;
        rows = table.rows;
        for (idx = 1; idx < (rows.length - 1); idx++) {
            switchBool = false;
            x = rows[idx].getElementsByTagName("td")[0];
            y = rows[idx + 1].getElementsByTagName("td")[0];
                if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                    switchBool = true;
                    break;
                }
        }
        if (switchBool) {
            rows[idx].parentNode.insertBefore(rows[idx + 1], rows[idx]);
            switcher = true;
        }
    }
}
function filterNames() {
    var table = document.getElementById("CTable");
    var forminput = document.getElementById("CFilter");
    var tr = table.getElementsByTagName("tr")
    console.log(forminput.value)
    var filterString = forminput.value.toUpperCase();
    for (i = 0; i < tr.length; i++){
        td = tr[i].getElementsByTagName("td")[0];
        if(td) {
            currencyName = td.textContent || td.innerText;
            if(currencyName.toUpperCase().indexOf(filterString) > -1)
            {
                tr[i].style.display = "";
            }
            else{
                tr[i].style.display = "none";
            }
        }
    }
}

function sortExc() {
    var table, rows, switcher, idx, x, y, switchBool;
    table = document.getElementById("CTable");
    switcher = true;
    while (switcher) {
        switcher = false;
        rows = table.rows;
        for (idx = 1; idx < (rows.length - 1); idx++) {
            switchBool = false;
            x = rows[idx].getElementsByTagName("td")[4];
            y = rows[idx + 1].getElementsByTagName("td")[4];
                if (Number(x.innerHTML) < Number(y.innerHTML)) {
                    switchBool = true;
                    break;
                }
        }
        if (switchBool) {
            rows[idx].parentNode.insertBefore(rows[idx + 1], rows[idx]);
            switcher = true;
        }
    }
}

function submitOptimalCurrencyForm() {
    var http = new XMLHttpRequest();
    http.open("POST", "/optimalcurrency", true);
    http.setRequestHeader("Content-type","application/x-www-form-urlencoded");
    var params = "cinput=" + document.getElementById("cinput").value
    http.send(params);
    http.onload = function() {
        var divField = document.getElementById("optimalCurrencyDiv")
        divField.innerHTML = "The optimal currency for you to be trading is: " + http.responseText
    }
}

function sortROI() {
    var table, rows, switcher, idx, x, y, switchBool;
    table = document.getElementById("CTable");
    switcher = true;
    while (switcher) {
        switcher = false;
        rows = table.rows;
        for (idx = 1; idx < (rows.length - 1); idx++) {
            switchBool = false;
            x = rows[idx].getElementsByTagName("td")[5];
            y = rows[idx + 1].getElementsByTagName("td")[5];
                if (Number(x.innerHTML) < Number(y.innerHTML)) {
                    switchBool = true;
                    break;
                }
        }
        if (switchBool) {
            rows[idx].parentNode.insertBefore(rows[idx + 1], rows[idx]);
            switcher = true;
        }
    }
}
