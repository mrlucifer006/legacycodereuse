#ifndef SUPPORT_HPP
#define SUPPORT_HPP
#include <string>
void adminMenu(); void agentMenu(); void customerMenu(); void showFlights();
void addFlight(const std::string&, const std::string&, int, int);
void updateFlight(const std::string&, int, int); void deleteFlight(const std::string&);
bool authenticate(const std::string&, const std::string&, const std::string&);
#endif
