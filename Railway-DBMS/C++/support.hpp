#ifndef SUPPORT_HPP
#define SUPPORT_HPP
#include <string>
#include <vector>
struct Train { std::string id,name,route; double fare; int seats; };
bool login(const std::string& file);
std::vector<Train> readTrains();
void addTrain(const Train& train);
void updateTrain(const std::string& id,const Train& train);
void deleteTrain(const std::string& id);
void showTrains();
#endif
