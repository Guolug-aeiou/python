# 商品名称常量
JSD = '金士顿U盘8G'
SC = '胜创16GTF卡'
DKQ = '读卡器'
WX = '网线2米'
COUNT = 1  # 数量
discount = 1  # 打折值
price_jsd = input(f'输入{JSD}的单价:')
price_sc = input(f'输入{SC}的单价:')
price_dkq = input(f'输入{DKQ}的单价:')
price_wx = input(f'输入{WX}的单价:')
# 总金额
sum = COUNT * float(price_jsd) + COUNT * float(price_sc) + COUNT * float(price_dkq) + COUNT * float(price_wx)
print('...........................................')
print('单号 : XH-202402150705')
print('时间 : 2025-02-24 19:56:35')
print('...........................................')
print('名称\t\t\t数量\t\t\t单价\t\t\t金额')
print(JSD, '\t', COUNT, '\t\t\t', price_jsd, '\t\t', COUNT * float(price_jsd))
print(SC, '\t', COUNT, '\t\t\t', price_sc, '\t\t', COUNT * float(price_sc))
print(DKQ, '\t\t', COUNT, '\t\t\t', price_dkq, '\t\t\t', COUNT * float(price_dkq))
print(WX, '\t\t', COUNT, '\t\t\t', price_wx, '\t\t\t', COUNT * float(price_wx))
print('...........................................')
print('总数: 4\t\t\t\t\t总金额:', sum)
print('折后金额:', discount * sum)
print('实收: ',sum,'\t\t\t找零: 0.00')
print('收银: 管理员')
print('...........................................')
