from datetime import datetime
import psutil


class pomodoro:
    def __init__(self):
        self.prompt()

    def prompt(self):
        texttoprompt = '''Hello do you want to lauch Pomodoro?:\n1: Yes\n2: No(Exit)\n'''
        option = input(texttoprompt)
        if option == "1" or option=="Yes":
            self.launchpomodoro()
        else:
            quit()

    def launchpomodoro(self):
        timeofwork = input("Tempo de Trabalho:")
        timeofrest = input("Tempo de Descanso:")
        intervals = input("Número de intervalos:")
        num_of_iterations = 0
        while num_of_iterations<int(intervals):
            (limithour, limitminutes, current_seconds)=self.timer(int(timeofwork))
            self.processChecker(limithour,limitminutes,current_seconds)
            print("Acabou o tempo de Trabalho")
            self.rest(int(timeofrest))
            print("Acabou o tempo de descanso")
            num_of_iterations+=1
            print("Acabou um ciclo")

    def rest(self, timeofrest):
        temp_time = datetime.now().time()
        temp_time = str(temp_time).split(":")
        current_hour= temp_time[0]
        current_minutes = temp_time[1]
        current_seconds = temp_time[2]
        #tirar os milisegundos
        current_seconds = current_seconds.split(".")
        current_seconds = current_seconds[0]

        (limithour, limitminutes, limitseconds) = self.timer(int(timeofrest))
        while(int(current_hour)<=int(limithour) or int(current_minutes)<=int(limitminutes) or int(current_seconds)<=int(limitseconds)):
            temp_time = datetime.now().time()
            temp_time = str(temp_time).split(":")
            current_hour= temp_time[0]
            current_minutes = temp_time[1]
            current_seconds = temp_time[2]
            #tirar os milisegundos
            current_seconds = current_seconds.split(".")
            current_seconds = current_seconds[0]


    def timer(self, timeofwork):
        temp_time = datetime.now().time()
        temp_time = str(temp_time).split(":")
        current_hour= temp_time[0]
        current_minutes = temp_time[1]
        current_seconds = temp_time[2]
        #tirar os milisegundos
        current_seconds = current_seconds.split(".")
        current_seconds = current_seconds[0]

        (limithour, limitminutes) = self.timeAfterWork(int(current_hour), int(current_minutes), int(current_seconds), int(timeofwork))
        return (limithour, limitminutes, current_seconds)

    def timeAfterWork(self, current_hour, current_minutes, current_seconds, time_of_work):
        limithour=current_hour
        if(current_minutes+time_of_work>60):
            while(current_minutes+time_of_work>=60):
                    limithour+=1
                    current_minutes=time_of_work+current_minutes-60
                    time_of_work=time_of_work-current_minutes
        else:
            current_minutes=current_minutes+time_of_work

        return(limithour,current_minutes)

    def processChecker(self,limit_hour, limit_minutes, limit_seconds):
        temp_time = datetime.now().time()
        temp_time = str(temp_time).split(":")
        current_hour= int(temp_time[0])
        current_minutes = int(temp_time[1])
        current_seconds = temp_time[2]
        current_seconds = int(current_seconds.split(".")[0])
        while(current_hour<=int(limit_hour) or current_minutes<=int(limit_minutes) or current_seconds<=int(limit_seconds)):
            temp_time = datetime.now().time()
            temp_time = str(temp_time).split(":")
            current_hour= int(temp_time[0])
            current_minutes = int(temp_time[1])
            current_seconds = temp_time[2]
            current_seconds = int(current_seconds.split(".")[0])
            for proc in psutil.process_iter():
                 if "chrome" in proc.name()or "discord" in proc.name():
                     proc.kill()

pomodoro()  