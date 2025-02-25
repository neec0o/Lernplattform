# Dashboard Lernplattform - Architektur & Features  

## Ziele  
- Tägliche Themenanzeige aus einem Pool von Themen  
- Multiple-Choice-Fragen mit Auswertung  
- Statistik zu bearbeiteten Themen und Fragenperformance  
- Möglichkeit zum Posten neuer Themen und Fragen  
- Benutzer-Authentifizierung und -Autorisierung  

---

## Frontend-Module  
### Dashboard  
- Themen des Tages  
- Fragekarten (Multiple-Choice)  
- Statistik (Themen & Fragen)  

### Posten & Erstellen  
- Neues Thema erstellen  
- Neue Frage erstellen  

### Benutzerbereich  
- Login & Registrierung  
- Profilverwaltung  

---

## Backend (FastAPI) Struktur  
### Endpoints  
- `POST /login` & `POST /register` – Benutzerverwaltung  
- `GET /topics/today` – Tägliche Themen  
- `GET /questions/daily` – Fragen des Tages  
- `POST /questions/submit` – Antworten übermitteln  
- `GET /statistics/topics` – Statistik zu bearbeiteten Themen  
- `GET /statistics/questions` – Fragenperformance  
- `POST /topics/new` – Neues Thema posten  
- `POST /questions/new` – Neue Frage posten  

### Services  
- **AuthService:** JWT-Token-Verwaltung  
- **TopicService:** Verwaltung der Themen  
- **QuestionService:** Verwaltung der Fragen  
- **StatisticsService:** Berechnung der Statistiken  

---

## Datenbankstruktur  
### User  
- `id`: Primärschlüssel  
- `username`: Benutzername  
- `password`: Gehashtes Passwort  
- `email`: E-Mail-Adresse  
- `created_at`: Registrierungsdatum  

### Topic  
- `id`: Primärschlüssel  
- `title`: Titel des Themas  
- `description`: Beschreibung des Themas  
- `created_at`: Erstellungsdatum  
- `author_id`: Referenz zu User  

### Question  
- `id`: Primärschlüssel  
- `question_text`: Die Frage selbst  
- `answer_options`: Liste der Antwortmöglichkeiten  
- `correct_answer`: Richtige Antwort  
- `topic_id`: Zugehöriges Thema  

### UserProgress  
- `user_id`: Referenz zu User  
- `completed_topics`: Liste von bearbeiteten Themen (Topic IDs)  
- `answered_questions`: Liste von beantworteten Fragen (Question IDs)  
- `statistics`: Richtig/Falsch Zähler  

---

## Authentifizierung & Autorisierung  
- **JWT-Token:**  
  - Login generiert Token  
  - Token bei jedem Request zur Authentifizierung geprüft  
  - Rollen: User, Admin (für das Erstellen von Themen & Fragen)  

---

## Technologie-Stack  
- **Backend:** FastAPI, SQLAlchemy (für ORM), Pydantic (Datenvalidierung)  
- **Datenbank:** PostgreSQL (oder SQLite für Entwicklung)  
- **Frontend:** Wahlweise plain HTML/JS oder mehr 'advanced' - React, Vue.js oder Svelte  
- **Authentifizierung:** JWT-Token mit FastAPI JWT Auth  
- **Hosting:** Docker-Containerisierung möglich  

---

## API-Flussdiagramm  

Frontend --> FastAPI Endpoint --> Authentifizierung (JWT-Token) --> Datenbank (PostgreSQL) 
<-- Antwort von FastAPI <--

---

## Tasks & Verantwortlichkeiten  
- **Backend-Entwicklung:** FastAPI Endpoints, AuthService, Datenbankmodelle  
- **Frontend-Entwicklung:** UI für Dashboard, Fragen, Statistiken, Login  
- **Datenbank:** Schema-Design, Migrationen, Datenvalidierung  
- **Testing:** Unit-Tests für Endpoints und Services  

