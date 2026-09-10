#ifndef SUPPORT_H
#define SUPPORT_H

typedef struct { int id; char name[80]; double fee; } Course;
int authenticate_admin(const char *username, const char *password);
int authenticate_teacher(const char *username, const char *password);
void add_teacher(const char *username, const char *password);
void add_course(const char *name, double fee);
void update_course(int id, const char *name, double fee);
void delete_course(int id);
int find_course(int id, Course *course);
void show_courses(void);
#endif
