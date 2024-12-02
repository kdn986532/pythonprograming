class Movie:
    def __init__(self, title, schedule):
        self.title = title
        self.schedule = schedule
        self.seats = {time: [False] * 10 for time in schedule}

    def reserve_seat(self, time, seat_number):
        if time not in self.schedule:
            print(f"{time} 상영 시간이 존재하지 않습니다.")
            return

        if seat_number < 1 or seat_number > 10:
            print("좌석 번호는 1부터 10까지 선택 가능합니다.")
            return

        if self.seats[time][seat_number - 1]:
            print(f"좌석 {seat_number}는 이미 예약되었습니다.")
        else:
            self.seats[time][seat_number - 1] = True
            print(f"{self.title} 영화의 {time} 상영 시간대에 좌석 {seat_number}가 예약되었습니다.")

    def get_available_seats(self, time):
        if time not in self.schedule:
            print(f"{time} 상영 시간이 존재하지 않습니다.")
            return 0
        available = self.seats[time].count(False)
        return available


class Theater:
    def __init__(self):
        self.movies = {}

    def add_movie(self, title, schedule):
        if title in self.movies:
            print(f"{title} 영화는 이미 추가되었습니다.")
        else:
            movie = Movie(title, schedule)
            self.movies[title] = movie
            print(f"{title} 영화가 추가되었습니다.")

    def reserve_movie_seat(self, title, time, seat_number):
        if title not in self.movies:
            print(f"{title} 영화는 존재하지 않습니다.")
            return
        movie = self.movies[title]
        movie.reserve_seat(time, seat_number)

    def get_movie_schedule(self, title):
        if title not in self.movies:
            print(f"{title} 영화는 존재하지 않습니다.")
            return

        movie = self.movies[title]
        print(f"{title} 영화의 상영 시간표와 예약 가능한 좌석 수:")
        for time in movie.schedule:
            available_seats = movie.get_available_seats(time)
            print(f"{time}: {available_seats}개의 좌석이 남아 있습니다.")

###########아직 공부중입니다.......#############

theater = Theater()


theater.add_movie("인셉션", ["14:00", "17:00", "20:00"])
theater.add_movie("인터스텔라", ["13:00", "16:00", "19:00"])


theater.reserve_movie_seat("인셉션", "14:00", 3)
theater.reserve_movie_seat("인셉션", "14:00", 3)
theater.reserve_movie_seat("인터스텔라", "19:00", 5)


theater.get_movie_schedule("인셉션")
theater.get_movie_schedule("인터스텔라")
