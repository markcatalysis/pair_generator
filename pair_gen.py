import random
from itertools import izip, combinations

# import os
# os.getcwd()
# os.chdir('/home/markcatalysis/Desktop/g45/pair_gen')

# may update to use sets instead of tuples!
# keep FULL student indices even if students leave to ensure that pairs_history still valid

class pair_maker(object):

    def __init__(self, current_number_students=[], hard_pair_avoid_list=[]):
        # self.hard_pair_avoid_list=[]
        self.pairs_history=[]
        self.import_history()
        #sort pairs
        self.pairs_history=[self.pair_sort(x) for x in self.pairs_history]
        self.student_list=[]
        self.fill_student_list()
        self.n=len([x for x in self.student_list if x != 'Empty'])
        self.day_counter=0
        self._fail_counter=0
        self.import_counters()
        self.missing_students=[]
        self.fill_missing()
        self.output_pair_list=[]
        self.index_pairs=[]
        self.triple=[]
        self.triple_list=[pair for pair in self.pairs_history if len(pair)==3 and type(pair)==tuple]
        self.soft_avoid_list=[]
        self.continue_gen=True

        # partners_history_includes triples instead of just pairs
        # starting at 4 due to previous day pairs. 4 means 5th day. 0 is first.

    def fill_student_list(self):
        self.student_list= ['Anh Nguyen',
        'Anushadevi Mohan',
        'Camilla Nawaz',
        'Elham Keshavarzian',
        'Himani Agrawal',
        'InHo (Edward) Rha',
        'Jacob Hawkesworth',
        'Jeremy Gozlan',
        'Jianda (Jay) Zhou',
        'Joseph Fang',
        'Joseph Wiley',
        'Kenneth Durell',
        'Empty',
        'Matthew Wong',
        'Nikhil Makaram',
        'Praveen Vaikunta Raman',
        'Rosina Norton',
        'Shige Tajima',
        'Urmi Mukherjee',
        'Yuwei (Kelly) Peng']

    def absent_students(self):
        students_absent=raw_input('Are there students absent?')
        if students_absent in [True, 'yes', 'y']:
            current_student_roster=zip([x for x in self.student_list if x!='Empty'], [self.student_list.index(x) for x in self.student_list if x!='Empty'])
            for i in current_student_roster:
                print i
            today_removal_list=input('Input as a list the indices of students who are not available')
            if type(today_removal_list)==list:
                for j in today_removal_list:
                    self.student_list[j]='Empty'

    def fill_missing(self):
        self.missing_students=[i for i,x in enumerate(self.student_list) if x=='Empty']

    def index_shuffler(self):

        """
        Uses random sampling to generate unique pairs. If could not create list in sufficient attempts, begins to return list to minimize repeat pair beyond 2 times.
        """
        #generate indices and remove Empty in pairs
        n_missing=len(self.missing_students)
        base_indices=range(len(self.student_list))
        if n_missing>=2:
            for i in xrange((n_missing/2)*2):
                base_indices.remove(self.missing_students[i])
                print 'successfully removed empty pairs'

        #shake up indices into randomized trial_list
        trial_list=random.sample(base_indices, k=self.n)

        #turn trial_list into trial_pairs
        trial_pairs=[self.pair_sort(x) for x in self.trial_pairs_gen(trial_list)]

        # make list for save and list to attempt multiple iterations of shuffling
        output_pair_list=[]
        student_recycle_list=[]

        # first iteration started manually
        for pair in trial_pairs:
            if pair in self.pairs_history:
                 student_recycle_list.extend(list(pair))
            else:
                 output_pair_list.append(pair)

        # more shuffling iterations
        # brute force shuffling of 100 new attempts
        counter=0
        while len(student_recycle_list)>0 and counter<=100:
            trial_list_cycle=random.sample(student_recycle_list, k=len(student_recycle_list))
            trial_pairs_cycle=[self.pair_sort(x) for x in self.trial_pairs_gen(trial_list_cycle)]
            student_recycle_list=[]
            for pair_s in trial_pairs_cycle:
                if pair_s in self.pairs_history:
                    student_recycle_list.extend(list(pair_s))
                else:
                     output_pair_list.append(pair_s)
            counter+=1
        # fix empty if odd then ship out pairs
        if len(student_recycle_list)==0:
            self.output_pair_list=output_pair_list
            if self.n%2>0:
                unpaired_student=self.odd_solver(output_pair_list)
                self.index_pairs=[]
                triple_output=self.make_a_triple(unpaired_student)
                if triple_output is None:
                    self.output_pair_list=False
                    return
                else:
                    self.index_pairs, self.triple = triple_output
                self.output_pair_list.extend(self.index_pairs)
                self.output_pair_list.append(self.triple)
            self.pairs_history.append('Start Day %s' % self.day_counter)
            self.pairs_history.extend(self.output_pair_list)
            self.pairs_history.append('End Day %s' % self.day_counter)
            self.day_counter +=1
            self.continue_gen=False
            return self.output_pair_list
        else:
            # print "failed after 100 tries. that's luck and brute force for ya."
            self._fail_counter +=1

    def odd_solver(self, list_of_tuples):
        missing_index=self.missing_students[-1]
        for tuples in list_of_tuples:
            if missing_index in tuples:
                self.output_pair_list.remove(tuples)
                pair_as_list=list(tuples)
                pair_as_list.remove(missing_index)
                unpaired_student=pair_as_list[0]
                return unpaired_student
        print 'this is why i broke'
        print list_of_tuples
        return

    def make_a_triple(self, unpaired_student):
        pair1,pair2=(False,False)
        if unpaired_student == None:
            return
        for pair in self.output_pair_list:
            if unpaired_student!=pair[0]:
                pair1=self.pair_sort(tuple((unpaired_student,pair[0])))
            if unpaired_student!=pair[1]:
                pair2=self.pair_sort(tuple((unpaired_student,pair[1])))
            if pair1 and pair2:
                if pair1 not in self.pairs_history and pair2 not in self.pairs_history:
                    output_triple=self.pair_sort(tuple((pair[0],pair[1],unpaired_student)))
                    if output_triple not in self.pairs_history:
                        output=([pair1,pair2],(output_triple))
                        # self.pairs_history.remove(self.pair_sort(pair))
                        if output[1] not in self.pairs_history:
                            self.continue_gen=False
                            return output
        # if code reached here, all triples already made before and unique pairs nearly exhausted. that's no good.
        # softening restrictions on pair formation by releasing pairs that were formed by triples:
        new_counter=0
        while new_counter<=30:
            self.relax_pairs_from_triples()
            self.index_shuffler()
            new_counter+=1
        print 'make_a_triple has failed you'

    def relax_pairs_from_triples(self):
        pairs_from_triples=[]
        for triple in self.triple_list:
            for subset in (combinations(triple, 2)):
                pairs_from_triples.append(subset)
        for pair in pairs_from_triples:
            if pair in self.pairs_history:
                self.pairs_history.remove(pair)

    def pair_sort(self, a_tuple):
        return tuple(sorted(a_tuple))

    def trial_pairs_gen(self, trial_list):
        return izip(trial_list[::2],trial_list[1::2])

    def index_to_user(self, index):
        return self.student_list[index]

    def name_history(self):
        pairs_sans_triple_pairs=[x for x in self.pairs_history if x not in self.index_pairs]
        return [tuple([self.index_to_user(i) for i in x]) if type(x)==tuple else x for x in pairs_sans_triple_pairs]

    def save_history(self):
        names = self.name_history()
        with open('name_history.txt', 'wb') as f:
            for name in names:
                #this is where we write appropriate day-starting script. can't use day counter method here.
                if 'Empty' not in name:
                    f.write(str(name)+'\n')
                #this is where we write appopriate day-ending text. can't use day counter method here.
        indices = self.pairs_history
        with open('index_history.txt', 'wb') as g:
            for index in indices:
                if type(index) == tuple:
                    g.write(str(index)+'\n')
        with open('counter_data.txt', 'wb') as c:
            c.write(str((self.day_counter,self.fail_counter)))

    def import_counters(self):
        with open('counter_data.txt', 'r') as c:
            counters=eval(c.readline())
            if counters:
                if type(counters)==tuple:
                    self.day_counter, self.fail_counter = counters

    def import_history(self):
        with open('index_history.txt', 'r') as f:
            for line in f:
                if type(eval(line))==tuple:
                    self.pairs_history.append(eval(line))

    def generate(self, number):
        self.continue_gen=True
        # number of attempts
        while self.continue_gen==True:
            for i in xrange(number):
                self.index_shuffler()
        if self.output_pair_list:
            self.save_history()
        self.continue_gen=True
        self.fill_student_list()
        self.pairs_history=[]
        self.import_history()

    def generate_one(self):
        # works best at low numbers
        # may yield nothing even if it tries really really hard because this algorithm is not a smart puppy
        # i'd make it a while loop but lord knows how dangerous while loops are
        # i will not make it a while loop. stop suggesting i make it a while loop.
        # no i will not use a smart algorithm. I want it random. I'm getting random.
        self.absent_students()
        while self.continue_gen==True:
            self.index_shuffler()
            if self.output_pair_list:
                self.save_history()
        self.continue_gen=True
        self.fill_student_list()
        self.pairs_history=[]
        self.import_history()

    def reset_counters(self):
        # hard reset
        self.day_counter=5
        self._fail_counter=0


# if __name__ == '__main__':
pm=pair_maker()
pm.reset_counters()
pm.generate_one()
pm.generate(2000)
pm.save_history()
pm.output_pair_list
pm.index_pairs
pm.pairs_history
pm.reset_counters()
pm.odd_solver(pm.output_pair_list)
pm.output_pair_list
# pm.generate(500)
# pairs_sans_triple_pairs=[x for x in pm.pairs_history if x not in pm.index_pairs]
# pairs_sans_triple_pairs
# pairs_sans_triple_pairs[0]
# pm.index_to_user(0)
# for x in pairs_sans_triple_pairs:
#     if type(x) ==tuple:
#         for i in x:
#             print(pm.index_to_user(i))
# pm.index_shuffler()
# [tuple([pm.index_to_user(i) for i in x]) if type(x)==tuple else x for x in pairs_sans_triple_pairs]
pm.odd_solver(pm.output_pair_list)


'''
old pairs for first three days if needed/overwritten:
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




(8, 14)
(5, 11)
(0, 10)
(2, 7)
(13, 16)
(12, 18)
(1, 6)
(3, 4)
(15, 17)
(0, 10)
(0, 18)
(10, 18)
(0, 10, 18)
(1, 9)
(6, 14)
(3, 10)
(2, 19)
(4, 12)
(13, 15)
(7, 18)
(0, 5)
(11, 17)
(2, 19)
(2, 4)
(4, 19)
(2, 4, 19)
(10, 15)
(5, 8)
(9, 19)
(2, 18)
(12, 16)
(6, 11)
(1, 3)
(4, 7)
(13, 17)
(10, 15)
(10, 16)
(15, 16)
(10, 15, 16)
(8, 10)
(2, 15)
(9, 16)
(0, 19)
(1, 7)
(5, 12)
(6, 18)
(13, 14)
(4, 17)
(9, 16)
(5, 9)
(5, 16)
(5, 9, 16)
(5, 7)
(2, 16)
(1, 18)
(8, 11)
(3, 12)
(14, 19)
(9, 17)
(0, 13)
(4, 10)
(2, 16)
(2, 3)
(3, 16)
(2, 3, 16)
(13, 18)
(12, 17)
(3, 7)
(6, 10)
(0, 16)
(1, 5)
(11, 19)
(2, 9)
(14, 15)
(12, 17)
(12, 17)
(17, 18)
(12, 17, 17)
(4, 9)
(18, 19)
(6, 8)
(0, 17)
(3, 14)
(12, 15)
(2, 13)
(1, 16)
(7, 10)
(4, 9)
(4, 15)
(9, 15)
(4, 9, 15)
(6, 9)
(10, 12)
(7, 8)
(0, 2)
(1, 15)
(4, 11)
(13, 19)
(14, 17)
(3, 18)
(14, 17)
(10, 14)
(10, 17)
(10, 14, 17)
(5, 10)
(9, 13)
(3, 8)
(11, 12)
(7, 14)
(6, 19)
(16, 17)
(0, 1)
(4, 18)
(9, 13)
(9, 11)
(11, 13)
(9, 11, 13)
(0, 11)
(3, 15)
(2, 6)
(5, 17)
(9, 18)
(12, 14)
(8, 13)
(4, 16)
(1, 19)
(9, 18)
(9, 14)
(14, 18)
(9, 14, 18)


'''
