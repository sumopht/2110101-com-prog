# # HW02 (ไม่ลบหรือแก้ไขบรรทัดนี้ หรือเพิ่มอะไรก่อนบรรทัดนี้ โดยเด็ดขาด)
# def get_sum(data):
#     id = []
#     score = []
#     for i in range(len(data)):
#         if i % 2 == 0:
#             id.append(data[i])
#         else:
#             score.append(data[i])
#     count = 1
#     sum = 0
#     id_output = []
#     score_output = []
#     for i in range(len(id)):
#         if i == 0:
#             min_score = score[i]
#             sum = sum + score[i]
#             count += 1
#         else:
#             if id[i] == id[i - 1]:
#                 count += 1
#                 if score[i] < min_score:
#                     min_score = score[i]
#                 sum = sum + score[i]
#                 if i == len(id) - 1:
#                     id_output.append(id[i])
#                     if count > 3:
#                         sum = sum - min_score
#                     score_output.append(sum)

#             else:
#                 id_output.append(id[i - 1])
#                 if count > 3:
#                     sum = sum - min_score
#                 score_output.append(sum)
#                 count = 1
#                 sum = 0
#                 sum = sum + score[i]
#                 min_score = score[i]
#     output = []
#     for i in range(len(score_output)):
#         output.append(id_output[i])
#         output.append(score_output[i])
#     return output


# # -----------------------------
# d = [
#     6610013121, 4, 6610013121, 4, 6610013121, 4, 6610013121, 4,
#     6610021021, 5, 6610021021, 5,
#     6610061121, 5, 6610061121, 5, 6610061121, 1,
#     6610000121, 3, 6610000121, 2, 6610000121, 2, 6610000121, 3, 6610000121, 3,
#     6531501921, 5, 6531501921, 8, 6531501921, 8, 6531501921, 2
# ]
# out = get_sum(d)
# print(out)  # ต้องแสดง [6610013121, 4, 6610021021, 10, 6610061121, 11, 6610000121, 8]
# # ข้อแนะนำ: ควรทดสอบ get_sum ด้วยข้อมูลชุดอื่นด้วย (ลิสต์ d ข้างบนอาจมีไม่ครอบคลุมทุกกรณี)
if 1:
    print("hello")
