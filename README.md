Hei, I denne guiden skal jeg vise hvordan
1. Installere OS til Raspberry Pi via RPI Imager (Raspberry pi imager)
2. Sette opp Pi
3. Sette opp SSH
4. Sette opp MariaDB

Først gå til https://www.raspberrypi.com/software/ bla ned og trykk på download for windows
![image](https://github.com/user-attachments/assets/ea38748d-a2f8-4d13-a993-eae9a892eb7f)
etter du har downloaded det trykk på downloads og trykk på imager_exe
![image](https://github.com/user-attachments/assets/9f01cefa-c675-45bb-bddd-785bc63cfa6e)

Etter det put in SD korte fra PI og put den i Pc'n 
eller en annen måte til å koble den til pc'n når imager_exe starter opp følg stege og la den runne

når du har kommet hit trykk på hvilken OS og hvilken versjon an Pi din er og velg SD korte på storage (I denne guiden bruker vi ubuntu)
![image](https://github.com/user-attachments/assets/14e2234f-a5e1-4117-b505-226415c82b4b)

trykk next og følg stegene, ta ut SD korte og put det inn i Raspberry Pi'en la den kjøre og følg stegene på startup f.eks velg norsk språk osv osv

når den har gjort alt det og du er på hjemskjermen til ubuntu trkk
**CTRL + ALt + T** for å ta opp cmd applikasjonen
skriv eller kopier og paste
```sudo apt update```
```sudo apt upgrade ```
dette oppdatterer og installerer til programvare som er installert
nå for brannmur gjør
```sudo apt install ufw```
```sudo ufw enable ```
```sudo ufw allow ssh``` (tillater ssh remote login)
og du kan gjøre ```sudo ufw status``` til å sjekke statusen

```kode```

**bold**

www.elkjøp.no
