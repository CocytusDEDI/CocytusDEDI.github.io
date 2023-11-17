const resources = document.querySelectorAll('.dropdownResource');

resources.forEach((resource, index) => {
  resource.addEventListener('click', function() {
    dropdownToggle(`dropdown${index + 1}`, `dropdownSymbol${index + 1}`);
  });
});

const dropdownHtml = {
    dropdown1: "<a href=\"../resources/donut.png\" target=\"_blank\"><span class=\"link\">View donut.png</span></a><br><br><span>This donut was my first project in blender which I had picked up to have a try at 3D modelling.</span>",
    dropdown2: "<a href=\"../resources/sla_s_v2.py\" download=\"sla_s_v2.py\"><span class=\"link\">Download sla_s_v2.py</span></a><br><a href=\"../resources/backdoor master.py\" download=\"backdoor master.py\"><span class=\"link\">Download backdoor master.py</span></a><br><br><span>These files are a pair, used to send and receive command line commands. They were made early in my programming career and thus are very basic.</span>",
    dropdown3: "<span class=\"warning\">WARNING: Don't run this program if you have epilepsy or unsaved files on your computer.</span><br><br><a href=\"../resources/VapourWave.py\" download=\"VapourWave.py\"><span class=\"link\">Download VapourWave.py</span></a><br><br><span>This program is the result of my experimentation with the python library Tkinter, since it was written ages ago, it is terribly written but does work. The program displays too windows, it resizes one and moves one, one of the programs will ask the user if they're an idiot, if no is clicked, the no button will move away randomly, if yes is clicked, an imitation of the 'You are an idiot' malware will start (It's harmless, the most it can do is crash your computer and that's unlikely). The imitation will make multiple windows appear that randomly teleport around the screen, flashing between two images that both call the user an idiot.</span>",
    dropdown4: "<a href=\"../resources/ZERO.py\" download=\"ZERO.py\"><span class=\"link\">Download ZERO.py</span></a><br><br><span>ZERO is a combination of some code I've written in the past put into one menu, it also includes the backdoor master program under the Backdoor Malware project.</span>",
    dropdown5: "<a href=\"../resources/RSA.py\" download=\"RSA.py\"><span class=\"link\">Download RSA.py</span></a><br><br><span>This python file contains the functions needed for RSA encryption algorithm and has an example at the bottom but it contains errors</span>",
    dropdown6: "<a href=\"https://studentrobotics.org/blog/2023-04-09-haberdashers-win-sr2023/\" target=\"_blank\"><span class=\"link\">Read the Student Robotics blog</span></a><br><a href=\"https://issuu.com/sherbornetimes/docs/st0140_june_2023_issuu/42\" target=\"_blank\"><span class=\"link\">Read the Sherborne Times article</span></a><br><br><span>I participated in the Student Robotics competition as the project manager for Sherborne School's team in which I also did all the electronics myself because of our lack of members. Our team came 6th out of 37 schools and won the rookie team award since it was our first time competing unlike many other schools, earning me the headmaster's commendation and a feature in the Sherborne Times.</span>",
    dropdown7: "<span>I used the Rasberry Pi's camera and it's GPIO pins and I wrote code for both to control them. In doing so I learnt about flashing Rasberry Pi's, operating systems and linux's command line. Unfortunately I don't have access to the orginal code currently.</span>"
};

function dropdownToggle(dropdownID, dropdownSymbolID) {
    if (document.getElementById(dropdownID).outerHTML == "<div id=\"" + dropdownID + "\"></div>") {
        document.getElementById(dropdownID).outerHTML = "<div class=\"dropdown\" id=\"" + dropdownID + "\">" + dropdownHtml[dropdownID] + "</div>";
        document.getElementById(dropdownSymbolID).innerHTML = "<path d=\"m12 8-6 6 1.41 1.41L12 10.83l4.59 4.58L18 14z\" fill=\"#ddd\"></path>"
    }
    else {
        document.getElementById(dropdownID).outerHTML = "<div id=\"" + dropdownID + "\"></div>"
        document.getElementById(dropdownSymbolID).innerHTML = "<path d=\"M16.59 8.59 12 13.17 7.41 8.59 6 10l6 6 6-6z\" fill=\"#ddd\"></path>"
    }
}
