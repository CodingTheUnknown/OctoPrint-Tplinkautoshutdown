
document.getElementById("turnOff").onclick = function turnOffPrinter() {
    var conf = confirm("Are you sure?");

    if (conf == true) {
        OctoPrint.simpleApiCommand("TpLinkAutoShutdown", "turnOff", {"value" : "False"})
            .done(function(responce) {
                alert(responce.res);
            });
    }else{
        console.log("Operation cancelled");
        alert("Operation cancelled");
    }
}

document.getElementById("turnOn").onclick = function turnOnPrinter() {
    var conf = confirm("are you sure?");

    if (conf == true) {
        OctoPrint.simpleApiCommand("TpLinkAutoShutdown", "turnOn", {"value" : "False"})
        .done(function(responce) {
            alert(responce.res);
        });
    }else{
        console.log("The operation has been cancelled");
    }
}
