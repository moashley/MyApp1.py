from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.font_definitions import theme_font_styles
from kivy.core.window import Window

Window.size = (300, 500)

screen_helper = """
ScreenManager: 
    MenuScreen:
    OpenedTags:

<MenuScreen>:
    name: 'menu'
    MDLabel:
        text: "BROWSE A SECTION"
        theme_text_color: "Primary"
        pos_hint: {'center_x':0.7, 'center_y':0.88}
        font_style: "H6"      
    MDRectangleFlatButton:
        text: 'Selling'
        pos_hint: {'center_x':0.3, 'center_y':0.7}
        font_size: (root.width**2 + root.height**2)/18**4
        size_hint: 0.3, 0.15
        on_release: 
            root.manager.current = 'openedtags'
            root.manager.transition.direction = 'left'

    MDRectangleFlatButton:
        text: 'School Events'
        pos_hint: {'center_x':0.3,'center_y':0.5}
        font_size: (root.width**2 + root.height**2)/18**4
        size_hint: 0.3, 0.15
        on_release: 
            root.manager.current = 'openedtags'
            root.manager.transition.direction = 'left'
    MDRectangleFlatButton:
        text: 'Clubs'
        pos_hint: {'center_x':0.3,'center_y':0.3}
        font_size: (root.width**2 + root.height**2)/18**4
        size_hint: 0.3, 0.15
        on_release: 
            root.manager.current = 'openedtags'
            root.manager.transition.direction = 'left'
    MDRectangleFlatButton:
        text: 'Volunteer'
        pos_hint: {'center_x':0.7,'center_y':0.7}
        font_size: (root.width**2 + root.height**2)/18**4
        size_hint: 0.3, 0.15
        on_release: 
            root.manager.current = 'openedtags'
            root.manager.transition.direction = 'left'
    MDRectangleFlatButton:
        text: 'Competitions'
        pos_hint: {'center_x':0.7,'center_y':0.5}
        font_size: (root.width**2 + root.height**2)/18**4
        size_hint: 0.3, 0.15
        on_release: 
            root.manager.current = 'openedtags'
            root.manager.transition.direction = 'left'
    MDRectangleFlatButton:
        text: 'Sports'
        pos_hint: {'center_x':0.7,'center_y':0.3}
        font_size: (root.width**2 + root.height**2)/18**4
        size_hint: 0.3, 0.15
        on_release: 
            root.manager.current = 'openedtags'
            root.manager.transition.direction = 'left'
    Screen:
    BoxLayout:
        MDBottomAppBar:
            MDToolbar:
                icon: 'plus'
                type: 'bottom'
                left_action_items: [["home", lambda x: navigate_menu()], ["magnify", lambda x: navigate_menu()]]
                right_action_items: [["message", lambda x: navigate_menu()], ["account", lambda x: navigate_menu()]]
                on_action_button: navigate_menu()

<OpenedTags>:
    name: "openedtags"
    MDRectangleFlatButton:
        text: '<Back'
        pos_hint: {'center_x':0.5,'center_y':0.6}
        on_release: 
            root.manager.current = 'menu'
            root.manager.transition.direction = 'right'
    Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Search:'
            left_action_items: [["menu", lambda x: app.navigation_draw()]]
            right_action_items: [["dots-vertical", lambda x: app.callback()]]
            elevation:5
                       
        MDLabel:
            text: ''
            halign: 'center'
    
    Screen:
    BoxLayout:
        MDBottomAppBar:
            MDToolbar:
                icon: 'plus'
                type: 'bottom'
                left_action_items: [["home", lambda x: navigate_menu()], ["magnify", lambda x: navigate_menu()]]
                right_action_items: [["message", lambda x: navigate_menu()], ["account", lambda x: navigate_menu()]]
                on_action_button: navigate_menu()
 
"""

class MenuScreen(Screen):
    pass
class OpenedTags(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(OpenedTags(name='openedtags'))


class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen


DemoApp().run()