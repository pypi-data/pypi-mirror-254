from attr import s
from selenium import webdriver


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
        self.driver_options_dict: dict = dict()


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
            prefs = {"download.default_directory": self.options.downloads_path}
            os_options_obj.add_experimental_option("prefs", prefs)

        for k, v in self.options.driver_options_dict.items():
            setattr(os_options_obj, k, v)

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
                service=webdriver.EdgeService(
                    self.options.driver_executable_path))

        if browser == Browser.CHROME:
            options = webdriver.ChromeOptions()
            self.add_options(options)
            return webdriver.Chrome(
                options=options,
                service=webdriver.ChromeService(
                    self.options.driver_executable_path))

        if browser == Browser.FIREFOX:
            options = webdriver.FirefoxOptions()
            self.add_options(options)
            return webdriver.Firefox(
                options=options,
                service=webdriver.FirefoxService(
                    self.options.driver_executable_path))
