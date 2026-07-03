# Moja Droga do DevOps

Cześć! Witaj w moim repozytorium. Dokumentuję tutaj swój proces nauki, budowania fundamentów oraz automatyzacji infrastruktury od absolutnego zera. 


## Co już potrafię i co znajduje się w tym repozytorium:

### 1. Administracja Linux & LVM
- Zarządzanie przestrzenią dyskową za pomocą LVM (tworzenie PV, VG, LV oraz bezpieczne rozszerzanie wolumenów w locie).
- Konfiguracja sieci, analiza portów (`ss`, `grep`) oraz zarządzanie bezpieczeństwem przez firewall (`UFW`).

### 2. Konteneryzacja (Docker)

### 3. Automatyzacja (Ansible)

### 4. Wstęp do Chmury Publicznej (AWS Cloud Practitioner Foundation)

#### Opis i cel
Rozpoczęcie przygotowań do certyfikacji AWS Certified Cloud Practitioner. Zrozumienie fundamentalnych pojęć biznesowych, modeli wdrażania usług oraz globalnej architektury chmury AWS.

### Kluczowe pojęcia opanowane w tym etapie:
1. **Modele wdrożeniowe chmury:**
   * *Public Cloud* (całość u dostawcy, np. AWS).
   * *Private Cloud / On-Premise* (własna serwerownia firmy).
   * *Hybrid Cloud* (łączenie infrastruktury własnej z chmują publiczną).
2. **Klasyfikacja usług chmurowych:**
   * **IaaS (Infrastructure as a Service):** Dostawca daje sprzęt, użytkownik zarządza systemem operacyjnym i aplikacją (np. AWS EC2).
   * **PaaS (Platform as a Service):** Dostawca zarządza systemem operacyjnym, użytkownik dba tylko o swój kod (np. AWS Elastic Beanstalk).
   * **SaaS (Software as a Service):** Gotowa aplikacja w przeglądarce (np. Gmail, Office365).
3. **Zasady Globalnej Infrastruktury AWS:**
   * **Regiony:** Całkowicie niezależne, odizolowane geograficznie lokalizacje na świecie (np. Frankfurt). Wybierane na podstawie prawa (*compliance*), kosztów oraz opóźnień (*latency*).
   * **Strefy Dostępności (Availability Zones - AZ):** Fizycznie odrębne centra danych wewnątrz jednego regionu. Architektura *Multi-AZ* zapewnia wysoką dostępność (*High Availability*) i odporność na katastrofy.
   * **Punkty Brzegowe (Edge Locations):** Lokalne punkty dystrybucji treści (CDN CloudFront), służące do cache'owania danych bliżej użytkownika końcowego (np. punkt w Warszawie).

---
*Repozytorium jest stale aktualizowane w miarę moich codziennych postępów.*
