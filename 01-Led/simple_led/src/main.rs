extern crate rust_gpiozero;
use rust_gpiozero::*;
use std::thread::sleep;
use std::time::Duration;


fn main() {
    let led = LED::new(17);

    loop {
        led.on();
        sleep(Duration::from_secs(1));
        led.off();
        sleep(Duration::from_secs(1));
    }
}
