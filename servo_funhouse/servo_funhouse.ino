#include <Servo.h>

Servo servo[5];

int pin_map[6] = {5, 8, 7, 3, 4, 1};

void setup() {
    pinMode(13, OUTPUT);
    Serial.begin(9600);

    servo[0].attach(20);
    servo[1].attach(21);
    servo[2].attach(22);
    servo[3].attach(23);
    servo[4].attach(6);

    for ( int i = 0; i < 5; i++ )
        servo[i].write(180);

    for ( int i = 0; i < 6; i++ )
        pinMode(i, OUTPUT);
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

            if ( target_servo >= 0 && target_servo < 5 ) {
                servo[target_servo].write(value);
            }
            else if ( target_servo == 5 ) {
                for ( int i = 0; i < 6; i++ )
                    digitalWrite(pin_map[i], value == 0 ? LOW : HIGH);
            }

            digitalWrite(13, HIGH);
            delay(10);
            digitalWrite(13, LOW);
        }
    }
}
