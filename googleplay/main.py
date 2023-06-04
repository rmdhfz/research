from google_play_scraper import search, app

# array
keywords = ["anxiety", "AR", "mobile application"]

total_results = 0
for key in keywords:
    results = search(
        key,
        n_hits=30
    )
    total_results += len(results)

    for r in results:
        app_info    = r['appId']
        title       = r['title']
        genre       = r['genre']
        free        = r['free']
        score       = r['score']
        developer   = r['developer']
        installs    = r['installs']

        print("App ID:", app_info)
        print("Title:", title)
        print("Genre:", genre)
        print("Free:", free)
        print("Score:", score)
        print("Developer:", developer)
        print("Installs:", installs)
        print()
        
print("Total Results:", total_results)
