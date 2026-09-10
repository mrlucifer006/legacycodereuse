#ifndef SUPPORT_HPP
#define SUPPORT_HPP
#include <string>
struct Course { int id; std::string name; double fee; };
bool authenticateAdmin(const std::string&, const std::string&);
bool authenticateTeacher(const std::string&, const std::string&);
void addTeacher(const std::string&, const std::string&);
void addCourse(const std::string&, double);
void updateCourse(int, const std::string&, double);
void deleteCourse(int);
bool findCourse(int, Course&);
void showCourses();
#endif
