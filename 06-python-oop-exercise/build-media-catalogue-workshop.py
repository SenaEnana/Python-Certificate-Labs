class Movie:
    def __str__(self):
        return f'{self.title} ({self.year}) - {self.duration} min, {self.director}'
    def __init__(self, title, year, director, duration):
        self.title = title
        self.year = year
        self.director = director
        self.duration = duration

    