# Feature expansion: transaction timestamp

Add an `enrollments.csv` receipt file after a student confirms checkout. Prompt for `y` or `n`; only `y` should write a timestamp in `YYYY-MM-DD HH:MM:SS` format together with the selected course IDs and final amount. Put CSV-writing logic in `support.c`, declare it in `support.h`, and call it from `main.c`.

Test a confirmed checkout, a declined checkout, and a checkout with no selected courses.
