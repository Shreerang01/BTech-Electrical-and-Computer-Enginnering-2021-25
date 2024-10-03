/*
Shreerang Mhatre
Rollno - 52
Batch - A3
Exp - 8

Write a program in C++  to manage a shopping list. Each shopping list item is
represented by a string stored in a container. Your design requires
a print function that prints out the contents of the shopping list.

Create an empty list.
Append the items, "eggs," "milk," "sugar","chocolate," and
"flour" to the list. Print the list.
Remove the first element from the list. Print the list.
Insert the item, "coffee" at the beginning of the list. Print the list.
Find the item, "sugar" and replace it with "honey." Print the list.
Insert the item, "baking powder" before "milk" in the list. Print the
list.
Sort and Search the item in the list.
*/

#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<std::string> shoppingList;

    // Append items to the list
    shoppingList.push_back("eggs");
    shoppingList.push_back("milk");
    shoppingList.push_back("sugar");
    shoppingList.push_back("chocolate");
    shoppingList.push_back("flour");

    // Print the list
    std::cout << "Shopping List:" << std::endl;
    for (const std::string& item : shoppingList) {
        std::cout << item << std::endl;
    }

    // Remove the first element
    shoppingList.erase(shoppingList.begin());

    // Print the modified list
    std::cout << "\nAfter removing the first item:" << std::endl;
    for (const std::string& item : shoppingList) {
        std::cout << item << std::endl;
    }

    // Insert "coffee" at the beginning
    shoppingList.insert(shoppingList.begin(), "coffee");

    // Print the modified list
    std::cout << "\nAfter inserting 'coffee' at the beginning:" << std::endl;
    for (const std::string& item : shoppingList) {
        std::cout << item << std::endl;
    }

    // Find and replace "sugar" with "honey"
    for (std::string& item : shoppingList) {
        if (item == "sugar") {
            item = "honey";
        }
    }

    // Print the modified list
    std::cout << "\nAfter replacing 'sugar' with 'honey':" << std::endl;
    for (const std::string& item : shoppingList) {
        std::cout << item << std::endl;
    }

    // Insert "baking powder" before "milk"
    auto it = std::find(shoppingList.begin(), shoppingList.end(), "milk");
    if (it != shoppingList.end()) {
        shoppingList.insert(it, "baking powder");
    }

    // Print the modified list
    std::cout << "\nAfter inserting 'baking powder' before 'milk':" << std::endl;
    for (const std::string& item : shoppingList) {
        std::cout << item << std::endl;
    }

    // Sort the list
    std::sort(shoppingList.begin(), shoppingList.end());

    // Print the sorted list
    std::cout << "\nSorted Shopping List:" << std::endl;
    for (const std::string& item : shoppingList) {
        std::cout << item << std::endl;
    }

    // Search for an item in the list
    std::string searchItem = "chocolate";
    auto searchResult = std::find(shoppingList.begin(), shoppingList.end(), searchItem);
    if (searchResult != shoppingList.end()) {
        std::cout << "\n'" << searchItem << "' found in the list." << std::endl;
    } else {
        std::cout << "\n'" << searchItem << "' not found in the list." << std::endl;
    }

    return 0;
}
