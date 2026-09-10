#include <stdio.h>
#include <string.h>
#include "support.h"

Train ask_train(void) { Train t; printf("ID Name Route Fare Seats: "); scanf("%19s %59s %79s %lf %d",t.id,t.name,t.route,&t.fare,&t.seats); return t; }
void admin(void) { int c; if(!login("admin.csv")){puts("Invalid credentials");return;} do { printf("1 Staff 2 Add 3 Update 4 Delete 5 View 0 Exit: ");scanf("%d",&c); if(c==1){FILE *f=fopen("employee.csv","a");char u[40],p[40];scanf("%39s %39s",u,p);fprintf(f,"%s,%s\n",u,p);fclose(f);} if(c==2)add_train(ask_train()); if(c==3){char id[20];scanf("%19s",id);update_train(id,ask_train());} if(c==4){char id[20];scanf("%19s",id);delete_train(id);} if(c==5)show_trains(); } while(c!=0); }
void staff(void) { int c; if(!login("employee.csv")){puts("Invalid credentials");return;} do { printf("1 Add 2 Update 3 View 0 Exit: ");scanf("%d",&c);if(c==1)add_train(ask_train());if(c==2){char id[20];scanf("%19s",id);update_train(id,ask_train());}if(c==3)show_trains();}while(c!=0); }
void passenger(void) { Train list[100]; int n=read_trains(list,100), c,qty; double subtotal=0; char id[20]; while(1){show_trains();printf("Train ID, C checkout, X exit: ");scanf("%19s",id);if(!strcmp(id,"X"))return;if(!strcmp(id,"C")){double tax=subtotal*.18,discount=subtotal<1000?subtotal*.1:0;printf("Subtotal %.2f Tax %.2f Discount %.2f Total %.2f\n",subtotal,tax,discount,subtotal+tax-discount);printf("Confirm 1/0: ");scanf("%d",&c);if(!c)puts("Booking confirmed");return;}for(c=0;c<n;c++)if(!strcmp(list[c].id,id)){printf("Tickets: ");scanf("%d",&qty);subtotal+=list[c].fare*qty;break;}if(c<n)break;} }
int main(void) { int role; do { printf("1 Admin 2 Employee 3 Passenger 0 Exit: ");scanf("%d",&role);if(role==1)admin();if(role==2)staff();if(role==3)passenger(); }while(role!=0);return 0; }
