import os
import re
import requests

# --- CONFIGURATION ---
API_KEY = '789671a9'  # Replace with your actual OMDb API key
POSTS_DIR = "_movies"           # Change to your collection folder if not using default posts
IMAGES_DIR = "assets/img/mp"   # Matches your exact image folder path
# ---------------------

def sanitize_filename(name):
    # Keep only alphanumeric characters, spaces, and hyphens
    clean = re.sub(r'[^a-zA-Z0-9\s\-]', '', name)
    # Replace spaces with hyphens and lowercase everything
    return re.sub(r'\s+', '-', clean).strip('-').lower()

# def add_movie():
#     movie_title = input("Enter movie title: ").strip()
#     if not movie_title:
#         print("Title cannot be empty.")
#         return

#     print(f"Searching for '{movie_title}'...")
#     url = f"http://www.omdbapi.com/?t={movie_title}&apikey={API_KEY}"
#     response = requests.get(url).json()

#     if response.get("Response") == "False":
#         print(f"Error: {response.get('Error', 'Movie not found.')}")
#         return

#     # Extract clean data from API response
#     title = response.get("Title")
#     director = response.get("Director")
    
#     # Handle Year as an integer
#     year_raw = response.get("Year", "")
#     # OMDb sometimes returns year ranges for TV shows (e.g., "1999–2004"), extract just the first 4 digits
#     year_match = re.search(r'\d{4}', year_raw)
#     year = int(year_match.group()) if year_match else 0

#     # Format tags/genres into a YAML array list: ["Sci-Fi", "Thriller"]
#     genre_string = response.get("Genre", "")
#     genres = [g.strip() for g in genre_string.split(",")] if genre_string else []
#     # Convert list to an explicit string format: ["Genre1", "Genre2"]
#     tags_formatted = "[" + ", ".join(f'"{g}"' for g in genres) + "]"

#     poster_url = response.get("Poster")
    
#     # Create filenames
#     safe_title = sanitize_filename(title)
#     markdown_filename = f"{safe_title}.md"
#     image_filename = f"{safe_title}.jpg"

#     # Ensure folders exist
#     os.makedirs(POSTS_DIR, exist_ok=True)
#     os.makedirs(IMAGES_DIR, exist_ok=True)

#     # Download the poster
#     relative_img_path = ""
#     if poster_url and poster_url != "N/A":
#         print("Downloading poster...")
#         try:
#             img_data = requests.get(poster_url).content
#             img_path = os.path.join(IMAGES_DIR, image_filename)
#             with open(img_path, 'wb') as handler:
#                 handler.write(img_data)
#             # Match your exact structure with a leading slash
#             relative_img_path = f"/{IMAGES_DIR}/{image_filename}"
#         except Exception as e:
#             print(f"Failed to download poster: {e}")
#     else:
#         print("No poster available.")

#     # Build Front Matter to match your example perfectly
#     front_matter = f"""---
# layout: post
# title: "{title}"
# director: "{director}"
# year: {year}
# poster: "{relative_img_path}"
# tags: {tags_formatted}
# ---"""

#     # Write the Markdown file
#     md_path = os.path.join(POSTS_DIR, markdown_filename)
#     with open(md_path, 'w', encoding='utf-8') as f:
#         f.write(front_matter)

#     print(f"\n🎉 Success!")
#     print(f"File created: {md_path}")
#     print(f"Poster saved: {IMAGES_DIR}/{image_filename}")

def add_movie():
    user_input = input("Enter movie title (add year at end if needed, e.g., 'Zen 2009'): ").strip()
    if not user_input:
        print("Title cannot be empty.")
        return

    # Check if the user typed a 4-digit year at the end of their input
    year_match = re.search(r'\s(\d{4})$', user_input)
    
    if year_match:
        # Extract the year and remove it from the movie title string
        search_year = year_match.group(1)
        movie_title = user_input[:year_match.start()].strip()
        print(f"Searching for exact match: '{movie_title}' from the year {search_year}...")
        url = f"http://www.omdbapi.com/?t={movie_title}&y={search_year}&apikey={API_KEY}"
    else:
        # No year provided, search normally
        movie_title = user_input
        print(f"Searching for '{movie_title}'...")
        url = f"http://www.omdbapi.com/?t={movie_title}&apikey={API_KEY}"

    response = requests.get(url).json()

    if response.get("Response") == "False":
        print(f"Error: {response.get('Error', 'Movie not found.')}")
        return

    # Extract clean data from API response
    title = response.get("Title")
    director = response.get("Director")
    
    # Handle Year as an integer
    year_raw = response.get("Year", "")
    final_year_match = re.search(r'\d{4}', year_raw)
    year = int(final_year_match.group()) if final_year_match else 0

    # Format tags/genres into a YAML array list: ["Sci-Fi", "Thriller"]
    genre_string = response.get("Genre", "")
    genres = [g.strip() for g in genre_string.split(",")] if genre_string else []
    tags_formatted = "[" + ", ".join(f'"{g}"' for g in genres) + "]"

    poster_url = response.get("Poster")
    
    # Create filenames
    safe_title = sanitize_filename(title)
    markdown_filename = f"{safe_title}.md"
    image_filename = f"{safe_title}.jpg"

    # Ensure folders exist
    os.makedirs(POSTS_DIR, exist_ok=True)
    os.makedirs(IMAGES_DIR, exist_ok=True)

    # Download the poster
    relative_img_path = ""
    if poster_url and poster_url != "N/A":
        print("Downloading poster...")
        try:
            img_data = requests.get(poster_url).content
            img_path = os.path.join(IMAGES_DIR, image_filename)
            with open(img_path, 'wb') as handler:
                handler.write(img_data)
            relative_img_path = f"/{IMAGES_DIR}/{image_filename}"
        except Exception as e:
            print(f"Failed to download poster: {e}")
    else:
        print("No poster available.")

    # Build Front Matter to match your example perfectly
    front_matter = f"""---
layout: post
title: "{title}"
director: "{director}"
year: {year}
poster: "{relative_img_path}"
tags: {tags_formatted}
---"""

    # Write the Markdown file
    md_path = os.path.join(POSTS_DIR, markdown_filename)
    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(front_matter)

    print(f"\n🎉 Success!")
    print(f"File created: {md_path}")
    print(f"Poster saved: {IMAGES_DIR}/{image_filename}")

if __name__ == "__main__":
    add_movie()