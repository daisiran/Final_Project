# -*- coding: utf-8 -*-
import math
import random


class Order:

    def __init__(self, per_order_fee, per_loss_fee, per_storage_fee, weight_choice_coef, gauss_coef):
        self.per_order_fee = per_order_fee
        self.per_loss_fee = per_loss_fee
        self.per_storage_fee = per_storage_fee
        self.weight_choice_coef = weight_choice_coef  # {"list":['1', '2', '3', '4'], "weight": [1, 5, 3, 1]}
        self.gauss_coef = gauss_coef  # {"miu": 50, "theta":5}

    def order_fee(self, s1, a, n):
        return self.per_order_fee

    def loss_fee(self, s1, a, n):
        return self.per_loss_fee * (n - s1 - a)

    def storage_fee(self, s1, a, n):
        if s1 + a >= n:
            s2 = s1 + a - n
        else:
            s2 = 0

        f3 = self.per_storage_fee * s2
        return f3

    def weight_choice(self):
        new_list = []
        for i, vals in enumerate(self.weight_choice_coef["list"]):
            new_list.extend(vals * self.weight_choice_coef["weight"][i])
        return random.choice(new_list)

    def ordering(self, Q, s1, P):
        # s1 = Q
        # d = Order.weight_choice(['1','2','3','4'],[1,5,3,1])
        avg_fee = 0
        for times in range(10):
            total_fee = 0
            exp_day = 0
            for day in range(1, 300):
                n = round(random.gauss(self.gauss_coef["miu"], self.gauss_coef["theta"]))
                # print('n', n)
                if day == exp_day:
                    a = Q
                else:
                    a = 0
                # print('a:', a)
                if (s1 + a - n < P) and (day > exp_day):
                    total_fee += self.order_fee(s1, a, n)
                    # print('order_fee', total_fee)
                    d = self.weight_choice()
                    # print('d', d)
                    exp_day = day + int(d)
                if (s1 + a < n):
                    total_fee += self.loss_fee(s1, a, n)
                    # print('loss_fee', total_fee)

                total_fee += self.storage_fee(s1, a, n)
                # print('storage', total_fee)
                # s1 = s2 the  amount of next morning before arrive product equals to the amount of product in the evening
                # 第二天早上的存货量 = 前一天晚的存货量
                # print(self.storage_fee(s1, a, n))
                s1 = self.storage_fee(s1, a, n) / self.per_storage_fee
                # print('s1:', s1)
                # print('---------------------------')
            # print(total_fee)
            avg_fee += total_fee

        print("avg:",avg_fee/10)
        return avg_fee/10


class Manage:

    def __init__(self):
        self.bicycles = []
        self.solution = []

    def addBicycle(self, per_order_fee, per_loss_fee, per_storage_fee, weight_choice_coef, gauss_coef):
        self.bicycles.append(Order(per_order_fee, per_loss_fee, per_storage_fee, weight_choice_coef, gauss_coef))

    #get the optimal solution (loop)
    def optimize(self, bicycle):
        # pass
        cost_min = 100000000

        for Q in range(180,250):
            for P in range(180,250):
                cost = bicycle.ordering(Q,Q,P)
                if cost < cost_min:
                    cost_min = cost
                    Q_optimal = Q
                    P_optimal = P
        print(cost_min,Q_optimal,P_optimal)

        return (cost_min,Q_optimal, Q_optimal, P_optimal)

    def globalSolution(self):
        pass
        for i in range(len(self.bicycles)):
            self.solution.append(self.optimize(self.bicycles[i]))



if __name__ == "__main__":
    #per_order_fee, per_loss_fee, per_storage_fee, weight_choice_coef, gauss_coef
    bicycle = Order(75, 50, 0.75, {"list": ['1', '2', '3', '4'], "weight": [1, 5, 3, 1]}, {"miu": 50, "theta": 5})
    bicycle.ordering(150, 150, 200)
    manage  = Manage()
    manage.addBicycle(75, 50, 0.75, {"list": ['1', '2', '3', '4'], "weight": [1, 5, 3, 1]}, {"miu": 50, "theta": 5})
    manage.optimize(bicycle)








