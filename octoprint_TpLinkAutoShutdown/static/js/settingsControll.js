
document.getElementById("update").onclick = function update_info (){
    var address = document.getElementById("address").value;
    OctoPrint.simpleApiCommand("TpLinkAutoShutdown", "update", {"url": address})
        .done(function(responce){
            console.log(responce.res.dev_name);
            document.getElementById("device_name").value = responce.res.dev_name;
        })
}
