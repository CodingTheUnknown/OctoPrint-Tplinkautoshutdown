// This function is orientated to allow a popup to appear to the user and allow them to cancel the printer switching off after a print

// This is run once the page is loaded
$(function(){
    function switchWaitViewModel(parameters){
        var self = this;
        self.status = false;

        // Controlled froom the event handler.
        self.onEventPrintDone = function(payload){
            console.log("We can now begin developing a timer")
            alert("We can now begin developing a timer")
        }


        self.onEventPrintStarted = function(payload){
            console.log("We can now begin developing a timer")
            alert("We can now begin developing a timer")
        }

        console.log("Operation testing here")

    }

    OCTOPRINT_VIEWMODELS.push([
        switchWaitViewModel,
        [],
        []
    ]);
})
