# Title: Random Inventory System Simulation
![alt text](https://bikeutah.org/wp-content/uploads/2017/04/Asset-1-1024x324.png)
## Team Member(s):
Xiaozheng Hou, Yinan Ni, Siran Dai


# Monte Carlo Simulation Scenario & Purpose:
In the process of supply, it is always necessary to maintain a certain inventory reserve since the arrivals and sales cannot be the same amount and synchronized. If there are too many stocks, it will cause the funded backlog and the rise of custodial fees; if there are few stocks, it may lead to out-of-stock, resulting in loss of merchants' reputation and loss of customers. Therefore, we need to choose a suitable inventory and ordering strategy based on order policy.

We believe that using Monte Carlo Simulation will help us to find the lowest expected loss strategy and solve this issue.

So in our scenario, we will help the manager of a bicycles warehouse make the decision of choosing the best inventory strategy which yield the lowest cost.

In our first stage, we assumed that the warehouse have only one type of bicycle, and we compared and simulated several existing plans and picked the one with the lowest cost.
After received feedbacks from the instructor and classmates, in the final stage, we decided to add the type of bicycles into our consideration as well as set the P(threshold of ordering) & Q(order amount) in a specific range based instead of some existing plans, which will make our scenario more realistic and applicable.

## Simulation's variables of uncertainty
![alt text](https://github.com/daisiran/Final_Project/blob/master/Assumptions.png?raw=true)

List and describe your simulation's variables of uncertainty (where you're using pseudo-random number generation). For each such variable, how did you decide the range and probability distribution to use?  Do you think it's a good representation of reality?

## Hypothesis or hypotheses before running the simulation:
Hypothesis 1: If there is only one type of bicycle, the manager believe that there is no inventory strategy that will yield the cost less than 110000.

Hypothesis 2: If there are 5 types of bicycles, the manager believe that there is no inventory strategy that will yield the cost less than 520000.


## Analytical Summary of your findings: (e.g. Did you adjust the scenario based on previous simulation outcomes?  What are the management decisions one could make from your simulation's output, etc.)
Based on our simulation, we found out that 

## Instructions on how to use the program:
First, download and run the '1.0.py' file.
Second, input iterate times and the number of types of bicycle.

## All Sources Used:
- https://translate.google.com/translate?sl=auto&tl=en&js=y&prev=_t&hl=en&ie=UTF-8&u=http%3A%2F%2Fxuewen.cnki.net%2FCJFD-GCXT200501023.html&edit-text=&act=url
- https://wenku.baidu.com/view/89425c0c52ea551810a6875b
- http://www.wanfangdata.com.cn/details/detail.do?_type=perio&id=wlkj200710013
- https://github.com/nikolausn/Final-project
- https://seaborn.pydata.org/generated/seaborn.heatmap.html?highlight=heatmap#seaborn.heatmap
