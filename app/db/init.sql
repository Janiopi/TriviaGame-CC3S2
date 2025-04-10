-- Create a new schema for the trivia app
CREATE SCHEMA IF NOT EXISTS trivia;

-- Create a table for trivia questions
CREATE TABLE IF NOT EXISTS trivia.questions (
    question_id SERIAL PRIMARY KEY,
    question_text TEXT NOT NULL,
    option_1 TEXT NOT NULL,
    option_2 TEXT NOT NULL,
    option_3 TEXT NOT NULL,
    option_4 TEXT NOT NULL,
    correct_answer INTEGER NOT NULL,  -- Stores the correct option number (1, 2, 3, or 4)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create a table for storing answers submitted by players
CREATE TABLE IF NOT EXISTS trivia.answers (
    answer_id SERIAL PRIMARY KEY,
    question_id INT NOT NULL,
    player_answer INTEGER NOT NULL,  -- Stores the option number chosen by the player (1, 2, 3, or 4)
    is_correct BOOLEAN NOT NULL,
    answered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (question_id) REFERENCES trivia.questions(question_id) ON DELETE CASCADE
);

-- Sample data for pop culture trivia questions
INSERT INTO trivia.questions (question_text, option_1, option_2, option_3, option_4, correct_answer)
VALUES 
    ('Which movie won the Oscar for Best Picture in 1994?', 
     'Forrest Gump', 'The Shawshank Redemption', 'Pulp Fiction', 'The Lion King', 1),  -- Correct: Forrest Gump
     
    ('Who sang the hit song "Thriller"?', 
     'Michael Jackson', 'Prince', 'Elton John', 'Madonna', 1),  -- Correct: Michael Jackson
     
    ('Which superhero is known as "The Dark Knight"?', 
     'Iron Man', 'Superman', 'Batman', 'Spider-Man', 3),  -- Correct: Batman
     
    ('In which year did the movie "The Matrix" come out?', 
     '1995', '1997', '1999', '2001', 3),  -- Correct: 1999
     
    ('Which famous singer is known as the "Queen of Pop"?', 
     'Madonna', 'Beyoncé', 'Lady Gaga', 'Rihanna', 1),  -- Correct: Madonna
     
    ('What was the name of the fictional band in the movie "Almost Famous"?', 
     'The Wonders', 'The Who', 'The Beatles', 'The Rolling Stones', 1),  -- Correct: The Wonders
     
    ('Who played Jack Dawson in the movie "Titanic"?', 
     'Matt Damon', 'Brad Pitt', 'Leonardo DiCaprio', 'Johnny Depp', 3),  -- Correct: Leonardo DiCaprio
     
    ('What is the name of the fictional town in the TV show "Stranger Things"?', 
     'Hawkins', 'Sunnydale', 'Raccoon City', 'Twin Peaks', 1),  -- Correct: Hawkins
     
    ('Which movie features a character named "Darth Vader"?', 
     'Star Wars', 'Star Trek', 'The Lord of the Rings', 'Indiana Jones', 1),  -- Correct: Star Wars
     
    ('Who was the first woman to win a Nobel Prize?', 
     'Marie Curie', 'Rosalind Franklin', 'Ada Lovelace', 'Hedy Lamarr', 1);  -- Correct: Marie Curie

-- Sample answers (assuming the player selected the options)
INSERT INTO trivia.answers (question_id, player_answer, is_correct)
VALUES
    (1, 1, TRUE),  -- Correct answer for "Which movie won the Oscar for Best Picture in 1994?" is option 1 (Forrest Gump)
    (2, 1, TRUE),  -- Correct answer for "Who sang the hit song 'Thriller'?" is option 1 (Michael Jackson)
    (3, 3, TRUE),  -- Correct answer for "Which superhero is known as 'The Dark Knight'?" is option 3 (Batman)
    (4, 3, TRUE),  -- Correct answer for "In which year did the movie 'The Matrix' come out?" is option 3 (1999)
    (5, 1, TRUE),  -- Correct answer for "Which famous singer is known as the 'Queen of Pop'?" is option 1 (Madonna)
    (6, 1, TRUE),  -- Correct answer for "What was the name of the fictional band in the movie 'Almost Famous'?" is option 1 (The Wonders)
    (7, 3, TRUE),  -- Correct answer for "Who played Jack Dawson in the movie 'Titanic'?" is option 3 (Leonardo DiCaprio)
    (8, 1, TRUE),  -- Correct answer for "What is the name of the fictional town in the TV show 'Stranger Things'?" is option 1 (Hawkins)
    (9, 1, TRUE),  -- Correct answer for "Which movie features a character named 'Darth Vader'?" is option 1 (Star Wars)
    (10, 1, TRUE); -- Correct answer for "Who was the first woman to win a Nobel Prize?" is option 1 (Marie Curie)
