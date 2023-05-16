from selenium import webdriver
from selenium.common import ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options = options, service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get("https://forms.office.com/Pages/ResponsePage.aspx?id=sUvtTf9rs0Ku12o2pQO_eoG9h3aWFuJHmfvBQG46FWZUNDg3TVBSVzlFRkFPUUFSUlBWMUo2NjczMS4u")
wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])

# # Question 1: Eerste keuze (radio button)
eerste_keuze = driver.find_element(By.XPATH, "//*[contains(text(), 'Kleuter Type 9')]")
eerste_keuze.click()

# # Question 2: Tweede keuze (leave void)

# # Question 3: Familienaam van de leerling
familienaam = driver.find_element(By.XPATH, "//*[contains(text(), 'Familienaam van de leerling')]/../../../following-sibling::div/div/span/input")
familienaam.send_keys("Delacourt")

# # Question 4: Voornaam van de leerling
voornaam = driver.find_element(By.XPATH, "//*[contains(text(), 'Voornaam van de leerling')]/../../../following-sibling::div/div/span/input")
voornaam.send_keys("Silas")

# Sloppy af
# Question 5: Geboortedatum van de leerling
geboortedatum = driver.find_element(By.ID, "DatePicker0-label")
geboortedatum_placeholder = geboortedatum.get_attribute("placeholder").lower()
geboortedatum.click()

if geboortedatum_placeholder.__contains__("dd/mm/yyyy"):
    geboortedatum.send_keys("24/08/2019")
elif geboortedatum_placeholder.__contains__("mm/dd/yyyy"):
    geboortedatum.send_keys("08/24/2019")
elif geboortedatum_placeholder.__contains__("m/dd/yyyy"):
    geboortedatum.send_keys("8/24/2019")
elif geboortedatum_placeholder.__contains__("dd/m/yyyy"):
    geboortedatum.send_keys("24/8/2019")

elif geboortedatum_placeholder.__contains__("dd-mm-yyyy"):
    geboortedatum.send_keys("08-24-2019")
elif geboortedatum_placeholder.__contains__("mm-dd-yyyy"):
    geboortedatum.send_keys("08-24-2019")
elif geboortedatum_placeholder.__contains__("m-dd-yyyy"):
    geboortedatum.send_keys("8-24-2019")
elif geboortedatum_placeholder.__contains__("dd-m-yyyy"):
    geboortedatum.send_keys("24-8-2019")

# # Question 6: Rijksregisternummer van de leerling (zie achterkant identiteitskaart)
rijksregisternummer = driver.find_element(By.XPATH, "//*[contains(text(), 'Rijksregisternummer')]/../../../following-sibling::div/div/span/input")
rijksregisternummer.send_keys("19082420148")

# # Question 7: Geslacht van de leerling
geslacht = driver.find_element(By.XPATH, "//*[contains(text(), 'Jongen')]")
geslacht.click()

# # Question 8: Domicilieadres van de leerling: straat en nummer
domicilie_straat_en_nr = driver.find_element(By.XPATH, "//*[contains(text(), 'straat')]/../../../following-sibling::div/div/span/input")
domicilie_straat_en_nr.send_keys("Sint-Arnolduslaan 35")
#
# # Question 9: Domicilieadres van de leerling: postcode en gemeente
domicilie_postcode_en_gemeente = driver.find_element(By.XPATH, "//*[contains(text(), 'postcode')]/../../../following-sibling::div/div/span/input")
domicilie_postcode_en_gemeente.send_keys("8200 Sint-Michiels")

# # Question 10: Familienaam en voornaam van de vader
# naam_vader = driver.find_element(By.XPATH, "//*[contains(text(), 'Familienaam en voornaam van de vader')]/../../../following-sibling::div/div/span/input")
# naam_vader.send_keys("Delacourt Mathias")

naam_vader = driver.find_element(By.XPATH, "//*[contains(text(), 'Familienaam')]/../../../following-sibling::div/div/span/input" and "//*[contains(text(), 'vader')]/../../../following-sibling::div/div/span/input")
naam_vader.send_keys("Delacourt Mathias")

# # Question 11: Telefoonnummer van de vader
telefoon_vader = driver.find_element(By.XPATH, "//*[contains(text(), 'Telefoonnummer van de vader')]/../../../following-sibling::div/div/span/input")
telefoon_vader.send_keys("0486776340")

# # Question 12: E-mailadres van de vader
email_vader = driver.find_element(By.XPATH, "//*[contains(text(), 'E-mailadres van de vader')]/../../../following-sibling::div/div/span/input")
email_vader.send_keys("mathias.delacourt@gmail.com")

# # Question 13: Familienaam en voornaam van de moeder
naam_moeder = driver.find_element(By.XPATH, "//*[contains(text(), 'Familienaam en voornaam van de moeder')]/../../../following-sibling::div/div/span/input")
naam_moeder.send_keys("Puystjens Nathalie")

# # Question 14: Telefoonnummer van de moeder
telefoon_moeder = driver.find_element(By.XPATH, "//*[contains(text(), 'Telefoonnummer van de moeder')]/../../../following-sibling::div/div/span/input")
telefoon_moeder.send_keys("0486909713")

# # Question 15: E-mailadres van de moeder
email_moeder = driver.find_element(By.XPATH, "//*[contains(text(), 'E-mailadres van de moeder')]/../../../following-sibling::div/div/span/input")
email_moeder.send_keys("nathaliepuystjens@gmail.com")

# # Question 16: De vorige school van de leerling
email_moeder = driver.find_element(By.XPATH, "//*[contains(text(), 'De vorige school van de leerling')]/../../../following-sibling::div/div/span/input")
email_moeder.send_keys("SBS De Geluksvogel")

# # Question 17: Is er een verslag van het CLB voor het buitengewoon onderwijs Type 3, type 7 of type 9
verslag = driver.find_element(By.XPATH, "//*[contains(text(), 'nog in opmaak')]")
verslag.click()


# Question 18: Verplicht om te kunnen inschrijven: Ben je akkoord met het schoolreglement en pedagogisch project van de school (zie link op website https://de-kade.be/nl/de-kade/onderwijs/bubao-het-anker )
akkoord_schoolreglement = driver.find_element(By.ID, "QuestionChoiceOption18")
akkoord_schoolreglement.click()

# Question 19: Als u uw kind inschrijft in onze school Het Anker gaat u akkoord met de uitwisseling van persoonsgegevens met de verantwoordelijke van het lokaal overlegplatform die de inschrijvingen in de Brugse scholen ondersteunt. Meer uitgebreide info kan je nalezen op onze website via de link over privacy. Als u niet akkoord bent met deze werkwijze, kan u dit melden via Tel 02 55 30 42 5 / GSM 0478669440 / e-mail luna.janssen@ond.vlaanderen.be


# Submit button:
# submit_buttons = driver.find_elements(By.TAG_NAME, "Button")
# submit_buttons[-1].click()

# browser.quit()
