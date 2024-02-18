import sqlite3, string, random
from tkinter import *
from tkinter import messagebox, ttk


class Window(Tk):
    def __init__(self, title, geometry):
        super().__init__() 
        self.title(title)
        self.geometry(geometry) 
        self.resizable(False, False)
       
    def logout(self):
        self.destroy()
        WindowAuth("Авторизация", "500x500", 0)
    
    def display_user_info(self):
        full_name, dob, photo_path = self.user_data[4], self.user_data[6], self.user_data[1] 
        if photo_path:
            photo_image = PhotoImage(file=photo_path)
            label_photo = Label(self, image=photo_image)
            label_photo.image = photo_image
            label_photo.pack(pady=50)
        Label(self, text=f"Роль: {self.title()}", font=("Times New Roman", 20)).pack()
        Label(self, text=f"Имя: {full_name}", font=("Times New Roman", 20)).pack()
        Label(self, text=f"Дата рождения: {dob}", font=("Times New Roman", 20)).pack()
        Button(self, text="Выйти", font=("Times New Roman", 20), command=self.logout).pack(pady=20)
    
    def show_data(self, title, table_name):
        data_window = Toplevel(self)
        data_window.title(title)
        data_window.geometry("800x400")
        tree = ttk.Treeview(data_window)
        tree.pack(pady=20, padx=20, expand=True, fill='both')

        connection = sqlite3.connect("lab_database.db")
        cursor = connection.cursor()

        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = [col_info[1] for col_info in cursor.fetchall()]

        tree['columns'] = columns
        tree.column("#0", width=0, stretch=NO)
        
        for col in columns:
            tree.column(col, anchor=W, width=120)
            tree.heading(col, text=col, anchor=W)

        cursor.execute(f"SELECT * FROM {table_name}")
        [tree.insert("", END, values=row) for row in cursor.fetchall()]

        connection.close()

class WindowAuth(Window):
    def __init__(self, title, geometry, lockout_time):
        super().__init__(title, geometry)
        self.failed_attempts = 0
        self.create_widgets()
        self.captcha_frame = None
        if lockout_time > 0:
            self.start_lockout(lockout_time)

    def create_widgets(self):
        Label(self, text="Авторизация", font=("Times New Roman", 30)).pack(pady=50)
        self.user_type_combobox = ttk.Combobox(self, values=["admin", "buh", "lab_is", "lab"], font=("Times New Roman", 20))
        self.user_type_combobox.pack(pady=5)
        Label(self, text="Пароль:", font=("Times New Roman", 20)).pack()
        self.entry_password = Entry(self, show="*", font=("Times New Roman", 20))
        self.entry_password.pack(pady=5)
        self.toggle_password_button = Button(self, text="Показать пароль", font=("Times New Roman", 20), command=self.toggle_password)
        self.toggle_password_button.pack(pady=5)
        self.login_button = Button(self, text="Войти", font=("Times New Roman", 20), command=self.authenticate)
        self.login_button.pack(pady=5)
        self.timer_label = Label(self, text="", font=('Times New Roman', 20))
        self.timer_label.place(x=10, y=10)

    def toggle_password(self):
        if self.entry_password.cget('show') == '*':
            self.entry_password.config(show='')
            self.toggle_password_button.config(text="Скрыть пароль")
        else:
            self.entry_password.config(show='*')
            self.toggle_password_button.config(text="Показать пароль")

    def authenticate(self):
        user_type = self.user_type_combobox.get()
        password = self.entry_password.get()

        if self.failed_attempts >= 1:
            entered_captcha = self.captcha_entry.get().upper()
            if entered_captcha != self.plain_captcha_code:
                messagebox.showerror("Ошибка", "Неверный код CAPTCHA")
                self.start_lockout(10)
                self.create_captcha()
                return

        user_data = self.check_credentials(user_type, password)
        if user_data:
            self.failed_attempts = 0
            self.destroy()
            self.open_user_window(user_data, user_type)
        else:
            self.failed_attempts += 1
            messagebox.showerror("Ошибка", "Неверный логин или пароль")
            if self.failed_attempts >= 1:
                self.create_captcha()
            
    def check_credentials(self, username, password):
        connection = sqlite3.connect("lab_database.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE login=? AND password=?", (username, password))
        return cursor.fetchone()
                
    def open_user_window(self, user_data, user_type):
        user_type = user_type
        if user_type == "admin":
            WindowAdmin("Администратор", "500x500", user_data)
        elif user_type == "buh":
            WindowBuh("Бухгалтер", "500x500", user_data)
        elif user_type == "lab_is":
            WindowLabIS("Лаборант-Исследователь", "500x800", user_data)
        elif user_type == "lab":
            WindowLab("Лаборант", "500x500", user_data)

    def start_lockout(self, lockout_time):
        self.lockout_time = lockout_time
        self.update_timer()
        self.login_button['state'] = 'disabled'

    def update_timer(self):
        if self.lockout_time > 0:
            self.timer_label.config(text=f"Блокировка: {self.lockout_time}s")
            self.lockout_time -= 1
            self.after(1000, self.update_timer)
        else:
            self.login_button['state'] = 'normal'
            self.timer_label.config(text="")

    def create_captcha(self):
        if self.captcha_frame:
            self.captcha_frame.destroy()
        self.captcha_frame = Frame(self)
        self.captcha_frame.pack(pady=10)

        plain_captcha_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        display_captcha_code = '\u0336'.join(plain_captcha_code) + '\u0336'

        captcha_label = Label(self.captcha_frame, text=f"Код: {display_captcha_code}", font=("Times New Roman", 20))
        captcha_label.pack(side=LEFT)

        self.captcha_entry = Entry(self.captcha_frame, width=6, font=("Times New Roman", 20))
        self.captcha_entry.pack(side=LEFT)

        refresh_captcha_button = Button(self.captcha_frame, text="Обновить", command=self.create_captcha)
        refresh_captcha_button.pack(side=LEFT)

        self.plain_captcha_code = plain_captcha_code

class WindowAdmin(Window):
    def __init__(self, title, geometry, user_data):
        super().__init__(title, geometry)
        self.user_data = user_data
        self.display_user_info()

class WindowBuh(Window):
    def __init__(self, title, geometry, user_data):
        super().__init__(title, geometry)
        self.user_data = user_data
        self.display_user_info()
        Button(self, text="Показать счета-фактуры", command=lambda: self.show_data("Счета-фактуры", "invoices")).pack(pady=10)

class WindowWithTimer(Window):
    def __init__(self, title, geometry, user_data, timer_duration=305):
        super().__init__(title, geometry)
        self.user_data = user_data
        self.display_user_info()

        self.remaining_time = timer_duration
        self.timer_label = Label(self, text=self.format_time(self.remaining_time), font=("Times New Roman", 20))
        self.timer_label.place(x=10, y=10)

        self.count = 0
        self.update_timer()
    
    def format_time(self, seconds):
        mins, secs = divmod(seconds, 60)
        return f"{mins:02d}:{secs:02d}"

    def update_timer(self):
        if self.remaining_time > 0:
            self.timer_label.config(text=self.format_time(self.remaining_time))
            self.remaining_time -= 1
            self.after(1000, self.update_timer)
        else:
            # Автовыход и блокировка входа на 60 сек
            self.destroy()
            WindowAuth("Авторизация", "500x500", 60)
        
        if self.remaining_time == 300:
            messagebox.showwarning("Предупреждение", "До автоматического выхода осталось 5 минут!")

class WindowLabIS(WindowWithTimer):
    def __init__(self, title, geometry, user_data):
        super().__init__(title, geometry, user_data)
        self.create_order_widgets()

    def create_order_widgets(self):
        Label(self, text="Создать заказ", font=("Times New Roman", 20)).pack(pady=10)
        Label(self, text="ID пользователя:", font=("Times New Roman", 20)).pack()
        self.user_id_entry = Entry(self, width=20, font=("Times New Roman", 20))
        self.user_id_entry.pack(pady=5)

        Button(self, text="Создать заказ в анализатор", command=self.create_order).pack(pady=10)
        Button(self, text="Просмотр заказов", command=lambda: self.show_data("Заказы", "orders")).pack(pady=10)

    # Добавление заказа/анализатор
    def create_order(self):
        user_id = self.user_id_entry.get()
        if user_id:
            with sqlite3.connect("lab_database.db") as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO orders (user_id, creation_date, status) VALUES (?, datetime('now'), 'В работе')", (user_id,))
                conn.commit()
                messagebox.showinfo("Успех", "Заказ создан")
        else:
            messagebox.showwarning("Предупреждение", "ID пользователя не указан")

class WindowLab(WindowWithTimer):
    def __init__(self, title, geometry, user_data):
        super().__init__(title, geometry, user_data)
        self.show_users_button = Button(self, text="Пользователи", command=lambda: self.show_data("Пользователи", "users"))
        self.show_users_button.pack(pady=10)

window = WindowAuth("Авторизация", "500x500", 0)
window.mainloop()