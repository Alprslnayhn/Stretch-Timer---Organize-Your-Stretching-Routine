import customtkinter as ctk
import time
import pygame  # Ses çalmak için pygame modülünü import et

# Pygame sesini başlat
pygame.mixer.init()

# Geri sayım fonksiyonu
def countdown_timer(seconds, label, message_label, set_number, direction):
    while seconds >= 0:
        mins, secs = divmod(seconds, 60)
        time_format = f"{mins:02}:{secs:02}"
        label.configure(text=f"Time Left: {time_format}")
        message_label.configure(text=f"Set {set_number}: {direction} Stretching")
        app.update()
        time.sleep(1)
        seconds -= 1

    # Süre bitince ses çalma
    pygame.mixer.Sound("beep.wav").play()  # "beep.wav" ses dosyasını çalar

# Zamanlayıcı başlatma fonksiyonu
def start_timer():
    try:
        total_sets = int(sets_entry.get())
        stretch_duration = int(stretch_entry.get())
        rest_duration = int(rest_entry.get())
        
        if total_sets <= 0 or stretch_duration <= 0 or rest_duration < 0:
            raise ValueError
        
        for set_number in range(1, total_sets + 1):
            # Sağ tarafa esneme
            countdown_timer(stretch_duration, timer_label, message_label, set_number, "Right")
            # Dinlenme
            if set_number != total_sets:  # Son set sonrası dinlenme olmaz
                countdown_timer(rest_duration, timer_label, message_label, set_number, "Rest")
            # Sol tarafa esneme
            countdown_timer(stretch_duration, timer_label, message_label, set_number, "Left")
            
        messagebox.showinfo("Done!", "All sets completed!")
        message_label.configure(text="Congratulations!")
        timer_label.configure(text="00:00")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid positive numbers!")

# Modern GUI oluşturma
ctk.set_appearance_mode("light")  # "dark" veya "light"
ctk.set_default_color_theme("blue")  # "dark-blue", "green", "blue"

app = ctk.CTk()
app.title("Stretch Timer")
app.geometry("500x400")

# Başlık
title_label = ctk.CTkLabel(app, text="Stretch Timer", font=("Arial", 24, "bold"))
title_label.pack(pady=20)

# Giriş alanları
frame = ctk.CTkFrame(app)
frame.pack(pady=10)

ctk.CTkLabel(frame, text="Number of Sets:", font=("Arial", 14)).grid(row=0, column=0, padx=10, pady=5, sticky="w")
sets_entry = ctk.CTkEntry(frame, width=150)
sets_entry.grid(row=0, column=1, pady=5)

ctk.CTkLabel(frame, text="Stretch Duration (sec):", font=("Arial", 14)).grid(row=1, column=0, padx=10, pady=5, sticky="w")
stretch_entry = ctk.CTkEntry(frame, width=150)
stretch_entry.grid(row=1, column=1, pady=5)

ctk.CTkLabel(frame, text="Rest Duration (sec):", font=("Arial", 14)).grid(row=2, column=0, padx=10, pady=5, sticky="w")
rest_entry = ctk.CTkEntry(frame, width=150)
rest_entry.grid(row=2, column=1, pady=5)

# Mesaj ve geri sayım alanları
message_label = ctk.CTkLabel(app, text="Welcome! Enter your preferences above.", font=("Arial", 14), text_color="green")
message_label.pack(pady=10)

timer_label = ctk.CTkLabel(app, text="00:00", font=("Arial", 30, "bold"), text_color="red")
timer_label.pack(pady=10)

# Başlat düğmesi
start_button = ctk.CTkButton(app, text="Start Timer", font=("Arial", 16), command=start_timer, fg_color="green")
start_button.pack(pady=20)

# Ana döngü
app.mainloop()
