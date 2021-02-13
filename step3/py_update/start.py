from step3.py_update.atm import ATM



def startUp():
    card = input("请输入卡号：")
    pwd = input("请输入密码：")
    salary = input("请输入工资：")

    atm = ATM()
    curr_money = atm.select_money(card, pwd)
    if curr_money == 1:
        print('用户不存在')
    elif curr_money == 0:
        print('密码错误')
    elif curr_money.isdigit():
        print(f"存入前余额：{curr_money}")
        print('开始存钱....')
        atm.save_money(card, pwd, salary)
        update_money = atm.select_money(card, pwd)
        print(f'存入后余额：{update_money}')

if __name__ == '__main__':
    startUp()