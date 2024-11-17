#!/usr/bin/python3
"""Module that countain
    a basic Python script to fetch posts from JSONPlaceholder"""
import requests
import csv


def fetch_and_print_posts():
    """ Fetches data from an API and prints post titles """
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    posts = r.json()
    if r.status_code == 200:
        print("Status Code: 200")
        for post in posts:
            print(post.get('title'))
    else:
        print(f"Status code: {r.status_code}")


def fetch_and_save_posts():
    ''' Fetches data from an API and saves it to a CSV file '''
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    posts = r.json()
    if r.status_code == 200:
        # Définir champs du fichier CSV
        fieldnames = ['id', 'title', 'body']        
        with open('posts.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()  # Écrit l'en-tête avec les noms des champs
            # Écrit chaque post dans le fichier CSV
            for post in posts:
                writer.writerow({'id': post.get('id'), 'title': post.get('title'), 'body': post.get('body')})
        print("Data has been written to posts.csv")
    else:
        print(f"Status code: {r.status_code}")

if __name__ == '__main__':
    fetch_and_print_posts()
    fetch_and_save_posts()