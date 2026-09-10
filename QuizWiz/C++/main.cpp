#include <iostream>
#include "support.hpp"
int main() { int c; while (true) { std::cout << "\nQuizWiz\n1 Admin\n2 QuizMaster\n3 Player\n4 Exit\nChoose: "; if (!(std::cin >> c)) return 0; if (c == 1) { if (login("admin.csv", true)) adminMenu(); else std::cout << "Invalid credentials.\n"; } else if (c == 2) { if (login("quizmaster.csv", false)) staffMenu(); else std::cout << "Invalid credentials.\n"; } else if (c == 3) playerMenu(); else if (c == 4) return 0; else std::cout << "Invalid option.\n"; } }
