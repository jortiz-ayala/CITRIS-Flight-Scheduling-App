from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp

screen_helper = """
ScreenManager:
    MenuScreen:
    ProfileScreen:
    PricingScreen:
    ScheduleScreenMS:
    ScheduleScreenMD:
    ScheduleScreenMB:
    PurchasingScreen:
    ConfirmationScreen:
    UpdatesScreen:
    
    
<MenuScreen>
    name: 'menu'
    MDRectangleFlatButton:
        text: 'Profile'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_press: root.manager.current = 'profile'

<ProfileScreen>
    name: 'profile'
    MDLabel:
        text: 'Welcome'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'menu'
    MDRectangleFlatButton:
        text: 'Forward'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_press: root.manager.current = 'pricing'

<PricingScreen>
    name: 'pricing'
    MDLabel:
        text: 'Pricing for each ride with a starting point at UC Merced (Round Trip):'
        pos_hint: {'center_x': 0.5, 'center_y': 0.95}
    MDLabel:
        text: 'Destination - Price:'
        pos_hint: {'center_x': 0.5, 'center_y': 0.88}
    MDLabel:
        text: 'UC Santa Scruz - Student/Faculty($10),   Non-Student ($15)'
        pos_hint: {'center_x': 0.5, 'center_y': 0.81}
    MDLabel:
        text: 'UC Davis - Student/Faculty($9),   Non-Student ($14)'
        pos_hint: {'center_x': 0.5, 'center_y': 0.74}
    MDLabel:
        text: 'UC Berkeley - Student/Faculty($10),   Non-Student ($15)'
        pos_hint: {'center_x': 0.5, 'center_y': 0.67}
    MDLabel:
        text: 'Select Ticket Option:'
        pos_hint: {'center_x': 0.5, 'center_y': 0.55}
    MDRectangleFlatButton:
        text: 'UC Merced - UC Santa Cruz'
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        on_press: root.manager.current = 'SchedulesMS'
    MDRectangleFlatButton:
        text: 'UC Merced - UC Davis'
        pos_hint: {'center_x': 0.5, 'center_y': 0.42}
        on_press: root.manager.current = 'SchedulesMD'
    MDRectangleFlatButton:
        text: 'UC Merced - UC Berkeley'
        pos_hint: {'center_x': 0.5, 'center_y': 0.34}
        on_press: root.manager.current = 'SchedulesMB'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'profile'

<ScheduleScreenMS>
    name: 'SchedulesMS'
    MDLabel:
        text: 'Available Schedules for UC Merced - UC Santa Cruz round trip:'
        pos_hint: {'center_x': 0.5, 'center_y': 0.95}
    MDLabel:
        text: 'Date, Departure Time, ETA, Return Time, Route Number:'
        pos_hint: {'center_x': 0.5, 'center_y': 0.88}
    MDRectangleFlatButton:
        text: 'Date, 12:00pm, 12:42pm, 4:00pm, 123456'
        pos_hint: {'center_x': 0.2, 'center_y': 0.81}
        on_press: root.manager.current = 'purchasing'
    MDRectangleFlatButton:
        text: 'Date, 12:00pm, 12:42pm, 4:00pm, 123456'
        pos_hint: {'center_x': 0.2, 'center_y': 0.74}
        on_press: root.manager.current = 'purchasing'
    MDRectangleFlatButton:
        text: 'Date, 12:00pm, 12:42pm, 4:00pm, 123456'
        pos_hint: {'center_x': 0.2, 'center_y': 0.67}
        on_press: root.manager.current = 'purchasing'
    MDRectangleFlatButton:
        text: 'Date, 12:00pm, 12:42pm, 4:00pm, 123456'
        pos_hint: {'center_x': 0.2, 'center_y': 0.60}
        on_press: root.manager.current = 'purchasing'
    MDRectangleFlatButton:
        text: 'Date, 12:00pm, 12:42pm, 4:00pm, 123456'
        pos_hint: {'center_x': 0.2, 'center_y': 0.53}
        on_press: root.manager.current = 'purchasing'
    MDRectangleFlatButton:
        text: 'Date, 12:00pm, 12:42pm, 4:00pm, 123456'
        pos_hint: {'center_x': 0.2, 'center_y': 0.46}
        on_press: root.manager.current = 'purchasing'
    MDRectangleFlatButton:
        text: 'Date, 12:00pm, 12:42pm, 4:00pm, 123456'
        pos_hint: {'center_x': 0.2, 'center_y': 0.39}
        on_press: root.manager.current = 'purchasing'
    MDRectangleFlatButton:
        text: 'Date, 12:00pm, 12:42pm, 4:00pm, 123456'
        pos_hint: {'center_x': 0.2, 'center_y': 0.32}
        on_press: root.manager.current = 'purchasing'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'pricing'

<ScheduleScreenMD>
    name: 'SchedulesMD'
    MDLabel:
        text: 'Available Schedules for UC Merced - UC Davis round trip:'
        pos_hint: {'center_x': 0.5, 'center_y': 0.95}
    MDLabel:
        text: 'Date, Departure Time, ETA, Return Time, Route Number:'
        pos_hint: {'center_x': 0.5, 'center_y': 0.88}
    MDRectangleFlatButton:
        text: 'Date, 12:00pm, 12:42pm, 4:00pm, 123456'
        pos_hint: {'center_x': 0.2, 'center_y': 0.81}
        on_press: root.manager.current = 'purchasing'
    MDRectangleFlatButton:
        text: 'Date, 12:00pm, 12:42pm, 4:00pm, 123456'
        pos_hint: {'center_x': 0.2, 'center_y': 0.74}
        on_press: root.manager.current = 'purchasing'
    MDRectangleFlatButton:
        text: 'Date, 12:00pm, 12:42pm, 4:00pm, 123456'
        pos_hint: {'center_x': 0.2, 'center_y': 0.67}
        on_press: root.manager.current = 'purchasing'
    MDRectangleFlatButton:
        text: 'Date, 12:00pm, 12:42pm, 4:00pm, 123456'
        pos_hint: {'center_x': 0.2, 'center_y': 0.60}
        on_press: root.manager.current = 'purchasing'
    MDRectangleFlatButton:
        text: 'Date, 12:00pm, 12:42pm, 4:00pm, 123456'
        pos_hint: {'center_x': 0.2, 'center_y': 0.53}
        on_press: root.manager.current = 'purchasing'
    MDRectangleFlatButton:
        text: 'Date, 12:00pm, 12:42pm, 4:00pm, 123456'
        pos_hint: {'center_x': 0.2, 'center_y': 0.46}
        on_press: root.manager.current = 'purchasing'
    MDRectangleFlatButton:
        text: 'Date, 12:00pm, 12:42pm, 4:00pm, 123456'
        pos_hint: {'center_x': 0.2, 'center_y': 0.39}
        on_press: root.manager.current = 'purchasing'
    MDRectangleFlatButton:
        text: 'Date, 12:00pm, 12:42pm, 4:00pm, 123456'
        pos_hint: {'center_x': 0.2, 'center_y': 0.32}
        on_press: root.manager.current = 'purchasing'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'pricing'

<ScheduleScreenMB>
    name: 'SchedulesMB'
    MDLabel:
        text: 'Available Schedules for UC Merced - UC Berkeley round trip:'
        pos_hint: {'center_x': 0.5, 'center_y': 0.95}
    MDLabel:
        text: 'Date, Departure Time, ETA, Return Time, Route Number:'
        pos_hint: {'center_x': 0.5, 'center_y': 0.88}
    MDRectangleFlatButton:
        text: 'Date, 12:00pm, 12:42pm, 4:00pm, 123456'
        pos_hint: {'center_x': 0.2, 'center_y': 0.81}
        on_press: root.manager.current = 'purchasing'
    MDRectangleFlatButton:
        text: 'Date, 12:00pm, 12:42pm, 4:00pm, 123456'
        pos_hint: {'center_x': 0.2, 'center_y': 0.74}
        on_press: root.manager.current = 'purchasing'
    MDRectangleFlatButton:
        text: 'Date, 12:00pm, 12:42pm, 4:00pm, 123456'
        pos_hint: {'center_x': 0.2, 'center_y': 0.67}
        on_press: root.manager.current = 'purchasing'
    MDRectangleFlatButton:
        text: 'Date, 12:00pm, 12:42pm, 4:00pm, 123456'
        pos_hint: {'center_x': 0.2, 'center_y': 0.60}
        on_press: root.manager.current = 'purchasing'
    MDRectangleFlatButton:
        text: 'Date, 12:00pm, 12:42pm, 4:00pm, 123456'
        pos_hint: {'center_x': 0.2, 'center_y': 0.53}
        on_press: root.manager.current = 'purchasing'
    MDRectangleFlatButton:
        text: 'Date, 12:00pm, 12:42pm, 4:00pm, 123456'
        pos_hint: {'center_x': 0.2, 'center_y': 0.46}
        on_press: root.manager.current = 'purchasing'
    MDRectangleFlatButton:
        text: 'Date, 12:00pm, 12:42pm, 4:00pm, 123456'
        pos_hint: {'center_x': 0.2, 'center_y': 0.39}
        on_press: root.manager.current = 'purchasing'
    MDRectangleFlatButton:
        text: 'Date, 12:00pm, 12:42pm, 4:00pm, 123456'
        pos_hint: {'center_x': 0.2, 'center_y': 0.32}
        on_press: root.manager.current = 'purchasing'
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'pricing'


<PurchasingScreen>
    name: 'purchasing'
    MDLabel:
        text: 'Please enter the following information: (Credit/Debit)'
        pos_hint: {'center_x': 0.5, 'center_y': 0.95}
    MDLabel:
        text: 'Card Number:'
        pos_hint: {'center_x': 0.5, 'center_y': 0.88}
    MDLabel:
        text: 'Billing Address:'
        pos_hint: {'center_x': 0.5, 'center_y': 0.81}
    MDLabel:
        text: 'Expiration Date:'
        pos_hint: {'center_x': 0.5, 'center_y': 0.74}
    MDLabel:
        text: 'Security Number:'
        pos_hint: {'center_x': 0.5, 'center_y': 0.67}
    MDRectangleFlatButton:
        text: 'Back'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'confirm'
    MDRectangleFlatButton:
        text: 'Confirm Purchase'
        pos_hint: {'center_x': 0.5, 'center_y': 0.3}
        on_press: root.manager.current = 'confirm'

<ConfirmationScreen>
    name: 'confirm'
    MDLabel:
        text: 'You Are All Set'
        halign: 'center'
    MDRectangleFlatButton:
        text: 'See Updates'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'updates'

<UpdatesScreen>
    name: 'updates'
    MDLabel:
        text: 'Live Updates on Your Flight'
        pos_hint: {'center_x': 0.5, 'center_y': 0.95}
    MDLabel:
        text: 'ETA: 12:50pm'
        pos_hint: {'center_x': 0.5, 'center_y': 0.88}
    MDLabel:
        text: 'Weather Conditions: Good'
        pos_hint: {'center_x': 0.5, 'center_y': 0.81}
    
    MDLabel:
        text: 'Delays: None'
        pos_hint: {'center_x': 0.5, 'center_y': 0.74}
    MDLabel:
        text: 'Charge: 80% ~ 2 Hours of  Flight Left'
        pos_hint: {'center_x': 0.5, 'center_y': 0.67}
    MDRectangleFlatButton:
        text: 'Refresh'
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}
        on_press: root.manager.current = 'updates'
"""

class MenuScreen(Screen):
    pass

class ProfileScreen(Screen):
    pass

class PricingScreen(Screen):
    pass

class ScheduleScreenMS(Screen):
    pass

class ScheduleScreenMD(Screen):
    pass

class ScheduleScreenMB(Screen):
    pass

class PurchasingScreen(Screen):
    pass

class ConfirmationScreen(Screen):
    pass

class UpdatesScreen(Screen):
    pass
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(PricingScreen(name='pricing'))
sm.add_widget(ScheduleScreenMS(name='SchedulesMS'))
sm.add_widget(ScheduleScreenMD(name='SchedulesMD'))
sm.add_widget(ScheduleScreenMB(name='SchedulesMB'))
sm.add_widget(PurchasingScreen(name='purchasing'))
sm.add_widget(ConfirmationScreen(name='confirm'))
sm.add_widget(UpdatesScreen(name='updates'))
class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(screen_helper)
        return screen


DemoApp().run()


