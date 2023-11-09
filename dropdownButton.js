document.getElementById("dropdownButton").addEventListener("click", dropdown);

function dropdown() {
    if (document.getElementById("dropdownTest").outerHTML == "<div id=\"dropdownTest\"></div>") {
        document.getElementById("dropdownTest").outerHTML = "<div class=\"dropdown\" id=\"dropdownTest\"><span>This is a test<br><br>This is a another test</span></div>"
        document.getElementById("dropdownSymbol").innerHTML = "<path d=\"m12 8-6 6 1.41 1.41L12 10.83l4.59 4.58L18 14z\" fill=\"#ddd\"></path>"
    }
    else {
        document.getElementById("dropdownTest").outerHTML = "<div id=\"dropdownTest\"></div>"
        document.getElementById("dropdownSymbol").innerHTML = "<path d=\"M16.59 8.59 12 13.17 7.41 8.59 6 10l6 6 6-6z\" fill=\"#ddd\"></path>"
    }
}
