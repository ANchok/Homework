import time


class UrTube:
    def __init__(self, users=[], videos=[], current_user=None):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                break

    def log_out(self):
        self.current_user = None

    def register(self, nickname, password, age):
        if not self.users:
            self.users.append(User(nickname, password, age))
            self.log_in(nickname, password)
        else:
            break_status = False
            for user in self.users:
                if user.nickname == nickname:
                    print(f'Пользователь {nickname} уже существует')
                    break_status = True
                    break
            if not break_status:
                self.users.append(User(nickname, password, age))
                self.log_in(nickname, password)

    def add(self, *args):
        i = 0
        while i < len(args):
            if not self.videos:
                self.videos.append(args[0])
                i += 1
            else:
                if args[i] in self.videos:
                    i += 1
                    continue
                else:
                    self.videos.append(args[i])
                    i += 1

    def get_videos(self, research_str):
        same_title_video = []
        for video in self.videos:
            if research_str.lower() in video.title.lower():
                same_title_video.append(video.title)
            elif video.title.lower() in research_str.lower():
                same_title_video.append(video.title)
        return same_title_video

    def watch_video(self, res_title):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for video in self.videos:
                if res_title == video.title:
                    if self.current_user.age < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    else:
                        while video.time_now <= video.duration:
                            print(video.time_now, end=" ")
                            video.time_now += 1
                            time.sleep(1)
                        print('Конец видео')
                        video.time_now = 0
                else:
                    continue


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title == other.title

    def __contains__(self, item):
        return any(item.nickname == obj.nickname for obj in UrTube.videos)


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
