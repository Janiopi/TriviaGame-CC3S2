-- Crear un nuevo esquema para la aplicación de trivia
CREATE SCHEMA IF NOT EXISTS trivia;

-- Crear una tabla para las preguntas de trivia
CREATE TABLE IF NOT EXISTS trivia.questions (
    question_id SERIAL PRIMARY KEY,
    question_text TEXT NOT NULL,
    option_1 TEXT NOT NULL,
    option_2 TEXT NOT NULL,
    option_3 TEXT NOT NULL,
    option_4 TEXT NOT NULL,
    correct_answer INTEGER NOT NULL,  -- Almacena el número de la opción correcta (1, 2, 3 o 4)
    difficulty TEXT NOT NULL,         -- Dificultad de la pregunta (por ejemplo: "fácil", "media", "difícil")
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insertar datos de ejemplo para preguntas de trivia
INSERT INTO trivia.questions (question_text, option_1, option_2, option_3, option_4, correct_answer, difficulty)
VALUES 
    ('¿Qué película ganó el Oscar a Mejor Película en 1994?', 
     'Forrest Gump', 'Cadena Perpetua', 'Pulp Fiction', 'El Rey León', 1, 'fácil'),  -- Correcta: Forrest Gump
     
    ('¿Quién cantó la famosa canción "Thriller"?', 
     'Michael Jackson', 'Prince', 'Elton John', 'Madonna', 1, 'fácil'),  -- Correcta: Michael Jackson
     
    ('¿Qué superhéroe es conocido como "El Caballero Oscuro"?', 
     'Iron Man', 'Superman', 'Batman', 'Spider-Man', 3, 'media'),  -- Correcta: Batman
     
    ('¿En qué año se estrenó la película "Matrix"?', 
     '1995', '1997', '1999', '2001', 3, 'media'),  -- Correcta: 1999
     
    ('¿Qué cantante famosa es conocida como la "Reina del Pop"?', 
     'Madonna', 'Beyoncé', 'Lady Gaga', 'Rihanna', 1, 'fácil'),  -- Correcta: Madonna
     
    ('¿Cuál es el nombre de la banda ficticia en la película "Casi Famosos"?', 
     'The Wonders', 'The Who', 'The Beatles', 'The Rolling Stones', 1, 'media'),  -- Correcta: The Wonders
     
    ('¿Quién interpretó a Jack Dawson en la película "Titanic"?', 
     'Matt Damon', 'Brad Pitt', 'Leonardo DiCaprio', 'Johnny Depp', 3, 'difícil'),  -- Correcta: Leonardo DiCaprio
     
    ('¿Cuál es el nombre de la ciudad ficticia en la serie de TV "Stranger Things"?', 
     'Hawkins', 'Sunnydale', 'Raccoon City', 'Twin Peaks', 1, 'media'),  -- Correcta: Hawkins
     
    ('¿Qué película presenta un personaje llamado "Darth Vader"?', 
     'Star Wars', 'Star Trek', 'El Señor de los Anillos', 'Indiana Jones', 1, 'fácil'),  -- Correcta: Star Wars
     
    ('¿Quién fue la primera mujer en ganar un Premio Nobel?', 
     'Marie Curie', 'Rosalind Franklin', 'Ada Lovelace', 'Hedy Lamarr', 1, 'difícil');  -- Correcta: Marie Curie

-- Insertar preguntas de trivia con diferentes niveles de dificultad
-- 10 preguntas fáciles
INSERT INTO trivia.questions (question_text, option_1, option_2, option_3, option_4, correct_answer, difficulty)
VALUES 
    ('¿Cuál es la capital de Francia?', 'Madrid', 'Londres', 'París', 'Berlín', 3, 'fácil'),
    ('¿Quién pintó la Mona Lisa?', 'Vincent van Gogh', 'Pablo Picasso', 'Leonardo da Vinci', 'Claude Monet', 3, 'fácil'),
    ('¿En qué continente se encuentra Egipto?', 'Asia', 'África', 'Europa', 'Oceanía', 2, 'fácil'),
    ('¿Cuántos días tiene un año bisiesto?', '365', '366', '364', '360', 2, 'fácil'),
    ('¿Qué fruta es amarilla y curvada?', 'Manzana', 'Plátano', 'Cereza', 'Sandía', 2, 'fácil'),
    ('¿Quién escribió "Cien años de soledad"?', 'Mario Vargas Llosa', 'Gabriel García Márquez', 'Jorge Luis Borges', 'Julio Cortázar', 2, 'fácil'),
    ('¿Cuál es el idioma oficial de Brasil?', 'Español', 'Portugués', 'Inglés', 'Francés', 2, 'fácil'),
    ('¿De qué color es el sol?','Azul', 'Rojo', 'Amarillo', 'Blanco', 3, 'fácil'),
    ('¿Qué es el aire?', 'Un gas', 'Un líquido', 'Un metal', 'Una planta', 1, 'fácil'),
    ('¿Cuántos continentes existen?', '7', '5', '6', '8', 1, 'fácil');

-- 10 preguntas intermedias
INSERT INTO trivia.questions (question_text, option_1, option_2, option_3, option_4, correct_answer, difficulty)
VALUES 
    ('¿Quién pintó "La última cena"?', 'Vincent van Gogh', 'Leonardo da Vinci', 'Pablo Picasso', 'Rembrandt', 2, 'media'),
    ('¿En qué país se encuentra el Machu Picchu?', 'Chile', 'Perú', 'México', 'Argentina', 2, 'media'),
    ('¿Cuál es el océano más grande?', 'Atlántico', 'Ártico', 'Pacífico', 'Índico', 3, 'media'),
    ('¿Qué animal es conocido por ser el rey de la selva?', 'Elefante', 'León', 'Tigre', 'Oso', 2, 'media'),
    ('¿Cuál es el país más grande del mundo?', 'Canadá', 'Rusia', 'China', 'Estados Unidos', 2, 'media'),
    ('¿Qué instrumento musical tiene 88 teclas?', 'Guitarra', 'Piano', 'Bajo', 'Violín', 2, 'media'),
    ('¿Qué científico desarrolló la teoría de la relatividad?', 'Isaac Newton', 'Albert Einstein', 'Galileo Galilei', 'Nikola Tesla', 2, 'media'),
    ('¿Cuál es la capital de Australia?', 'Sídney', 'Melbourne', 'Canberra', 'Adelaida', 3, 'media'),
    ('¿Quién es el autor de "Don Quijote de la Mancha"?', 'Jorge Luis Borges', 'Carlos Fuentes', 'Miguel de Cervantes', 'Mario Vargas Llosa', 3, 'media'),
    ('¿Qué país tiene más población del mundo?', 'India', 'Estados Unidos', 'China', 'Rusia', 3, 'media');

-- 10 preguntas difíciles
INSERT INTO trivia.questions (question_text, option_1, option_2, option_3, option_4, correct_answer, difficulty)
VALUES 
    ('¿En qué año se firmó la Declaración de Independencia de los Estados Unidos?', '1776', '1789', '1791', '1800', 1, 'difícil'),
    ('¿Quién desarrolló la teoría cuántica?', 'Isaac Newton', 'Albert Einstein', 'Max Planck', 'Niels Bohr', 3, 'difícil'),
    ('¿En qué país se originó el sushi?', 'China', 'Corea del Sur', 'Japón', 'Tailandia', 3, 'difícil'),
    ('¿Cuántos elementos hay en la tabla periódica?', '104', '118', '125', '130', 2, 'difícil'),
    ('¿En qué ciudad se celebró la primera Copa del Mundo de fútbol?', 'Madrid', 'Buenos Aires', 'Río de Janeiro', 'Montevideo', 4, 'difícil'),
    ('¿Cuál es el nombre del primer satélite artificial lanzado al espacio?', 'Apolo 11', 'Sputnik 1', 'Hubble', 'Explorer 1', 2, 'difícil'),
    ('¿En qué siglo ocurrió la Revolución Francesa?', 'XIV', 'XVII', 'XVIII', 'XIX', 3, 'difícil'),
    ('¿Cuál es el más grande de los planetas del sistema solar?', 'Júpiter', 'Saturno', 'Neptuno', 'Urano', 1, 'difícil'),
    ('¿Cuál es la capital de Mongolia?', 'Ulaanbaatar', 'Beijing', 'Almaty', 'Astana', 1, 'difícil'),
    ('¿En qué año se inventó la televisión?', '1920', '1910', '1930', '1890', 1, 'difícil');
