var tablinks = document.getElementsByClassName("tab-links");
console.log(tablinks)
var tabcontents = document.getElementsByClassName("tab-contents");
console.log(tabcontents)
function opentab(tabname){
    for(tablink of tablinks){
        console.log(tablink)
        tablink.classList.remove("active-link");
    }

    for(tabcontent of tabcontents){
        console.log(tabcontent)
        tabcontent.classList.remove("active-tab");
    }

    event.currentTarget.classList.add("active-link");
    document.getElementById(tabname).classList.add("active-tab")
}


// Script for open and close bar menue
var sidemenue = document.getElementById("sidemenu");
function openmenu(){
    sidemenue.style.right= "0"
}

function closemenu(){
    sidemenue.style.right= "-200px"
}





