# models = lemon.project_ledger
#
# c = models.ProjectTab.select(
#             peewee.fn.Sum(models.ProjectTab.budget)
#         ).scalar()
# print(c)

models = lemon.lemon_rag

c = models.AuthUserTab.select().where(models.AuthUserTab.username == "小孩子2").first()
print(dir(c))
print(dir(c.system_user))
print(dir(c.account))
print(c.system_user.唯一标识符)
# print(c.系统用户表.外部标识符)
print(c.系统用户表.姓名)
print(c.系统用户表.工号)
# print(c.系统用户表.用户id)
print(c.系统用户表.id)
print(lemon.system.current_user.uuid)

# lemon.system.obj.account.creator.系统用户表.