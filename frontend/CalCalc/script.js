function printOutput() {
    calories = document.getElementById('calories').value

    //Actual API Call for when we have a working API
    /*
    calculateSteps(calories, function(steps) {
        document.getElementById("output").innerHTML = steps;
    });
    */

    //Psuedo Calculation for demontration
    document.getElementById("output").innerHTML = 

    '<div class="alert alert-danger" role="alert">' +
      calories + ' Calories' +
    '</div>' +
    '<div class="alert alert-success" role="alert">' +
       calories * 20 + ' Steps' +
    '</div>';
}

function calculateSteps(calories, callback) {
    fetch("/calCalc?calories=" + calories)
    .then(response => response.text())
    .then(steps => {
        callback(steps);
    });
}
