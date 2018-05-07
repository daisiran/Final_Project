# -*- coding: utf-8
"""
Doctest
>>> bike = Order(70,20,10,10,{"list": ['1', '2', '3', '4'], "weight": [1, 5, 3, 1]},[{"miu": 50, "theta":5}], [{"miu": 5, "theta":5}])
>>> bike.order_fee(10,20,10)
70
>>> bike.loss_fee(10,20,40)
200
>>> bike.loss_fee(100,200,400)
2000
>>> bike.return_fee(1)
10
>>> bike.storage_fee(100)
10
>>> bike.storage_fee(2000)
200
"""
import math
import random
import numpy as np


class Order:

    def __init__(self, per_order_fee, per_loss_fee, per_cube_storage_fee, per_return_fee, weight_choice_coef, buy_gauss_coef, return_gauss_coef):
        self.per_order_fee          = per_order_fee
        self.per_loss_fee           = per_loss_fee
        self.per_cube_storage_fee   = per_cube_storage_fee
        self.per_return_fee         = per_return_fee
        self.weight_choice_coef     = weight_choice_coef  # {"list":['1', '2', '3', '4'], "weight": [1, 5, 3, 1]}
        self.buy_gauss_coef         = buy_gauss_coef  # [{"miu": 50, "theta":5}, {"miu": 50, "theta":5}, ...]
        self.return_gauss_coef      = return_gauss_coef  # [{"miu": 5, "theta":5}, {"miu": 5, "theta":5}, ...]

    def order_fee(self, s1, a, n):
        """
        calculate the order fee!
        :param s1: the number of product in the morning
        :param a: the number of product which arrive in the morning
        :param n: the random amount of need
        :return: float
        """
        return self.per_order_fee

    def loss_fee(self, s1, a, n):
        """
        calculate the loss fee if run short of the product !
        :param s1: the number of product in the morning
        :param a: the number of product which arrive in the morning
        :param n: the random amount of need
        :return: float
        """
        return self.per_loss_fee * (n - s1 - a)

    def return_fee(self, num):
        '''
        calculate the loss fee of customer return
        :param num: the number of bicycle customer return in a day.
        :return: float
        '''
        return self.per_return_fee * num;

    def storage_fee(self, num):
        """
       calculate the storage fee for all bike.
       One warehouse can store 100 bikes, and the price for rent one warehouse is 100.
       :param num: the total number of product which left in the evening
       :return: float
       """
        if num>0:
            cube_num = math.ceil(num/100)
        else:
            cube_num = 0

        f3 = self.per_cube_storage_fee * cube_num
        return f3


    def weight_choice(self):
        '''
        simulate the delay time after ordering
        :return: string
        '''
        new_list = []
        for i, vals in enumerate(self.weight_choice_coef["list"]):
            new_list.extend(vals * self.weight_choice_coef["weight"][i])
        return random.choice(new_list)

    def ordering(self, Q, s1, P,iterTimes):
        # s1 = Q
        """
       the process to calculate the total loss fee
       :param Q: the number of products purchase each time
       :param s1: the number of product in the morning
       :param P: the minimum number of product for ordering, which means owner need to order products if the number of products is less than P
       :param iterTimes: times fot iterate
       :return: float
       """
        avg_fee = 0
        # iterTimes = 200
        for times in range(iterTimes):

            total_fee = 0
            exp_day = [0]*len(Q)

            for day in range(1, 300):
                total_left = 0
                for kind in range(len(Q)):

                    n = round(random.gauss(self.buy_gauss_coef[kind]["miu"], self.buy_gauss_coef[kind]["theta"]))

                    rt = round(random.gauss(self.return_gauss_coef[kind]["miu"], self.return_gauss_coef[kind]["theta"]))
                    total_fee += self.return_fee(rt)
                    # print('n', n)
                    if day == exp_day[kind]:
                        a = Q[kind]
                    else:
                        a = 0
                    # print('a:', a)
                    if (s1[kind] + a - n < P[kind]) and (day > exp_day[kind]):
                        total_fee += self.order_fee(s1[kind], a, n)
                        # print('order_fee', total_fee)
                        d = self.weight_choice()
                        # print('d', d)
                        exp_day[kind] = day + int(d)
                    if (s1[kind] + a < n):
                        total_fee += self.loss_fee(s1[kind], a, n)
                        # print('loss_fee', total_fee)
                    if(s1[kind]+a-n > 0):
                        total_left += s1[kind]+a-n
                        s1[kind] = s1[kind]+a-n

                    else:
                        s1[kind] = 0

                total_fee += self.storage_fee(total_left)
                # s1 = s2 the  amount of next morning before arrive product equals to the amount of product in the evening

            avg_fee += total_fee
        # print("avg:",avg_fee/iterTimes)
        return avg_fee/iterTimes


if __name__ == "__main__":
    # per_order_fee, per_loss_fee, per_storage_fee, weight_choice_coef, gauss_coef
    bicycle = Order(75, 50, 100, 10, {"list": ['1', '2', '3', '4'], "weight": [1, 5, 3, 1]},\
        [{"miu": 50, "theta": 5}, {"miu": 30, "theta": 5}, {"miu": 40, "theta": 5}, {"miu": 50, "theta": 5}, {"miu": 30, "theta": 5}],\
        [{"miu": 10, "theta": 2}, {"miu": 8, "theta": 2}, {"miu": 9, "theta": 2}, {"miu": 7, "theta": 2}, {"miu": 5, "theta": 2}])

    minFee = 1e10
    # bicycleNum = 5
    print('----------------------------------------------------------')
    iterate_time    = int(input('How many times do you want to iterate?'))
    bicycleNum      = int(input('How many kinds of bicycle do you want to calculate?(Range in 1-5)'))
    while bicycleNum <1 or bicycleNum >5:
        bicycleNum  = int(input('How many kinds of bicycle do you want to calculate?(Range in 1-5)'))

    P_l             = []
    Q_l             = []
    cost_l          = []
    for times in range(50):
        P           = np.random.randint(0,500, bicycleNum)
        Q           = np.random.randint(60,500, bicycleNum)
        s1          = Q[:]
        minP        = tuple(P)
        # mins1 = tuple(s1)
        minQ        = tuple(Q)
        nowFee      = bicycle.ordering(minQ,s1,minP,iterate_time)
        P_l         .append(minP[0])
        Q_l         .append(minQ[0])
        cost_l      .append(nowFee)
        if (nowFee < minFee):
            minFee  = nowFee
            nowQ    = minQ
            nowP    = minP
    # print('p:',P_l,'q',Q_l,'cost',cost_l)
    print('MinFee:',minFee)
    print("P:", nowP, "Q:", nowQ)
