class Movie:
    def __init__(self, title, year, director, duration):
        if title.strip() == '':
            raise ValueError('Title cannot be empty')
        
        self.title = title
        self.year = year
        self.director = director
        self.duration = duration
    def __str__(self):
        return f'{self.title} ({self.year}) - {self.duration} min, {self.director}'

movie1 = Movie('The Matrix', 1999, 'The Wachowskis', 136)
print(movie1)