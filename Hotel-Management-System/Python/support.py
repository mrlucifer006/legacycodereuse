import pandas as pd

def add_data(name, price):
    try:
        df = pd.read_csv("rooms.csv", index_col=0)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["room_type", "price"])

    new_index = len(df)
    df.loc[new_index] = [name, price]
    df.to_csv("rooms.csv", index=True)

def del_data(name):
    try:
        df = pd.read_csv("rooms.csv", index_col=0)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["room_type", "price"])
    df = df[df["room_type"] != name]
    df.to_csv("rooms.csv", index=True)

def update_data(upd_name, upd_prc):
    try:
        df = pd.read_csv("rooms.csv", index_col=0)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["room_type", "price"])
    df.loc[df["room_type"] == upd_name, "price"] = upd_prc
    df.to_csv("rooms.csv", index=True)

def display_data():
    try:
        df = pd.read_csv("rooms.csv", index_col=0)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["room_type", "price"])
    for idx in df.index:
        print(f"{idx}  : {df.loc[idx, 'room_type']} - ₹{df.loc[idx, 'price']}")

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

def check_receptionist(uid, pas):
    try:
        df = pd.read_csv("receptionist.csv", index_col=0)
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

def view_receptionists():
    try:
        df = pd.read_csv("receptionist.csv", index_col=0)
    except FileNotFoundError:
        df = pd.DataFrame(columns=['emp_id', 'emp_pas'])
        df.to_csv('receptionist.csv', index=True)
        print("The file does not exists..")
        print("Contact the developer ....")
        return
    for ind in df.index:
        print(f"{ind} : {df.loc[ind, 'emp_id']} - {df.loc[ind, 'emp_pas']}")

def add_receptionist(new_id, new_pas):
    try:
        df = pd.read_csv("receptionist.csv", index_col=0)
    except FileNotFoundError:
        df = pd.DataFrame(columns=['emp_id', 'emp_pas'])

    new_index = len(df)
    df.loc[new_index] = [new_id, new_pas]
    df.to_csv("receptionist.csv", index=True)
