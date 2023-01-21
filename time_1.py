# Импортируйте datetime. 
import datetime
# Импортируйте time.
import time

class Quest:
    def __init__(self, name, description, goal):
        self.name = name
        self.description = description
        self.goal = goal
        self.start_time = None
        self.end_time = None
        # Допишите два свойства класса. готово
    
    # Напишите методы приема и сдачи квеста.
    def accept_quest(self):
        self.start_time = datetime.datetime.now()
        if self.end_time != None:
            print ('С этим испытанием вы уже справились.')
        print (f'Начало {quest_name} положено.')

    def pass_quest(self):
        self.end_time = datetime.datetime.now()
        if self.start_time == None:
            print (f'Нельзя завершить то, что не имеет начала!')
        
        completione_time = self.end_time - self.start_time
        print (f'Квест {quest_name} окончен. Время выполнения квеста {completione_time}')     


quest_name = 'Сбор пиксельники'
quest_goal = 'Соберите 12 ягод пиксельники.'
quest_description = '''
В древнем лесу Кодоборье растёт ягода "пиксельника".
Она нужна для приготовления целебных снадобий.
Соберите 12 ягод пиксельники.'''

new_quest = Quest(quest_name, quest_description, quest_goal) 

print(new_quest.pass_quest())