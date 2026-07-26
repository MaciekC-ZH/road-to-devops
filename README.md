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
4. **Root User vs IAM User:** Konto główne (Root) posiada nieograniczony dostęp i po konfiguracji MFA powinno być zabezpieczone i nieużywane      do codziennej pracy. Do operacji DevOps tworzy się dedykowanych użytkowników IAM o ograniczonym dostępie.
5. **Struktury IAM:**
   * **Users:** Tożsamości dla fizycznych osób lub zewnętrznych aplikacji.
   * **Groups:** Zbiory użytkowników ułatwiające masowe nadawanie uprawnień.
   * **Roles:** Tożsamości o charakterze tymczasowym przeznaczone dla maszyn i usług wewnętrznych AWS, eliminujące potrzebę używania              niebezpiecznych, statycznych kluczy dostępowych (*Access Keys*).
6. **Logika Polityk IAM (JSON):** Domyślnie każdy dostęp w AWS jest zabroniony (*Implicit Deny*). Uprawnienia są nadawane przez deklaracje   `Allow`. Kluczowa zasada bezpieczeństwa: jawne zaprzeczenie (*Explicit Deny*) zawsze nadpisuje i blokuje wszelkie pozwolenia `Allow`.
7. **Skala Korporacyjna (AWS Organizations):** Centralne zarządzanie wieloma kontami AWS za pomocą jednej skonsolidowanej faktury oraz globalne ograniczanie uprawnień na poziomie całych kont za pomocą polityk SCP (*Service Control Policies*).
8. ### Moce Obliczeniowe Chmury (AWS EC2 & EBS)
A. **Amazon EC2 (Elastic Compute Cloud):** Wirtualne serwery w chmurze (model IaaS). Dzielą się na rodziny instancji w zależności od potrzeb: General Purpose (ogólne, np. t2.micro we Free Tier), Compute Optimized (pod procesor) oraz Memory Optimized (pod dużą ilość RAM, np. dla bazy Redis).
B. **Amazon EBS (Elastic Block Store):** Wirtualne, sieciowe dyski twarde dopinane do maszyn EC2. Żyją niezależnie od samych serwerów, co pozwala na bezpieczne przepinanie danych między instancjami w przypadku awarii komputera.
C. **Modele zakupowe EC2:**
   * **On-Demand:** Płatność za sekundy działania, pełna elastyczność, najwyższa cena bazowa.
   * **Reserved Instances / Savings Plans:** Zniżki do 72% w zamian za deklarację korzystania z maszyn przez 1 rok lub 3 lata (dla stałych systemów produkcyjnych).
   * **Spot Instances:** Giełda wolnych mocy AWS ze zniżkami do 90%. Ryzyko wyłączenia maszyny przez AWS w ciągu 2 minut. Idealne do zadań odpornych na przerwania (np. przetwarzanie wsadowe, renderowanie, testy).
   * **Dedicated Hosts:** Wynajem całego fizycznego serwera na wyłączność.
   * * **Spot Instances:** Giełda wolnych mocy AWS ze zniżkami do 90%. Ryzyko wyłączenia maszyny przez AWS w ciągu 2 minut. Dane na podpiętym dysku EBS nie giną (EBS żyje niezależnie), jednak automatyczne uruchomienie nowej maszyny Spot i ponowne wpięcie dysku wymaga oprogramowania automatyzacji (np. za pomocą Auto Scaling Group i skryptów startowych). Idealne do zadań odpornych na przerwania.
* ### Status Konta AWS:
- AWS Free Tier Account: UTWORZONE (Gotowe do laboratoriów praktycznych).
- AWS Admin-user (non-root), zabezpieczenia.
  ### Status Laboratorium EC2 (Pierwsze Wdrożenie):
- Pierwszy serwer w chmurze: URUCHOMIONY (`moj-pierwszy-serwer-devops` w regionie eu-central-1).
- Zabezpieczenie sieciowe: Firewall (Security Group) skonfigurowany wyłącznie na domowy publiczny adres IP.
- Autentykacja: Pomyślne połączenie SSH przy użyciu dedykowanego klucza `.pem` z restrykcyjnymi uprawnieniami `chmod 400`.
- Weryfikacja zasobów: Maszyna pomyślnie zweryfikowana komendami `uname` oraz `free -h` pod kątem parametrów Free Tier.
  **Warstwowość zabezpieczeń sieciowych (Security Group vs NACL):**
   * **Security Group:** Firewall stanowy (*stateful*) na poziomie pojedynczego serwera EC2. Automatycznie zezwala na ruch powrotny. Używany do codziennego zarządzania portami aplikacji (np. port 22 dla SSH, port 80 dla HTTP).
   * **NACL (Network Access Control List):** Firewall bezstanowy (*stateless*) na poziomie całej podsieci (*subnet*). Wymaga jawnego definiowania ruchu wejściowego i wyjściowego. Służy do globalnych reguł bezpieczeństwa (np. masowe blokowanie złośliwych adresów IP).
* ### Automatyzacja Instancji (EC2 User Data):
- Bootstrapping: Pomyślnie wdrożono automatyczną konfigurację serwera Nginx za pomocą skryptu instalacyjnego Bash przekazanego jako *User Data*.
- Diagnostyka i Troubleshooting: Opanowano proces weryfikacji logów automatyzacji chmurowej w pliku `/var/log/cloud-init-output.log` zarządzanym przez mechanizm `cloud-init`.
- Świadomość sieciowa: Przeanalizowano zachowanie przeglądarek wymuszających protokół HTTPS (port 443) i upewniono się o konieczności jawnego testowania nieszyfrowanych portów HTTP (port 80) w fazie deweloperskiej.
- ## Chmurowy Magazyn Danych (Amazon S3)
### Opis i cel
Zrozumienie działania bezserwerowego magazynu obiektów (Object Storage) Amazon S3, konfiguracji polityk dostępu (Bucket Policies) oraz optymalizacji kosztów przechowywania danych.
### Opanowane pojęcia i umiejętności:
1. **Zasada działania S3:** Magazynowanie obiektów (pliki + metadane) w kubełkach (Buckets). Globalna unikalność nazw kubełków oraz trwałość danych na poziomie 11 dziewiątek (99.999999999%) dzięki automatycznej replikacji między minimum 3 Strefami Dostępności (AZ).
2. **Zarządzanie uprawnieniami (JSON Bucket Policy):** Zrozumienie, że wyłączenie *Block Public Access* to za mało – domyślnie zasoby są zablokowane (*Implicit Deny*). Skonfigurowano politykę kubełka w formacie JSON (`s3:GetObject`), udostępniającą pliki statyczne dla całego internetu (`Principal: *`).
3. **Klasy przechowywania (Storage Classes):**
   * *S3 Standard* – wysoka wydajność, ciągły dostęp.
   * *S3 Infrequent Access (IA)* – rzadki dostęp, tańszy zapis, opłata za odczyt.
   * *S3 Glacier (Deep Archive)* – zamrażarka danych, najniższy koszt, czas odmrażania danych do kilkunastu godzin (pod backupy i compliance).
* ## Zarządzalne Bazy Danych (Amazon RDS)
### Opis i cel
Uruchomienie i konfiguracja relacyjnej bazy danych MySQL w chmurze za pomocą usługi Amazon RDS (Platform as a Service) oraz zabezpieczenie jej na poziomie sieciowym.
### Opanowane pojęcia i umiejętności:
1. **Zalety Amazon RDS:** Automatyzacja backupów, patchowania oraz skalowania zasobów bez konieczności administracji systemem operacyjnym.
2. **Architektura wysokiej dostępności i wydajności:**
   * **Multi-AZ:** Synchroniczna replikacja do zapasowej bazy w innej strefie dostępności z automatycznym failoverem (High Availability).
   * **Read Replicas:** Asynchroniczne kopie bazy służące do odciążania ruchu poprzez kierowanie zapytań `SELECT` na serwery lustrzane.
3. **Zabezpieczenie sieciowe bazy:** Przypisanie dedykowanej grupy bezpieczeństwa `sg-baza-rds` i otwarcie portu domyślnego dla MySQL (**3306**) wyłącznie dla bezpiecznego, domowego adresu IP (*My IP*).
4. **Troubleshooting interfejsu AWS:** Opanowanie modyfikacji parametrów łączności i grup bezpieczeństwa bezpośrednio na działającym zasobie chmurowym.
5. ## Wirtualne Sieci Prywatne (AWS VPC)
### Opis i cel
Zrozumienie podstaw projektowania odizolowanych środowisk sieciowych w chmurze AWS oraz separacji zasobów na podsieci publiczne i prywatne.
### Opanowane pojęcia:
1. **AWS VPC:** Prywatne, wirtualne centrum danych inżyniera w chmurze z własną adresacją CIDR.
2. **Podsieci (Subnets):**
   * *Public Subnet* – podsieć z trasą do Internet Gateway, dedykowana dla usług frontendowych/serwerów WWW.
   * *Private Subnet* – odizolowana podsieć bez dostępu ze świata, dedykowana dla baz danych (RDS) i backendu.
3. **Internet Gateway (IGW) & Route Tables:** Mechanizmy routowania ruchu chmurowego i definiowania "okien na świat" dla podsieci publicznych.
4. **Ruch wewnętrzny:** Zrozumienie, że komunikacja między podsiecią publiczną a prywatną odbywa się bezpiecznie wewnątrz chmury za pomocą tras lokalnych (*Local Route*), bez potrzeby wystawiania wrażliwych zasobów do internetu.
Tydzień powtórkowy:
D1 - pisanie na sucho dockerfile + Ansible + pytania toretyczne
D2 - pisanie na sucho playbooka + pytania o ARN, porty efemeryczne, sieć publiczna vs prywatna
D3 - zadanie praktyczne. Konfiguracja instancji EC2 za pomocą playbooka Ansible: dodanie maszyny do pliku hosts w celu uzyskania połączenia SSH, automatyczne skopiowanie pliku docker-compose z lokalnej VM na EC2 oraz uruchomienie stacku kontenerów (Nginx + MySQL).
D4 - wstęp teoretycny do Boto3, czyli zadządzanie EC2 za pomocą biblioteki Pythona - początki automatyzacji.
D5 - połączenie się do EC2 przez API Pythona, działające połączenie.
D6 - wyciąganie danych o instancji EC2 za pomocą Boto3 - praktyczne zrozumienie podstaw.
D7 - pobieranie danych za pomocą Boto3 - ciąg dalszy. Powtórki Pythona z pętli, słowników i funkcji.
D8 - upload i dowload z bucketu S3. Listowanie obiektów z S3 i wybranych parametrów. Skrypt do audytu i automatycznego czyszczenia plików wg. kryteriów.
---
*Repozytorium jest stale aktualizowane w miarę moich codziennych postępów.*
