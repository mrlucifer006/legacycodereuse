#include <iostream>
#include "support.hpp"
int main() { int choice; do { std::cout << "\nBank Service Billing System\n1. Admin\n2. Teller\n3. Customer\n4. Exit\nChoose: "; if (!(std::cin >> choice)) return 0; if (choice == 1) adminMenu(); else if (choice == 2) tellerMenu(); else if (choice == 3) customerMenu(); } while (choice != 4); }
