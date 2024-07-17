def test_engeto_testingakademie(page):
    page.goto('https://engeto.cz')
    # potvrzeni cookies pokud je potřeba
    page.get_by_role("button", name="Chápu a přijímám!").click()
    # klikni na tlačitko kurzy
    page.get_by_role("link", name="Kurzy", exact=True).click()
    # ověření zda se na stránce nachází odkaz s nazvem testing akademie
    assert page.get_by_role("link", name="Testing Akademie")


def test_odber(page):
    page.goto('https://engeto.cz')
    page.get_by_role("button", name="Chápu a přijímám!").click()
    # kliknutí do labelu
    page.get_by_placeholder("Zadejte váš e-mail").click()
    # vyplnění validní emailové adresy
    page.get_by_placeholder("Zadejte váš e-mail").fill('example@gmail.com')
    # kliknout na tlačítko odebírat
    page.get_by_role("link", name="Odebírat").click()
    # ověření zda se po odeslání požadavku zobrazí správný text
    assert page.get_by_text("Děkujeme, už se můžeš těšit na čerstvou dávku novinek!")


def test_prazdny_odber(page):
    page.goto('https://engeto.cz')
    page.get_by_role("button", name="Chápu a přijímám!").click()
    page.get_by_placeholder("Zadejte váš e-mail").click()
    # do labelu nic nevyplnit
    page.get_by_placeholder("Zadejte váš e-mail").fill('')
    page.get_by_role("link", name="Odebírat").click()
    # ověření zda validace funguje a vypíše očekávaný text
    assert page.get_by_text("Prosím zadejte validní emailovou adresu")
