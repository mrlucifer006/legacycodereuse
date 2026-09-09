#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "support.h"

void admin_menu() {
    printf("Admin Menu:\n1. View Agents\n2. View Flights\n");
}

void agent_menu() {
    printf("Agent Menu:\n1. View Flights\n2. Book Flight\n");
}

void customer_menu() {
    printf("Customer Menu:\n1. View Available Flights\n");
}
