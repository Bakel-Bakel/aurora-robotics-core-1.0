// two_link_sliders.cpp
#include <opencv2/opencv.hpp>
#include <cmath>
#include <string>

static const double L1 = 150.0; // pixels
static const double L2 = 100.0; // pixels

int main() {
    const int W = 600, H = 600;
    const cv::Point center(W/2, H/2);  // base at window center

    int theta1_deg = 30;  // initial angles (degrees)
    int theta2_deg = 30;

    cv::namedWindow("2R Planar Arm", cv::WINDOW_AUTOSIZE);
    cv::createTrackbar("theta1 (deg)", "2R Planar Arm", &theta1_deg, 360);
    cv::createTrackbar("theta2 (deg)", "2R Planar Arm", &theta2_deg, 360);

    while (true) {
        // background
        cv::Mat img(H, W, CV_8UC3, cv::Scalar(245, 245, 245));

        // convert to radians
        double th1 = theta1_deg * CV_PI / 180.0;
        double th2 = theta2_deg * CV_PI / 180.0;

        // forward kinematics (pixel coordinates, y down)
        cv::Point joint(
            static_cast<int>(center.x + L1 * std::cos(th1)),
            static_cast<int>(center.y - L1 * std::sin(th1))  // minus because screen y goes down
        );
        cv::Point ee(
            static_cast<int>(joint.x + L2 * std::cos(th1 + th2)),
            static_cast<int>(joint.y - L2 * std::sin(th1 + th2))
        );

        // draw grid (optional)
        for (int x = 0; x < W; x += 50) cv::line(img, {x,0}, {x,H}, cv::Scalar(230,230,230));
        for (int y = 0; y < H; y += 50) cv::line(img, {0,y}, {W,y}, cv::Scalar(230,230,230));

        // draw links
        cv::line(img, center, joint, cv::Scalar(60, 90, 200), 4);
        cv::line(img, joint, ee,    cv::Scalar(60, 200, 120), 4);

        // draw joints
        cv::circle(img, center, 6, cv::Scalar(0,0,0), -1);
        cv::circle(img, joint,  6, cv::Scalar(0,0,0), -1);
        cv::circle(img, ee,     6, cv::Scalar(0,0,0), -1);

        // info text
        char buf[256];
        double xee = (ee.x - center.x);
        double yee = -(ee.y - center.y); // back to math y-up
        std::snprintf(buf, sizeof(buf),
                      "EE: x=%.1f, y=%.1f | theta1=%d deg, theta2=%d deg",
                      xee, yee, theta1_deg, theta2_deg);
        cv::putText(img, buf, {10, 25}, cv::FONT_HERSHEY_SIMPLEX, 0.7, cv::Scalar(20,20,20), 2);

        cv::imshow("2R Planar Arm", img);
        int key = cv::waitKey(15);
        if (key == 27 || key == 'q') break; // ESC or q to quit
    }
    return 0;
}
