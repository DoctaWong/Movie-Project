import media
import fresh_tomatoes

# Schindler's List

schindlers_list = media.Movie("Schindler's List",
                              "History",
                              "195 minutes",
                              "8.9",
                              "http://www.spacemov.net/wp-content/uploads/2014/06/schindlers-list-656694l.jpg",  # noqa
                              "https://www.youtube.com/watch?v=JdRGC-w9syA",
                              "1993")

# The Sound of Music

sound_of_music = media.Movie("The Sound of Music",
                             "Drama",
                             "174 minutes",
                             "8.0",
                             "http://moviefiles.alphacoders.com/459/poster-459.jpg",  # noqa
                             "https://www.youtube.com/watch?v=DGABqdbtQnA",
                             "1965")

# West Side Story

west_side_story = media.Movie("West Side Story",
                              "Drama",
                              "174 minutes",
                              "8.0",
                              "http://tctimesonline.com/wp-content/uploads/2015/09/West-Side-Story-Regina-124.jpg",  # noqa
                              "https://www.youtube.com/watch?v=JBTzjbvagIQ",
                              "1961")

# Titanic

titanic = media.Movie("Titanic",
                      "Drama",
                      "174 minutes",
                      "8.0",
                      "http://cdn.traileraddict.com/content/paramount-pictures/titanic.jpg",  # noqa
                      "https://www.youtube.com/watch?v=DNyKDI9pn0Q",
                      "1997")

# Alien

alien = media.Movie("Alien",
                    "Science Fiction",
                    "177 minutes",
                    "8.5",
                    "https://s-media-cache-ak0.pinimg.com/736x/4d/e5/8d/4de58d1c5d92228e7d941fc482eaaee3.jpg",  # noqa
                    "https://www.youtube.com/watch?v=vQ6SUTI1j9M",
                    "1979")

# The Dark Knight

dark_knight = media.Movie("The Dark Knight",
                          "Action",
                          "152 minutes",
                          "9.0",
                          "https://smilingldsgirl.files.wordpress.com/2013/06/xemphimso_ky-si-bong-dem-1.jpg",  # noqa
                          "https://www.youtube.com/watch?v=EXeTwQWrcwY",
                          "2008")

# Gladiator

gladiator = media.Movie("Gladiator",
                        "Action",
                        "127 minutes",
                        "8.1",
                        "http://img07.deviantart.net/8423/i/2008/233/6/1/gladiator_movie_poster_by_mdr9inchnails.jpg",  # noqa
                        "https://www.youtube.com/watch?v=owK1qxDselE",
                        "2000")

# Jurassic Park

jurassic_park = media.Movie("Jurassic Park",
                            "Adventure",
                            "127 minutes",
                            "8.1",
                            "https://img.buzzfeed.com/buzzfeed-static/static/2014-08/12/12/enhanced/webdr10/enhanced-14020-1407861668-13.jpg",  # noqa
                            "https://www.youtube.com/watch?v=lc0UehYemQA",
                            "1993")

# adds the above instances to the list movies
movies = [schindlers_list, sound_of_music, west_side_story,
          titanic, alien, dark_knight, gladiator, jurassic_park]

# opens each of the movies in the above list in the fresh_tomatoes page
fresh_tomatoes.open_movies_page(movies)
