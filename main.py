from selenium import webdriver
from selenium.common import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

IN_TEST = True

test_form_url = "https://forms.office.com/Pages/ResponsePage.aspx?id=sUvtTf9rs0Ku12o2pQO_eoG9h3aWFuJHmfvBQG46FWZUNDg3TVBSVzlFRkFPUUFSUlBWMUo2NjczMS4u"
form_url = "https://forms.office.com/e/QGEDJR02YU"

options = Options()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))


def main():
    open_form()
    fill_in_form()
    # submit_form()
    # quit_browser()


def open_form():
    if IN_TEST:
        url = test_form_url
    else:
        url = form_url

    driver.implicitly_wait(10)
    driver.get(url)
    WebDriverWait(driver, timeout=10, poll_frequency=1,
                  ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])


def select_radiobutton_by_xpath_of_answer(xpath):
    driver.find_element(By.XPATH, xpath).click()


def select_radiobutton_by_keywords_of_question(question_keywords, answer):
    question_xpath = find_question_xpath_by_question_keywords(question_keywords)
    next_radio_button_xpath = f"{question_xpath}/following::span[@data-automation-id='radio' and @data-automation-value='{answer}']"
    driver.find_element(By.XPATH, next_radio_button_xpath).click()


def fill_in_text_field_by_question_keywords(question_keywords, answer):
    input_field = driver.find_element(By.XPATH, find_xpath_of_text_field_by_question_keywords(question_keywords))
    input_field.send_keys(answer)


def find_xpath_of_text_field_by_question_keywords(question_keywords):
    question_xpath = find_question_xpath_by_question_keywords(question_keywords)
    return f"{question_xpath}/following::input[@data-automation-id='textInput'][1]"


def find_question_xpath_by_question_keywords(question_keywords):
    keyword_conditions = [f"contains(text(), '{kw}')" for kw in question_keywords]
    question_xpath = f"//*[{' and '.join(keyword_conditions)}]"
    return question_xpath


def fill_in_form():
    # # Question 1: Eerste keuze (radio button)
    answer_xpath = find_question_xpath_by_question_keywords(["Kleuter", "Type", "9"])
    select_radiobutton_by_xpath_of_answer(answer_xpath)

    # # Question 2: Tweede keuze (leave void)

    # Question 3: Familienaam van de leerling
    keywords = ["Familienaam", "leerling"]
    answer = "Delacourt"
    fill_in_text_field_by_question_keywords(keywords, answer)

    # # Question 4: Voornaam van de leerling
    keywords = ["Voornaam", "leerling"]
    answer = "Silas"
    fill_in_text_field_by_question_keywords(keywords, answer)

    # Sloppy af
    # Question 5: Geboortedatum van de leerling
    birthdate = driver.find_element(By.ID, "DatePicker0-label")
    birthdate_placeholder = birthdate.get_attribute("placeholder").lower()
    birthdate.click()

    if birthdate_placeholder.__contains__("dd/mm/yyyy"):
        birthdate.send_keys("24/08/2019")
    elif birthdate_placeholder.__contains__("mm/dd/yyyy"):
        birthdate.send_keys("08/24/2019")
    elif birthdate_placeholder.__contains__("m/dd/yyyy"):
        birthdate.send_keys("8/24/2019")
    elif birthdate_placeholder.__contains__("dd/m/yyyy"):
        birthdate.send_keys("24/8/2019")

    elif birthdate_placeholder.__contains__("dd-mm-yyyy"):
        birthdate.send_keys("08-24-2019")
    elif birthdate_placeholder.__contains__("mm-dd-yyyy"):
        birthdate.send_keys("08-24-2019")
    elif birthdate_placeholder.__contains__("m-dd-yyyy"):
        birthdate.send_keys("8-24-2019")
    elif birthdate_placeholder.__contains__("dd-m-yyyy"):
        birthdate.send_keys("24-8-2019")

    # # Question 6: Rijksregisternummer van de leerling (zie achterkant identiteitskaart)
    keywords = ["Rijksregisternummer"]
    answer = "19082420148"
    fill_in_text_field_by_question_keywords(keywords, answer)

    # # Question 7: Geslacht van de leerling
    geslacht = driver.find_element(By.XPATH, "//*[contains(text(), 'Jongen')]")
    geslacht.click()

    # # Question 8: Domicilieadres van de leerling: straat en nummer
    keywords = ["adres", "leerling", "straat"]
    answer = "Sint-Arnolduslaan 35"
    fill_in_text_field_by_question_keywords(keywords, answer)

    # # Question 9: Domicilieadres van de leerling: postcode en gemeente
    keywords = ["postcode", "gemeente"]
    answer = "8200 Sint-Michiels"
    fill_in_text_field_by_question_keywords(keywords, answer)

    # # Question 10: Familienaam en voornaam van de vader
    keywords = ["Familienaam", "voornaam", "vader"]
    answer = "Delacourt Mathias"
    fill_in_text_field_by_question_keywords(keywords, answer)

    # # Question 11: Telefoonnummer van de vader
    keywords = ["Telefoonnummer", "vader"]
    answer = "0486776340"
    fill_in_text_field_by_question_keywords(keywords, answer)

    # # Question 12: E-mailadres van de vader
    keywords = ["E-mailadres", "vader"]
    answer = "mathias.delacourt@gmail.com"
    fill_in_text_field_by_question_keywords(keywords, answer)

    # # Question 13: Familienaam en voornaam van de moeder
    keywords = ["Familienaam", "voornaam", "moeder"]
    answer = "Puystjens Nathalie"
    fill_in_text_field_by_question_keywords(keywords, answer)

    # # Question 14: Telefoonnummer van de moeder
    keywords = ["Telefoonnummer", "moeder"]
    answer = "0486909712"
    fill_in_text_field_by_question_keywords(keywords, answer)

    # # Question 15: E-mailadres van de moeder
    keywords = ["E-mailadres", "moeder"]
    answer = "nathaliepuystjens@gmail.com"
    fill_in_text_field_by_question_keywords(keywords, answer)

    # # Question 16: De vorige school van de leerling
    keywords = ["vorige", "school"]
    answer = "SBS De Geluksvogel"
    fill_in_text_field_by_question_keywords(keywords, answer)

    # # Question 17: Is er een verslag van het CLB voor het buitengewoon onderwijs Type 3, type 7 of type 9
    answer_xpath = find_question_xpath_by_question_keywords(["in", "opmaak"])
    select_radiobutton_by_xpath_of_answer(answer_xpath)

    # Question 18: Verplicht om te kunnen inschrijven: Ben je akkoord met het schoolreglement en pedagogisch project van de school (zie link op website https://de-kade.be/nl/de-kade/onderwijs/bubao-het-anker )
    select_radiobutton_by_keywords_of_question(["schoolreglement"], "ja")

    # Question 19: Als u uw kind inschrijft in onze school Het Anker gaat u akkoord met de uitwisseling van persoonsgegevens met de verantwoordelijke van het lokaal overlegplatform die de inschrijvingen in de Brugse scholen ondersteunt. Meer uitgebreide info kan je nalezen op onze website via de link over privacy. Als u niet akkoord bent met deze werkwijze, kan u dit melden via Tel 02 55 30 42 5 / GSM 0478669440 / e-mail luna.janssen@ond.vlaanderen.be


def submit_form():
    submit_buttons = driver.find_elements(By.TAG_NAME, "Button")
    submit_buttons[-1].click()


def quit_browser():
    driver.quit()


if __name__ == "__main__":
    main()
