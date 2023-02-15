
class InfoMessage:
    """Класс информационного сообщения."""

    def __init__(self, 
                 training_type: str, 
                 duration: float, 
                 distance: float, 
                 speed: float, 
                 calories: float) -> None:
        self.training_type = training_type #Тип тренировки
        self.duration = duration #Длительность тренировки
        self.distance = distance #Дистанция за тренировку
        self.speed = speed #Средняя скорость
        self.calories = calories #Потраченные калории 
    
    def get_message(self):
        """Метод возвращает полную информацию о прошедшей тренировке."""
        
        return (f'Тип тренировки: {self.training_type}; '
                f'Длительность: {self.duration:.3f} ч.; '
                f'Дистанция: {self.distance:.3f} км; ' 
                f'Ср. скорость: {self.speed:.3f} км/ч; ' 
                f'Потрачено ккал: {self.calories:.3f}.')


class Training:
    """Базовый класс тренировки."""
    
    M_IN_KM = 1000 #Константа перевода из метров в киллометры
    LEN_STEP = 0.65 #Константа перевода в метры если бег или ходьба
    HOUR_TO_MIN = 60
    def __init__(self,
                 action: int,
                 duration: float,
                 weight: float,
                 ) -> None:
        self.action = action #Количество шагов/гребков
        self.duration = duration #Длительность тренировки в часах
        self.weight = weight #Вес спортсмена



    def get_distance(self) -> float:
        """Получить дистанцию в км."""
        
        distance = self.action * self.LEN_STEP / self.M_IN_KM
        
        return distance
        

    def get_mean_speed(self) -> float:
        """Получить среднюю скорость движения."""

        speed= self.get_distance() / self.duration
        
        return speed

    def get_spent_calories(self) -> float:
        """Получить количество затраченных калорий."""
        pass

    def show_training_info(self) -> InfoMessage:
        """Вернуть информационное сообщение о выполненной тренировке."""
        inf = InfoMessage( type(self).__name__,
                            self.duration,
                            self.get_distance(),
                            self.get_mean_speed(),
                            self.get_spent_calories())
        return inf


class Running(Training):
    """Тренировка: бег."""

    def get_spent_calories(self):
        """Получение затраченных калорий при беге."""
        RUN_COEF_1 = 18
        RUN_COEF_2 = 20
        M_IN_KM = self.M_IN_KM 
        avg_speed = self.get_mean_speed()
        weight = self.weight
        duration = self.duration * self.HOUR_TO_MIN #Длительность трени в минутах
        
        result = ((RUN_COEF_1 
                    * avg_speed - RUN_COEF_2) 
                    * weight / M_IN_KM * duration) 
        
        return result


class SportsWalking(Training):
    """Тренировка: спортивная ходьба."""
    def __init__(self,  
                 action: int, 
                 duration: float, 
                 weight: float, 
                 height:int) -> None:
        super().__init__(action, duration, weight)
        self.height = height #Рост спорсмена в см.
    
    def get_spent_calories(self) -> float:
        """Получение затраченных калорий при хотьбе."""
        WLK_COEF_1 = 0.035
        WLK_COEF_2 = 0.029
        KMH_TO_MS = 0.278 #Коэффициент перевода из км/ч в м/с
        avg_speed = self.get_mean_speed()
        height = self.height
        weight = self.weight
        duration = self.duration * self.HOUR_TO_MIN #Время тренировки в минутах
        result = ((WLK_COEF_1 
                    * weight  + (KMH_TO_MS * avg_speed) ** 2 
                    // height * WLK_COEF_2 * weight) * duration)
        
        return result

class Swimming(Training):
    """Тренировка: плавание."""
    LEN_STEP = 1.38 #Коэф первода из гребков в метры
    def __init__(self, 
                 action: int, 
                 duration: float, 
                 weight: float,
                 length_pool: int,
                 count_pool: int) -> None:
        super().__init__(action, duration, weight)
        self.length_pool = length_pool
        self.count_pool = count_pool

    def get_mean_speed(self) -> float:
        """Получение средней скорости при плавании."""
        length_pool = self.length_pool #Длинна бассеина
        count_pool = self.count_pool # Количество проплытых бассеинов
        M_IN_KM = self.M_IN_KM
        duration = self.duration
        result = length_pool * count_pool / M_IN_KM / duration
        
        return result
    
    def get_spent_calories(self) -> float:
        """Получение затраченных калорий при плавании"""
        SWM_KOEF_1 = 1.1
        weight = self.weight
        avg_speed = self.get_mean_speed()# ср скорость при плавании
        result = (avg_speed + SWM_KOEF_1) * 2 * weight
        
        return result

def read_package(workout_type: str, data: list) -> Training:
    """Прочитать данные полученные от датчиков."""
    trainig_types={
        'RUN':Running,
        'WLK':SportsWalking,
        'SWM':Swimming
    }
    object=trainig_types[workout_type](*data)
    
    return object


def main(training: Training) -> None:
    """Главная функция."""
    info = training.show_training_info().get_message()
    print(info)


if __name__ == '__main__':
    packages = [
        ('SWM', [720, 1, 80, 25, 40]),
        ('RUN', [15000, 1, 75]),
        ('WLK', [9000, 1, 75, 180]),
    ]

    for workout_type, data in packages:
        training = read_package(workout_type, data)
        main(training)
