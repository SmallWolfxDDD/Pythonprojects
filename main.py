import MES

excel = MES.Excel_Editor("Score.xlsx", "Main")

excel.fill_first_row(["ID", "Score", "Used_score", "Paper", "Bottle"])

def new_user(user):
    if not excel.find_row_index([user]):
        row = excel.sheet.max_row+1
        excel.add_new_row([user, f"=D{row}*F1+E{row}*G1-C{row}", 0, 0, 0])
    else:
        print("Fail: There exists a user:", user)

def update_score(user, type, value):
    user = excel.find_row_index([user])
    if user:
        excel.fill_block(user, type, value, False)
    else:
        print("Fail: There exists no user:", user)
        
new_user("s201136")
update_score("s201136", "Paper", 1.3)