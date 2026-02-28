# Forensics Tool

## Structura:
1. Collector (live)
    -> salvez fisiere + output comenzi intr-un folder
    ex: evidence/<case>/raw

2. Collector(offline)
    -> montez imaginea read_only si copiez/extrag aceleasi artefacte

3. Memory dump (optional)
    -> Fac dump RAM, analizez cu Volatility

4. Parsare artefacte
    -> Construiesc timeline (CSV/JSON)

5. IOC scan
    -> calculez hash pentru fisiere relevante si la compar cu lista IOC

6. Raport (HTML)
    -> friendly, contine system info, conexiuni, comenzi istorice, procese suspecte, logs, timeline, IOC hits

7. Manifest/hash (optional)
    -> calculez sha256 pt fisire brute

M-am gandit ca pentru fiecare caz analizat, tool-ul sa creeze 3 directoare: raw, parsed si reports;
raw contine date brute colectate;
parsed va contine datele procesate;
reports va contine raporturile generate in urma rularii tool-ului.

artifacts/system_info.py colecteaza informatii live despre sistem;
salveaza output-ul raw, genereaza artifac JSON in parsed;
Practic, va colecta hostname, OS info, kernel version, uptime, current user, lista utilizatori si data aprox a instalarii
