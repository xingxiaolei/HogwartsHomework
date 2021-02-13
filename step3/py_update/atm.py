import json
import os


class ATM:

    def select_money(self, card_num, pwd):
        with open('./cus.json') as f:
            data = json.load(f)
            val = data.get(card_num)
            if val:
                if pwd == val['pwd']:
                    return val['balance']
                else:
                    return 0
            else:
                return 1


    def save_money(self, card_num, pwd, money):
        curr_money = self.select_money(card_num, pwd)
        if isinstance(curr_money, str):
            new_money = int(curr_money) + int(money)
            with open('./cus.json') as f1:
                data = json.load(f1)
                data[card_num]['balance'] = str(new_money)
                with open('./cus_sub.json', 'w') as f2:
                    json.dump(data, f2)

            os.remove('./cus.json')
            os.rename('./cus_sub.json', 'cus.json')
        else:
            pass

if __name__ == '__main__':

    a = ATM()
    print(a.select_money("123456", '123456'))
    a.save_money('123456','123456', 100)
    print(a.select_money('123456','123456'))