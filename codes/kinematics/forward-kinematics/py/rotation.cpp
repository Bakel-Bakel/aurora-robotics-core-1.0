#include <cmath>
#include <array>
#include <iostream>
#include <iomanip>
#include <cctype>

using Mat3 = std::array<std::array<double,3>,3>;

Mat3 Rx(double t){
    double c = std::cos(t), s = std::sin(t);
    return {{{1, 0, 0},
             {0, c,-s},
             {0, s, c}}};
}
Mat3 Ry(double t){
    double c = std::cos(t), s = std::sin(t);
    return {{{ c, 0, s},
             { 0, 1, 0},
             {-s, 0, c}}};
}
Mat3 Rz(double t){
    double c = std::cos(t), s = std::sin(t);
    return {{{c,-s, 0},
             {s, c, 0},
             {0, 0, 1}}};
}

void pretty_print(const Mat3& R, const std::string& label, int width=10, int prec=4){
    std::cout << label << " =\n";
    std::cout << std::fixed << std::setprecision(prec);
    for(const auto& row : R){
        std::cout << "[ ";
        for(size_t j=0;j<3;++j){
            std::cout << std::setw(width) << row[j] << (j<2 ? "  " : "");
        }
        std::cout << " ]\n";
    }
}

int main(){
    char axis;
    std::cout << "Axis (x/y/z): ";
    if(!(std::cin >> axis)) return 1;
    axis = std::tolower(axis);

    double ang_deg;
    std::cout << "Angle (degrees): ";
    if(!(std::cin >> ang_deg)) return 1;

    double t = ang_deg * M_PI / 180.0;

    Mat3 R;
    std::string label;
    if(axis == 'x'){ R = Rx(t); label = "R_x(" + std::to_string(ang_deg) + "°)"; }
    else if(axis == 'y'){ R = Ry(t); label = "R_y(" + std::to_string(ang_deg) + "°)"; }
    else if(axis == 'z'){ R = Rz(t); label = "R_z(" + std::to_string(ang_deg) + "°)"; }
    else { std::cerr << "Axis must be x, y, or z.\n"; return 1; }

    pretty_print(R, label);
    return 0;
}
