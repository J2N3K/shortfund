markdown = '''

# **SHORTFUND 📉🏛️**

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
Celem niniejszego projektu jest ułatwienie analizy danych, tworzenie pełnego obrazu rynku oraz pomaganie
przy podejmowaniu potencjalnych decyzji inwestycyjnych.

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


---
<style>
<!--
#pp_t{width:180px; background-color:#d9d9d9;}#pp_t td{padding:1px 2px; border: 1px solid #d9d9d9;}#pp_h{font-size:75%; font-family:arial; font-weight:bold; color:#ffffff; background-color:#6677aa;}#pp_s{font-size:69%; font-family:arial; color:#000000; text-decoration:none;}#pp_v{font-size:69%; font-family:arial;}#pp_cu{font-size:69%; font-family:arial; color:#005500;}#pp_cd{font-size:69%; font-family:arial; color:#ff0000;}#pp_d{font-size:69%; font-family:arial;}#pp_r1{background-color:#ffffff;}#pp_r2{background-color:#ffffff;}#pp_n{display:table-row;}
-->
</style>

<script type="text/javascript">
<!--
function pp_m(a){a.setAttribute('target','_new');}
-->
</script>

<script type="text/javascript" src="https://static.stooq.com/pp/gc.js"></script>

---

<center><a href="https://stooq.com/c/?p&s=cdr&c=3y"><img src="https://stooq.com/c/?p&s=cdr&c=3y" border="0"></a><br><div style="width:1px;height:3px"><!-- --></div><font id="f10"><a href="https://stooq.com/c/?p&s=cdr&c=1d">1d</a> | <a href="https://stooq.com/c/?p&s=cdr&c=5d">5d</a> | <a href="https://stooq.com/c/?p&s=cdr&c=1m">1m</a> | <a href="https://stooq.com/c/?p&s=cdr&c=5m">5m</a> | <a href="https://stooq.com/c/?p&s=cdr&c=1y">1r</a> | <a href="https://stooq.com/c/?p&s=cdr&c=5y">5l</a></font></center>


<div id="crazyBox" style="text-align: center; padding: 10px; border-top-left-radius: 8px; border-top-right-radius: 8px; color: #fffaaa; font-family: Arial, sans-serif;">
  eheahaeh © 2025
</div>

<style>
  #crazyBox {
    background: linear-gradient(45deg, #ff5f6d, #ffc371, #42a5f5, #66bb6a);
    background-size: 300% 300%;
    animation: crazyGradient 5s ease-in-out infinite;
  }

  @keyframes crazyGradient {
    0% { background-position: 0% 50%; }
    25% { background-position: 50% 100%; }
    50% { background-position: 100% 50%; }
    75% { background-position: 50% 0%; }
    100% { background-position: 0% 50%; }
  }
</style>



'''