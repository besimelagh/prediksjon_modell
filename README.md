# Prediksjon Modell

Denne løsningen er utviklet for oppgaven beskrevet av Butikken™ for å bygge en prediksjonsmodell som estimerer sannsynligheten for at en kunde vil kjøpe deres nyeste produkt. Løsningen er laget i Python og inkluderer:

- Dataforedling
- Bygging av en logistisk regresjonsmodell
- Evaluering og visualisering av modellen (ROC-kurve)
- Lagring av prediksjonsresultater i en CSV-fil

## Innhold

### Filer
- `butikken.csv`: Datasettet levert for oppgaven.
- `prediction_model.py`: Hovedskriptet som utfører dataforedling, modelltrening og evaluering.
- `prediction_results.csv`: Output med sannsynligheter, prediksjoner og sanne etiketter for testsettet.

### Hvordan kjøre løsningen
1. Klon dette repositoriet:
   ```bash
   git clone https://github.com/besimelagh/prediksjon_modell.git
   ```

2. Naviger til prosjektmappen:
   ```bash
   cd prediksjon_modell
   ```

3. Installer nødvendige avhengigheter:
   ```bash
   pip install -r requirements.txt
   ```

4. Kjør modellen:
   ```bash
   python prediction_model.py
   ```

### Resultater
- Modellen oppnådde en **ROC-AUC score på 0.71**.
- En ROC-kurve visualiseres for å vurdere modellens ytelse.
- Prediksjonsresultater er lagret i filen `prediction_results.csv`.

### Produksjonsklar løsning
For en verdiskapende løsning kan modellen integreres i en pipeline som:
1. Automatisk henter og forbereder nye kundeopplysninger.
2. Predikerer sannsynligheten for kjøp ved hjelp av modellen.
3. Oppdaterer kundegrensesnittet eller et dashboard med anbefalinger.

Løsningen kan distribueres som en API-tjeneste for sanntidsprediksjoner.

---

Ta gjerne kontakt hvis det er spørsmål eller ytterligere behov!