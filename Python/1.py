terms = ["A 6", "B 12", "C 3"]
today = "2022.05.19"
privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C", "2022.10.01 C"]

today = "2020.01.01"
terms = ["Z 36", "D 36"]
privacies = ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]


###### 월, 일 처리 좀 더 깔끔하게 할 방법이 없나 ######
def get_valid_date(terms, reg_date, valid_type):
    for term in terms:
        term_type, valid_term = term.split()
        print(f'term_type : {term_type} valid_type : {valid_type}')
        if valid_type == term_type:
            r_year, r_month, r_day = reg_date.split(".")
            month = int(r_month) + int(valid_term)
            year = int(r_year)
            day = int(r_day) - 1
            # 월 처리
            if month > 12:
                year += month // 12
                month %= 12
                if month % 12 == 0:
                    month = 12
                    year -= 1
            # 일 처리
            if day < 1:
                day = 28
                month -= 1
                if month < 1:
                    month = 12
                    year -= 1
            valid_date = str(year) + "." + str(month).zfill(2) + "." + str(day).zfill(2)
            # 출력 부
            print(f'reg_date : {reg_date}')
            print(f'valid_type : {valid_type}')
            print(f'valid_term : {valid_term}')
            print(f'valid_date : {valid_date}')
            return valid_date
    return today


def solution(today, terms, privacies):
    i = 1
    answer = []
    for privacy in privacies:
        reg_date, valid_type = privacy.split()
        print('========================================================================================')
        print(f'{i} today : {today} reg_date : {reg_date}, valid_type : {valid_type}')
        # valid_type 에 해당하는 기간을 terms 에서 찾아서 계산(get_valid_date)
        valid_date = get_valid_date(terms, reg_date, valid_type)
        print(f'result : {valid_date}')
        # today 가 valid_date 이후일 경우 answer 에 추가(is_validated)
        year, month, day = today.split(".")
        v_year, v_month, v_day = valid_date.split(".")

        if int(year) > int(v_year):
            answer.append(i)
        elif int(year) == int(v_year) and int(month) > int(v_month):
            answer.append(i)
        elif int(year) == int(v_year) and int(month) == int(v_month) and int(day) > int(v_day):
            answer.append(i)
        i += 1
    return answer


print(solution(today, terms, privacies))


# 제출 답안
# def get_valid_date(today, terms, reg_date, valid_type):
#     for term in terms:
#         term_type, valid_term = term.split()
#         if valid_type == term_type:
#             r_year, r_month, r_day = reg_date.split(".")
#             month = int(r_month) + int(valid_term)
#             year = int(r_year)
#             if month > 12:
#                 month -= 12
#                 year += 1
#             valid_date = str(year) + "." + str(month).zfill(2) + "." + r_day
#             return valid_date
#     return today
#
#
# def solution(today, terms, privacies):
#     i = 1
#     answer = []
#     for privacy in privacies:
#         reg_date, valid_type = privacy.split()
#         valid_date = get_valid_date(today, terms, reg_date, valid_type)
#         year, month, day = today.split(".")
#         v_year, v_month, v_day = valid_date.split(".")
#
#         if int(year) > int(v_year):
#             answer.append(i)
#         elif int(year) >= int(v_year) and int(month) > int(v_month):
#             answer.append(i)
#         elif int(year) >= int(v_year) and int(month) >= int(v_month) and int(day) >= int(v_day):
#             answer.append(i)
#         i += 1
#     return answer
