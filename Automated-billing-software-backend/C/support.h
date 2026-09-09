#ifndef SUPPORT_H
#define SUPPORT_H

void admin();
void employee();
void customer();
void display_data();
void add_data(const char* name, int amount);
void update_data(const char* name, int amount);
void del_data(const char* name);
int check_admin(const char* uid, const char* pas);
int check_employee(const char* uid, const char* pas);

#endif
