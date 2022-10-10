#!/usr/bin/env python
# coding: utf-8

# In[1]:


class GreenZoneIndex:
    def __init__(self, territory_name, territory_area, green_zones):
        """
        :param territory_name: Название территории
        :param territory_area: Площадь территории
        :param green_zones: Список площадей парков
        """
        # TODO все аргументы конструктора записать в атрибуты экземпляра класса
        self.territore_name = territory_name
        self.territory_area = territory_area
        self.green_zones = green_zones

        self.green_index = None  # индекс озеленения
        # TODO посчитать индекс озеленения с помощью метода calculate_green_index
        self.green_index = self.calculate_green_index() #вызываю функцию

    def calculate_green_index(self):
        """
        Метод для вычисления индекса озеленения.

        Индекс рассчитывается как отношение площади всех парков к площади территории
        """
        ...
        # TODO посчитать индекс озеленения с атрибутов экземпляра класса
        total_square = 0 #обнуляю счетчик
        for zone in green_zones: #цикл, чтобы сосчитать все зоны
          total_square += zone
        green_index = total_square/self.territory_area #высчитываю индекс озеленения
        return round(green_index, 4) #округляю индекс озеленения

territory_name = "Пушкин"
territory_area = 28676
green_zones = [302, 487, 420, 325, 471, 363, 404]
# TODO Создать экземпряр класса и с помощью его атрибутов распечатать индекс озеленения в процентах до 2 знака после запятой.

pushkin =  GreenZoneIndex(territory_name = "Пушкин",territory_area = 28676, green_zones = [302, 487, 420, 325, 471, 363, 404])

print(f'Индекс озеленения территории {territory_name} равен {pushkin.green_index*100}%') # Ожидаемый ответ Индекс озеленения территории Пушкин равен 9.67%


# In[2]:


list_territories = [
    {
        "territory_name": "Пушкин",
        "territory_area": 28676,
        "green_zones": [302, 487, 420, 325, 471, 363, 404]
    },
    {
        "territory_name": "Павловск",
        "territory_area": 21025,
        "green_zones": [360, 375, 223, 258, 345, 296, 303]
    },
    {
        "territory_name": "Петергоф",
        "territory_area": 44274,
        "green_zones": [364, 447, 438, 223, 336, 431, 442]
    },
]

new_list = []
for city in list_territories:
  new_list.append(GreenZoneIndex(territory_name = city['territory_name'], territory_area = city['territory_area'], green_zones = city['green_zones']))
print(new_list)


# In[3]:


def get_mean_green_index (new_list):
  total_index = 0 #переменная для подсчета суммы
  for city in new_list: 
    total_index += city.green_index
  avg_index = total_index/len(new_list) #среднее значение индекса
  return avg_index
print(get_mean_green_index(new_list))


# In[4]:


def filter_min_green_index (new_list, min_green=0.1):
  total_territories = 0 #счетчик
  for city in new_list:
    if city.green_index < min_green: #применяем условие 
      total_territories +=1
  return total_territories
print(filter_min_green_index(new_list))

