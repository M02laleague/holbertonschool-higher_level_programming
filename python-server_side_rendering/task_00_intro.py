import os
import logging

def generate_invitations(template, attendees):
    # Vérification des types d'entrée
    if not isinstance(template, str):
        logging.error('Invalid input: template should be a string.')
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        logging.error('Invalid input: attendees should be a list of dictionaries.')
        return
    
    # Gestion des entrées vides
    if not template:
        logging.error('Template is empty, no output files generated.')
        return
    if not attendees:
        logging.error('No data provided, no output files generated.')
        return

    # Traitement de chaque participant
    for index, attendee in enumerate(attendees, start=1):
        name = attendee.get('name', 'N/A')
        event_title = attendee.get('event_title', 'N/A')
        event_date = attendee.get('event_date', 'N/A')
        event_location = attendee.get('event_location', 'N/A')

        # Remplacement des placeholders
        output = template.replace('{name}', name)
        output = output.replace('{event_title}', event_title)
        output = output.replace('{event_date}', str(event_date))
        output = output.replace('{event_location}', event_location)

        # Nommage du fichier
        output_file = f'output_{index}.txt'
        if os.path.exists(output_file):
            logging.warning(f'File {output_file} already exists, skipping.')
            continue

        # Écriture du fichier de sortie
        with open(output_file, 'w') as file:
            file.write(output)