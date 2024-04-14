import MultiTerm
display_size = MultiTerm.os.get_terminal_size()
screen = MultiTerm.canvas(display_size)
screen.clear()
cluster = MultiTerm.cluster([screen])