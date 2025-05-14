# Future Skills Assignment – DevOps Engineer (Modernisation)

Uitwerking van de future skills assignment

## Hoe kan ik alles uitvoeren:
Alle projecten heb ik in studio code gezet met de docker plugin. Je kan dan gewoon rechtsklikken op de docker compose file en builden. Zelf deed ik visio vanuit een wsl gebruiken. Dan stonden de containers meteen op mijn wsl.

1. Zorg ervoor dat Docker en Docker compose geïnstalleerd zijn op je machine.
2. Open je terminal en navigeer naar de projectmap waarin je `docker-compose.yml` staat.
3. klik rechts op de docker-compose file en klik docker compose up

## Reverse Proxy Logic

In deze opdracht is een reverse prox opgezet met Nginx, die inkomende verzoeken op poort 80 en 443 doorstuurt naar de frontend (`web`) en backend (`backend`) services. 

De reverse proxy is geconfigureerd via een Nginx-configuratiebestand (`default.conf`), waarin de volgende logica is geïmplementeerd:
- Frontend (web): Verzoeken naar de root van de applicatie (bijv. `/`) worden doorverwezen naar de `web` container.
- Backend: Verzoeken naar de backend-API (bijv. `/api/`) worden doorverwezen naar de `backend` container.

Het configuratiebestand maakt gebruik van de standaard Nginx-functionaliteit voor load balancingen request forwarding.

Een voorbeeld van de reverse proxy configuratie in `default.conf`:
```nginx
server {
    listen 80;

    location / {
        proxy_pass http://web:80;
    }

    location /api {
        proxy_pass http://backend:5000;
    }
}

## Security and Test Plans

### Security
- De Docker containers worden beheerd met behulp van environment variables voor configuratie-instellingen zoals de `DEBUG` mode in de backend.
- Er wordt een reverse proxy (Nginx) gebruikt voor het afschermen van de backend services van direct extern verkeer. Alleen de reverse proxy is direct toegankelijk vanaf het internet via poorten 80 en 443.
- SSL en HTTPS configuraties kunnen in de toekomst worden toegevoegd voor versleuteling van het verkeer.

### Test Plans
- Healthchecks: Zowel de webservice als de backendservice zijn voorzien van healthchecks. Deze zorgen ervoor dat Docker kan controleren of de services gezond zijn en automatisch opnieuw opstarten als dat nodig is.
- Backend Healthcheck:
  - Test: `curl http://localhost:5000/api/health`
  - Als de service niet reageert, zal de container opnieuw opstarten.
- Web Healthcheck:
  - Test: `curl http://localhost/`
  - Als de webservice niet reageert, wordt de container opnieuw opgestart.



**Opdracht 1**
Doel: Simpele reverse proxy setup tussen Nginx en een webservice.
Structuur:
•	reverse-proxy: maakt een Nginx-image uit ./nginx.
•	web: maakt een webcontainer uit ./web.
Netwerk:
•	Beide containers zitten in een custom bridge netwerk app-network.
Poorten:
•	Externe poorten 80 en 443 worden gemapt naar de Nginx container.

![image](https://github.com/user-attachments/assets/93a63564-d96a-4747-87ef-8302e53214f6)

________________________________________
**Opdracht 2**
Doel: Reverse proxy met een frontend (web) en een backend service, beide met healthchecks.
Structuur:
•	web: Frontend container met healthcheck op /.
•	backend: Backend met healthcheck op /api/health.
•	reverse-proxy: Gebaseerd op nginx:alpine en gebruikt een custom default.conf.
Omgevingsvariabelen:
•	DEBUG voor de backend.
•	WEB_PORT voor poortmapping van de proxy.

![image](https://github.com/user-attachments/assets/c2a5fd9d-6238-4765-9cb9-c0ea21c5bb52)

________________________________________
**Opdracht 3**
Doel: Monitoringstack met twee backend containers, reverse proxy, en observability tools (Grafana + Loki + Promtail).
Structuur:
•	backend1 & backend2: Twee identieke backends voor load balancing.
•	nginx: Reverse proxy die beide backends kan load balancen.
•	loki: Logging
•	promtail: Verzamelt logs van containers.
•	grafana: verzamelt logs in dashboards.
Credentials Grafana:
•	Gebruiker: patrick
•	Wachtwoord: hallo2
Poorten:
•	Nginx: 80, 443
•	Loki: 3100
•	Grafana: 3000

![image](https://github.com/user-attachments/assets/82ec6475-0843-40ab-a5ae-8bfb09b6949b)

