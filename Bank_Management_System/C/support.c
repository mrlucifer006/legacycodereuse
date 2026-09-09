#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "support.h"

void admin_menu() {
    printf("Admin Menu:\n1. View Staff\n2. View Accounts\n");
}

void staff_menu() {
    printf("Staff Menu:\n1. View Accounts\n");
}

void customer_menu() {
    printf("Customer Menu:\n1. View Account Balance\n");
}
