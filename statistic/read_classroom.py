# #encoding:gbk
# import json
#
# def writeJson(data, filename):
#     f = open(filename, 'w')
#     json.dumps(data, f)
#     f.close()
#
# def readJson(filename):
#     f = open(filename)
#     s = json.load(f)
#     f.close()
#     return s
#
# import xlrd
# import re
# data = xlrd.open_workbook(r'''/Users/zhounaiding/Desktop/code.xls''')
# table = data.sheets()[0]
# nrows = table.nrows
# ncols = table.ncols
# cell_A1 = table.cell(0,0).value
# matrix = []
# for i in range(1,nrows):
#     line = [table.cell(i,0).value,table.cell(i,1).value,table.cell(i,2).value]
#     matrix.append(line)
# length = len(matrix)
# info = {"N":{},"S":{}}
# beiqu = matrix[0][1][0:2]
# for i in range(length):
#     if matrix[i][1][0:2] == beiqu:
#         reg = u"[\u4e00-\u9fa5]{3,9}"
#         building_name = re.findall(reg, matrix[i][1])
#         number = re.findall(r"[0-9]{3,4}", matrix[i][1].encode("utf-8"))
#         if building_name[0] not in info["N"]:
#             if len(number) > 0:
#                 info["N"][building_name[0]] = {number[0][-3]:[(matrix[i][0].encode("utf-8"),matrix[i][2])]}
#         else:
#             if len(number) > 0:
#                 if number[0][-3] not in info["N"][building_name[0]]:
#                     info["N"][building_name[0]][number[0][-3]] = [(matrix[i][0].encode("utf-8"),matrix[i][2])]
#                 else:
#                     info["N"][building_name[0]][number[0][-3]].append((matrix[i][0].encode("utf-8"),matrix[i][2]))
#     else:
#         reg = u"[\u4e00-\u9fa5]{3,9}"
#         building_name = re.findall(reg, matrix[i][1])
#         number = re.findall(r"[0-9]{3,4}", matrix[i][1].encode("utf-8"))
#         if building_name[0] not in info["S"]:
#             if len(number) > 0:
#                 info["S"][building_name[0]] = {
#                     number[0][-3]: [(matrix[i][0].encode("utf-8"), matrix[i][2])]}
#         else:
#             if len(number) > 0:
#                 if number[0][-3] not in info["S"][building_name[0]]:
#                     info["S"][building_name[0]][number[0][-3]] = [(matrix[i][0].encode("utf-8"), matrix[i][2])]
#                 else:
#                     info["S"][building_name[0]][number[0][-3]].append((matrix[i][0].encode("utf-8"), matrix[i][2]))
# print(info["S"][u"教二楼"]["4"])
#
# with open("classroom.json", "w") as f:
#   json.dump(info, f)
#
# # writeJson(info, 'classroom.json')
# a = json.dumps(info)
