
#include <opencv4/opencv2/opencv.hpp>
#include <iostream>
#include <cmath>

struct ReferencePos {
    int x = 0;
    int y = 0;
};

struct FK {
    static const int L1 = 150.0; // everyone that uses FK.L1 access the same memory address
    static const int L2 = 100.0; // everyone that uses FK.L2 access the same memory address
    int theta1 = 30; //initial angles (deg)
    int theta2 = 30; //initial angles (deg)
};

struct EEPosition {
    double x1;
    double y1;
    double x2;
    double y2;
};


EEPosition calculateEE(const FK &values, const ReferencePos &base) {
    
    EEPosition position;

    //convert FK theta to radians as std::cos&sin takes radian
    double theta1_rad = values.theta1 * M_PI / 180.0;
    double theta2_rad = values.theta2 * M_PI / 180.0;

    double x1 = base.x + values.L1 * std::cos(theta1_rad); // l1 position wrt reference (assuming reference has been included in l1)
    double y1 = base.y - values.L1 * std::sin(theta1_rad); // l1 position wrt reference (assuming reference has been included in l1)

    double x2 = x1 + values.L2 * std::cos(theta1_rad + theta2_rad); // l2 position wrt l1
    double y2 = y1 - values.L2 * std::sin(theta1_rad + theta2_rad); // l2 position wrt l1

    // double X = values.L1 * std::cos(theta1_rad) + values.L2 * std::cos(theta1_rad + theta2_rad);
    // double Y = values.L1 * std::sin(theta1_rad) + values.L2 * std::sin(theta1_rad + theta2_rad);

    position = {x1, y1, x2, y2};
    return position;
};


int main() {

    // static const double L1 = 150.0; // pixels
    // static const double L2 = 100.0; // pixels
    const int W = 600, H = 600; // window position

    FK fp;
    ReferencePos pos = {W/2, H/2}; //set baseline at centre of the window
    const cv::Point centre(pos.x, pos.y);

    cv::namedWindow("2D Planar Arm", cv::WINDOW_AUTOSIZE); // same name as that of the trackbar; else diff windows

    // an improvment here would be passing a callback function rahter than a pointer of the value (fp.theta)
    cv::createTrackbar("Theta1 (deg)", "2D Planar Arm", &fp.theta1, 360); //make sure fp.theta1 is an int and a pointer is passed in
    cv::createTrackbar("Theta2 (deg)", "2D Planar Arm", &fp.theta2, 360); 

    
    while (true) {
        // grey background
        cv::Mat img(H, W, CV_8UC3, cv::Scalar(128, 128, 128));

        EEPosition position = calculateEE(fp, pos);
        cv::Point joint(static_cast<int>(position.x1), static_cast<int>(position.y1));
        cv::Point ee(static_cast<int>(position.x2), static_cast<int>(position.y2));

        //draw links
        cv::line(img, centre, joint, cv::Scalar(60, 90, 200), 5);
        cv::line(img, joint, ee, cv::Scalar(60, 200, 120), 5); // link2 ref. link1

        //draw joints
        cv::circle(img, centre, 6, cv::Scalar(0,0,0), -1);
        cv::circle(img, joint,  6, cv::Scalar(0,0,0), -1);
        cv::circle(img, ee,     6, cv::Scalar(0,0,0), -1);

        // info text
        char buf[256];
        double xee = (ee.x - pos.x);
        double yee = -(ee.y - pos.y); 
        std::snprintf(buf, sizeof(buf),
                      "EE: x=%.1f, y=%.1f | theta1=%d deg, theta2=%d deg",
                      xee, yee, fp.theta1, fp.theta2);
        cv::putText(img, buf, {10, 25}, cv::FONT_HERSHEY_SIMPLEX, 0.7, cv::Scalar(20,20,20), 2);

        cv::imshow("2D Planar Arm", img);
        int key = cv::waitKey(15); //15ms to redraw arm and joint
        if (key == 27 || key == 'q') break;
    }
    
    cv::destroyAllWindows(); //free resources and deletes window
    return 0;
}