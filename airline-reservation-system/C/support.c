#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void display_data() {
    FILE *file = fopen("flights.csv", "r");
    if (!file) {
        printf("No flights available.\n");
        return;
    }
    char line[256];
    int idx = 0;
    while (fgets(line, sizeof(line), file)) {
        line[strcspn(line, "\n")] = 0;
        char *name = strtok(line, ",");
        char *amount_str = strtok(NULL, ",");
        if (name && amount_str) {
            printf("%d : %s - $%s\n", idx++, name, amount_str);
        }
    }
    fclose(file);
}

void add_data(const char* name, int amount) {
    FILE *file = fopen("flights.csv", "a");
    if (file) {
        fprintf(file, "%s,%d\n", name, amount);
        fclose(file);
    }
}

void update_data(const char* name, int amount) {
    FILE *file = fopen("flights.csv", "r");
    FILE *temp = fopen("temp.csv", "w");
    if (!file || !temp) {
        if (file) fclose(file);
        if (temp) fclose(temp);
        return;
    }
    char line[256];
    while (fgets(line, sizeof(line), file)) {
        char line_copy[256];
        strcpy(line_copy, line);
        line_copy[strcspn(line_copy, "\n")] = 0;
        char *current_name = strtok(line_copy, ",");
        if (current_name && strcmp(current_name, name) == 0) {
            fprintf(temp, "%s,%d\n", name, amount);
        } else {
            fprintf(temp, "%s", line);
        }
    }
    fclose(file);
    fclose(temp);
    remove("flights.csv");
    rename("temp.csv", "flights.csv");
}

void del_data(const char* name) {
    FILE *file = fopen("flights.csv", "r");
    FILE *temp = fopen("temp.csv", "w");
    if (!file || !temp) {
        if (file) fclose(file);
        if (temp) fclose(temp);
        return;
    }
    char line[256];
    while (fgets(line, sizeof(line), file)) {
        char line_copy[256];
        strcpy(line_copy, line);
        line_copy[strcspn(line_copy, "\n")] = 0;
        char *current_name = strtok(line_copy, ",");
        if (current_name && strcmp(current_name, name) != 0) {
            fprintf(temp, "%s", line);
        }
    }
    fclose(file);
    fclose(temp);
    remove("flights.csv");
    rename("temp.csv", "flights.csv");
}

int check_admin(const char* uid, const char* pas) {
    FILE *file = fopen("admin.csv", "r");
    if (!file) return 0;
    char line[256];
    while (fgets(line, sizeof(line), file)) {
        line[strcspn(line, "\n")] = 0;
        char *id = strtok(line, ",");
        char *pw = strtok(NULL, ",");
        if (id && pw && strcmp(id, uid) == 0 && strcmp(pw, pas) == 0) {
            fclose(file);
            return 1;
        }
    }
    fclose(file);
    return 0;
}

void admin() {
    char uid[50], pas[50];
    printf("Enter your user id : ");
    scanf("%s", uid);
    printf("Enter your password : ");
    scanf("%s", pas);
    if (check_admin(uid, pas)) {
        char ch = 'y';
        while (ch == 'y' || ch == 'Y') {
            system("cls");
            printf("1.Add Flight Data\n2.Update Flight Data\n3.Delete Flight Data\n4.View Flight Data\n5.Exit\n");
            int choice;
            printf("Enter your choice: ");
            scanf("%d", &choice);
            char name[50];
            int amount;
            switch(choice) {
                case 1:
                    printf("Flight Name/Route: ");
                    scanf("%s", name);
                    printf("Price: ");
                    scanf("%d", &amount);
                    add_data(name, amount);
                    printf("Added successfully!\n");
                    break;
                case 2:
                    printf("Flight Name/Route: ");
                    scanf("%s", name);
                    printf("New Price: ");
                    scanf("%d", &amount);
                    update_data(name, amount);
                    printf("Updated successfully!\n");
                    break;
                case 3:
                    printf("Flight Name/Route: ");
                    scanf("%s", name);
                    del_data(name);
                    printf("Deleted successfully!\n");
                    break;
                case 4:
                    display_data();
                    break;
                case 5:
                    return;
                default:
                    printf("Invalid input.\n");
            }
            printf("Do you want to continue (y/n)? ");
            scanf(" %c", &ch);
        }
    } else {
        printf("Invalid username or password\n");
    }
}

int check_agent(const char* uid, const char* pas) {
    FILE *file = fopen("agent.csv", "r");
    if (!file) return 0;
    char line[256];
    while (fgets(line, sizeof(line), file)) {
        line[strcspn(line, "\n")] = 0;
        char *id = strtok(line, ",");
        char *pw = strtok(NULL, ",");
        if (id && pw && strcmp(id, uid) == 0 && strcmp(pw, pas) == 0) {
            fclose(file);
            return 1;
        }
    }
    fclose(file);
    return 0;
}

void agent() {
    char uid[50], pas[50];
    printf("Enter your user id : ");
    scanf("%s", uid);
    printf("Enter your password : ");
    scanf("%s", pas);
    if (check_agent(uid, pas)) {
        char ch = 'y';
        while (ch == 'y' || ch == 'Y') {
            system("cls");
            printf("1.Add Flight Data\n2.Update Flight Data\n3.View Flight Data\n4.Exit\n");
            int choice;
            printf("Enter your choice: ");
            scanf("%d", &choice);
            char name[50];
            int amount;
            switch(choice) {
                case 1:
                    printf("Flight Name/Route: ");
                    scanf("%s", name);
                    printf("Price: ");
                    scanf("%d", &amount);
                    add_data(name, amount);
                    printf("Added successfully!\n");
                    break;
                case 2:
                    printf("Flight Name/Route: ");
                    scanf("%s", name);
                    printf("New Price: ");
                    scanf("%d", &amount);
                    update_data(name, amount);
                    printf("Updated successfully!\n");
                    break;
                case 3:
                    display_data();
                    break;
                case 4:
                    return;
                default:
                    printf("Invalid input.\n");
            }
            printf("Do you want to continue (y/n)? ");
            scanf(" %c", &ch);
        }
    } else {
        printf("Invalid username or password\n");
    }
}

void customer() {
    char ch = 'y';
    int total_price = 0;
    while (ch == 'y' || ch == 'Y') {
        system("cls");
        printf("1.View Flights\n2.Book Flight\n3.Checkout\n4.Exit\n");
        int choice;
        printf("Enter your choice: ");
        scanf("%d", &choice);
        switch(choice) {
            case 1:
                display_data();
                break;
            case 2:
                display_data();
                printf("Enter flight number to book (enter index from list): ");
                int num;
                scanf("%d", &num);

                printf("Flight booked tentatively!\n");
                total_price += 100;
                break;
            case 3:
                printf("Total Price: $%d\n", total_price);
                printf("Confirm booking (y/n)? ");
                char confirm;
                scanf(" %c", &confirm);
                if (confirm == 'y' || confirm == 'Y') {
                    printf("Booking confirmed! Thank you.\n");
                    total_price = 0;
                }
                break;
            case 4:
                return;
            default:
                printf("Invalid input.\n");
        }
        printf("Do you want to continue (y/n)? ");
        scanf(" %c", &ch);
    }
}
