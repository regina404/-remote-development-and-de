# -remote-development-and-debugging-BeagleBone-Black

There are many reasons for using remote development and debugging techniques for embedded systems. Embedded systems are often placed 
in hard-to-reach places or hazardous environments. Or embedded systems are mass-produced and direct access to each unit is not 
possible. Remote development can also significantly speed up the development cycle, allowing you to develop, update and test in 
real-time without the need for physical interaction with the device. Or when you need to give control to non-technical users so 
they can easily control embedded systems. You can use such connection options as connecting via ssh or using VNC (Virtual Network
Computing). But still, the options are no longer suitable for permanent adventures. Therefore, let's consider an http server and a VPN for remote development and debugging of embedded systems.

We will consider 2 options for remote development and debugging of embedded systems - the BeagleBone Black microcontroller
1) HTTP server
We will use the Django framework to configure the HTTP server. (Code provided on github). This is one of the options for how you can 
remotely control the built-in system, without having any technical skills. Because the logic of all the buttons is written and all 
you have to do is press the button. Such websites or applications are used for "smart home". Users of this website are users who have 
installed embedded systems.
After creating the Django project framework, install Adafruit_BBIO.GPIO: This is a library for programming embedded systems, specifically 
for the BeagleBone Black board, using the Python programming language, which provides an easy and convenient way to interact with GPIOs on the BeagleBone Black.
Let's watch a video:


https://github.com/regina404/-remote-development-and-de/assets/63124387/d8a91cf2-1a1e-45ad-869a-efcbdc7a244d


We use the command "sudo pip3 install Adafruit_BBIO"

<img width="600" alt="Adafruit_BBIO" src="https://github.com/regina404/-remote-development-and-de/assets/63124387/d7981b32-3097-4856-8320-4ef898240538">

Django's views.py file is a Python module that contains functions that run the logic for processing HTTP requests and return the corresponding 
HTTP responses. The views.py file defines the following functions:
led_pins – This dictionary maps LED names (LED1, LED2, LED3, LED4) to corresponding GPIO pins (USR0, USR1, USR2, USR3). The loop then sets the GPIO pin settings as output.
<img width="600" alt="led_pins" src="https://github.com/regina404/-remote-development-and-de/assets/63124387/9d047400-9b6f-4932-a6cb-f899972fc9bf">

get_led_status(led): The function returns the current state of the LED.
set_led_status(led, status): The function sets the state of the led to the status value.
index(request): The function handles requests to the main page and returns the index.html template.
<img width="400" alt="get_led_status" src="https://github.com/regina404/-remote-development-and-de/assets/63124387/0c734c32-dd99-41a3-a4c1-fff855baf60b">

toggle_led(request, led): The function toggles the state of the led and returns a JSON response with information about the result of the operation.
The toggle_led(request, led) function takes a led parameter that indicates the specific LED whose state needs to be changed. Using the functions get_led_status(led) and set_led_status(led, status), the current state of the LED is obtained and the opposite state is set. A JSON response is then generated containing the result of the operation and a message indicating the status of the LED.
<img width="600" alt="toggle_led" src="https://github.com/regina404/-remote-development-and-de/assets/63124387/7dee4279-4c03-4317-9580-97d96fc92d8e">

toggle_all(request): The function toggles the state of all LEDs and returns a JSON response with information about the operation result.
The toggle_all(request) function toggles the state of all LEDs. First, the current state of one of the LEDs (current_state) is determined. Then a new state opposite to the current one (new_state) is defined. The GPIO.output(pin, new_state) function changes the state of all LEDs. A JSON response is generated with the result of the operation and a message indicating the new state of all LEDs.
<img width="600" alt="toggle_all" src="https://github.com/regina404/-remote-development-and-de/assets/63124387/f256b431-53a4-4fb7-a3b6-77079bbcab26">

The function running_leds(request) is the logic of sequential inclusion and
turning off all LEDs with a certain delay between them.
If the request method is 'POST', the function gets the delay value
(delay) from the POST request parameters.
The cycle goes through all LEDs from the led_pins list. At each iteration
the LED is set to the "On" state (set_led_status(led, True)), then there is a pause (time.sleep(delay)), after which the LED is set to the "Off" state (set_led_status(led, False)).
At the end of the loop, the function returns a JSON response with a success field indicating that the operation was successful.
If the request method is not 'POST', the function returns a JSON response with an error and the message "Invalid request method".<br>

<img width="600" alt="running_leds" src="https://github.com/regina404/-remote-development-and-de/assets/63124387/769dff0c-5c34-4dd0-8ec4-4681f377067d">

The function toggle_led_without_request(led) is the logic for switching the state of the LED without the need to receive a request from the client.
It takes an argument led, which represents the name of the LED from the led_pins dictionary. The function uses set_led_status(led, status) to toggle the LED state.
Inside the function, the function get_led_status(led) is called to get the current state of the LED, and then the state is not inverted using the statement. The result is transferred to set_led_status(led, status) of changing the state of the LED to the opposite.
Thus, the function toggle_led_without_request allows you to toggle the state of the specified LED between on and off without having to receive a request from the client.<br>
<img width="600" alt="toggle_led_without_request" src="https://github.com/regina404/-remote-development-and-de/assets/63124387/8ad1c4d3-2373-4ac2-98de-20836b724d70">

The random_leds_blink(request) function is the logic for blinking random LEDs with a certain delay between them.
If the request method is 'POST', the function gets the delay value (delay) and blink_count (blink_count) from the POST request parameters.
The loop repeats blink_count times. At each iteration, a random LED is selected from the list of available LEDs (led_pins.keys()) using random.choice(). The function toggle_led_without_request(led) is then called to toggle the state of the selected LED.
This is followed by a pause (time.sleep(delay)) to create a delay between LED flashes.
At the end, the function returns a JSON response with a success field indicating the successful execution of the operation.<br>
<img width="600" alt="random_leds_blink" src="https://github.com/regina404/-remote-development-and-de/assets/63124387/7cc79d0b-612f-4fb4-976a-4ce7c8e6ad7a">

The code in the script.js file contains several functions that use the fetch method to send AJAX requests to the server and retrieve data in JSON format.
toggleLed(led) - a function for switching the state of the LED with the specified one
by name (led). It sends a GET request to the path /toggle/<str:led>/ and outputs the received data to the console. We call this function 4 times in the file index.html onclick="toggleLed('LED1'), onclick="toggleLed('LED2'), onclick= "toggleLed('LED3'), onclick="toggleLed('LED4' ).
<img width="600" alt="js" src="https://github.com/regina404/-remote-development-and-de/assets/63124387/3bb2a88a-c09b-4738-8500-6fb7e763f573">
<img width="600" alt="html" src="https://github.com/regina404/-remote-development-and-de/assets/63124387/beb7489c-0e6c-4e09-9095-79c71de4feb5">

toggleAll() - a function to switch the state of all LEDs. It sends a GET request to the path /toggle_all/ and outputs the received data to the console. We call this function in the file index.html onclick="toggleAll().
<img width="600" alt="toggleAll" src="https://github.com/regina404/-remote-development-and-de/assets/63124387/6848438c-0273-4a0c-982f-3fd21482a905">

runningLeds() - function to start running lights on LEDs. It sends a POST request to the path /running_leds/ with a delay in the request. A CSRF token (X-CSRFToken) is also transmitted in the request headers, which is commonly used to protect request forgery. The received data is output to the console. We call this function in the file index.html onclick="runningLeds()".
<img width="600" alt="runningLeds" src="https://github.com/regina404/-remote-development-and-de/assets/63124387/58c8c087-cc91-477a-b923-9e5fb4d4ad91">

randomLedsBlink() - a function for random LED blinking. It sends a POST request to the path /random_leds_blink/ with a delay (delay) and the number of blinks (count) in the request body. Similarly, the CSRF token is passed in the request headers. The received data is output to the console. We call this function in the file index.html onclick="randomLedsBlink()".
<img width="600" alt="randomLedsBlink" src="https://github.com/regina404/-remote-development-and-de/assets/63124387/07074190-7ddd-44cc-81c6-346ba2f0e5ee">

<img width="600" alt="randomLedsBlink html" src="https://github.com/regina404/-remote-development-and-de/assets/63124387/bf9fa543-4583-4a58-84d1-52c5ce9f2d86">


Let's start the server:<br>
<img width="1000" alt="server" src="https://github.com/regina404/-remote-development-and-de/assets/63124387/2c5f627b-e5b3-40a7-98f8-7c24e375b17a">


Server response output:<br>
<img width="600" alt="output" src="https://github.com/regina404/-remote-development-and-de/assets/63124387/dd842946-7620-4a67-87ea-ea29275380fc">

<img width="600" alt="output" src="https://github.com/regina404/-remote-development-and-de/assets/63124387/a36d012b-b846-48b0-b0c6-8e88401c6560">


1) AWS
Сreate a virtual private cloud (VPC) for remote development and debugging. A VPC is an isolated network within AWS where network settings are controlled.
Сreate an EC2 instance (Elastic Compute Cloud) - this is a virtualization service that enables the creation of virtual machines in AWS clouds. 
Select AMI (Amazon Machine Image) for the EC2 instance.
Сreate a VPN environment for secure management of the embedded system. Using environment we change the IP for all clients (which will have access to connect via ssh using the IP within the VPN). The access is provided by the server. Then generate security keys and trensfer client configuration for the clients.
Let's watch a video:
[<img src="http://img.youtube.com/vi/WQIdi1BHIZw/0.jpg" width="1000">](https://youtu.be/WQIdi1BHIZw)

In this project (shown in the video), the EC2 instance will be our server from which two clients are generated. 
The first client is the BeagleBone Black. From the second client, we connect via ssh to the BeagleBone Black client using the internal VPN IP.
 Access to this IP is available only to clients connected to the VPN with generated security keys and transferred client configuration.
Configure OpenVPN, to create a secure channel between the local machine and the AWS virtual machine, we install OpenVPN on the client machine and on the EC2 instance. Configuring OpenVPN includes creating security certificates, server and client configurations.
Now let's create a client for the BeagleBone Black, and another client from which we will remotely connect to the board.
Let's start the OpenVPN server using the server configuration file.
Using the command “sudo openvpn --config /etc/openvpn/server.conf ”<br>
<img width="600" alt="client" src="https://github.com/regina404/-remote-development-and-de/assets/63124387/572d8603-3377-44c2-91a1-d16922346b30">

Let's start the OpenVPN client on the BeagleBone Black using the client configuration file. Using the command “sudo openvpn --config /home/debian/OpenVncClient/client.ovpn”<br>
<img width="600" alt="client" src="https://github.com/regina404/-remote-development-and-de/assets/63124387/c33e6271-93cb-46fd-bbde-74b243950908">

Let's run the OpenVPN client on another client using the client configuration file.
<img width="600" alt="vpn" src="https://github.com/regina404/-remote-development-and-de/assets/63124387/4612ac57-732e-4d61-a7f5-90b5e28a2550"><br>
When another client is connected to the VPN, we have access to the BeagleBone Black via the IP address it assigned inside the VPN. You can now SSH into the BeagleBone Black board inside the VPN.
We now have access from other clients created on the server to the BeagleBone Black in the configured OpenVPN system.
