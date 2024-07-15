# all the locator at one location (Testlocator package name and Imdblocators python file
class Imdblocators:
    # xpath for Imdb_page
    name_locator = "//label//span[1]//div[text()='Name']"
    name_search_box_locator = "//div[@class='ipc-textfield__container']//input[@placeholder='e.g. Audrey Hepburn']"
    Birth_date_locator = "//label//span//div[text()='Birth date']"
    result_locator = "//button//span[text()='See results']"
    start_date_locator = "//input[@data-testid='birthDate-start']"
    end_date_locator = "//input[@data-testid='birthDate-end']"
    search_data = "aamir khan"
    start_date = "05/10/1960"
    end_date = "05/10/1990"
    actor_locator = "//div[@data-testid='nlib-title']"
