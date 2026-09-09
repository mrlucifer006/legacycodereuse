#ifndef SUPPORT_HPP
#define SUPPORT_HPP

#include <string>

class Support {
public:
    void admin();
    void employee();
    void customer();
    void display_data();
    void add_data(const std::string& name, int amount);
    void update_data(const std::string& name, int amount);
    void del_data(const std::string& name);
    int check_admin(const std::string& uid, const std::string& pas);
    int check_employee(const std::string& uid, const std::string& pas);
    void add_employee(const std::string& new_id, const std::string& new_pas);
    void view_employee();
    void get_product_by_index(int num, std::string& out_name, int& out_price);
};

#endif
