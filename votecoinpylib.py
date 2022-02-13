import string


class vote():
    def questions(self,title,question,duration,category,options):
        self.title = title #Title of the question
        self.question = question #Question
        self.duration = duration#duration of how long a question is valid
        self.category = category #category of the question
        self.options = options #The various options for the question
        
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

        print(self.title,self.question,self.duration,self.category,self.options)


    def cast_vote(self,id,op1,op2):
        self.id = id #transaction id of question message
        self.op1 = op1 #Valid vote options
        self.op2 = op2
        id = self.id.split()
        

        if len(id) < 1:
            print('minimum wordlength is 1')

        elif len(id) > 60:
            print('exceeded worldlength limit')

    def vote_delegation(self,d):
        self.d = {
            "any":{"TESTB74MOARQDWSX4433VWVNO4VJK3PDQWQ4JEOVQQTK3ZIX2MK3JF55TE":20,
            "TESTC2TMLDK273INHLXCSV235NFJ5LITNFDXZPU7JTZCVCBAZDUSJS4OPU":80},
            "finance":{"TESTDUUODZVXNO4YKEK4I5I6UU67ANYBJ77JZUI444VAD7V3TL26DVOMFA":1}
        }

    def trusted_list(self,trusted,untrusted):
        trusted_list = ["TESTDUUODZVXNO4YKEK4I5I6UU67ANYBJ77JZUI444VAD7V3TL26DVOMFA", "TESTAUZJU4JRAPUZBH4FCPYDLEWIFIFRPVILUZBSYP6IBZLYF6M6YVMMX4"]
        self.trusted = trusted
        self.untrusted = untrusted

        trusted = self.trusted.split()
        untrusted = self.untrusted.split()

        if len(trusted) < 1:
            print('wordlength less than 1')
        elif len(untrusted) > 60:
            print('wordlength is greater 60')

        trusted_list.append(self.trusted)
        trusted_list.remove(self.untrusted)

        print(trusted_list)
    
    


        


vote = vote()

vote.questions("best coin\n","what is the best coin in choice coin and vote coin",1000000, '\ncommunity\n','A:choice coin\n B:vote coin')
vote.cast_vote("CRID3AHJGGVE75UTDO5GI7PXM6PUD6WXB7BTAD3IPWFTMUXUKHDA", 34,23)
vote.trusted_list("TESTB74MOARQDWSX4433VWVNO4VJK3PDQWQ4JEOVQQTK3ZIX2MK3JF55TE", "TESTDUUODZVXNO4YKEK4I5I6UU67ANYBJ77JZUI444VAD7V3TL26DVOMFA")