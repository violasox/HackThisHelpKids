#include <ros.h>
#include <geometry_msgs/Point.h>
#include <Servo.h>

Servo servo[6];

void handle_servo(const geometry_msgs::Point& value) {
    double command = value.y / 127.0;
    command *= 90;
    command += 90;
    servo[(int)value.x].write((int)command);
}

void setup() {
    servo[0].attach(20);
    servo[1].attach(21);
    servo[2].attach(22);
    servo[3].attach(23);
    servo[4].attach(5);
    servo[5].attach(6);

    for ( int i = 0; i < 6; i++ )
        servo[i].write(90);
}

void loop() {
    ros::NodeHandle nh;
    nh.initNode();
    ros::Subscriber<geometry_msgs::Point> servosub("/servo", &handle_servo);

    nh.subscribe(servosub);

    while (1) {
        nh.spinOnce();
        delay(100);
    }
}
