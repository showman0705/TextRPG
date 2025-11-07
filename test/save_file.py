# '''
# 프로그램이름 : BookListMaker
# 제작자 : 10903 김동규
# 주의사항 : 엑셀파일에 저장하고나서 그 파일이 열린 상태로 실행시키면 오류가 생김

# 프로젝트를 만들게 된 계기 : 학기 초에 독서활동을 기록하는 과제를 하면서 계속 새로 파일을 만들고 내용을 작성하는 등의 과정에서 시간이 너무 낭비된다는
# 생각을 해서 간단하게 입력하는 것만으로 정리되는 프로그램을 만들게 됬다.

# 프로젝트를 만들면서 어려웠던 점과 극복 : 이 프로젝트를 만들면서 입력받은 값을 엑셀에다 저장하는 과정이 어려웠다. 완전히 생소한 개념이었기 때문에 openpyxl이라는
# 모듈도 이번에 처음 사용해보았다. 하지만 유튜브나 인터넷의 강의들을 들으면서 새로 배우고 정보 시간에 배웠던 배열을 통해서 입력받은 정보를 정리하는 과정을
# 통해서 문제를 해결할 수 있었다. 이런 과정을 통해 새로운 것을 배우는 것에 대한 즐거움을 느낄 수 있었다. 또 배웠던 것을 복습하는 과정에서 알고 있던 지식을
# 더욱 확고하게 정리할 수 있는 계기가 되기도 했다. 

# 프로젝트를 만들면서 느낀 점 : 정보 시간에 배운 코딩에 대한 지식과 파이썬이라는 언어를 통해서 내가 필요한 것을 만드는 경험은 내가 처음 프로그래머가 되겠다는
# 생각을 했을때 가지게 된 꿈인 디지털 세상 속에 나만의 세상을 만들겠다는 것이 점점 가까워지는 것처럼 느끼게 된 계기가 되었다. 프로젝트를 진행하면서 위와 같은
# 어려운 점도 있었지만 직접 탐구하고 알아보면서 극복하고 배웠던 것을 다시 이용해보면서 성장할 수 있었다. 추후 나는 이 프로젝트에 GUI를 적용시켜 사용자의 편의성을
# 개선하고 프로젝트의 함수를 파일별로 나누어보면서 코드의 가독성을 늘려보고자 한다. 또 그래프를 통해서 저장된 책의 통계를 확인할 수 있는 기능도 추가해보고 싶다.
# '''



# import json
# import os
# import openpyxl
# def generate_book_id(records): # id만들기(가장 큰 수의 아이디 + 1)
#     if not records:
#         return 1
#     return max(book["ID"] for book in records) + 1

# JSON_KEYS = ["ID", "제목", "작가", "읽은 날짜", "평점", "리뷰", "장르"] # json 헤더

# JSON_FILENAME = "booklist.json"
# TXT_FILENAME  = "booklist.txt" # 각 파일 제목
# XL_FILENAME = "booklist.xlsx" 

# def load_data(filename): # json 파일 가져오기
#     if not os.path.exists(filename): #없으면 빈 배열로 처리 => 아직 기록 x
#         return []
#     with open(filename, "r", encoding="utf-8") as f:
#         return json.load(f)

# def save_data(records, filename): #json으로 결과 저장
#     with open(filename, "w", encoding="utf-8") as f:
#         json.dump(records, f, ensure_ascii=False, indent=4)

# def save_datainexcel(records, filename): # 엑셀에 저장(입력된 배열을 순서대로 저장)
#     wb = openpyxl.Workbook()
#     ws = wb.active
#     ws.append(JSON_KEYS)  # 첫 행에 표지
#     for book in records:
#         ws.append([book.get(key, "") for key in JSON_KEYS]) # 자료들 추가
#     wb.save(filename)


# def add_book(records, title, author, read_date, rating, review, genre): # 리스트에 데이터 저장
#     book = {
#         "ID": generate_book_id(records),
#         "제목": title,
#         "작가": author,
#         "읽은 날짜": read_date,
#         "평점": rating,
#         "리뷰": review,
#         "장르": genre
#     }
#     records.append(book)

# def update_book(records, book_id, new_data): # id로 책 찾고 새로운 정보 업데이트
#     for book in records:
#         if book["ID"] == book_id:
#             book.update(new_data)
#             return True
#     return False

# def delete_book(records, book_id): # 책 삭제
#     for book in records:
#         if book["ID"] == book_id:
#             records.remove(book)
#             return True
#     return False

# def view_all_books(records): # 입력된거(저장된것까지) 출력
#     return [
#         f"{b['ID']}: {b['제목']} by {b['작가']} ({b['읽은 날짜']}) - 평점: {b['평점']}"
#         for b in records
#     ]

# def search_book(records, keyword, search_by="제목"): # 제목, 작가 기준으로 검색
#     key = search_by if search_by in ("제목", "작가") else "제목" # 포함된 것들 
#     return [
#         f"{b['ID']}: {b['제목']} by {b['작가']} ({b['읽은 날짜']})" 
#         for b in records
#         if keyword.lower() in str(b.get(key, "")).lower()
#     ]

# def main(): # 메인 반복(종료시 6번 필수)
#     records = load_data(JSON_FILENAME)

#     while True:
#         print("\n독서 기록 시스템")
#         print("1. 책 추가")
#         print("2. 전체 목록 보기")
#         print("3. 책 검색")
#         print("4. 책 수정")
#         print("5. 책 삭제")
#         print("6. 종료")
#         choice = input("선택: ")

#         if choice == '1':
#             title  = input("제목: ")
#             author = input("작가: ")
#             date   = input("읽은 날짜(YYYY-MM-DD): ")
#             rating = int(input("평점(1~5): "))
#             review = input("리뷰: ")
#             genre  = input("장르: ")
#             add_book(records, title, author, date, rating, review, genre)
#             save_data(records, JSON_FILENAME)
#             save_datainexcel(records, XL_FILENAME)
#             print(f"엑셀 파일로 저장 완료: {XL_FILENAME}")
#             print("추가 완료.")

#         elif choice == '2':
#             for line in view_all_books(records):
#                 print(line)

#         elif choice == '3':
#             keyword = input("검색어: ")
#             by      = input("검색 기준 (제목/작가): ")
#             for line in search_book(records, keyword, by):
#                 print(line)

#         elif choice == '4':
#             book_id = int(input("수정할 책 ID: "))
#             new_data = {
#                 "제목":      input("새 제목: "),
#                 "작가":      input("새 작가: "),
#                 "읽은 날짜": input("새 읽은 날짜: "),
#                 "평점":      int(input("새 평점: ")),
#                 "리뷰":      input("새 리뷰: "),
#                 "장르":      input("새 장르: ")
#             }
#             if update_book(records, book_id, new_data): 
#                 print("수정 완료.")
#             else:
#                 print("해당 ID를 찾을 수 없습니다.")

#         elif choice == '5':
#             book_id = int(input("삭제할 책 ID: "))
#             if delete_book(records, book_id):
#                 print("삭제 완료.")
#             else:
#                 print("해당 ID를 찾을 수 없습니다.")

#         elif choice == '6':
#             save_data(records, JSON_FILENAME)
#             save_datainexcel(records, XL_FILENAME)
#             print(f"엑셀 파일로 저장 완료: {XL_FILENAME}")
#             print("프로그램 종료.")
#             break

#         else:
#             print("잘못된 입력입니다. 다시 선택하세요.")

# if __name__ == "__main__":
#     main()


import json
import os

# ────────────────────────────────────────────
# 예시용 클래스 (기존 RPG 코드와 호환)
# ────────────────────────────────────────────
class Player:
    def __init__(self, name, level, hp, max_hp, basic_damage, inventory=None):
        self.name = name
        self.level = level
        self.hp = hp
        self.max_hp = max_hp
        self.basic_damage = basic_damage
        self.inventory = inventory if inventory is not None else []

class Enemy:
    def __init__(self, name, level, hp, basic_defense):
        self.name = name
        self.level = level
        self.hp = hp
        self.basic_defense = basic_defense

# ────────────────────────────────────────────
# 저장/불러오기 함수
# ────────────────────────────────────────────
SAVE_FILE = "savefile.json"

def save_game(player, enemy, current_stage):
    """현재 플레이어, 적, 스테이지 정보를 저장"""
    state = {
        "player": {
            "name": player.name,
            "level": player.level,
            "hp": player.hp,
            "max_hp": player.max_hp,
            "basic_damage": player.basic_damage,
            "inventory": player.inventory,
        },
        "enemy": {
            "name": enemy.name,
            "level": enemy.level,
            "hp": enemy.hp,
            "basic_defense": enemy.basic_defense,
        },
        "current_stage": current_stage
    }

    with open(SAVE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=4, ensure_ascii=False)
    print(f"✅ 게임이 저장되었습니다! ({SAVE_FILE})")


def load_game():
    """저장된 파일을 불러와 객체로 복원"""
    if not os.path.exists(SAVE_FILE):
        print("⚠ 저장된 파일이 없습니다.")
        return None, None, None

    with open(SAVE_FILE, "r", encoding="utf-8") as f:
        state = json.load(f)

    player_data = state["player"]
    enemy_data = state["enemy"]

    player = Player(**player_data)
    enemy = Enemy(**enemy_data)
    current_stage = state["current_stage"]

    print("✅ 게임이 불러와졌습니다!")
    return player, enemy, current_stage


# ────────────────────────────────────────────
# 실행 예시
# ────────────────────────────────────────────
if __name__ == "__main__":
    # 처음 시작할 때
    player = Player("Showman", 5, 120, 120, 15, ["Potion", "Sword"])
    enemy = Enemy("Goblin", 2, 60, 3)
    current_stage = 1

    # 저장
    save_game(player, enemy, current_stage)

    # 불러오기
    p2, e2, stage2 = load_game()
    print(f"플레이어 이름: {p2.name}, 체력: {p2.hp}/{p2.max_hp}")
    print(f"적 이름: {e2.name}, 체력: {e2.hp}")
    print(f"현재 스테이지: {stage2}")
