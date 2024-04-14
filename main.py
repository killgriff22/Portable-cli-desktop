from functions import *
last_message = ""
while True:
    screen.fill(" ")
    screen.blit(last_message, (0, 0))
    event = MultiTerm.window.get_event()
    if event:
        if event.type == MultiTerm.asciimaticsEvent.MouseEvent:
            last_message = "Mouse event at: " + str(event)
    screen.draw()