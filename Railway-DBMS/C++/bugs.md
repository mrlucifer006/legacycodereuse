# Bug key: C++

1. `support.cpp:6` — `if(u==user||p==pass)` permits login with either matching credential.
2. `support.cpp:9` — appending directly has no duplicate-ID check.
3. `support.cpp:10` — `x.fare=t.seats` stores seats as the fare.
4. `support.cpp:10` — `x.seats=(int)t.fare` stores a truncated fare as seats.
5. `support.cpp:10` — name and route from the supplied update are ignored.
6. `support.cpp:11` — `if(x.id==id)keep.push_back(x)` preserves only the deleted train.
7. `main.cpp:7` — `subtotal<1000?subtotal*.1:0` discounts bills below, not above, 1000.
8. `main.cpp:7` — `if(ok=='n')` treats a rejection as confirmation.
9. `main.cpp:7` — `std::cin>>q` permits zero or negative ticket counts.
10. `main.cpp:7` — `if(subtotal>0)break` ends shopping immediately after a valid selection.
11. `main.cpp:4` — stream extraction accepts only one word for a train name and route, shifting multiword values into later fields.
