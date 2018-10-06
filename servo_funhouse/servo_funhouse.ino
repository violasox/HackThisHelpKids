#include <Servo.h>

Servo servo[6];

void setup() {
    pinMode(13, OUTPUT);
    Serial.begin(9600);

    servo[0].attach(20);
    servo[1].attach(21);
    servo[2].attach(22);
    servo[3].attach(23);
    servo[4].attach(5);
    servo[5].attach(6);

    for ( int i = 0; i < 6; i++ )
        servo[i].write(90);
}

#define PACKET_START 1337
uint16_t start_pkt_buffer = 0;

void loop() {
    if ( Serial.available() ) {
        uint8_t buf = Serial.read();
        start_pkt_buffer = (uint16_t)start_pkt_buffer >> 8;
        uint16_t temp = (uint16_t)buf << 8;
        start_pkt_buffer = start_pkt_buffer | temp;
        if ( start_pkt_buffer == PACKET_START ) {
            while ( !Serial.available() );
            uint8_t target_servo = Serial.read();
            while ( !Serial.available() );
            uint8_t value = Serial.read();

            if ( target_servo >= 0 && target_servo < 6 ) {
                digitalWrite(13, HIGH);
                servo[target_servo].write(value);
                delay(10);
                digitalWrite(13, LOW);

            }
        }
    }
}
