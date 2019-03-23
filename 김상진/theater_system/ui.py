from movie import movieManager, movie, schedule, scheduler
from datetime import datetime
from dateutil.parser import parse

class ui:
    def __init__(self):                  #movie라는 입력값이 없는데 넣으면 에러뜸
        self.address = movieManager()
        self.scheduler = scheduler()

    def function_list(self):
        print("기능을 선택하시오")
        print("1. 영화목록 입력")
        print("2. 영화목록 보기")
        print("3. 영화목록 삭제")
        print("4. 영화상영 스케줄표")


    def run(self):
        while 1:                        # while == 1 이 아니야.
            op = input("번호를 입력하세요")
            if op == '1':
                m1 = self.input_movie()
                self.address.add_movie(m1)
            if op == '2':
                for movie in self.address.get_list():
                    print(movie.title)
            if op == "3":
                key = input("어떤 영화를 삭제하시겠습니까?")
                self.address.del_list(key)
            if op == '4':
                for movie in self.address.get_schedule():
                    print(movie.time, movie.title, movie.room)
                    # 시간대별로 정리하고 싶어.
                    # sort로 정리 <- time이라는 형태로 입력값 받기
			if op == '5':
				print('스케쥴 추가')
				time = input("시간 : ")
				room = input("룸 : ")
				title = input("영화제목 : ")
				movie = self.address.get_movie(title)
				
				if movie != None:
					s = schedule(time, room, movie)
					self.scheduler.add_schedule()


    def input_movie(self):                        #입력값 쓸 필요가 없지. input으로 넣을거니까
        inputtitle = input('제목:')
        inputtime = int(input('시간:'))
		inputroom = input('상영관: ')
		
        return movie(inputtitle, dt, inputroom)