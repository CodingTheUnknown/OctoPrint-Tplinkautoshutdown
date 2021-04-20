
document.getElementById("turnOff").onclick = function turnOffPrinter() {
    var conf = confirm("Are you sure you wish to turn OFF your smart plug?");

    if (conf == true) {
        OctoPrint.simpleApiCommand("TpLinkAutoShutdown", "turnOff", {"value" : "False"})
            .done(function(responce) {if (responce.res != "") alert(responce.res)});
    }else{
        console.log("Operation cancelled");
        alert("Operation cancelled");
    }
}

document.getElementById("turnOn").onclick = function turnOnPrinter() {
    var conf = confirm("Are you sure you wish to turn ON your smart plug?");

    if (conf == true) {
        OctoPrint.simpleApiCommand("TpLinkAutoShutdown", "turnOn", {"value" : "False"})
        .done(function(responce) {});
    }else{
        console.log("The operation has been cancelled");
    }
}
