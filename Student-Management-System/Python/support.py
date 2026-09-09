import pandas as pd

def add_data(name, price):
    try:
        df = pd.read_csv("students.csv", index_col=0)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["student_name", "marks"])

    new_index = len(df)
    df.loc[new_index] = [name, price]
    df.to_csv("students.csv", index=True)

def del_data(name):
    try:
        df = pd.read_csv("students.csv", index_col=0)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["student_name", "marks"])
    df = df[df["student_name"] != name]
    df.to_csv("students.csv", index=True)

def update_data(upd_name, upd_prc):
    try:
        df = pd.read_csv("students.csv", index_col=0)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["student_name", "marks"])
    df.loc[df["student_name"] == upd_name, "marks"] = upd_prc
    df.to_csv("students.csv", index=True)

def display_data():
    try:
        df = pd.read_csv("students.csv", index_col=0)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["student_name", "marks"])
    for idx in df.index:
        print(f"{idx}  : {df.loc[idx, 'student_name']} - {df.loc[idx, 'marks']}")

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

def check_teacher(uid, pas):
    try:
        df = pd.read_csv("teacher.csv", index_col=0)
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

def view_teachers():
    try:
        df = pd.read_csv("teacher.csv", index_col=0)
    except FileNotFoundError:
        df = pd.DataFrame(columns=['emp_id', 'emp_pas'])
        df.to_csv('teacher.csv', index=True)
        print("The file does not exists..")
        print("Contact the developer ....")
        return
    for ind in df.index:
        print(f"{ind} : {df.loc[ind, 'emp_id']} - {df.loc[ind, 'emp_pas']}")

def add_teacher(new_id, new_pas):
    try:
        df = pd.read_csv("teacher.csv", index_col=0)
    except FileNotFoundError:
        df = pd.DataFrame(columns=['emp_id', 'emp_pas'])

    new_index = len(df)
    df.loc[new_index] = [new_id, new_pas]
    df.to_csv("teacher.csv", index=True)
