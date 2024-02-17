from attr import s
from selenium import webdriver
import webdriver_manager.microsoft as wd_microsoft
import webdriver_manager.chrome as wd_chrome
import webdriver_manager.firefox as wd_firefox

class Browser:
    EDGE = 'Edge'
    CHROME = 'Chrome'
    FIREFOX = 'Firefox'


class ScraperOptions:
    def __init__(self):
        self.incognito: bool = True
        self.show_process: bool = False
        self.downloads_path: str or None = None
        self.driver_version: str or None = None
        self.driver_executable_path: str or None = None
        self.driver_install_path: str or None = None


class DriverMagic:
    def __init__(self, options: ScraperOptions):
        self.options = options

    def add_options(self, os_options_obj):
        os_options_obj.add_argument('--ignore-certificate-errors')
        os_options_obj.add_experimental_option('excludeSwitches', ['enable-logging'])
        if self.options.incognito:
            os_options_obj.add_argument('--incognito')
        if not self.options.show_process:
            os_options_obj.add_argument('--headless')
        if self.options.downloads_path:
            prefs = {"download.default_directory": self.optionsdownloads_path}
            os_options_obj.add_experimental_option("prefs", prefs)

    def get(self, browser: Browser):
        """
        choose a browser you already have installed on your machine
        """
        version = self.options.driver_version
        
        if browser == Browser.EDGE:
            options = webdriver.EdgeOptions()
            self.add_options(options)
            return webdriver.Edge(
                options=options,
                service=webdriver.edge.service.Service(
                    self.options.driver_executable_path or
                    wd_microsoft.EdgeChromiumDriverManager(version=version).install()))

        if browser == Browser.CHROME:
            options = webdriver.ChromeOptions()
            self.add_options(options)
            return webdriver.Chrome(
                options=options,
                service=webdriver.chrome.service.Service(
                    self.options.driver_executable_path or
                    wd_chrome.ChromeDriverManager(driver_version=version).install()))

        if browser == Browser.FIREFOX:
            options = webdriver.FirefoxOptions()
            self.add_options(options)
            return webdriver.Firefox(
                options=options,
                service=webdriver.firefox.service.Service(
                    self.options.driver_executable_path or
                    wd_firefox.GeckoDriverManager(
                        version=version).install()))
