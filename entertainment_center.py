import fresh_tomatoes
import media

#Movies being defined and added
grandmas_boy = media.Movie("Grandma's Boy", "A 35 year old video game tester has"
                           "to move in with his grandma and her two old lady "
                           "roommates.","http://bit.ly/2fi1uVM",
                           "https://www.youtube.com/watch?v=vsEuOw3ihbs")

deadpool = media.Movie("Deadpool", "A fast-talking mercenary with a morbid sense of humor"
                       " is subjected to a rogue experiment that leaves him with accelerated "
                       "healing powers and a quest for revenge.", "http://bit.ly/2eorTC7",
                       "https://www.youtube.com/watch?v=SB0YRDkUlnk&t=2m14s")

the_dark_knight = media.Movie("The Dark Knight", "When the menace known as the Joker wreaks "
                              "havoc and chaos on the people of Gotham, the caped crusader must "
                              "come to terms with one of the greatest psychological tests of his "
                              "ability to fight injustice.", "http://bit.ly/2fDGK8W",
                              "https://www.youtube.com/watch?v=EXeTwQWrcwY")

mean_machine = media.Movie("Mean Machine", "A soccer star jailed for assault leads a group of "
                           "inmates in a match against prison guards.", "http://bit.ly/2fWWffY",
                           "https://www.youtube.com/watch?v=oc3LtcVT1WA")

the_godfather = media.Movie("The Godfather", "The aging patriarch of an organized crime dynasty "
                            "transfers control of his clandestine empire to his reluctant son.",
                            "http://bit.ly/2fDH6MW", "https://www.youtube.com/watch?v=sY1S34973zA")

#Create movies container
movies = [grandmas_boy, deadpool, the_dark_knight, mean_machine, the_godfather]

#Generate HTML
fresh_tomatoes.open_movies_page(movies)
