
# -*- coding: utf-8 -*-
import random

def d10():
 random.seed(100)
 return random.randint(1, 10)

def d4():
 random.seed(100)
 return random.randint(1, 4)

def d6():
 random.seed(100)
 return random.randint(1, 6)

def d12():
 random.seed(100)
 return random.randint(1, 12)

def d20():
 random.seed(100)
 return random.randint(1, 20)
