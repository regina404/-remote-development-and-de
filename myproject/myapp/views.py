from django.shortcuts import render
from django.http import JsonResponse
import random
import time
import Adafruit_BBIO.GPIO as GPIO

led_pins = {"LED1": "USR0", "LED2": "USR1", "LED3": "USR2", "LED4": "USR3"}

for pin in led_pins.values():
    GPIO.setup(pin, GPIO.OUT)

#Повертає поточний стан світлодіода
def get_led_status(led):
    return GPIO.input(led_pins[led])

#Встановлює стан світлодіода
def set_led_status(led, status):
    GPIO.output(led_pins[led], status)


def index(request):
    return render(request, 'index.html')

#Перемикає стан світлодіода
def toggle_led(request, led):
    set_led_status(led, not get_led_status(led))
    response_data = {
        "result": "success",
        "message": f"LED {led} {'ON' if get_led_status(led) else 'OFF'}",
    }
    return JsonResponse(response_data)

#Перемикає стан всіх світлодіодів
def toggle_all(request):
    current_state = GPIO.input(led_pins["LED1"])

    new_state = not current_state
    for pin in led_pins.values():
        GPIO.output(pin, new_state)

    response_data = {
        "result": "success",
        "message": f"All LEDs {'ON' if new_state else 'OFF'}",
    }
    return JsonResponse(response_data)

#Встановлює стан всіх світлодіодів
def set_all_leds(status):
    for led in led_pins:
        set_led_status(led, status)

#Вмикає кожен світлодіод послідовно з певною затримкою між ними.
def running_leds(request):
    if request.method == 'POST':
        delay = float(request.POST.get('delay', 0.1))
        for led in led_pins:
            set_led_status(led, True)
            time.sleep(delay)
            set_led_status(led, False)
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'error': 'Invalid request method'})

#Вмикає і вимикає випадковий світлодіод декілька разів з певною затримкою між кожним переключенням.
def toggle_led_without_request(led):
    set_led_status(led, not get_led_status(led))

def random_leds_blink(request):
    if request.method == 'POST':
        delay = float(request.POST.get('delay', 0.1))
        blink_count = int(request.POST.get('count', 10))

        for _ in range(blink_count):
            led = random.choice(list(led_pins.keys()))
            toggle_led_without_request(led)
            time.sleep(delay)
            toggle_led_without_request(led)

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'error': 'Invalid request method'})

