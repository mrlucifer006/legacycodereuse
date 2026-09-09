#ifndef SUPPORT_H
#define SUPPORT_H

void admin_menu(void);
void agent_menu(void);
void customer_menu(void);
void show_flights(void);
void add_flight(const char *id, const char *destination, int price, int seats);
void update_flight(const char *id, int price, int seats);
void delete_flight(const char *id);
int authenticate(const char *file_name, const char *username, const char *password);

#endif
