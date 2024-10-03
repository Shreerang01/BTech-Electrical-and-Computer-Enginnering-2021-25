/*

Shreerang Mhatre
Rollno -52
Batch - A3
Exp -4

Friend Function in C++

In C++ define a class Box consisting of the following
data members length, breadth and height member functions

1 one default constructor
2 Two overloaded operator member function '<<' and '>>'
to display and read box dimensions
3 One member function '+' to add two box objects and one friend function to compute the volume
and the box using operator overloading

*/

#include <iostream>

class Box {
private:
    double length;
    double breadth;
    double height;

public:
    // Default constructor
    Box() : length(0.0), breadth(0.0), height(0.0) {}

    // Overloaded '<<' operator to display box dimensions
    friend std::ostream& operator<<(std::ostream& os, const Box& box) {
        os << "Length: " << box.length << " Breadth: " << box.breadth << " Height: " << box.height;
        return os;
    }

    // Overloaded '>>' operator to read box dimensions
    friend std::istream& operator>>(std::istream& is, Box& box) {
        std::cout << "Enter length: ";
        is >> box.length;
        std::cout << "Enter breadth: ";
        is >> box.breadth;
        std::cout << "Enter height: ";
        is >> box.height;
        return is;
    }

    // Member function to add two Box objects
    Box operator+(const Box& other) {
        Box result;
        result.length = this->length + other.length;
        result.breadth = this->breadth + other.breadth;
        result.height = this->height + other.height;
        return result;
    }

    // Friend function to compute the volume of the Box
    friend double computeVolume(const Box& box) {
        return box.length * box.breadth * box.height;
    }
};

int main() {
    Box box1, box2, result;

    std::cout << "Enter dimensions for Box 1:" << std::endl;
    std::cin >> box1;
    std::cout << "Enter dimensions for Box 2:" << std::endl;
    std::cin >> box2;

    std::cout << "Box 1: " << box1 << std::endl;
    std::cout << "Box 2: " << box2 << std::endl;

    result = box1 + box2;
    std::cout << "Sum of Box 1 and Box 2: " << result << std::endl;

    double volume = computeVolume(result);
    std::cout << "Volume of the sum of Box 1 and Box 2: " << volume << std::endl;

    return 0;
}