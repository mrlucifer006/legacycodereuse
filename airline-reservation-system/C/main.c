#include <stdio.h>
#include "support.h"

int main() {
    int choice;
    printf("Welcome to Airline Reservation System\n");
    printf("1. Admin\n2. Agent\n3. Customer\n4. Exit\nChoose role: ");
    if (scanf("%d", &choice) != 1) return 0;
    
    switch (choice) {
        case 1: admin_menu(); break;
        case 2: agent_menu(); break;
        case 3: customer_menu(); break;
        case 4: break;
        default: printf("Invalid choice.\n");
    }
    return 0;
}
