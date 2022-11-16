from DrawingPanel import *
import datetime


def main():
    create_panel()

    while True:
        panel.set_title("ANALOG CLOCK")
        panel.draw_oval(100, 100, 300, 300, color="White")
        panel.draw_string("saat : Blue", 20, 60, color="Blue", font=str)
        panel.draw_string("dakika : Red", 20, 80, color="Red", font=str)
        panel.draw_string("saniye: Yellow", 20, 100, color="Yellow", font=str)
        panel.draw_string("12", 240, 80, "White", font="")
        panel.draw_string("3", 410, 230, "White", font="")
        panel.draw_string("6", 250, 410, "White", font="")
        panel.draw_string("9", 90, 230, "White", font="")

        panel.fill_rect(248, 95, 5, 10, color="White")
        panel.fill_rect(248, 395, 5, 10, color="White")
        panel.fill_rect(95, 250, 10, 5, color="White")
        panel.fill_rect(395, 250, 10, 5, color="White")
        saniye = datetime.datetime.now().second
        dakika = datetime.datetime.now().minute
        saat = datetime.datetime.now().hour
        birim = str(saat) + " : " + str(dakika) + " : " + str(saniye)
        panel.draw_string(birim, 300, 50, "white")

        if saat <= 15:
            panel.draw_line(250, 250, 250 + 10 * saat, 100 + 10 * saat, color="Blue")
        elif saat <= 30:
            x = saat - 15
            panel.draw_line(250, 250, 400 - x * 10, 100 + saniye * 10, color="Blue")
        elif saat <= 45:
            x = saat - 15
            y = saat - 30
            panel.draw_line(250, 250, 400 - x * 10, 400 - y * 10, color="Blue")
        else:
            x = saat - 45
            y = saat - 45
            panel.draw_line(250, 250, 100 + x * 10 - 10, 250 - y * 10, color="Blue")
        if dakika <= 15:
            panel.draw_line(250, 250, 250 + 10 * dakika, 100 + 10 * dakika, color="Red")
        elif dakika <= 30:
            x = dakika - 15
            panel.draw_line(250, 250, 400 - x * 10, 100 + saniye * 10, color="Red")
        elif dakika <= 45:
            x = dakika - 15
            y = dakika - 30
            panel.draw_line(250, 250, 400 - x * 10, 400 - y * 10, color="Red")
        else:
            x = dakika - 45
            y = dakika - 45
            panel.draw_line(250, 250, 100 + x * 10 - 10, 250 - y * 10, color="Red")
        if saniye <= 15:
            panel.draw_line(
                250, 250, 250 + 10 * saniye, 100 + 10 * saniye, color="Yellow"
            )
        elif saniye <= 30:
            x = saniye - 15
            panel.draw_line(250, 250, 400 - x * 10, 100 + saniye * 10, color="Yellow")
        elif saniye <= 45:
            x = saniye - 15
            y = saniye - 30
            panel.draw_line(250, 250, 400 - x * 10, 400 - y * 10, color="Yellow")
        else:
            x = saniye - 45
            y = saniye - 45
            panel.draw_line(250, 250, 100 + x * 10 - 10, 250 - y * 10, color="Yellow")
        panel.sleep(900)
        panel.clear()


def create_panel():
    global panel
    panel = DrawingPanel(550, 550, background="black")


main()
