#include <stdio.h>
#include "support.h"

int main() {
    int choice;
    printf("Welcome to Bank Management System\n");
    printf("1. Admin\n2. Staff\n3. Customer\n4. Exit\nChoose role: ");
    if (scanf("%d", &choice) != 1) return 0;
    
    switch (choice) {
        case 1: admin_menu(); break;
        case 2: staff_menu(); break;
        case 3: customer_menu(); break;
        case 4: break;
        default: printf("Invalid choice.\n");
    }
    return 0;
}
