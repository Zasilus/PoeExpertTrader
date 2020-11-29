function sortName() {
    var table, rows, switcher, idx, x, y, switchBool;
    table = document.getElementById("DTable");
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
    var table = document.getElementById("DTable");
    var forminput = document.getElementById("DFilter");
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
function sortPPC() {
    var table, rows, switcher, idx, x, y, switchBool;
    table = document.getElementById("DTable");
    switcher = true;
    while (switcher) {
        switcher = false;
        rows = table.rows;
        for (idx = 1; idx < (rows.length - 1); idx++) {
            switchBool = false;
            x = rows[idx].getElementsByTagName("td")[1];
            y = rows[idx + 1].getElementsByTagName("td")[1];
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
function sortPPS() {
    var table, rows, switcher, idx, x, y, switchBool;
    table = document.getElementById("DTable");
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
function sortNet() {
    var table, rows, switcher, idx, x, y, switchBool;
    table = document.getElementById("DTable");
    switcher = true;
    while (switcher) {
        switcher = false;
        rows = table.rows;
        for (idx = 1; idx < (rows.length - 1); idx++) {
            switchBool = false;
            x = rows[idx].getElementsByTagName("td")[6];
            y = rows[idx + 1].getElementsByTagName("td")[6];
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
function sortROI() {
    var table, rows, switcher, idx, x, y, switchBool;
    table = document.getElementById("DTable");
    switcher = true;
    while (switcher) {
        switcher = false;
        rows = table.rows;
        for (idx = 1; idx < (rows.length - 1); idx++) {
            switchBool = false;
            x = rows[idx].getElementsByTagName("td")[7];
            y = rows[idx + 1].getElementsByTagName("td")[7];
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
