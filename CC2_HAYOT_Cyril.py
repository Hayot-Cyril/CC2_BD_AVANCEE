import pymssql

# Fonction pour vérifier l'utilisateur
def verifier_utilisateur(login, mdp):
    try:
        # Remplacez ces informations par les informations de votre serveur SQL Server
        server = "ASUS_DU_HAYOT"
        database = "videotheque"
        
        # Établir la connexion au serveur SQL Server
        conn = pymssql.connect(server, database=database)
        cursor = conn.cursor()
        
        # Vérifier l'utilisateur en fonction du login et du mot de passe
        query = f"SELECT id FROM [dbo].[USER] WHERE login = '{login}' AND mdp = '{mdp}'"
        cursor.execute(query)
        user_id = cursor.fetchone()
        
        # Fermer la connexion
        conn.close()
        
        return user_id
    
    except pymssql.Error as e:
        print("Erreur lors de la connexion à SQL Server ou de la vérification de l'utilisateur:", e)
        return None

# Fonction pour afficher les films par année
def afficher_films_par_annee(min_annee, max_annee):
    try:
        # Remplacez ces informations par les informations de votre serveur SQL Server
        server = "ASUS_DU_HAYOT"
        database = "videotheque"
        
        # Établir la connexion au serveur SQL Server
        conn = pymssql.connect(server, database=database)
        cursor = conn.cursor()
        
        # Afficher les films par année entre MIN et MAX
        for annee in range(min_annee, max_annee + 1):
            query = f"""
                SELECT titre
                FROM [dbo].[FILMS]
                WHERE annee = {annee}
            """
            cursor.execute(query)
            films = cursor.fetchall()
            
            print(f"{annee} ({len(films)} Films)")
            for film in films:
                print(f"o {film[0]}")
        
        # Fermer la connexion
        conn.close()
    
    except pymssql.Error as e:
        print("Erreur lors de la connexion à SQL Server ou de l'affichage des films:", e)

# Programme principal
if __name__ == "__main__":
    user_id = None
    while user_id is None:
        login = input("Entrez votre login : ")
        mdp = input("Entrez votre mot de passe : ")
        
        user_id = verifier_utilisateur(login, mdp)
        
        if user_id:
            min_annee = int(input("Entrez l'année MIN : "))
            max_annee = int(input("Entrez l'année MAX : "))
            afficher_films_par_annee(min_annee, max_annee)
        else:
            print("Utilisateur non trouvé. Veuillez réessayer.")

