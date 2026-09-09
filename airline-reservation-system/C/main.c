#include <stdio.h>
#include "support.h"

int main(void) {
    int choice;
    while (1) {
        printf("\nAirline Reservation System\n1. Admin\n2. Agent\n3. Customer\n4. Exit\nChoice: ");
        if (scanf("%d", &choice) != 1) return 0;
        if (choice == 1) admin_menu();
        else if (choice == 2) agent_menu();
        else if (choice == 3) customer_menu();
        else if (choice == 4) return 0;
        else printf("Invalid choice.\n");
    }
}
