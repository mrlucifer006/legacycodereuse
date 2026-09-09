import pandas as pd

def add_data(name, price):
    try:
        df = pd.read_csv("payroll.csv", index_col=0)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["category", "amount"])

    new_index = len(df)
    df.loc[new_index] = [name, price]
    df.to_csv("payroll.csv", index=True)

def del_data(name):
    try:
        df = pd.read_csv("payroll.csv", index_col=0)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["category", "amount"])
    df = df[df["category"] != name]
    df.to_csv("payroll.csv", index=True)

def update_data(upd_name, upd_prc):
    try:
        df = pd.read_csv("payroll.csv", index_col=0)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["category", "amount"])
    df.loc[df["category"] == upd_name, "amount"] = upd_prc
    df.to_csv("payroll.csv", index=True)

def display_data():
    try:
        df = pd.read_csv("payroll.csv", index_col=0)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["category", "amount"])
    for idx in df.index:
        print(f"{idx}  : {df.loc[idx, 'category']} - ₹{df.loc[idx, 'amount']}")

def check_admin(uid, pas):
    try:
        df = pd.read_csv("admin.csv", index_col=0)
    except FileNotFoundError:
        print("Some important resources are missing ...")
        print("Please contact the developer....")
        return None
    for ind in df.index:
        if df.loc[ind, "admin_id"] == uid:
            if df.loc[ind, "admin_pass"] == pas:
                return "verified"
            return None
        else:
            return "not_valid"
    return None

def check_hr(uid, pas):
    try:
        df = pd.read_csv("hr.csv", index_col=0)
    except FileNotFoundError:
        print("Some important resources are missing ...")
        print("Please contact the admin....")
        return None
    for ind in df.index:
        if df.loc[ind, "emp_id"] == uid:
            if df.loc[ind, "emp_pas"] == pas:
                return "verified"
            else:
                return "not_valid"
        return None
    return None

def view_hrs():
    try:
        df = pd.read_csv("hr.csv", index_col=0)
    except FileNotFoundError:
        df = pd.DataFrame(columns=['emp_id', 'emp_pas'])
        df.to_csv('hr.csv', index=True)
        print("The file does not exists..")
        print("Contact the developer ....")
        return
    for ind in df.index:
        print(f"{ind} : {df.loc[ind, 'emp_id']} - {df.loc[ind, 'emp_pas']}")

def add_hr(new_id, new_pas):
    try:
        df = pd.read_csv("hr.csv", index_col=0)
    except FileNotFoundError:
        df = pd.DataFrame(columns=['emp_id', 'emp_pas'])

    new_index = len(df)
    df.loc[new_index] = [new_id, new_pas]
    df.to_csv("hr.csv", index=True)
