import pair_gen
from pair_gen import pair_maker
from pprint import pprint

pm=pair_maker()
pm.generate_one()

# names=['Anh (DA) Nguyen',
# 'Anushadevi Mohan',
# 'Camilla Nawaz',
# 'Elham Keshavarzian',
# 'Himani Agrawal',
# 'InHo (Edward) Rha',
# 'Jacob Hawkesworth',
# 'Jeremy Gozlan',
# 'Jianda (Jay) Zhou',
# 'Joseph Fang',
# 'Joseph Wiley',
# 'Kenneth Durell',
# 'Empty',
# 'Matthew Wong',
# 'Nikhil Makaram',
# 'Praveen Vaikunta Raman',
# 'Rosina Norton',
# 'Shige Tajima',
# 'Urmi Mukherjee',
# 'Yuwei (Kelly) Peng']

# (0, 3)
# ahn Elham
# (1, 14)
# Anusha Nikhil
# (13, 17)
# Matt Shige
# (6, 15)
# Jacob Praveen *
# (2, 7)
# Camilla Jeremy
# (4, 5)
# Himani Edward
# (8, 11)
# Jay Kenny
# (16, 19)
# Rosina Kelly *
# (9, 10, 18)
# Joseph Fang Joseph Wiley Urmi
# num_name=zip(xrange(len(names)), names)
# pprint (num_name)

# Start Day 23
# ('Anushadevi Mohan', 'Joseph Wiley')
# ('Joseph Fang', 'Shige Tajima')
# ('Jacob Hawkesworth', 'Yuwei (Kelly) Peng')
# ('Elham Keshavarzian', 'Himani Agrawal')
# ('Anh (DA) Nguyen', 'Kenneth Durell')
# ('Jeremy Gozlan', 'Jianda (Jay) Zhou')
# ('Praveen Vaikunta Raman', 'Urmi Mukherjee')
# ('Camilla Nawaz', 'InHo (Edward) Rha')
# ('Matthew Wong', 'Nikhil Makaram', 'Rosina Norton')
# End Day 23
# Date & Time of Creation: Tue Jul 18 09:53:36 2017
#
# Start Day 24
# ('Anushadevi Mohan', 'InHo (Edward) Rha')
# ('Jianda (Jay) Zhou', 'Praveen Vaikunta Raman')
# ('Jeremy Gozlan', 'Yuwei (Kelly) Peng')
# ('Camilla Nawaz', 'Nikhil Makaram')
# ('Kenneth Durell', 'Shige Tajima')
# ('Jacob Hawkesworth', 'Matthew Wong')
# ('Anh (DA) Nguyen', 'Joseph Wiley')
# ('Elham Keshavarzian', 'Joseph Fang')
# ('Himani Agrawal', 'Rosina Norton', 'Urmi Mukherjee')
# End Day 24
# Date & Time of Creation: Tue Jul 18 09:58:21 2017
#
# Start Day 25
# ('Praveen Vaikunta Raman', 'Shige Tajima')
# ('Anushadevi Mohan', 'Himani Agrawal')
# ('Joseph Wiley', 'Rosina Norton')
# ('InHo (Edward) Rha', 'Yuwei (Kelly) Peng')
# ('Camilla Nawaz', 'Jacob Hawkesworth')
# ('Nikhil Makaram', 'Urmi Mukherjee')
# ('Anh (DA) Nguyen', 'Matthew Wong')
# ('Jianda (Jay) Zhou', 'Joseph Fang')
# ('Elham Keshavarzian', 'Jeremy Gozlan', 'Kenneth Durell')
# End Day 25
# Date & Time of Creation: Tue Jul 18 09:58:55 2017



#deleted first 110 points from history to generate new pairs. that's ~9 days worth of student pairs.
#keeping triples in list? will do in a bit. need to generate custom pairs for today.
#specifically was asked to make a triplet with Ahn/DA in it.

'''
deleted points

(0, 9)
(1, 11)
(2, 12)
(3, 13)
(4, 14)
(5, 15)
(6, 16)
(7, 17)
(8, 18)
(10, 19)
(1, 4)
(16, 18)
(3, 5)
(6, 17)
(2, 14)
(11, 15)
(9, 12)
(10, 13)
(8, 19)
(0, 7)
(0, 12)
(7, 19)
(3, 17)
(6, 15)
(11, 18)
(14, 16)
(2, 5)
(4, 8)
(1, 13)
(9, 10)
(8, 16)
(15, 18)
(1, 17)
(2, 10)
(11, 14)
(3, 19)
(5, 13)
(7, 9)
(0, 4)
(4, 6)
(0, 6)
(0, 4, 6)
(1, 18)
(2, 19)
(3, 4)
(5, 10)
(6, 8)
(7, 15)
(11, 17)
(13, 16)
(0, 9, 14)
(10, 15)
(1, 2)
(4, 5)
(7, 13)
(8, 17)
(6, 14)
(3, 11)
(0, 19)
(9, 18)
(10, 16)
(15, 16)
(10, 15, 16)
(2, 8)
(6, 19)
(7, 16)
(0, 10)
(9, 17)
(3, 14)
(4, 15)
(1, 5)
(13, 18)
(2, 11)
(8, 11)
(2, 8, 11)
(11, 13)
(2, 4)
(1, 3)
(17, 19)
(8, 9)
(5, 14)
(6, 7)
(10, 18)
(0, 15)
(2, 16)
(4, 16)
(2, 4, 16)
(13, 14)
(1, 9)
(2, 7)
(0, 11)
(4, 19)
(8, 10)
(15, 17)
(1, 6)
(6, 9)
(3, 5)
(1, 6, 9)
(6, 13)
(5, 18)
(4, 10)
(0, 1)
(11, 19)
(14, 17)
(2, 3)
(7, 8)
(9, 15)
(0, 16)
(1, 16)
(0, 1, 16)
(0, 18)
(4, 9)
(5, 11)
(7, 14)
(1, 10)
(13, 17)
(3, 8)
(2, 6)
(16, 19)
(3, 15)
(8, 15)
(3, 8, 15)
(0, 14)
(18, 19)
(6, 10)
(8, 13)
(4, 7)
(5, 17)
(2, 9)
(3, 16)
(1, 15)
(6, 11)
(10, 11)
(6, 10, 11)
'''

'''
old triplets

(0, 4, 6)
(0, 9, 14)
(10, 15, 16)
(2, 8, 11)
(2, 4, 16)
(1, 6, 9)
(0, 1, 16)
'''


'''
saved history

(0, 18)
(4, 9)
(5, 11)
(7, 14)
(1, 10)
(13, 17)
(3, 8)
(2, 6)
(16, 19)
(3, 15)
(8, 15)
(3, 8, 15)
(0, 14)
(18, 19)
(6, 10)
(8, 13)
(4, 7)
(5, 17)
(2, 9)
(3, 16)
(1, 15)
(6, 11)
(10, 11)
(6, 10, 11)
(4, 11)
(1, 8)
(16, 17)
(2, 18)
(0, 3)
(14, 15)
(5, 6)
(9, 19)
(7, 10)
(9, 13)
(13, 19)
(9, 13, 19)
(0, 8)
(7, 18)
(1, 19)
(9, 11)
(3, 6)
(4, 17)
(10, 14)
(5, 16)
(2, 15)
(2, 13)
(13, 15)
(2, 13, 15)
(1, 7)
(4, 13)
(0, 2)
(3, 10)
(9, 14)
(6, 18)
(15, 19)
(11, 16)
(5, 8)
(0, 17)
(2, 17)
(0, 2, 17)
'''

'''
"new" pairs

(0, 9)
(5, 7)
(4, 8)
(14, 19)
(11, 13)
(10, 15)
(1, 18)
(2, 3)
(6, 17)
(0, 16)
(9, 16)
(0, 9, 16)
'''


'''
Generated but unused pairs...

(3, 11)
(15, 17)
(1, 4)
(10, 16)
(5, 19)
(2, 6)
(14, 18)
(0, 13)
(8, 9)
(3, 7)
(7, 11)
(3, 7, 11)
(5, 14)
(17, 18)
(2, 4)
(10, 13)
(15, 16)
(1, 3)
(6, 8)
(7, 9)
(0, 19)
(5, 11)
(11, 14)
(5, 11, 14)

'''
