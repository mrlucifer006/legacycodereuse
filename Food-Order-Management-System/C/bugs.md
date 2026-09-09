# C bug key

| # | File and line | Faulty code | Effect |
|---|---|---|---|
|1|`support.c:6`|`!strcmp(a,user)||!strcmp(b,pass)`|One matching credential grants access.| 
|2|`support.c:8`|append without a duplicate scan|Duplicate delivery staff accounts are allowed.| 
|3|`support.c:10`|`if(current!=id)`|Updating one price changes every other menu row.| 
|4|`support.c:10`|`currentPrice` in selected row|The chosen item cannot receive its new price.| 
|5|`support.c:11`|`if(current==id)`|Delete retains the target and erases all other rows.| 
|6|`support.c:12`|`price+qty`|The cart adds a price and quantity instead of multiplying.| 
|7|`support.c:12`|`found=0` outside order loop|After one successful lookup, an unknown later id can be accepted.| 
|8|`support.c:12`|`subtotal>1000?subtotal*.18f`|Discount rate is 18% instead of the required 10%.| 
|9|`support.c:12`|`tax=subtotal*.10f`|Tax is 10% instead of 18%.| 
|10|`support.c:12`|`if(strcmp(confirm,"yes"))`|A non-yes answer confirms the order.| 
