#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "support.h"

int main() {
    char ch = 'y';
    while (ch == 'y' || ch == 'Y') {
        system("cls");
        printf("An automated airline reservation software\n");
        printf("1.Admin\n2.Agent\n3.Customer\n4.Exit\n");
        printf("Enter user type(1/2/3/4): ");
        int user_type;
        if (scanf("%d", &user_type) != 1) {
            printf("Invalid input.\n");
            while (getchar() != '\n');
            continue;
        }

        switch (user_type) {
            case 1:
                system("cls");
                admin();
                break;
            case 2:
                system("cls");
                agent();
                break;
            case 3:
                system("cls");
                customer();
                printf("Thank you for using our service.\n");
                break;
            case 4:
                system("cls");
                printf("Exited. Thank you for using our service.\n");
                return 0;
            default:
                printf("Invalid input. Enter a valid choice.\n");
        }
        printf("Do you want to continue (y/n)? ");
        scanf(" %c", &ch);
    }
    return 0;
}
