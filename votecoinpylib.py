class vote():
    def __init__(self):
        self.dic1 = {}
        print(self.dic1)
    def questions(self,title,question,duration,category,num_options):
        self.title = title #Title of the question
        self.question = question #Question
        self.duration = duration#duration of how long a question is valid
        self.category = category #category of the question
        self.options = num_options #The various options for the question
        
        title_split = self.title.split()
        question = self.question.split()
        category = self.category.split()

        if len(title_split) < 1:
            print("The minimum title length is 1")

        elif len(title_split) > 50:
            print("You have exceeded the title limit of 50 characters")
        
        elif len(question) < 1:
            print("The minimum question number is 1")

        elif len(question) > 500:
            print('you have exceeded the maximum wordlength of 500 for questions')

        elif duration < 1:
            print('minimum duration for question')
        elif duration > 1000000:
            print('exceeded the maximum duration integer of 1000000')

        elif len(category) < 1:
            print('The minimum wordlength for category is 1')
        elif len(category) >50:
            print('maximum wordlength for category is 50')
    def options2(self,op1, op2):
        dic  = {}
        dic['A'] = op1 
        dic['B'] = op2

        print([self.title, self.question,self.duration,self.category, dic])
    def options3(self,op1, op2, op3):
        dic  = {}
        dic['A'] = op1 
        dic['B'] = op2
        dic['C'] = op3

        print(self.title, self.question,self.duration,self.category, dic)
    def options4(self,op1, op2, op3, op4):
        dic  = {}
        dic['A'] = op1 
        dic['B'] = op2
        dic['C'] = op3
        dic['D'] = op4

        print(self.title, self.question,self.duration,self.category, dic)
    def cast_vote(self,id,vote):
        self.id = id #transaction id of question message
        self.vote = vote
        a = 0
        b = 0
        c = 0
        d = 0       
        id = self.id.split()
        if len(id) < 1:
            print('minimum wordlength is 1')

        elif len(id) > 60:
            print('exceeded worldlength limit')
        if self.options == 2:
            if self.vote == 'A':
                a+=1
            elif self.vote == 'B':
                b+=1
            self.dic1['A'] = a
            self.dic1['B'] = b
            print(self.id, self.dic1)
        if self.options == 3:
            if self.vote == 'A':
                a+=1
            elif self.vote == 'B':
                b+=1
            elif self.vote == 'C':
                c+=1
            self.dic1['A'] = a
            self.dic1['B'] = b
            self.dic1['C'] = c
            print(self.id, self.dic1)

        if self.options == 4:
            if self.vote == 'A':
                a+=1
            elif self.vote == 'B':
                b+=1
            elif self.vote == 'C':
                c+=1
            elif self.vote == 'D':
                d+=1
            self.dic1['A'] = a
            self.dic1['B'] = b
            self.dic1['C'] = c
            self.dic1['D'] = d
            print(self.id, self.dic1)
    def trusted_list(self,trusted,untrusted):
        self.trusted_lists = ["TESTDUUODZVXNO4YKEK4I5I6UU67ANYBJ77JZUI444VAD7V3TL26DVOMFA", "TESTAUZJU4JRAPUZBH4FCPYDLEWIFIFRPVILUZBSYP6IBZLYF6M6YVMMX4", "TESTC2TMLDK273INHLXCSV235NFJ5LITNFDXZPU7JTZCVCBAZDUSJS4OPU"]
        self.trusted = trusted
        self.untrusted = untrusted

        trusted = self.trusted.split()
        untrusted = self.untrusted.split()

        if len(trusted) < 1:
            print('wordlength less than 1')
        elif len(untrusted) > 60:
            print('wordlength is greater 60')

        self.trusted_lists.append(self.trusted)
        self.trusted_lists.remove(self.untrusted)

        print(self.trusted_lists)

    def vote_delegation(self,id1_vote, id2_vote, id3_vote):
        self.id1 = id1_vote
        self.id2 = id2_vote
        self.id3 = id3_vote
        dic2 = {}
        id1 = str(self.trusted_lists[0])
        id2 = str(self.trusted_lists[1])
        id3 = str(self.trusted_lists[2])
        #assumming the vote power limit for all persons in 100%
        #giving the fact they are 3 persons each person is assigned 33.3% voting power
        id1_vp = 33.3
        id2_vp = 33.3
        id3_vp = 33.3
        if self.id1 == 2: #this means the user is allocating his/her voting power to person2
            id1_vp = 0.1
            id2_vp = 66.6
            id3_vp = 33.3
            dic2[id1] = id1_vp
            dic2[id2] = id2_vp
            dic2[id3] = id3_vp
            print(dic2)
        elif self.id1 == 3:
            id1_vp = 0.1
            id2_vp = 33.3
            id3_vp = 66.6
            dic2[id1] = id1_vp
            dic2[id2] = id2_vp
            dic2[id3] = id3_vp
            print(dic2)
        if self.id2 == 1:
            id1_vp = 66.6
            id2_vp = 0.1
            id3_vp = 33.3
            dic2[id1] = id1_vp
            dic2[id2] = id2_vp
            dic2[id3] = id3_vp
            print(dic2)
        elif self.id2==3:
            id1_vp = 33.3
            id2_vp = 0.1
            id3_vp = 66.6
            dic2[id1] = id1_vp
            dic2[id2] = id2_vp
            dic2[id3] = id3_vp
            print(dic2)
        if self.id3 == 1:
            id1_vp = 66.6
            id2_vp = 33.3
            id3_vp = 0.1
            dic2[id1] = id1_vp
            dic2[id2] = id2_vp
            dic2[id3] = id3_vp
            print(dic2)
        elif self.id3 == 2:
            id1_vp = 33.3
            id2_vp = 66.6
            id3_vp = 0.1
            dic2[id1] = id1_vp
            dic2[id2] = id2_vp
            dic2[id3] = id3_vp
            print(dic2)
        
    


        


vote = vote()

vote.questions("finance","how do we spend w4 tinyman earning",1000000, 'community',3)
vote.options2('choice coin', 'vote coin')
vote.cast_vote("CRID3AHJGGVE75UTDO5GI7PXM6PUD6WXB7BTAD3IPWFTMUXUKHDA",'A')
vote.trusted_list("TESTB74MOARQDWSX4433VWVNO4VJK3PDQWQ4JEOVQQTK3ZIX2MK3JF55TE", "TESTDUUODZVXNO4YKEK4I5I6UU67ANYBJ77JZUI444VAD7V3TL26DVOMFA")
vote.vote_delegation(2,2,3)