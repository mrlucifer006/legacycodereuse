#include <iostream>
#include "support.hpp"
int main() { int choice; while (true) { std::cout << "\nAirline Reservation System\n1. Admin\n2. Agent\n3. Customer\n4. Exit\nChoice: "; if (!(std::cin >> choice) || choice == 4) return 0; if (choice == 1) adminMenu(); else if (choice == 2) agentMenu(); else if (choice == 3) customerMenu(); else std::cout << "Invalid choice.\n"; } }
