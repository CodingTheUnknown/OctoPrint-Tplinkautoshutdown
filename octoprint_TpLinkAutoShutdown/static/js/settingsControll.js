
document.getElementById("update").onclick = function update_info (){
    var address = document.getElementById("address").value;
    OctoPrint.simpleApiCommand("TpLinkAutoShutdown", "update", {"url": address})
        .done(function(responce){
            //console.log(responce.res.dev_name);
            document.getElementById("deviceName").value = responce.res.dev_name;
            document.getElementById("firmwareVersion").value = responce.res.sw_ver;
        })
}
