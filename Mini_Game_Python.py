import curses
import random
import time

def main_menu(stdscr):
    curses.curs_set(0)  # Nasconde il cursore

    # Imposta le dimensioni della finestra del menu
    menu_height = 5
    menu_width = 30
    menu_y = int((curses.LINES - menu_height) / 2)
    menu_x = int((curses.COLS - menu_width) / 2)

    # Crea la finestra del menu
    menu_win = curses.newwin(menu_height, menu_width, menu_y, menu_x)

    # Disegna il titolo del menu
    menu_win.addstr(1, 5, "MENU DI GIOCO")

    # Disegna le opzioni del menu
    menu_win.addstr(2, 2, "1. Inizia il gioco")
    menu_win.addstr(3, 2, "2. Mostra le istruzioni")
    menu_win.addstr(4, 2, "3. Esci dal gioco")

    # Aggiorna la finestra del menu
    menu_win.refresh()

    # Leggi l'input dell'utente
    key = 0
    while key not in [ord('1'), ord('2'), ord('3')]:
        key = stdscr.getch()

    # Chiudi la finestra del menu
    menu_win.clear()
    menu_win.refresh()
    curses.curs_set(1)  # Riporta il cursore

    # Aggiorna lo stato del gioco in base all'input
    if key == ord('1'):
        # Inizia il gioco
        game(stdscr)
    elif key == ord('2'):
        # Mostra le istruzioni
        game_area = curses.newwin(curses.LINES - 4, curses.COLS - 4, 2, 2)
        game_area.border()
        game_area.addstr(2, 2, "Istruzioni:")
        game_area.addstr(4, 4, "Il tuo obiettivo è evitare gli ostacoli che cadono dall'alto")
        game_area.addstr(5, 4, "Muovi il giocatore a sinistra o a destra usando le frecce direzionali")
        game_area.addstr(7, 4, "Premi qualsiasi tasto per tornare al menu")
        game_area.refresh()
        stdscr.getch()
    elif key == ord('3'):
        # Esci dal gioco
        exit()

def game(stdscr):
    # Imposta le dimensioni dell'area di gioco
    game_area_height = curses.LINES - 4
    game_area_width = curses.COLS - 4
    game_area_y = 2
    game_area_x = 2

    # Crea l'area di gioco
    game_area = curses.newwin(game_area_height, game_area_width, game_area_y, game_area_x)
    game_area.keypad(True)  # Abilita l'input da tastiera
    game_area.timeout(100)  # Imposta il timeout di lettura dell'input

    # Disegna il bordo dell'area di gioco
    game_area.border()

    # Inizializza le variabili del gioco
    player_char = "☻"
    player_x = int(game_area_width / 2)
    player_y = game_area_height - 2
    obstacle_char = "█"
