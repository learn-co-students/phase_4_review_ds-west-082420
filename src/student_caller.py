import numpy as np
from itertools import permutations


class CohortCaller:

    def __init__(self, student_list):

        self.student_list = student_list
        self.mutable_student_list = self.student_list.copy()
        self.all_pairs = []
        self.mutable_pairs = None

    def call_n_students(self, number_of_students=1):

        """
        Instruct n_random_students to select a given number of students
        from the class list. 
        :param number_of_students: The number of students to choose in each call
        :returns: 
        """

        # Reset the list if there are not enough students to be called
        if len(self.mutable_student_list) < number_of_students:
            print(self.mutable_student_list)

            self.mutable_student_list = self.student_list.copy()

        choice =  np.random.choice(self.mutable_student_list,
                                   number_of_students, replace=False)

        self.mutable_student_list = [student for student in
                                     self.mutable_student_list if
                                     student not in choice]

        return choice

    def generate_pairs(self):


        '''
        Pairs of students are generated from the student list using itertools
        combinations.
        After each pair activities, the used pairs are removed
        from the mutable pairs list
        '''

        pairs = list(permutations(self.student_list, 2))
        if self.mutable_pairs == None:
            # np.random.choice doesn't work when choosing tuples from a list
            # so pair tupples are converted to strings
            self.all_pairs = [pair[0] +' '+ pair[1] for pair in pairs]
            self.mutable_pairs = self.all_pairs.copy()

        '''The number of pairs should be the total number of students
         divided by 2 rounded down.
         If there is an odd number of students, the odd student will
         be added to the last group'''

        # if the class has an odd number of students
        if len(self.student_list)%2:
            number_of_pairs = len(self.student_list)//2

            activity_pairs = np.random.choice(self.mutable_pairs, number_of_pairs,
                                            replace=False)

            selected_students = set([student for pair in activity_pairs
                                for student in pair.split(' ')])

            # if not all students were selected, recreate the pairs
            # subtract 1 from len because of odd number of students 
            while len(selected_students) != len(self.student_list)-1:
                activity_pairs = np.random.choice(self.mutable_pairs, number_of_pairs,
                                            replace=False)
                selected_students = set([student for pair in activity_pairs
                                for student in pair.split(' ')])


            # Add statement if selected list != len of students, then regenerate pairs
            # for classes with an odd number of students
            for pair, group in zip(activity_pairs, range(1,len(activity_pairs)+1)):
                print('Group ' + str(group) + ': Driver --> ' + pair + ' <--Navigator')

                self.mutable_pairs.remove(pair)

            # with odd number of students, one student won't be selected
            # print out and add to the last group
            student_not_selected = [student for student in self.student_list
                                    if student not in selected_students]

            print('Group ' + str(group) + ': ' + student_not_selected[0])


        # if the class has an even number of students
        else:

            number_of_pairs = len(self.student_list)//2

            activity_pairs = np.random.choice(self.mutable_pairs, number_of_pairs,
                                            replace=False)

            # Determine which students were randomly selected
            selected_students = set([student for pair in activity_pairs
                                for student in pair.split(' ')])

            # if not all students were selected, recreate the pairs
            while len(selected_students) != len(self.student_list):
                activity_pairs = np.random.choice(self.mutable_pairs, number_of_pairs,
                                            replace=False)
                selected_students = set([student for pair in activity_pairs
                                for student in pair.split(' ')])

            if not len(self.student_list)%2:
                for pair, group in zip(activity_pairs, range(1,len(activity_pairs)+1)):
                    print('Group ' + str(group) + ': Driver --> ' + pair + ' <--Navigator')
                    self.mutable_pairs.remove(pair)