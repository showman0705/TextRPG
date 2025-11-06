# # import curses

# # def move_curs(stdscr):
# #     stdscr.keypad(True)
# #     curses.start_color()
# #     curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_YELLOW)  # 강조 색상
# #     stdscr.clear()
# #     # 화면에 출력할 텍스트들 (y, x, 텍스트)
# #     texts = [
# #         (5, 10, "Hello World"),
# #         (7, 20, "Python"),
# #         (10, 5, "Curses Library"),
# #         (12, 30, "Text"),
# #         (15, 15, "Programming"),
# #         (8, 50, "Code"),
# #     ]
    
# #     # 초기 커서 위치
# #     y, x = 10, 10
    
# #     while True:
# #         stdscr.clear()
        
# #         # 모든 텍스트 출력
# #         for text_y, text_x, text in texts:
# #             # 커서가 이 텍스트 위에 있는지 확인
# #             if text_y == y and text_x <= x < text_x + len(text):
# #                 # 강조 표시
# #                 stdscr.addstr(text_y, text_x, "<" + text + ">", curses.A_BOLD)
# #             else:
# #                 # 일반 표시
# #                 stdscr.addstr(text_y, text_x, text)
        
# #         # 현재 위치에 커서 표시
        
        
# #         # 정보 표시
# #         stdscr.addstr(0, 0, f"위치: ({y}, {x}) | 화살표로 이동 | q를 눌러 종료")
        
# #         # 현재 커서 위치의 텍스트 정보
# #         current_text = None
# #         for text_y, text_x, text in texts:
# #             if text_y == y and text_x <= x < text_x + len(text):
# #                 current_text = text
# #                 break
        
# #         if current_text:
# #             stdscr.addstr(1, 0, f"현재 텍스트: '{current_text}'")
# #         else:
# #             stdscr.addstr(1, 0, f"현재 텍스트: (없음)      ")
        
# #         stdscr.refresh()
        
# #         key = stdscr.getch()
        
# #         # 화면 크기 확인
# #         max_y, max_x = stdscr.getmaxyx()
        
# #         if key == curses.KEY_UP and y > 0:
# #             y -= 1
# #         elif key == curses.KEY_DOWN and y < max_y - 1:
# #             y += 1
# #         elif key == curses.KEY_LEFT and x > 0:
# #             x -= 1
# #         elif key == curses.KEY_RIGHT and x < max_x - 1:
# #             x += 1
# #         elif key == ord('q'):
# #             break

# # curses.wrapper(move_curs)

# import curses

# def main(stdscr):
#     curses.curs_set(1)        # 커서 보이기
#     stdscr.clear()
#     stdscr.refresh()

#     # 새 윈도우 생성 (10줄 높이, 30칸 너비, 화면 좌상단에서 y=5, x=10 위치)
#     win = curses.newwin(10, 30, 5, 10)
#     win.box()                  # 테두리 표시
#     win.keypad(True)           # 방향키 입력 허용
#     win.refresh()

#     # 커서의 초기 위치
#     y, x = 1, 1
#     win.move(y, x)

#     while True:
#         key = win.getch()      # 입력 받기

#         if key == ord('q'):    # q 누르면 종료
#             break

#         # 방향키 처리
#         elif key == curses.KEY_UP:
#             y = max(1, y - 1)
#         elif key == curses.KEY_DOWN:
#             y = min(8, y + 1)
#         elif key == curses.KEY_LEFT:
#             x = max(1, x - 1)
#         elif key == curses.KEY_RIGHT:
#             x = min(28, x + 1)

#         # 화면 갱신
#         win.clear()
#         win.box()
#         win.addstr(y, x, '⬤')  # 현재 커서 위치에 점 표시
#         win.move(y, x)
#         win.refresh()

# curses.wrapper(main)

