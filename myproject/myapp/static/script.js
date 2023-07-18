function toggleLed(led) {
    fetch(`/toggle/${led}/`)
        .then(response => response.json())
        .then(data => console.log(data));
}

function toggleAll() {
    fetch('/toggle_all/')
        .then(response => response.json())
        .then(data => console.log(data));
}

function runningLeds() {
    fetch('/running_leds/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': window.csrfToken
        },
        body: JSON.stringify({ delay: 0.1 })
    })
        .then(response => response.json())
        .then(data => console.log(data));
}

function randomLedsBlink() {
    fetch('/random_leds_blink/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': window.csrfToken
        },
        body: JSON.stringify({ delay: 0.1, count: 10 })
    })
        .then(response => response.json())
        .then(data => console.log(data));
}
