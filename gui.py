from tkinter import *

from launcher_main_tools import main_edit_file, main_change_position
from Activity.mouse_runer import run
from constants import SEO_TITLE_LOW_LIMIT, SEO_TITLE_UP_LIMIT
from constants import SEO_DESC_LOW_LIMIT, SEO_DESC_UP_LIMIT


class GuiWorkMix(Frame):
    def __init__(self, master=None):
        self.text = ""
        self.len_with_no_space = 0
        self.margin_text = None

        super().__init__(master)
        self.master = master
        self.master.title("Work Mix")
        self.master.geometry("465x350+300+400")
        self.create_widgets()

    def create_widgets(self):
        Button(self.master, text="Run", command=run).grid(column=1, row=0)

        Label(self.master, text="Put your text below").grid(column=1, row=1)

        self.margin_text = Entry(self.master, width=50)
        self.margin_text.grid(column=1, row=2)
        self.margin_text.focus()

        Button(self.master, text="Count characters!", command=self.character_counter).grid(column=1, row=3)

        Button(self.master, text="Translate files", command=main_edit_file).grid(column=1, row=4)

        Button(self.master, text="Change files position", command=main_change_position).grid(column=1, row=5)

    def character_counter(self):
        if not self.margin_text.get():
            return 0

        text_without_space = self.margin_text.get().replace(" ", "")
        self.len_with_no_space = len(text_without_space)

        Label(self.master, text="Characters without space: {0}".format(self.len_with_no_space)).grid(column=1, row=6)

        self.seo_title_limit()
        self.seo_description_limit()

    def seo_title_limit(self):
        if self.len_with_no_space in range(SEO_TITLE_LOW_LIMIT, SEO_TITLE_UP_LIMIT):
            Label(self.master, text="WITHIN limit for SEO Title", foreground="green").grid(column=1, row=7)
        else:
            Label(self.master, text="WITHIN NO limit for SEO Title!", foreground="red").grid(column=1, row=7)

        Label(self.master, text="Title character limit: {}-{}".format(SEO_TITLE_LOW_LIMIT,
                                                                      SEO_TITLE_UP_LIMIT)).grid(column=1, row=8)

    def seo_description_limit(self):
        if self.len_with_no_space in range(SEO_DESC_LOW_LIMIT, SEO_DESC_UP_LIMIT):
            Label(self.master, text="WITHIN limit for SEO Description", foreground="green").grid(column=1, row=9)
        else:
            Label(self.master, text="WITHIN NO limit for SEO Description!", foreground="red").grid(column=1, row=9)

        Label(self.master, text="Description character limit: {}-{}".format(SEO_DESC_LOW_LIMIT,
                                                                            SEO_DESC_UP_LIMIT)).grid(column=1, row=11)


if __name__ == "__main__":
    root = Tk()
    gui = GuiWorkMix(master=root)
    gui.mainloop()
