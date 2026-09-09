import pandas as pd

def add_data(name, price):

    try:
        df = pd.read_csv("database.csv", index_col=0)

    except FileNotFoundError:
        df = pd.DataFrame(columns=["item_name", "price"])

    new_index = len(df)
    df.loc[new_index] = [name, price]

    df.to_csv("database.csv", index=True)

def del_data(name):

    try:
        df = pd.read_csv("database.csv", index_col=0)

    except FileNotFoundError:
        df = pd.DataFrame(columns=["item_name", "price"])

    df = df[df["item_name"] != name]

    df.to_csv("database.csv", index=True)

def update_data(upd_name, upd_prc):

    try:
        df = pd.read_csv("database.csv", index_col=0)

    except FileNotFoundError:
        df = pd.DataFrame(columns=["item_name", "price"])

    df.loc[df["item_name"] == upd_name, "price"] = upd_prc

    df.to_csv("database.csv", index=True)

def display_data():

    try:
        df = pd.read_csv("database.csv", index_col=0)

    except FileNotFoundError:
        df = pd.DataFrame(columns=["item_name", "price"])

    for idx in df.index:

        print(f"{idx}  : {df.loc[idx, 'item_name']} - ₹{df.loc[idx, 'price']}")

def check_admin (uid,pas):

    try:
        df = pd.read_csv("admin.csv",index_col=0)

    except FileNotFoundError:
        print("Some important resources are missing ...")
        print("Please contact the developer....")

    for ind in df.index:
        if df.loc[ind,"admin_id"] == uid:
            if df.loc[ind,"admin_pass"] == pas:

                return "verified"

            return None
        else:
            return "not_valid"
    return None

def check_employee (uid,pas):

    try:
        df = pd.read_csv("employee.csv",index_col=0)

    except FileNotFoundError:
        print("Some important resources are missing ...")
        print("Please contact the admin....")

    for ind in df.index:
        if df.loc[ind,"emp_id"] == uid:
            if df.loc[ind,"emp_pas"] == pas:

                return "verified"

            else:
                return "not_valid"
        return None
    return None

def view_employee ():

    try:
        df = pd.read_csv("employee.csv",index_col=0)

    except FileNotFoundError:
        df = pd.DataFrame(columns=['emp_id','emp_pas'])
        df.to_csv('employee.csv',index=True)
        print("The file does not exists..")
        print("Contact the developer ....")
        return

    for ind in df.index:

        print(f"{ind} : {df.loc[ind,"emp_id"]} - {df.loc[ind,"emp_pas"]}")

def add_employee(new_id,new_pas):

    try:
        df = pd.read_csv("employee.csv", index_col=0)

    except FileNotFoundError:
        print("error")

    new_index = len(df)
    df.loc[new_index] = [new_id, new_pas]

    df.to_csv("employee.csv", index=True)
