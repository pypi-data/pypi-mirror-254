import wikirate4py
from wikirate4py import Cursor

api = wikirate4py.API('ThessaloWikiRate')

# cursor = Cursor(api.get_answers_by_id, identifier=3233883, source="Source-000162318", per_page=100)
# answers = []
# while cursor.has_next():
#     answers.extend(cursor.next())
#
# print(len(answers))
# for answer in answers:
#     print(answer)
#     api.delete_wikirate_entity(id=answer.id)

metrics = [6908731, 8408492, 14019318, 14019304, 13006160, 8396541, 14019252]
# metrics = []
# metrics = []
for metric in metrics:
    print(metric)
    api.delete_wikirate_entity(id=metric)


# metrics = [13006134, 8412610, 14019233]

# for metric in metrics:
#     cursor = Cursor(api.get_answers_by_id, identifier=metric, per_page=100)
#     while cursor.has_next():
#         answers = cursor.next()
#         for answer in answers:
#             print(answer.id)
#             try:
#                 a = api.update_research_metric_answer_by_id(
#                     id=answer.id,
#                     metric_name='MSA_State_imposed_forced_labour',
#                     metric_designer='Walk Free',
#                     year=answer.year,
#                     company=answer.company)
#             except Exception as e:
#                 print(e)
