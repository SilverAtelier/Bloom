from kivy.properties import ObjectProperty
from kivymd.app import MDApp
from kivymd.uix.scrollview import MDScrollView
from kivy.uix.screenmanager import ScreenManager, Screen
import connector as con


class LoginScreen(Screen):
    username = ObjectProperty()
    password = ObjectProperty()

    def verify_credentials(self):
        if con.login_user(self.username.text, self.password.text):
            # Login successful, navigate to main screen
            self.manager.current = "main"
        if con.login_user(self.username.text, self.password.text) == 'wrong password':
            self.password.text = ""
            self.password.text = ""
            self.password.focus = True
            self.password.error = True
        else:
            # Login failed, show error message
            self.username.text = ""
            self.username.text = ""
            self.username.focus = True
            self.username.error = True


class SignupScreen(Screen):
    username = ObjectProperty()
    password = ObjectProperty()
    confirm = ObjectProperty()

    def verify_pass(self):

        if self.password.text == self.confirm.text:
            con.register_user(self.username.text, self.password.text)
            if con.register_user:
                self.manager.current = "login"
        else:
            # output passwords don't match
            self.confirm.text = ""
            self.confirm.focus = True
            self.password.focus = True
            self.confirm.error = True


class NewMessageScreen(Screen):
    recipient = ObjectProperty()
    subject = ObjectProperty()
    message = ObjectProperty()

    def send_message(self):
        if self.recipient.text.strip() and self.subject.text.strip() and self.message.text.strip():
            print('message sent', self.recipient.text, self.message.text)
        else:
            print('not sent')


class NavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()


class MainScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)


class BloomApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(MainScreen(name="main"))
        sm.add_widget(SignupScreen(name="signup"))
        sm.add_widget(NewMessageScreen(name="new_message_screen"))

        return sm

    def switch_to_main_screen(self):
        self.root.current = "main"

    def switch_to_newchat_screen(self):
        self.root.current = "new_message_screen"

    def switch_to_login_screen(self):
        self.root.current = "login"

    def switch_to_signup_screen(self):
        self.root.current = "signup"


if __name__ == "__main__":
    BloomApp().run()
