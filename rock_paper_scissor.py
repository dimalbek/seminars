from random import shuffle
while True:
    try:
        red = "\033[91m"
        yellow = "\033[93m"
        green = "\033[92m"
        reset = "\033[0m"  # Reset color to default
        inp = input("""Vyberite
                    1 Kamen
                    2 Nojnicy
                    3 Bumaga
                    """)
        inp = int(inp)
        lst = [1, 2, 3]
        if inp not in lst:
            raise Exception
        shuffle(lst)
        bot = lst[0]
        win = ''
        if inp == bot:
            win = 'Nichya'
            print(f"{yellow}{win}.{reset}")
        if inp == 1:
            if bot == 2:
                win = 'Ty pobedil'
            if bot == 3:
                win = "Bot pobedil"
        elif inp == 2:
            if bot == 3:
                win = 'Ty pobedil'
            if bot == 1:
                win = 'Bot pobedil'
        elif inp == 3:
            if bot == 1:
                win = 'Ty pobedil'
            if bot == 2:
                win = 'Bot pobedil'
        if win == 'Ty pobedil':
            print(f"{green}{win}.{reset}")
        elif win == 'Bot pobedil':
            print(f"{red}{win}.{reset}")
        print('Go eshe? (y/n)')
        b = True
        while True:
            inp = input()
            if inp in ('y', 'Y'):
                b = True
                break
            if inp in ('n', 'N'):
                b = False
                break
            print('"y" or "n" only!!!!')
        if b is False:
            break
    except Exception:
        print("vyberi 1 ili 2 ili 3!!!")
