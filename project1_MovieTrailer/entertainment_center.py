import media
import fresh_tomatoes
starwar = media.Movie("Star Wars: The Force Awakens",
                      "The lastest Star War movie",
                      "https://upload.wikimedia.org/wikipedia/en/a/a2/Star_Wars_The_Force_Awakens_Theatrical_Poster.jpg",
                      "https://www.youtube.com/watch?v=sGbxmsDFVnE")
lobster = media.Movie("The Lobster",
                      "A dystopian near future where single people are " +
                      "arrested and transferred to a creepy hotel",
                      "http://exclaim.ca/images/thelobsterposter.jpg",
                      "https://www.youtube.com/watch?v=z069ldsumxA")
theory_of_everything = media.Movie("The Theory of Everything",
                      "The extraordinary story of Jane and Stephen Hawking",
                      "http://www.yifysub.com/wp-content/uploads/2015/08/The-Theory-of-Everything-12.jpg",
                      "https://www.youtube.com/watch?v=x8QYUgO-tZo")

movies = [starwar, lobster, theory_of_everything]
fresh_tomatoes.open_movies_page(movies)