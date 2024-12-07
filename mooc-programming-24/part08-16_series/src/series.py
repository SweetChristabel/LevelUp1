# Write your solution here:
class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.rating = []

    def __str__(self):
        if len(self.rating) == 0:
            review = "no ratings"
        else:
            review = f"{len(self.rating)} ratings, average {round(sum(self.rating)/len(self.rating),1)} points"
        return f"{self.title} ({self.seasons} seasons)\ngenres: {', '.join(self.genres)}\n{review}"
    
    def rate(self, rating: float):
        self.rating.append(rating)

def minimum_grade(rating: float, series_list: list):
    hits = []
    for series in series_list:
        if sum(series.rating)/len(series.rating) >= rating:
            hits.append(series)
        else:
            continue
    return hits

def includes_genre(genre: str, series_list: list):
    hits = []
    for series in series_list:
        if genre in series.genres:
            hits.append(series)
        else:
            continue
    return hits


if __name__ == "__main__":

    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)