# Title: Random Inventory System Simulation of a Bicycles Warehouse
![alt text](https://bikeutah.org/wp-content/uploads/2017/04/Asset-1-1024x324.png)
## Team Member(s):
Xiaozheng Hou, Yinan Ni, Siran Dai


# Monte Carlo Simulation Scenario & Purpose:
In the process of supply, it is always necessary to maintain a certain inventory reserve since the arrivals and sales cannot be the same amount and synchronized. If there are too many stocks, it will cause the funded backlog and the rise of custodial fees; if there are few stocks, it may lead to out-of-stock, resulting in loss of merchants' reputation and loss of customers. Therefore, we need to choose a suitable inventory and ordering strategy based on order policy.

We believe that using Monte Carlo Simulation will help us to find the lowest expected loss strategy and solve this issue.

So in our scenario, we will help the manager of a bicycles warehouse to , 

## Simulation's variables of uncertainty
The random variable will be daily demand, arrival delay after order.
List and describe your simulation's variables of uncertainty (where you're using pseudo-random number generation). For each such variable, how did you decide the range and probability distribution to use?  Do you think it's a good representation of reality?

Daily demand ～ Normal distribution N(50, 52)
Probability distribution of delivery lead time

## Hypothesis or hypotheses before running the simulation:
Hypothesis 1: , the manager believe there is no that will less than ******.

Hypothesis 2: If there are 5 types of bicycles, the manager believe there is no that will less than 500000.


## Analytical Summary of your findings: (e.g. Did you adjust the scenario based on previous simulation outcomes?  What are the management decisions one could make from your simulation's output, etc.)
Based on our simulation, we found that 

## Instructions on how to use the program:
Download and run the '1.0.py' file.

## All Sources Used:
- https://translate.google.com/translate?sl=auto&tl=en&js=y&prev=_t&hl=en&ie=UTF-8&u=http%3A%2F%2Fxuewen.cnki.net%2FCJFD-GCXT200501023.html&edit-text=&act=url
- https://wenku.baidu.com/view/89425c0c52ea551810a6875b
- http://www.wanfangdata.com.cn/details/detail.do?_type=perio&id=wlkj200710013
- https://github.com/nikolausn/Final-project
- https://seaborn.pydata.org/generated/seaborn.heatmap.html?highlight=heatmap#seaborn.heatmap
