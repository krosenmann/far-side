
# -*- coding: utf-8 -*-

class Сharacter:
 def __init__(self, characterName):
   self.characterName = ""
   self.description = ""

   self.strength = 0
   self.agila = 0
   self.intellegense = 0
   self.perception = 0
   self.body = 0
   self.charisma = 0
   self.luck = 0
   self.will = 0
   
   self.perks = { 'meele-weapon': 0, 'guns': 0, 'meele': 0, 
           'breaking': 0, 'repair': 0, 'investigation': 0, 
           'research': 0, 
           'stealing': 0, 'lie': 0, 'conviction':0, 'tricks':0,
           'surgeons': 0, 'first-aid': 0}
   self.xp = 0
   self.lvl = 1
   self.description = ""
   self.sort = ""
   self.inventory = []
   self.log = ""

 def lvlup(self, xp, lvl):
 
 def death(self):
     itemsDrop(self.inventory)
     self.description+=log
