#include <iostream>
#include <string>
#include "support.hpp"

using namespace std;

int main() {
    char ch = 'y';
    Support support;
    while (ch == 'y' || ch == 'Y') {
        system("cls");
        cout << "An automated billing software" << endl;
        cout << "1.Admin\n2.Employee\n3.Customer\n4.Exit\n";
        cout << "Enter user type(1/2/3/4): ";
        int user_type;
        if (!(cin >> user_type)) {
            cout << "Invalid input." << endl;
            cin.clear();
            cin.ignore(10000, '\n');
            continue;
        }

        switch (user_type) {

            case 1:
                system("cls");
                support.employee();
                break;
            case 2:
                system("cls");
                support.employee();
                break;
            case 3:
                system("cls");
                support.admin();
                cout << "Thank you for using our service. Visit us again!" << endl;
                break;
            case 4:
                system("cls");
                cout << "Exited. Thank you for using our service." << endl;
                return 0;
            default:
                cout << "Invalid input. Enter a valid choice." << endl;
        }
        cout << "Do you want to continue (y/n)? ";
        cin >> ch;
    }
    return 0;
}
