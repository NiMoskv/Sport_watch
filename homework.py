class InfoMessage:
    """Информационное сообщение о тренировке."""
    pass


class Training:
    """Базовый класс тренировки."""

    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 working_type: str
                 ) -> None:
        self.working_type = workout_type
        self.action = action
        self.duration = duration
        self.weight = weight
        self.M_IN_KM = 1000
        if working_type == 'SWM':
            self.LEN_STEP = 1.38
        elif working_type == 'RUN' or working_type == 'WLK':
            self.LEN_STEP = 0.65


    def get_distance(self) -> float:
        """Получить дистанцию в км."""

        return self.action * self.LEN_STEP / self.M_IN_KM
        

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""
        
        return self.get_distance() / self.duration

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""

        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        info = InfoMessage()
        print(info)


class Running(Training):
    """Тренировка: бег."""
    def __init__(self, working_type: str, action: int, duration: float, weight: float) -> None:
        super().__init__(working_type, action, duration, weight)

    def get_spen_calories(self):
         return (18 * self.get_mean_speed - 20) * self.weight / self.M_IN_KM * (self.duration * 60) 

class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self, 
                 working_type: str, 
                 action: int, 
                 duration: float, 
                 weight: float, 
                 height:int) -> None:
        super().__init__(working_type, action, duration, weight)
        self.height = height
    
    def get_spent_calories(self) -> float:
        return (0.035 * self.height + (self.get_mean_speed ** 2 // self.height) * 0.029 * self.weight) * self.duration * 60

class Swimming(Training):
    """Тренировка: плавание."""
    def __init__(self, 
                 working_type: str, 
                 action: int, 
                 duration: float, 
                 weight: float,
                 length_pool: int,
                 count_pool: int) -> None:
        super().__init__(working_type, action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        return self.length_pool * self.count_pool / self.M_IN_KM / (self.duration *60)
    
    def get_spent_calories(self) -> float:
        return (self.get_mean_speed + 1.1) * 2 * self.weight


class InfoMessage:
    """Класс информационного сообщения."""

    def __init__(self, training_type, duration, distace, speed, calories) -> None:
        self.training_type = training_type
        self.duration = duration
        self.distance = distace
        self.speed = speed
        self.calories = calories
    
    def get_message(self):
        return (f'Тип тренировки: {self.training_type};'
                f'Длительность: {self.duration} ч.;'
                f'Дистанция: {self.distance} км;' 
                f'Ср. скорость: {self.speed} км/ч;' 
                f'Потрачено ккал: {self.calories}')

def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    if workout_type == 'WLK':
        data.append('WLK')
        return SportsWalking(data)


def main(training: Training) -> None:
    """Главная функция."""
    Training.show_training_info(training)
    pass


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
