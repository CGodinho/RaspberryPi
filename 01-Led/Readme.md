# LED

## Introduction

This project blinks a led.
The led is lighted for 10 seconds and blank for 5, continouslly.
A second version of the code uses 3 leds to create a semaphore.

## Material

* LED
* Resistor 220 &Omega;

## Circuit

![model](circuit_start.png)

![mount](circuit_final.png)

## Code

Code is available in Python.

* ``led_acende_apaga.py``
* ``led_semaforo.py``

It uses library ``RPi.GPIO``.

GPIO board is used in OUTPUT mode, connected to a port.
Method ``output`` allows to change signal from port.

An example (simple case) is Rust is also available in a project:

* ``simple_led``