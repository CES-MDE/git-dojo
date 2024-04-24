# git-dojo

## Introduction à GitHub

### Qu'est-ce que GitHub ?

GitHub est une plateforme de développement de logiciels basée sur le système de contrôle de version Git. Il offre un environnement collaboratif pour les développeurs afin de travailler ensemble sur des projets logiciels, de gérer les versions de code et de suivre les problèmes. Autrement dit c'est système de partage et de sauvegarde de code. 

### Pourquoi utiliser GitHub ?

GitHub présente plusieurs avantages pour les développeurs et les équipes de développement :

- **Gestion du code source :** GitHub permet de stocker et de gérer efficacement le code source de projets logiciels, offrant un historique complet des modifications apportées au code.
- **Collaboration :** Les équipes peuvent collaborer facilement sur des projets, travailler simultanément sur des branches et fusionner leurs modifications en toute sécurité.
- **Suivi des problèmes :** GitHub propose un système de gestion des problèmes (issues) permettant de signaler les bugs, de demander des fonctionnalités et de suivre les discussions.
- **Pull requests :** Les pull requests sont utilisées pour proposer des modifications de code à intégrer dans le projet principal. Elles facilitent la revue de code et la collaboration entre les membres de l'équipe.
- **Documentation :** GitHub offre des fonctionnalités pour créer et héberger des wikis et des pages de documentation, facilitant ainsi la création et la maintenance de documentation pour les projets.(si vous êtes chaud)
- **Intégrations et automatisation :** GitHub propose des intégrations avec de nombreux outils de développement tiers, ainsi que des fonctionnalités d'automatisation (GitHub Actions) pour automatiser les workflows de développement.(si vous êtes vraiment hyper chaud)

### Création d'un compte GitHub

Pour créer un compte GitHub, suivez ces étapes simples :

1. Rendez-vous sur le site web de GitHub à l'adresse [github.com](https://github.com/).
2. Cliquez sur le bouton "Sign up" (S'inscrire) en haut à droite de la page d'accueil.
3. Remplissez le formulaire d'inscription en fournissant votre nom d'utilisateur, votre adresse e-mail et votre mot de passe.
4. Suivez les instructions pour vérifier votre adresse e-mail et terminez le processus d'inscription.
5. Une fois votre compte créé, vous pouvez commencer à utiliser GitHub pour héberger vos projets, collaborer avec d'autres utilisateurs et contribuer à des projets open source.

### Installation de Git

Pour installer Git sur votre ordinateur, suivez les instructions spécifiques à votre système d'exploitation :

- **Windows :** Téléchargez l'installateur Git à partir du site web officiel de Git à l'adresse [git-scm.com](https://git-scm.com/) et suivez les instructions d'installation.
- **MacOS :** Vous pouvez installer Git en utilisant Homebrew, un gestionnaire de paquets pour MacOS. Ouvrez Terminal et exécutez la commande suivante : 
```bash
brew install git
```
- **Linux :** Utilisez le gestionnaire de paquets de votre distribution Linux pour installer Git. Par exemple, sur Ubuntu, vous pouvez installer Git en exécutant la commande suivante dans Terminal : 
```bash
sudo apt-get install git
```

## Utilisation de ce repository

1. **Clonage du repository :** Pour cloner ce repository sur votre ordinateur, utilisez la commande suivante :
```bash
git clone https://github.com/QuentinSamudioMines/git-dojo.git
```
**Si vous avez VScode**, quand vous ouvrez une nouvelle fenêtre, vous pouvez directement appuyer sur "Clone Git Repository ...". 

2. **Création d'une nouvelle branche :**  Pour créer une nouvelle branche à partir de la branche principale (généralement main ou master), utilisez la commande suivante :
```bash
git checkout -b ma-nouvelle-branche
```
**Si vous avez VScode**, vous pouver clicker sur le signe de git en bas à gauche de l'écran puis appuyé sur entré. Insérer ensuite le nom de la branch. Vous pouvez maintenant publier la branche en retournant dans la fenêtre "Source Control.

2. **Ajout et commit des modifications :** Faites vos modifications dans les fichiers du projet. Une fois vos modifications terminées et sauvegardé sur votre machine, utilisez les commandes suivantes pour ajouter et commit vos changements :
```bash
git add .
git commit -m "Description de votre modification"
```
**Si vous avez VScode**, dans le fenêtre "Source Control" appuyer sur les signes + à coté des fichiers que vous voulez commit pour les "stage" / "mettre en scène" / "pre-commit". Une fois les modification que vous voulez commits "staged" vous pouvez appuyer sur commit pour le sauvegarder en local. Appuyer ensuite sur push ou publish pour l'envoyer sur Github. 