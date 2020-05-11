## Travail effectué 

=> Description hebdomadaire du travail effectué (variez les auteurs    ! )          
### Semaine 1

Durant cette semaine nous avons pu distribuer les tâches de la recherche au sein du groupe. Nous avons pu mettre en évidence certains points sur lesquels nous aurions pu avoir certaines difficultés, c'est ainsi que nous avons pu attribuer les délais pour les tâches. Nous avons aussi profité de cette semaine pour créer les bases du support de la recherche.

##### Par G. Kounkoud

Durant cette semaine j'ai pu me replonger dans mes cours de Python du premier semestre, faisant une liste des éléments que j'aurais potentiellement besoin lors de la programmation du programme. J'ai d'emblée su que j'aurais besoin d'une interface simple, comportant un tableau de n * n cases. Le besoin de boutons pour lancer la simulation, l'arrêter et fermer la fenêtre.
Trouver une manière d'éditer le tableau pour pouvoir ajouter ou retirer des cellules dans le tableau.

##### Par Y. Soukehal

Cette semaine était également consacrée à un travail de recherche gobale de mon côté. En effet je ne connaissais pas encore cet automate cellulaire. Ainsi, j'ai pu m'informer sur son origine, et plus globalement, sur les causes de sa popularité.

##### Par C. Lebrati & K. Vallipuram

### Semaine 2

J'ai commencé la base du programme, créé une fenêtre, ainsi que le tableau composé d'un tableau composé de lignes verticales et horizontales créant les cellules dans lesquelles on pourra éditer la disposition des cellules.
La base faite, j'ai pu me pencher sur la question des boutons intégrés à l'interface graphique. Pour cela j'ai du m'appuyer sur quelques forum de programmation Python.
L'addition d'un bouton pour fermer la fenètre est donc maintenant faite (ce qui rend le visuel et l'utilisation plus intuitif.).

##### Par Y. Soukehal

Ma deuxième semaine de travail était consacrée à la recherche, plus détaillée, sur le fonctionnement du jeu de la vie, ses résultats tous différents les uns des autres, ses variantes de règles et les possibilités qu'offre cet automate cellulaire.

##### Par C. Lebrati & K. Vallipuram

Semaine d'initiation Github, début de la mise en place du corps du site. A l'aide des videos mises en place sur Moodle ainsi que quelque videos sur l'installation de Git sur mac la création des premiers fichiers du site, choix du thème, test d'envoie des fichiers en local ont été faits.

##### Par G.Kounkoud

### Semaine 3

Cette semaine sera consacrée à la réalisation plus complexe du code. Avant tout, il fallait que je puisse transcrire les règles du jeu de la vie en Python, pour cela, j'ai passé une bonne heure et demie à imaginer chaque situation et à écrire le code Python. J'ai finalement réalisé que ça serait bien plus compliqué que ce que je pensais.
J'ai donc posé les bases du programme, c'est à dire éditer le tableau (ajouter une cellule ou la supprimer). Une fonction pour le clique droit et pour le clique gauche ont donc été créés.

##### Par Y. Soukehal

La troisième semaine de travail était consacrée, pour moi, à la vérification des sources que j'ai utilisé lors de mes recherches, j'ai entrecoupé et vérifié les informations afin d'être sûr de ne pas me tromper sur le jeu de la vie.

##### Par C. Lebrati & K. Vallipuram

### Semaine 4

J'ai accordé cette semaine à la longue partie concernant le coeur du programme. Une fonction pour compter le nombre de cellules vivantes autour d'une cellule donnée. Avant tout il faut créer des boutons pour démarrer et stopper la simulation qui progressera au sein du tableau. Ceci étant fait, j'ai finalement rédigé les lignes du compteur, représentant les 4 réglès du Jeu de La Vie.

##### Par Y. Soukehal

Lors de la semaine 4, j'ai principalement continuer mes recherches, j'ai aussi commencé à rédiger une partie du carnet de bord, l'introduction, mais c'était un brouillon que je pourrais étoffer plus tard.

##### Par C. Lebrati & K. Vallipuram

Analyse du programme Python en cours, debut de la mise en place des différentes informations sur le site pour un test afin d'évaluer le rendu. Début de l'analyse basé sur le fonctionnement du jeu de la vie et reflexion sur la stratégie à adopter pour la présentation des résultats.

##### Par G.Kounkoud

### Semaine 5

Durant cette semaine je fais face au problème sur lequel j'étais tombé la semaine dernière: je n'avais pas pensé à comment
les cellules evolueraient au sein du tableau, je créé alors une fonction Image_Suivante qui permettra d'afficher l'état du tableau au tour n+1, et je met à jour mon code réalisé la semaine dernière.
Encore un nouveau problème: la boucle n'est pas bien réalisée et il faut donc que j'appuie consécutivement sur le bouton Commencer pour incrémenter d'un tour. De plus, il semblerait que le programme fonctionne, mais hors des limites du tableau créées.
Après de multiples essais et une relecture acharnée du code, j'ai réalisé qu'une erreur d'indentation était la cause du problème.

##### Par Y. Soukehal

Durant la semaine 5, j'ai paufiné l'introduction du carnet de bord. J'ai aussi commencé la carte holistique du carnet de bord. De plus, j'ai commencé le point 5 du carnet de bord, et la vérification des sources.

##### Par C. Lebrati & K. Vallipuram

### Semaine 6

Cette semaine sera consacrée au paufinement du programme. J'ai rajouté un titre en entête, ainsi que les commentaires au code.
Après réflexion, j'ai eu la brillante idée de rajouter un bouton disposant les cellules de manière aléatoire (c'était quand même un des paramètres de la recherche), après ça je me suis dis qu'il serait intéressant d'ajouter un bouton pour nettoyer le tableau (ou le vider), car pour cela il fallait fermer puis réouvrir le programme, ce qui pouvait être assez lassant à force.
Par ailleurs, si j'initialisais le tableau plus grand que ce que pouvait afficher le moniteur, les bouttons disparraissaient. Par manque de temps, je n'ai pas pu régler ce problème, j'ai donc juste laisser un avertissement en commentaire dans mon code.

##### Par Y. Soukehal
 
La semaine 6 était dédiée a l'amélioration et à la finition du carnet de bord avant le rendu. J'ai fini l'introduction et la carte mentale du carnet de bord.

##### Par C. Lebrati & K. Vallipuram

Pour cette semaine, reception du code final. Mise en place des experiences à réaliser avec le code afin de valider notre hypothèse. Premier test avec une simulation sans cellule, qui démontre que ce n'est pas possible. Ensuite second test avec des cellules placées manuellement qui quand à lui m'a permis d'avoir de réels résultats. Donc j'ai opté pour faire deux phases: une avec une configuration manuelle (placement de plusieurs cellules au hasard) puis une autre avec une configuration aléatoire (automatique). Le résultats de ces deux simulations permet de déduire la validité de notre hypothèse.

##### Par G.Kounkoud

< A  href = "index.html" > Retour à la page principale </ a>
