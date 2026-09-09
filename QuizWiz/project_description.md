# QuizWiz

QuizWiz is a command-line quiz-pack catalog and purchase system. It stores accounts and quiz-pack information in CSV files so the application can be run without a database server.

Administrators sign in to create QuizMaster accounts and manage every quiz pack. QuizMasters sign in to add, revise, and view the catalog. Players do not need an account: they can browse available quiz packs, add packs to a cart, and check out. Checkout shows the subtotal, tax, any qualifying discount, and a final confirmation.

Every implementation provides the same workflow and data model: `admin.csv` holds administrator credentials, `quizmaster.csv` holds staff credentials, and `quiz_packs.csv` holds pack id, title, category, price, and available slots.
