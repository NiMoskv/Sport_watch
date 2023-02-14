class Training:
    """Базовый класс тренировки."""

    def __init__(*self,
                 action: int,
                 duration: float,
                 weight: float,
                 working_type: str
                 ) -> None:
        self.working_type = working_type
        self.action = action
        self.duration = duration
        self.weight = weight
        self.M_IN_KM = 1000
        if working_type == 'SWM':
            self.LEN_STEP = 1.38
        elif working_type == 'RUN' or working_type == 'WLK':
            self.LEN_STEP = 0.65
    
    def __str__(self) -> str:
        return (f'steps: {self.action} , duration: {self.duration}, weight: {self.weight}, working_type: {self.working_type} ')

r1 = Training(*[720, 1, 80, 'SWM'])
print(r1)