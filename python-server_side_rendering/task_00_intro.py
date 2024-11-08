def generate_invitations(template, attendees):
    # Vérification des types
    if not isinstance(template, str) or not isinstance(attendees, list):
        print("Invalid input types.")
        return
    
    # Vérification si le modèle est vide
    if not template:
        print("Template is empty, no output files generated.")
        return

    # Vérification si la liste d'invités est vide
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Parcourir la liste des invités et créer les fichiers
    for i, attendee in enumerate(attendees, start=1):
        # Remplacement des valeurs dans le modèle
        content = template.format(
            name=attendee.get("name", "N/A"),
            event_title=attendee.get("event_title", "N/A"),
            event_date=attendee.get("event_date", "N/A"),
            event_location=attendee.get("event_location", "N/A")
        )

        # Écrire le contenu dans un fichier
        with open(f'output_{i}.txt', 'w') as file:
            file.write(content)
