# Web App Flask PDF to Excel Table

Ce projet permet de convertir des fichiers PDF contenant des tables en fichiers Excel à l'aide d'une application web développée avec Flask. L'application extrait les tables de chaque page du PDF et les combine dans un fichier Excel téléchargeable.

## Fonctionnalités

- **Conversion PDF en Excel** : Extrait les tables contenues dans un fichier PDF et les convertit en un fichier Excel.
- **Support de plusieurs pages** : Extrait les tables de toutes les pages du PDF, et non seulement de la première.
- **Interface utilisateur simple** : Une interface web intuitive pour télécharger le fichier PDF et récupérer le fichier Excel converti.

## Technologies utilisées

- **Flask** : Framework web Python pour développer l'application.
- **pdfplumber** : Librairie Python pour extraire des tables à partir de fichiers PDF.
- **pandas** : Librairie pour manipuler les données et les convertir en format Excel.
- **HTML, CSS** : Pour l'interface utilisateur.
- **PythonAnywhere** : Hébergement de l'application web en ligne.

# Déployer une Application Flask sur PythonAnywhere

Suivez ces étapes pour déployer votre application Flask sur **PythonAnywhere**.

## Prérequis

Avant de commencer, assurez-vous que vous avez :
- Un compte sur **PythonAnywhere** (si vous n'en avez pas, créez-en un sur [PythonAnywhere](https://www.pythonanywhere.com/)).
- Le code de votre projet prêt à être déployé.

## Étapes de Déploiement

### 1. Créer un Compte PythonAnywhere

- Allez sur [PythonAnywhere](https://www.pythonanywhere.com/).
- Créez un compte ou connectez-vous si vous en avez déjà un.

### 2. Créer une Nouvelle Application Web

1. Une fois connecté à votre compte PythonAnywhere, cliquez sur l'onglet **"Web"** en haut de la page.
2. Cliquez sur le bouton **"Add a new web app"**.
3. Sélectionnez le **nom de domaine** que vous souhaitez (par exemple, `votre_utilisateur.pythonanywhere.com`).
4. Choisissez le framework **Flask** parmi les options proposées.
5. Sélectionnez la version de Python que vous utilisez pour votre application.

### 3. Configurer l'Application Flask sur PythonAnywhere

1. **Télécharger votre code sur PythonAnywhere** :
   - Vous pouvez utiliser l'éditeur de fichiers intégré pour créer des fichiers ou charger vos fichiers directement via **SFTP**.
   - Vous pouvez également utiliser **Git** pour cloner votre repository GitHub directement sur PythonAnywhere :

2. **Configurer le WSGI** :
   - PythonAnywhere crée automatiquement un fichier `wsgi.py` pour votre application Flask.
   - Modifiez ce fichier en ajoutant les bonnes configurations. Le fichier `wsgi.py` devrait ressembler à ceci :
     ```python
     WSGI.py
     import sys
     sys.path.insert(0, '/home/votre_utilisateur')  # Remplacez ce chemin par le bon chemin de votre répertoire
     Importation de l'application Flask depuis MH.py
     from MH import app as application  # L'instance 'app' de votre application Flask est renvoyée sous le nom 'application'voyée sous le nom 'application'
     ```
   - Remplacez `votre_utilisateur` par votre nom d'utilisateur PythonAnywhere et assurez-vous que le chemin vers votre projet est correct.
  
 3. **Explication des dépendances** :

- **Flask** : Framework web léger pour développer des applications web en Python.
- **pdfplumber** : Bibliothèque pour extraire des tables à partir de fichiers PDF.
- **pandas** : Bibliothèque de manipulation et d'analyse de données, utilisée pour convertir les tables extraites en format Excel.
- **openpyxl** : Bibliothèque nécessaire pour écrire des fichiers Excel avec Pandas.

### 4. Configurer les Dossiers de Fichiers

1. Assurez-vous que les dossiers `uploads/` et `outputs/` sont créés dans le répertoire de votre projet. Ces dossiers sont utilisés pour stocker les fichiers téléchargés et générés.
   
2. Vous pouvez créer ces dossiers via l'interface de gestion des fichiers de PythonAnywhere ou directement depuis la console PythonAnywhere :
   ```bash
   mkdir /home/votre_utilisateur/pdf-to-excel-converter/uploads
   mkdir /home/votre_utilisateur/pdf-to-excel-converter/outputs

## 5. Redémarrer l'Application Web

Une fois toutes les étapes de configuration terminées, revenez à l'onglet **"Web"** de PythonAnywhere.

1. Cliquez sur le bouton **"Reload"** pour redémarrer votre application et appliquer les changements.

## 6. Accéder à Votre Application Web

Une fois l'application redémarrée, vous pouvez accéder à votre application Flask via l'URL suivante :

[https://mhamed.pythonanywhere.com/](https://mhamed.pythonanywhere.com/) 

(remplacez `mhamed` par votre nom d'utilisateur PythonAnywhere).

## Contributing
Feel free to contribute by submitting issues or pull requests.

## License
This project is licensed under the MIT License.

## Author
[Kurama-90](https://github.com/Kurama-90)
