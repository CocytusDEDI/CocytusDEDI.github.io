const resources = document.querySelectorAll('.dropdownResource');

resources.forEach((resource, index) => {
  resource.addEventListener('click', function() {
    dropdown(`dropdown${index + 1}`, `dropdownSymbol${index + 1}`);
  });
});

const dropdownHtml = {
    dropdown1: "<a href=\"../resources/donut.png\" target=\"_blank\"><span class=\"downloadLink\">View donut.png</span></a><br><br><span>This donut was my first project in blender which I had picked up to have a try at 3D modelling</span>",
    dropdown2: "<a href=\"../resources/sla_s_v2.py\" download=\"sla_s_v2.py\"><span class=\"downloadLink\">Download sla_s_v2.py</span></a><br><a href=\"../resources/backdoor master.py\" download=\"backdoor master.py\"><span class=\"downloadLink\">Download python backdoor master.py</span></a><br><br><span>These files are a pair, used to send and receive command line commands. They were made early in my programming career and thus are very basic.</span>"
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
