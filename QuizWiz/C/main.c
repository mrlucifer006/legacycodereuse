#include <stdio.h>
#include "support.h"

int main(void) {
    int choice;
    while (1) {
        printf("\nQuizWiz\n1 Admin\n2 QuizMaster\n3 Player\n4 Exit\nChoose: ");
        if (scanf("%d", &choice) != 1) return 0;
        if (choice == 1) { if (login("admin.csv", 1)) admin_menu(); else puts("Invalid credentials."); }
        else if (choice == 2) { if (login("quizmaster.csv", 0)) staff_menu(); else puts("Invalid credentials."); }
        else if (choice == 3) player_menu();
        else if (choice == 4) return 0;
        else puts("Invalid option.");
    }
}
