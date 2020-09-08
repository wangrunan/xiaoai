from page.adddevicepage import AddDeicePage
from page.addtrainpage import AddTrainPage
from page.centerpage import CenterPage
from page.childinfopage import ChildinfoPage
from page.deviceguidepage import DeviceGuidePage
from page.historyrecordpage import HistoryRecordPage
from page.homepage import HomePage
from page.loginpage import LoginPage
from page.matecirclepage import MateCirclePage

from page.musicpreferencepage import MusicPreferencePage
from page.mydevicepage import MyDevicePage
from page.myprizepage import MyprizePage
from page.mytrainpage import MyTrainPage
from page.personaldatapage import PersonalDataPage
from page.sessionpage import SessionPage
from page.suggestpage import SuggestPage
from page.xiaoailaboratorypage import XiaoaiLaboratoryPage
from page.dialoguetranslationpage import DialogueTranslationPage
from page.shortcutpage import ShortCutPage
from page.translation import TranslationPage

class Page:

    def __init__(self, driver):
        self.driver = driver


    #Python内置的 @ property装饰器就是负责把一个方法变成属性调用的
    @property
    def homepage(self):
        return HomePage(self.driver)


    @property
    def loginpage(self):
        return LoginPage(self.driver)

    @property
    def centerpage(self):
        return CenterPage(self.driver)

    @property
    def sessionpage(self):
        return SessionPage(self.driver)

    @property
    def historyrecordpage(self):
        return HistoryRecordPage(self.driver)

    @property
    def personaldatapage(self):
        return PersonalDataPage(self.driver)

    @property
    def mytrainpage(self):
        return MyTrainPage(self.driver)

    @property
    def deviceguidepage(self):
        return DeviceGuidePage(self.driver)

    @property
    def mydevicepage(self):
        return MyDevicePage(self.driver)

    @property
    def childinfopage(self):
        return ChildinfoPage(self.driver)

    @property
    def musicpreferencePage(self):
        return MusicPreferencePage(self.driver)

    @property
    def suggestpage(self):
        return SuggestPage(self.driver)

    @property
    def adddeicepage(self):
        return AddDeicePage(self.driver)

    @property
    def addtrainpage(self):
        return AddTrainPage(self.driver)
    @property
    def myprizepage(self):
        return MyprizePage(self.driver)

    @property
    def xiaoailaboratorypage(self):
        return XiaoaiLaboratoryPage(self.driver)

    @property
    def matemiraclepage(self):
        return MateCirclePage(self.driver)

    @property
    def dialoguetranslationpage(self):
        return DialogueTranslationPage(self.driver)

    @property
    def shortcutpage(self):
        return ShortCutPage(self.driver)

    @property
    def translation(self):
        return TranslationPage(self.driver)