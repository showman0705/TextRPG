import json
from curses import wrapper
import time

save_data = []

def save_game_data():
    '''게임 데이터 저장 함수'''
    with open('C:\\Users\\showm\\TextRPG\\savefile.json', 'r') as f:
        save_data = json.load(f)
        save_data['save'] += 1
    with open('C:\\Users\\showm\\TextRPG\\savefile.json', 'w') as f:
        json.dump(save_data, f, indent= 4, ensure_ascii=False)

def new_save(i):
    '''새 게임'''
    save_json = {
    "save" : 1 
}
    for save in range(4):
        save_file = f"save{save}"
        
    with open(save_data[], 'w') as f:
        json.dump(save_json, f, indent = 4, ensure_ascii=False)
    

def continue_game(stdscr, save, current, chapter):
    '''불러오기'''
    if save == current:
        type(stdscr, chapter)
        wrapper(save_game_data)
        time.sleep(1)