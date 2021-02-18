
document.getElementById("update").onclick = function update_info (){
    var address = document.getElementById("address").value;
    OctoPrint.simpleApiCommand("TpLinkAutoShutdown", "update", {"url": address})
        .done(function(responce){
            alert(responce);
        })
    alert("Clicked");
}
