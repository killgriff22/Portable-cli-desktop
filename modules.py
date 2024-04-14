import MultiTerm
display_size = MultiTerm.os.get_terminal_size()
screen = MultiTerm.canvas(display_size)
cluster = MultiTerm.cluster([screen])