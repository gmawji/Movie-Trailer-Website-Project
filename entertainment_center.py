import fresh_tomatoes
import media

#Movies being defined and added
grandmas_boy = media.Movie("Grandma's Boy", "A 35 year old video game tester has"
                           " to move in with his grandma and her two old lady "
                           "roommates.","http://bit.ly/2fi1uVM",
                           "https://www.youtube.com/watch?v=vsEuOw3ihbs", "R", "94 mins", "2006")
deadpool = media.Movie("Deadpool", "A fast-talking mercenary with a morbid sense of humor"
                       " is subjected to a rogue experiment that leaves him with accelerated "
                       "healing powers and a quest for revenge.", "http://bit.ly/2eorTC7",
                       "https://www.youtube.com/watch?v=SB0YRDkUlnk&t=2m14s", "R", "108 mins", "2016")
the_dark_knight = media.Movie("The Dark Knight", "When the menace known as the Joker wreaks "
                              "havoc and chaos on the people of Gotham, the caped crusader must "
                              "come to terms with one of the greatest psychological tests of his "
                              "ability to fight injustice.", "http://bit.ly/2fDGK8W",
                              "https://www.youtube.com/watch?v=EXeTwQWrcwY", "PG-13", "152 mins", "2008")
mean_machine = media.Movie("Mean Machine", "A soccer star jailed for assault leads a group of "
                           "inmates in a match against prison guards.", "http://bit.ly/2fWWffY",
                           "https://www.youtube.com/watch?v=oc3LtcVT1WA", "R", "99 mins", "2001")
the_godfather = media.Movie("The Godfather", "The aging patriarch of an organized crime dynasty "
                            "transfers control of his clandestine empire to his reluctant son.",
                            "http://bit.ly/2fDH6MW", "https://www.youtube.com/watch?v=sY1S34973zA", "R", "175 mins", "1972")
friday = media.Movie("Friday", "Two homies, Smokey and Craig, smoke a dope dealer's"
                      " weed and try to figure a way to get the $200 they owe to the"
                      " dealer by 10 p.m. that same night. In that time, they"
                      " smoke more weed and get jacked and shot at in a drive-by.",
                      "http://bit.ly/2eV8p35", "https://www.youtube.com/watch?v=nH1Ulp4PBtA", "R", "91 mins", "1995")

#Create movies container
movies = [grandmas_boy, deadpool, the_dark_knight, mean_machine, the_godfather, friday]

#Generate HTML
fresh_tomatoes.open_movies_page(movies)
