# ClientHub — CI/CD

Application Flask proposant deux endpoints :
- /health : indique que l'application fonctionne.
- /clients : retourne une liste de clients.

## Pipeline

Chaque push sur main déclenche automatiquement :
1. Les tests unitaires avec pytest.
2. Les tests E2E par requêtes HTTP vers l'application conteneurisée.
3. La construction et la publication de l'image sur Docker Hub.
4. Le déploiement sur une VM Azure via SSH.
5. La vérification HTTP de l'application déployée.

Si les tests échouent, l'image n'est pas publiée et le déploiement ne se lance pas.

## Choix techniques

- Flask pour l'API.
- pytest et requests pour les tests.
- Docker pour conteneuriser l'application.
- GitHub Actions pour automatiser la pipeline.
- Une image identifiée par le SHA du commit pour déployer la version testée.
- Un conteneur nommé clienthub-jason, remplace a chaque deploiement, pour eviter les doublons.
- Le port public 8023 redirige vers le port 5000 du conteneur.
- Les identifiants Docker Hub et SSH sont stockés dans GitHub Secrets.

## Tests locaux

Depuis la racine du projet :
py -m pytest tests/test_unit.py

Pour les tests E2E, demarrer le conteneur sur le port local 5002 puis lancer :
py -m pytest tests/test_e2e.py
