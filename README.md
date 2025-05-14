**Future Skills Assignment – DevOps Engineer (Modernisation)**
Uitwerking van de future skills assignment

**Opdracht 1**
Doel: Simpele reverse proxy setup tussen Nginx en een webservice.
Structuur:
•	reverse-proxy: maakt een Nginx-image uit ./nginx.
•	web: maakt een webcontainer uit ./web.
Netwerk:
•	Beide containers zitten in een custom bridge netwerk app-network.
Poorten:
•	Externe poorten 80 en 443 worden gemapt naar de Nginx container.
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

Gebruik
Alle projecten heb ik in studio code gezet met de docker plugin. Je kan dan gewoon rechtsklikken op de docker compose file en builden. Zelf deed ik visio vanuit een wsl gebruiken. Dan stonden de containers meteen op mijn wsl.

