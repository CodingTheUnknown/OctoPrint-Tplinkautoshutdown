
window.onload = function() {
    document.getElementById("smartPlugDeviceInfo").style.display = "none";
    document.getElementById("smartPlugOptions").style.display = "none";
    document.getElementById("smartStripOptions").style.display = "none";
    document.getElementById("btnControl").style.display = "none";
}

document.getElementById("update").onclick = function update_info (){
    var address = document.getElementById("address").value;
    var deviceType = document.getElementById("deviceType").value;
    OctoPrint.simpleApiCommand("TpLinkAutoShutdown", "update", {"url": address, "deviceType": deviceType})
        .done(function(responce){
            //console.log(responce.res.dev_name);
            document.getElementById("deviceName").value = responce.res.dev_name;
            document.getElementById("firmwareVersion").value = responce.res.sw_ver;
        })

    if (deviceType == "smartPlug"){
       document.getElementById("smartPlugDeviceInfo").style.display = "block";
       document.getElementById("smartPlugOptions").style.display = "block";
       document.getElementById("smartStripOptions").style.display = "none";
       document.getElementById("btnControl").style.display = "none";
    }else if (deviceType == "smartStrip"){
       document.getElementById("smartPlugDeviceInfo").style.display = "block";
       document.getElementById("smartPlugOptions").style.display = "none";
       document.getElementById("smartStripOptions").style.display = "block";
       document.getElementById("btnControl").style.display = "block";
    }else{
       document.getElementById("smartPlugDeviceInfo").style.display = "none";
       document.getElementById("smartPlugOptions").style.display = "none";
       document.getElementById("btnControl").style.display = "none";
    }
}
