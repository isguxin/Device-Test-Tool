import ttkbootstrap as t
from ttkbootstrap import DANGER, WARNING, DARK

root = t.Window(
    title="Device Test Tool V2022.08",
    size=(1200, 900),
    resizable=(False, False),
    alpha=1.0
)

display_top = t.Frame(root, style=DANGER)
display_top.place(x=10, width=1180, y=10, height=60)

display_lower_left = t.Frame(root, style=WARNING)
display_lower_left.place(x=10, width=710, y=70, height=820)

display_lower_right = t.Frame(root, style=DARK)
display_lower_right.place(x=720, width=470, y=70, height=820)

root.mainloop()
