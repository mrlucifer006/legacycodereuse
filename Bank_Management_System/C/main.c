#include <stdio.h>
#include "support.h"
int main(void) { int choice; do { printf("\nBank Service Billing System\n1. Admin\n2. Teller\n3. Customer\n4. Exit\nChoose: "); if (scanf("%d", &choice) != 1) return 0; if (choice == 1) admin_menu(); else if (choice == 2) teller_menu(); else if (choice == 3) customer_menu(); } while (choice != 4); return 0; }
