# **SHORTFUND 📉🏛️**

### TLDR;
A web application for data visualization and insights derived from the KNF short selling register, developed in Python using the Shiny framework. This application enables users to analyze and interpret short selling data through interactive charts and dashboards.

This project is a work in progress. Watch the demo below ⬇️

https://github.com/user-attachments/assets/c34a4cf8-8974-4521-a6dd-245cc421fa8d

---

### O projekcie

**Shortfund** to projekt, który ma na celu prezentować dane o pozycjach 
krótkich (shortach), zawieranych przez fundusze inwestycyjne na spółkach 
z Giełdy Papierów Wartościowych w Warszawie.

> ✨ Dane pobierane są *automatycznie* z [Rejestru Pozycji Krótkich KNF](https://rss.knf.gov.pl/)
w cogodzinnych odstępach.

Publikowane dane ze strony Komisji Nadzoru Finansów mają surowy, tabelaryczny charakter, oraz nie przedstawiają skali zjawisk
jak i zmian w czasie, w sposób jasny i czytelny.

###### Przykładowe dane:
```
| L.P.| Posiadacz pozycji krótkiej   | Nazwa papieru | ISIN         | Pozycja krótka netto(%) | Data obliczenia pozycji | Data ostatniej aktualizacji |
|     | --------------------------   | ------------- | -----------  | ----------------------- | ----------------------- | --------------------------- |
|  1  |  Marshall Wace LLP           |    JSW        | PLJSW0000015 |           0.54          |        2025-02-25       |           2025-02-26        |
|  2  |  AQR Capital Management, LLC |    CDPROJEKT  | PLOPTTC00011 |           0.69          |        2024-12-05       |           2024-12-06        |
|  3  |  Kintbury Capital LLP        |    LPP        | PLLPP0000011 |           0.99          |        2025-02-05       |           2025-02-06        |
```

Celem niniejszego projektu jest ułatwienie analizy danych, tworzenie pełniejszego obrazu rynku oraz pomaganie
przy podejmowaniu potencjalnych decyzji inwestycyjnych.

---

### Funkcje

Strona umożliwia:
- 📊 Wizualizację danych
    - pozycji zajętych na danej spółce
    - pozycji zajmowanych przez wybrany fundusz
    - zagregowanej ilości shortów na spółce
- 💵 Aktualne statystyki dot. aktywności funduszy
- 📈 Podgląd notowań ze Stooq oraz statystyki sesji
- TBA
- TBA

---

### Do zrobienia

- [x] Wykres słupkowy plotly, wizualizacja po nazwie spółki
- [x] Elementy "value_box" wyświetlające liczbę shortów, fundów, update
- [x] Wykres słupkowy plotly, wizualizacja po nazwie funduszu
- [x] Sekcja about me w Markdown
- [x] Overhaul graficzny nr 1 (zakładki, tabelki, cards, unfluid)
- [x] Suma shortów na spółce + liczba akcji do wykupienia, ~~utilization, short squeeze~~
- [x] Dane ze stooq - wykres według spółki, statystyki ogólne sesji
- [x] Logo & favicon
- [x] Stopka strony
- [x] Alert
- [ ] Alt progress bar przy załadowywaniu wykresów / Reactive calc
- [ ] Wykresy szeregu czasowego
- [ ] Overhaul graficzny nr 2 (Custom CSS)

