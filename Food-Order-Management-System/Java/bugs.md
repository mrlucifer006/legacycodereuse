# Java bug key

|#|File and line|Faulty code|Effect|
|---|---|---|---|
|1|`Support.java:4`|`x[0].equals(u)||x[1].equals(p)`|One matching credential grants access.|
|2|`Support.java:6`|append only|Duplicate staff usernames are accepted.|
|3|`Support.java:8`|`!=id`|The price update changes every non-target item.|
|4|`Support.java:8`|`x[2]` target branch|The selected item keeps its old price.|
|5|`Support.java:9`|`==id`|Delete saves only the item that should be removed.|
|6|`Support.java:10`|`price+qty`|Cart totals do not multiply unit price and quantity.|
|7|`Support.java:10`|`subtotal*.18` discount|Discount percentage is 18 instead of 10.|
|8|`Support.java:10`|`subtotal*.10` tax|Tax percentage is 10 instead of 18.|
|9|`Support.java:10`|empty-cart checkout|A customer can confirm a zero-value order.|
|10|`Support.java:10`|`!sc.next().equals("yes")`|A rejected confirmation is marked confirmed.|
