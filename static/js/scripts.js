document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
        let alerts = document.querySelectorAll(".alert");
        alerts.forEach(function(alert) {
            let fadeEffect = setInterval(function () {
                if (!alert.style.opacity) {
                    alert.style.opacity = 1;
                }
                if (alert.style.opacity > 0) {
                    alert.style.opacity -= 0.1;
                } else {
                    clearInterval(fadeEffect);
                    alert.remove();
                }
            }, 50);
        });
    }, 2000); 
});

//obesity form reset on submit- bug

function resetForm() {
    setTimeout(() => {
        document.querySelector("form").reset();
    }, 100);  
}