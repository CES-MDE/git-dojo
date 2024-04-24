# Le chiffrement de Vigenère

Le chiffrement de Vigenère est une méthode de cryptographie qui utilise un mot-clé pour chiffrer un message. Voici comment cela fonctionne :

## Clé

Vous avez un mot-clé, par exemple "KEY". Ce mot-clé est répété pour avoir la même longueur que le message que vous voulez chiffrer.

## Chiffrement

Chaque lettre du message original est déplacée vers le haut dans l'alphabet selon la lettre correspondante dans le mot-clé. Par exemple, si la première lettre du message est "A" et la première lettre du mot-clé est "K", alors la lettre chiffrée serait "K".

## Répétition

Une fois que vous avez chiffré une lettre, vous passez à la suivante dans le mot-clé pour chiffrer la prochaine lettre du message. Si vous arrivez à la fin du mot-clé, vous revenez au début.

## Déchiffrement

Pour déchiffrer le message, vous faites l'opération inverse. Vous déplacez chaque lettre du message chiffré vers le bas dans l'alphabet selon la lettre correspondante dans le mot-clé.

---

### Répétition de la clé

Nous répétons la clé "KEY" pour avoir la même longueur que le message "HELLO". Ainsi, la clé devient "KEYKE".

### Chiffrement

Maintenant, nous déplaçons chaque lettre du message original vers le haut dans l'alphabet en fonction de la lettre correspondante dans la clé. Par exemple :

- Pour la première lettre "H" et la première lettre de la clé "K", nous décalons "H" de 10 positions vers le haut (car "K" est la 11ème lettre de l'alphabet). Ainsi, "H" devient "R".
- Pour la deuxième lettre "E" et la deuxième lettre de la clé "E", nous décalons "E" de 4 positions vers le haut (car "E" est la 5ème lettre de l'alphabet). Ainsi, "E" devient "I".
- Pour la troisième lettre "L" et la troisième lettre de la clé "Y", nous décalons "L" de 24 positions vers le haut (car "Y" est la 25ème lettre de l'alphabet). Ainsi, "L" devient "B".
- Pour la quatrième lettre "L" et la quatrième lettre de la clé "K", nous décalons "L" de 10 positions vers le haut (car "K" est la 11ème lettre de l'alphabet). Ainsi, "L" devient "V".
- Pour la cinquième lettre "O" et la cinquième lettre de la clé "E", nous décalons "O" de 4 positions vers le haut (car "E" est la 5ème lettre de l'alphabet). Ainsi, "O" devient "S".

Donc, le message chiffré est "RIBVS".

C'est ainsi que le chiffrement de Vigenère fonctionne en utilisant une clé pour décaler chaque lettre du message original vers le haut dans l'alphabet.
