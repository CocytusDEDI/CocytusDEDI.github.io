const resources = document.querySelectorAll('.dropdownResource');

resources.forEach((resource, index) => {
  resource.addEventListener('click', function() {
    dropdown(`dropdown${index + 1}`, `dropdownSymbol${index + 1}`);
  });
});

const dropdownHtml = {
    dropdown1: "<a href=\"../resources/donut.png\" target=\"_blank\"><span>View donut.png</span></a>",
    dropdown2: "<a href=\"../resources/sla_s_v2.py\" download=\"sla_s_v2.py\"><span>Download sla_s_v2.py</span></a>"
};

function dropdown(dropdownID, dropdownSymbolID) {
    if (document.getElementById(dropdownID).outerHTML == "<div id=\"" + dropdownID + "\"></div>") {
            document.getElementById(dropdownID).outerHTML = "<div class=\"dropdown\" id=\"" + dropdownID + "\">" + dropdownHtml[dropdownID] + "</div>";
        document.getElementById(dropdownSymbolID).innerHTML = "<path d=\"m12 8-6 6 1.41 1.41L12 10.83l4.59 4.58L18 14z\" fill=\"#ddd\"></path>"
    }
    else {
        document.getElementById(dropdownID).outerHTML = "<div id=\"" + dropdownID + "\"></div>"
        document.getElementById(dropdownSymbolID).innerHTML = "<path d=\"M16.59 8.59 12 13.17 7.41 8.59 6 10l6 6 6-6z\" fill=\"#ddd\"></path>"
    }
}
