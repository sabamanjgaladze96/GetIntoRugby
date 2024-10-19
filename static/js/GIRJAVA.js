function turndark(){ 
    var body = document.body;
    var currentColor = body.style.backgroundColor;

    if (currentColor === "black") {
        body.style.backgroundColor = "#eeeeee";
    } else {
        body.style.backgroundColor = "black";
    }
    
    var experiments = document.getElementsByClassName("experiment");

    for (var i = 0; i < experiments.length; i++) {
        var experiment = experiments[i];
        var currentColor = window.getComputedStyle(experiment).backgroundColor;

        if (currentColor === "rgb(0, 0, 0)") {
            experiment.style.backgroundColor = "#eeeeee";
        } else {
            experiment.style.backgroundColor = "black";
        }
    }
}

function welcome(){
alert("WELCOME!");
}