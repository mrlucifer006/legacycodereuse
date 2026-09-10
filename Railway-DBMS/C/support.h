#ifndef SUPPORT_H
#define SUPPORT_H
typedef struct { char id[20]; char name[60]; char route[80]; double fare; int seats; } Train;
int login(const char *file);
int read_trains(Train trains[], int max);
void add_train(Train train);
void update_train(const char *id, Train train);
void delete_train(const char *id);
void show_trains(void);
#endif
