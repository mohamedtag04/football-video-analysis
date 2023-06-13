from tkinter import *
import tools


def btn_clicked():
    value = entry.get()
    tools.countInCrops(int(value))

def startWindow():
    window = Tk()

    window.geometry("1268x836")
    window.configure(bg = "#343a72")
    canvas = Canvas(
        window,
        bg = "#343a72",
        height = 836,
        width = 1268,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"gui/background.png")
    background = canvas.create_image(
        573.5, 427.5,
        image=background_img)

    img0 = PhotoImage(file = f"gui/img0.png")
    get_num_of_players = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")

    get_num_of_players.place(
        x = 649, y = 700,
        width = 240,
        height = 49)

    img1 = PhotoImage(file = f"gui/img1.png")
    players_mask = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = tools.playersVid,
        relief = "flat")

    players_mask.place(
        x = 629, y = 162,
        width = 280,
        height = 172)

    img2 = PhotoImage(file = f"gui/img2.png")
    players_ball_mask = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = tools.playersBallVid
        ,
        relief = "flat")

    players_ball_mask.place(
        x = 629, y = 373,
        width = 280,
        height = 178)

    img3 = PhotoImage(file = f"gui/img3.png")
    combined_mask = Button(
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = tools.combVid,
        relief = "flat")

    combined_mask.place(
        x = 286, y = 595,
        width = 277,
        height = 154)

    img4 = PhotoImage(file = f"gui/img4.png")
    og = Button(
        image = img4,
        borderwidth = 0,
        highlightthickness = 0,
        command = tools.originalVid,
        relief = "flat")

    og.place(
        x = 286, y = 418,
        width = 277,
        height = 168)

    entry0_img = PhotoImage(file = f"gui/img_textBox0.png")
    entry0_bg = canvas.create_image(
        768.5, 674.5,
        image = entry0_img)

    global entry
    entry = Entry(
        bd = 0,
        bg = "#ce3524",
        highlightthickness = 0)

    entry.place(
        x = 646, y = 657,
        width = 245,
        height = 33)

    window.resizable(False, False)
    window.mainloop()
