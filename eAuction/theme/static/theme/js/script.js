function confirmDelete(urlDelete) {
    var yes = confirm("Tem certeza que deseja excluir?");
    if (yes) {
        location.href = urlDelete;
    }
}

function confirmDeactivate(urlDelete) {
    var yes = confirm("Tem certeza que deseja desativar?");
    if (yes) {
        location.href = urlDelete;
    }
}

function confirmActivate(urlDelete) {
    var yes = confirm("Tem certeza que deseja ativar?");
    if (yes) {
        location.href = urlDelete;
    }
}

function countDown(start_date, end_date, bid_countdown, bid_button) {        
    // Set the date we're counting down to
    var initDate = new Date(start_date).getTime();
    var countDownDate = new Date(end_date).getTime();
    // Update the count down every 1 second
    var x = setInterval(function() {

        // Get today's date and time
        var now = new Date().getTime();

        // Find the distance between now and the count down date
        var timeBefore = initDate - now;
        var distance = countDownDate - now;

        // Time calculations for days, hours, minutes and seconds
        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);

        var daysBefore = Math.floor(timeBefore / (1000 * 60 * 60 * 24));
        var hoursBefore = Math.floor((timeBefore % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutesBefore = Math.floor((timeBefore % (1000 * 60 * 60)) / (1000 * 60));
        var secondsBefore = Math.floor((timeBefore % (1000 * 60)) / 1000);

        // Display the result in the element object
        if (timeBefore > 0) {
            bid_countdown.innerHTML = "Tempo para começar: " + daysBefore + "d " + hoursBefore + "h "
            + minutesBefore + "m " + secondsBefore + "s ";
        } else {
            bid_countdown.innerHTML = days + "d " + hours + "h "
            + minutes + "m " + seconds + "s ";
        }
        
        // If the count down is finished, write some text
        if (timeBefore > 0) {
            clearInterval(x)
            bid_button.style.visibility = "hidden";
        } else {
            if (distance < 0) {
                clearInterval(x);
                bid_countdown.innerHTML = "EXPIRADO";
                bid_button.style.visibility = "hidden";
            }
        }    
    }, 1000);
}

