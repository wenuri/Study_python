#delete
#1. 빈 리스트 생성
#2. append를 이용해 데이터 추가
#3. pop을 이용해 데이터 삭제
#4. 또다른 리스트를 만들어 3번에서 삭제한 인덱스, 데이터 저장
#5. 저장된 리스트에 역순으로 데이터를 뽑아  insert 이용해 복원

#1, 2
data = []
data.append( int(input('숫자 입력 : ')))  #키보드에서 입력받는 모든 input은 문자열로 인식한다 그러므로 정수형으로 바꿔줘야함
data.append( int(input('숫자 입력 : ')))
data.append( int(input('숫자 입력 : ')))

print('data = ', data)

#3
removed_list = []
removed_data = data.pop(1) #data [10. 20]
removed_list.append([1,removed_data]) #[ [1.30]]

print('1번 데이타 삭제값 :', removed_list)

removed_data = data.pop(0) #data []
removed_list.append([0,removed_data]) #[[1,30],[0,10],[0,20]]
print('0번 데이타 삭제값 :', removed_list)
print('data = ', data)


