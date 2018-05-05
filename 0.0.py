# import math
# import random
#
# class Order:
#
#     @staticmethod
#     def order_fee(s1,a,n):
#         """
#         calculate the order fee!
#         :param s1: the number of product in the morning
#         :param a: the number of product which arrive in the morning
#         :param n: the random amount of need
#         :param p: dinghuodian P
#         :return: float
#         """
#         # f1 = 0
#         # if s1+a-n<p:
#         #     f1 = 75
#         # else:
#         #     f1 = 0
#         return 75
#
#     @staticmethod
#     def loss_fee(s1,a,n):
#         """
#         calculate the loss fee if run short of the product !
#         :param s1: the number of product in the morning
#         :param a: the number of product which arrive in the morning
#         :param n: the random amount of need
#         :return: float
#         """
#         # f2 = 0
#         # if s1+a<n:
#         #     f2 = 50*(n-s1-a)
#         # else:
#         #     f2 = 0
#         return 50*(n-s1-a)
#
#     @staticmethod
#     def storage_fee(s1,a,n):
#         """
#         storage fee
#         :param s1: the number of product in the morning
#         :param a: the number of product which arrive in the morning
#         :param n: the random amount of need
#         :param s2:the number of product which left in the evening
#         :return: float
#         """
#         if s1+a >=n:
#             s2 = s1 + a - n
#         else:
#             s2 = 0
#
#         f3 = 0.75 * s2
#         return f3
#
#
#     @staticmethod
#     def weight_choice(lst,weight):
#         """
#         judge if the product arrive time of product.
#         :param list:
#         :param weight:
#         :return:
#         """
#         new_list = []
#         for i,vals in enumerate(lst):
#             new_list.extend(vals * weight[i])
#         return random.choice(new_list)
#
#     @staticmethod
#     def ordering(Q,s1,P):
#         #s1 = Q
#         # d = Order.weight_choice(['1','2','3','4'],[1,5,3,1])
#
#         total_fee = 0
#         exp_day = 0
#
#
#         for day in range(1,300):
#             n = round(random.gauss(50, 5))
#             # print('n',n)
#             if day == exp_day:
#                 a = Q
#             else:
#                 a = 0
#             # print('a:',a)
#             if (s1+a-n<P) and (day>exp_day):
#                 total_fee += Order.order_fee(s1,a,n)
#                 # print('order_fee',total_fee)
#                 d = Order.weight_choice(['1', '2', '3', '4'], [1, 5, 3, 1])
#                 # print('d',d)
#                 exp_day = day + int(d)
#             if (s1+a<n):
#                 total_fee += Order.loss_fee(s1,a,n)
#                 # print('loss_fee',total_fee)
#
#             total_fee += Order.storage_fee(s1,a,n)
#             # print('storage',total_fee)
#             #s1 = s2 the  amount of next morning before arrive product equals to the amount of product in the evening
#             #第二天早上的存货量 = 前一天晚的存货量
#             # print(Order.storage_fee(s1,a,n))
#             s1 = Order.storage_fee(s1, a, n)/ 0.75
#             # print('s1:', s1)
#             # print('---------------------------')
#
#         print(total_fee)
#
#
# Order.ordering(150,150,120)
# Order.ordering(200,200,120)
# Order.ordering(200,200,150)
# Order.ordering(250,250,200)
# Order.ordering(200,200,250)
#


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
        return self.per_order_fee;

    def loss_fee(self, s1, a, n):
        return self.per_loss_fee * (n - s1 - a);

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

        total_fee = 0
        exp_day = 0

        for day in range(1, 300):
            n = round(random.gauss(self.gauss_coef["miu"], self.gauss_coef["theta"]))
            print('n', n)
            if day == exp_day:
                a = Q
            else:
                a = 0
            print('a:', a)
            if (s1 + a - n < P) and (day > exp_day):
                total_fee += self.order_fee(s1, a, n)
                print('order_fee', total_fee)
                d = self.weight_choice()
                print('d', d)
                exp_day = day + int(d)
            if (s1 + a < n):
                total_fee += self.loss_fee(s1, a, n)
                print('loss_fee', total_fee)

            total_fee += self.storage_fee(s1, a, n)
            print('storage', total_fee)
            # s1 = s2 the  amount of next morning before arrive product equals to the amount of product in the evening
            # 第二天早上的存货量 = 前一天晚的存货量
            print(self.storage_fee(s1, a, n))
            s1 = self.storage_fee(s1, a, n) / self.per_storage_fee
            print('s1:', s1)
            print('---------------------------')

        print(total_fee)


class Manage:

    def __init__(self):
        self.bicycles = []
        self.solution = []

    def addBicycle(self, per_order_fee, per_loss_fee, per_storage_fee, weight_choice_coef, gauss_coef):
        bicycles.append(Order(per_order_fee, per_loss_fee, per_storage_fee, weight_choice_coef, gauss_coef))

    def optimize(self, bicycle):
        pass
        return (Q, s1, P)

    def globalSolution(self):
        pass
        for i in range(len(bicycles)):
            self.solution.append(self.optimize(bicycles[i]))


if __name__ == "__main__":
    bicycle = Order(75, 50, 0.75, {"list": ['1', '2', '3', '4'], "weight": [1, 5, 3, 1]}, {"miu": 50, "theta": 5})
    bicycle.ordering(150, 150, 200)


