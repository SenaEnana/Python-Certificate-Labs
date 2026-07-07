class Movie:
    def __init__(self, title, year, director, duration):
        if not title.strip():
            raise ValueError('Title cannot be empty')
        if year < 1895:
            raise ValueError('Year must be 1895 or later')
        if not director.strip():
            raise ValueError('Director cannot be empty')
        
        self.title = title
        self.year = year
        self.director = director
        self.duration = duration
    def __str__(self):
        return f'{self.title} ({self.year}) - {self.duration} min, {self.director}'

movie1 = Movie('The Matrix', 1999, 'The Wachowskis', 136)
print(movie1)