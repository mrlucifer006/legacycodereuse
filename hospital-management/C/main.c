#include <stdio.h>
#include "support.h"
int main(void) {
    int choice;
    do {
        printf("Patient orders: 1 admin 2 doctor 3 customer 0 exit: ");
        if (scanf("%d", &choice) != 1) return 0;
        if (choice == 1) { if (!login("admin.csv")) { puts("Access denied"); continue; } do { printf("Admin: 1 staff 2 add 3 update 4 delete 5 view 0 exit: "); scanf("%d", &choice); if(choice==1)add_staff(); if(choice==2)add_patient(); if(choice==3)update_patient(); if(choice==4)delete_patient(); if(choice==5)view_patient(); } while(choice); }
        if (choice == 2) { if (!login("doctor.csv")) { puts("Access denied"); continue; } do { printf("Staff: 1 add 2 update 3 view 0 exit: "); scanf("%d", &choice); if(choice==1)add_patient(); if(choice==2)update_patient(); if(choice==3)view_patient(); } while(choice); }
        if (choice == 3) customer_order();
    } while (choice);
    return 0;
}
