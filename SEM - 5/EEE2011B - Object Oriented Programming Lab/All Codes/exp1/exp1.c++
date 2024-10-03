/*
Problem statement:
    Airline details format and its attributes
    1)Name of the pasenger
    2) Age
    3)Flight no
    4)Departure time
    5)location		
    write a c++ code to accept and display the values of the passenger for the airline

Author: Shreerang P Mhatre
Date: 23/08/2023

Input:  Enter the name of the Passenger: Shree
        Enter the age of the Passenger: 20
        Enter the Flight Number: 5674
        Enter the Departure Time: 5
        Enter the current source: pune

Output: Airline Details: 
        Name: Shree
        Age: 20
        Flight No: 5674
        Departure Time: 5
        Source: pune
*/

#include<iostream>
using namespace std;

// Airline class to accept and display data
class airline{
private:
    string name;
    int age;
    int flight;
    int time;
    string source;

public:
    void readDeatails(); //Function to read data
    void displayDetails(); //Function to display data
};

// Accept the input values from the passenger
void airline::readDeatails() {
    cout<<"Enter the name of the Passenger: ";
    cin >> name;

    cout<<"Enter the age of the Passenger: ";
    cin >> age;

    cout<<"Enter the Flight Number: ";
    cin >> flight;

    cout<<"Enter the Departure Time: ";
    cin >> time;

    cout<<"Enter the current source: ";
    cin >> source;
}

//Display the accepted values in organized format
void airline::displayDetails() {
    cout << "Name: " << name << endl;
    cout << "Age: " << age << endl;
    cout << "Flight No: " << flight << endl;
    cout << "Departure Time: " << time << endl;
    cout << "Source: " << source << endl;
}

// Main function
int main() {
    airline air;

    air.readDeatails();

    cout << "Airline Details: "<< endl;
    air.displayDetails();

    return 0;
}