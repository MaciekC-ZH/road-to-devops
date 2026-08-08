# 🚀 Moja Droga do DevOps

Witaj w moim głównym repozytorium dokumentującym moją ścieżkę nauki, budowania fundamentów infrastruktury oraz automatyzacji od absolutnego zera. 

Znajdziesz tutaj zestawienie moich umiejętności, ustrukturyzowane notatki oraz opisy zrealizowanych projektów i laboratoriów praktycznych.

---

## 🛠️ Fundamenty Inżynierskie

*(Szczegółowe projekty i kod dla poniższych modułów znajdują się w osobnych, dedykowanych repozytoriach).*

### 1. Administracja Linux & LVM
- **Zarządzanie dyskami (LVM):** Tworzenie Physical Volumes (PV), Volume Groups (VG), Logical Volumes (LV) oraz bezpieczne rozszerzanie wolumenów w locie.
- **Sieć i Bezpieczeństwo:** Konfiguracja interfejsów, diagnostyka portów (`ss`, `grep`), analiza ruchu oraz zarządzanie zaporą sieciową (`UFW`).

### 2. Konteneryzacja (Docker & Docker Compose)
- **Konteneryzacja aplikacji:** Pisanie autorskich plików `Dockerfile`, optymalizacja cache warstw, budowanie lekkich obrazów i stosowanie dobrych praktyk bezpieczeństwa (`USER non-root`).
- **Orkiestracja i Sieć:** Tworzenie wielokontenerowych środowisk w `docker-compose.yml`, komunikacja wizualizacyjna przez wewnętrzny DNS Dockera oraz trwałe podpinanie danych (*Volumes* & *Bind Mounts*).

### 3. Automatyzacja Konfiguracji (Ansible)
- **Playbooki i Logika:** Tworzenie deklaratywnych skryptów konfiguracyjnych, obsługa pętli (`loop`), warunków (`when`), powiadomień (`handlers`) oraz struktur odpornych na błędy (`block/rescue`).
- **Sekrety i Bezpieczeństwo:** Szyfrowanie wrażliwych danych za pomocą `Ansible Vault` oraz rozdzielanie logiki od danych (zrealizowane projekty finałowe: *Kosmiczny Port* oraz *Cyber-Bank*).

---

## ☁️ Chmura Publiczna (AWS Foundation & Networking)

Rozpoczęcie przygotowań do certyfikacji **AWS Certified Cloud Practitioner** oraz praktyczne wdrażanie architektury chmurowej.

### 1. Architektura i Fundamenty Chmury
- **Modele wdrożeniowe:** Rozróżnianie chmury publicznej (*Public Cloud*), prywatnej (*On-Premise*) oraz hybrydowej (*Hybrid Cloud*).
- **Klasyfikacja usług:** IaaS (np. AWS EC2), PaaS (np. AWS Elastic Beanstalk / RDS), SaaS (np. Gmail, Office365).
- **Globalna Infrastruktura AWS:**
  - **Regiony:** Geograficznie odizolowane lokalizacje wybierane pod kątem opóźnień (*latency*), kosztów i zgodności prawnej (*compliance*).
  - **Strefy Dostępności (Availability Zones - AZ):** Fizycznie odrębne centra danych. Projektowanie w architekturze *Multi-AZ* pod wysoką dostępność (*High Availability*).
  - **Edge Locations:** Punkty CDN (CloudFront) służące do cache'owania treści blisko użytkownika końcowego.

### 2. Tożsamość i Zarządzanie Dostępem (AWS IAM)
- **Root vs IAM User:** Zabezpieczenie konta głównego (MFA) i codzienne operacje na dedykowanych użytkownikach IAM.
- **Struktury IAM:**
  - **Users & Groups:** Tożsamości i masowe nadawanie uprawnień.
  - **Roles:** Dostęp tymczasowy dla usług i maszyn AWS, eliminujący potrzebę stosowania statycznych kluczy dostępowych (*Access Keys*).
- **Polityki JSON:** Zasada *Implicit Deny* (domyślny brak dostępu) oraz *Explicit Deny* (bezwzględne nadpisanie pozwoleń `Allow`).
- **AWS Organizations:** Centralne zarządzanie wieloma kontami oraz ograniczenia globalne przez polityki SCP (*Service Control Policies*).

### 3. Zasoby Obliczeniowe i Magazynowe (EC2 & EBS)
- **Amazon EC2 (Elastic Compute Cloud):** Wirtualne serwery IaaS. Dobór rodzin instancji (*General Purpose*, *Compute Optimized*, *Memory Optimized*).
- **Amazon EBS (Elastic Block Store):** Trwałe dyski sieciowe odseparowane od cyklu życia samej maszyny wirtualnej.
- **Modele zakupowe EC2:**
  - *On-Demand:* Pełna elastyczność i płatność za sekundy.
  - *Reserved Instances / Savings Plans:* Zniżki do 72% przy deklaracji na 1–3 lata.
  - *Spot Instances:* Wykorzystanie wolnych mocy AWS ze zniżką do 90% (dla zadań odpornych na przerwania pracy). Dane na dyskach EBS pozostają bezpieczne.
  - *Dedicated Hosts:* Najem fizycznego serwera na wyłączność.

### 4. Wirtualne Sieci Prywatne (AWS VPC)
- **Struktura VPC:** Projektowanie prywatnego centrum danych z własną adresacją CIDR.
- **Podsieci (Subnets):**
  - *Public Subnet:* Podsieć z trasą do Internet Gateway (IGW), dedykowana dla serwerów brzegowych/WWW.
  - *Private Subnet:* Odizolowana podsieć bez bezpośredniego dostępu ze świata (dla baz danych i backendu).
- **Ruch wewnętrzny:** Bezpieczna komunikacja między podsieciami wewnątrz chmury za pomocą tras lokalnych (*Local Route*).
- **Warstwy Bezpieczeństwa:**
  - *Security Groups:* Firewall stanowy (*stateful*) na poziomie pojedynczej instancji EC2.
  - *NACL (Network Access Control List):* Firewall bezstanowy (*stateless*) na poziomie całej podsieci.

### 5. Magazyn Obiektowy (Amazon S3) & Bazy Danych (Amazon RDS)
- **Amazon S3:** Bezserwerowy magazyn obiektów o trwałości 11 dziewiątek (99.999999999%). Konfiguracja *Bucket Policies* (JSON) oraz klas przechowywania (*Standard*, *Infrequent Access*, *Glacier*).
- **Amazon RDS:** Zarządzalne bazy relacyjne (PaaS). Konfiguracja replikacji synchronicznej (*Multi-AZ*) oraz asynchronicznych kopii odczytu (*Read Replicas*).
---

## ☁️ Chmura Publiczna (AWS) – Ścieżka Praktyczna & Laboratoria

Poniższe zestawienie przedstawia chronologiczny przebieg moich prac w chmurze AWS – od konfiguracji zabezpieczeń i infrastruktury sieciowej, po automatyzację za pomocą Ansible, Basha i biblioteki `boto3` w Pythonie.

### 📍 Krok 1: Fundamenty, Bezpieczeństwo i IAM
* **Inicjalizacja konta:** Skonfigurowanie konta w *AWS Free Tier* oraz wdrożenie podstawowych zasad bezpieczeństwa.
* **Tożsamość i Dostęp (IAM):**
  * Zabezpieczenie konta `Root` (MFA) i odstawienie go od codziennych operacji.
  * Utworzenie dedykowanego użytkownika technicznego `Admin-user` z ograniczonymi uprawnieniami.
  * Zrozumienie struktur IAM: przeznaczenia użytkowników (*Users*), grup (*Groups*) oraz ról (*Roles*) i polityk tymczasowych.
  * Praca na politykach w formacie JSON (analiza reguł `Allow`, `Implicit Deny` oraz nadpisującego `Explicit Deny`).

### 📍 Krok 2: Pierwsze Wdrożenie EC2 & Warstwy Sieciowe
* **Uruchomienie serwera:** Utworzenie pierwszej maszyny wirtualnej `moj-pierwszy-serwer-devops` (instancja `t2.micro` w regionie `eu-central-1`).
* **Zabezpieczenie dostępu:** 
  * Wygenerowanie klucza SSH (`.pem`), nadanie restrykcyjnych uprawnień lokalnych (`chmod 400`) i nawiązanie bezpiecznego połączenia.
  * Skonfigurowanie zapory *Security Group* z dostępem SSH (port 22) ograniczonym wyłącznie do własnego, publicznego adresu IP.
* **Weryfikacja parametrów:** Diagnostyka serwera z poziomu terminala za pomocą komend `uname` oraz `free -h`.
* **Praca z zaporami sieciowymi:** Przeanalizowanie różnic między stanowym firewallem maszyny (*Security Group*) a bezstanową listą dostępu na poziomie podsieci (*NACL*).

### 📍 Krok 3: Automatyzacja Maszyn (Bootstrapping) & Usługi Pomocnicze
* **EC2 User Data:** Napisanie i wdrożenie skryptu w Bashu przekazywanego przy starcie instancji, który automatycznie instaluje i uruchamia serwer WWW (Nginx).
* **Troubleshooting chmurowy:** Analiza logów startowych `cloud-init` w `/var/log/cloud-init-output.log` oraz weryfikacja ruchu na porcie HTTP (port 80).
* **Storage & Bazy Danych (S3 & RDS):**
  * **Amazon S3:** Utworzenie kubełka, konfiguracja *Bucket Policy* w JSON (`s3:GetObject`) pod serwowanie plików statycznych oraz przeanalizowanie klas przechowywania (*Standard*, *IA*, *Glacier*).
  * **Amazon RDS:** Uruchomienie relacyjnej bazy danych MySQL (PaaS) w architekturze *Multi-AZ*, powiązanie dedykowanej grupy bezpieczeństwa `sg-baza-rds` (port 3306) i modyfikacja parametrów na żywej instancji.

### 📍 Krok 4: Projektowanie Wirtualnej Sieci (AWS VPC)
* **Budowa architektury:** Stworzenie prywatnego centrum danych (VPC) z własną adresacją CIDR.
* **Podział na podsieci:**
  * *Public Subnet:* Podpięcie do *Internet Gateway (IGW)* i tablicy routingu pod usługi wystawione na świat (Nginx / Frontend).
  * *Private Subnet:* Odizolowanie podsieci bez dostępu z internetu dla baz danych (RDS) i backendu.
* **Komunikacja wewnętrzna:** Skonfigurowanie bezpiecznej wymiany ruchu między podsieciami za pomocą tras lokalnych (*Local Route*).

### 📍 Krok 5: Tydzień Konsolidacji – Łączenie AWS, Ansible & Dockera
* **Dzień 1–3 (Trening Składni):** Pisanie na sucho plików `Dockerfile` i playbooków Ansible oraz test z zakresu portów efemerycznych, sieci i identyfikatorów ARN.
* **Dzień 4-6 (Integracja Hybrydowa):** Automatyczna konfiguracja instancji EC2 za pomocą Ansible. Dodanie maszyny do pliku `hosts`, transfer plików `docker-compose.yml` przez SSH i uruchomienie wielokontenerowego stacka (Nginx + MySQL) w chmurze.

### 📍 Krok 6: Programistyczna Automatyzacja Chmury (Python & Boto3)
* **Połączenie z API AWS:** Wstęp do automatyzacji chmury z użyciem Pythona. Konfiguracja biblioteki `boto3` i nawiązanie stabilnego połączenia z API AWS z poziomu kodu.
* **Audyt i Zarządzanie EC2:** Pobieranie szczegółowych metadanych o instancjach EC2 za pomocą API. Praktyczne wykorzystanie pętli, słowników i funkcji w Pythonie do filtrowania i kontroli stanu maszyn wirtualnych.
* **Automatyzacja Magazynu S3:** 
  * Programistyczny upload, download oraz listowanie obiektów w bucketach S3.
  * Stworzenie autorskiego skryptu narzędziowego w Pythonie do audytu i automatycznej retencji/czyszczenia plików w chmurze według określonych kryteriów.
  * Skrypty Boto3 do tworzenia, zarzadzania cyklem zycia i automatycznego sprzatania EC2 po tagach.
* **Tydzień powtórkowy:**
* D1 - Orkiestracja generowania raportu S3 za pomoca Basha i Pythona. Bash uruchamia skrypt w Boto3, który pobiera potrzebne info o zawartości S3 + generuje raport.csv. Bash wyświetla jego treść.
* D2 - konteneryzacja skryptu Boto3 - pobieranie raportu S3 wewnatrz Dockera. Mix: boto3, Dockerfile, docker-compose
* D3 - uruchamianie EC2 z Bashem w UserData, który instaluje nginx w celu wygenerowania raportu z podstawowymi info o systemie.
* D4 - tworzenie EC2 w Boto3 i pelna konfiguracja przez Ansible - spore problemy z kluczami.
* D5 - Wdrozenie pelnego hybrydowego pipeline'a Python Boto3 + Ansible na AWS EC2. Teoria i zrozumienie działania, jutro praktyka.
* D6 - pełny pipeline Boto3 > Ansible > AWS EC2. W 85% moja robota. Oficjalne zakończenie powtórek. Wstęp teoretyczny do Terraform.
### 📍 Krok 7: Rozpoczęcie nauki Terraform
* Teoria i zapoznanie się ze składnią.
* Pierwsze uruchomienie Bucketa S3 i zastosowanie variables.tf i outputs.tf przy budowaniu S3.
* Pobieranie AMI przez data source, Security Group i instancja EC2.
---
*Repozytorium jest stale aktualizowane w miarę moich codziennych postępów w nauce DevOps.*
