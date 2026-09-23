import shutil



def alert_box(alert_text):
    width, height = shutil.get_terminal_size()
    width = width-2
    space_left_after_text = width - len(str(alert_text)) - 1

    print("┏", end="")
    print("━"*width, end="")
    print("┓")
    print("┃ " + alert_text + " " * space_left_after_text + "┃")




alert_box("selamlar")
    
    

