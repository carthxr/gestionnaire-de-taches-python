import os
import json

# ---------- FICHIER ----------
FICHIER = "taches.json"

taches = {}


# ---------- SAUVEGARDE / CHARGEMENT ----------
def sauvegarder():
    with open(FICHIER, "w", encoding="utf-8") as f:
        json.dump(taches, f, indent=4, ensure_ascii=False)


def charger():
    global taches
    if os.path.exists(FICHIER):
        with open(FICHIER, "r", encoding="utf-8") as f:
            taches = json.load(f)


# ---------- CLEAR TERMINAL ----------
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


# ---------- AJOUTER TACHES ----------
def ajouter():
    while True:
        nb = input("Combien de tâches ajouter ? : ")
        if nb.isdigit() and int(nb) >= 0:
            nb = int(nb)
            break
        print("Nombre invalide")

    for i in range(nb):
        clear()
        print("TÂCHE", i + 1)

        # Nom sans doublon
        while True:
            nom = input("Nom : ")
            if nom == "":
                print("Nom vide interdit")
            elif nom in taches:
                print("Cette tâche existe déjà")
            else:
                break

        # Priorité
        while True:
            prio = input("Priorité (0 à 3) : ")
            if prio.isdigit() and 0 <= int(prio) <= 3:
                prio = int(prio)
                break
            print("Priorité invalide")

        taches[nom] = {
            "priorite": prio,
            "status": "A faire"
        }

    sauvegarder()
    input("Tâches ajoutées. Entrée pour continuer...")


# ---------- AFFICHER ----------
def afficher():
    clear()
    if not taches:
        print("Aucune tâche")
        input("Entrée...")
        return

    print("LISTE DES TÂCHES\n")
    i = 1
    for nom, infos in taches.items():
        print(i, "-", nom, "| Priorité :", infos["priorite"], "| Status :", infos["status"])
        i += 1

    input("\nEntrée pour continuer...")


# ---------- CHOIX PAR NUMÉRO ----------
def choisir_tache():
    noms = list(taches.keys())

    for i in range(len(noms)):
        print(i + 1, "-", noms[i])

    while True:
        choix = input("Numéro : ")
        if choix.isdigit() and 1 <= int(choix) <= len(noms):
            return noms[int(choix) - 1]
        print("Numéro invalide")


# ---------- MODIFIER STATUS ----------
def modifier():
    clear()
    if not taches:
        print("Aucune tâche")
        input("Entrée...")
        return

    nom = choisir_tache()

    while True:
        status = input("Nouveau status (A faire / En cours / Terminée) : ")
        if status.lower() in ["a faire", "en cours", "terminée", "terminee"]:
            break
        print("Status invalide")

    taches[nom]["status"] = status.capitalize()
    sauvegarder()
    input("Status modifié. Entrée...")


# ---------- SUPPRIMER ----------
def supprimer():
    clear()
    if not taches:
        print("Aucune tâche")
        input("Entrée...")
        return

    nom = choisir_tache()
    confirm = input("Supprimer ? (o/n) : ")

    if confirm.lower() == "o":
        del taches[nom]
        sauvegarder()
        print("Tâche supprimée")
    else:
        print("Annulé")

    input("Entrée...")


# ---------- MENU ----------
charger()

while True:
    clear()
    print("===== GESTION DES TÂCHES =====")
    print("1. Afficher")
    print("2. Ajouter")
    print("3. Modifier status")
    print("4. Supprimer")
    print("5. Quitter")

    choix = input("Choix : ")

    if choix == "1":
        afficher()
    elif choix == "2":
        ajouter()
    elif choix == "3":
        modifier()
    elif choix == "4":
        supprimer()
    elif choix == "5":
        print("Au revoir")
        break
    else:
        input("Choix invalide. Entrée...")

