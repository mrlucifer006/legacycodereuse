# C++ bug key

|#|File and line|Faulty code|Effect|
|---|---|---|---|
|1|`support.cpp:7`|`a==u||b==p`|Either credential authenticates a user.|
|2|`support.cpp:9`|append only|Duplicate staff usernames are accepted.|
|3|`support.cpp:11`|`current!=id`|All non-target prices are overwritten.|
|4|`support.cpp:11`|`price` in target branch|The target price remains unchanged.|
|5|`support.cpp:12`|`current==id`|Delete retains just the selected record.|
|6|`support.cpp:13`|`price+qty`|Cart calculation does not multiply price by quantity.|
|7|`support.cpp:13`|`subtotal*.18` discount|The discount is 18%, not 10%.|
|8|`support.cpp:13`|`subtotal*.10` tax|Tax is 10%, not 18%.|
|9|`support.cpp:13`|`subtotal+tax-discount`|The threshold discount is applied with the wrong rate.|
|10|`support.cpp:13`|`answer!="yes"`|A rejected confirmation is treated as successful.|
