# 최대 힙 구현
class Element: # 힙 내부에서 값을 편하게 불러오기 위해 	Element라는 클래스 생성
    def __init__(self, key):
        self.__key = key

    @property # get 역할을 하는 어노테이션. @property = 이 key가 무엇인지 알아내는 용도
    def key(self):
        return self.__key

    @key.setter #  set역할을 하는 어노테이션. @key.setter = key의 값을 설정하는 용도
    def key(self, k):
        self.__key = k

class MaxHeap:
    MAX = 10 # 최대 힙 사이즈, 클래스 선언할 때 받는게 더 좋을 수도 있다.
    def __init__(self):
        self.__heapsize = 0
        # 배열을 사용한 힙 구현, 힙 사이즈만큼 일단 None을 채워준다.
        self.__container = [None for _ in range(MaxHeap.MAX)]

    # 부모와 자식노드의 인덱스를 구하는 내부 메소드
    def __get_parent_idx(self, cur): # 부모 찾으려면 2로 나누면 됨. (이건 루트 노드 인덱스가 1이라는 가정), 앞에 '__'가 붙으면 클래스 내부에서 쓰는 이름.
        return cur // 2

    def __get_left_child_idx(self, cur): # 왼쪽 자식은 2로 곱하면 됨. 예를 들어 2의 왼쪽 자식은 4.
        return cur * 2

    def __get_right_child_idx(self, cur): # 오른쪽 자식이 있다면, 왼쪽 자식의 오른쪽이니 +1 해주면 됨.
        return cur * 2 + 1

    def is_empty(self): #힙의 데이터가 비었는지 확인
        if self.__heapsize == 0:
            return True
        else:
            return False

    def is_full(self): #힙의 데이터가 꽉 찼는지 확인
        if self.__heapsize >= MaxHeap.MAX:
            return True
        return False

    def push(self, key): # 힙에 데이터를 넣기.
        if self.is_full():
            return
        self.__heapsize += 1 
        #완전 이진트리가 되려면 왼쪽부터 아래로 삽입 해야되니까 사이즈를 1늘린다.
        self.__container[self.__heapsize] = Element(key) 
        # heapsize는 결국 마지막 인덱스니까 거기에 추가할 노드를 삽입.
        
        cur = self.__heapsize # 마지막 노드의 인덱스
        par = self.__get_parent_idx(cur) # 마지막 노드의 부모 노드 인덱스
        
        while cur != 1: # 루트 노드로 올라가면 반복문 종료
            if self.__container[par].key < self.__container[cur].key: 
            # 부모 노드가 현재 넣은 노드보다 작다면 (최대힙은 더 크면 부모가 되니까)
                self.__container[par].key, self.__container[cur].key = self.__container[cur].key, self.__container[par].key 
                cur = par
                par = par // 2
                # 자식은 부모 인덱스로 가고, 부모는 상위 부모 인덱스로 가게 세팅
            else:
                break

    # 자식노드 중 더 큰 값을 가지는 자식의 인덱스를 반환하는 메소드
    def __get_bigger_child_idx(self, cur): 
    # 어떤 부모노드의 자식 노드가 2개 있다면 어떤 걸 반환할지 결정
        
        if cur * 2 > self.__heapsize: 
        # 자식노드가 힙 크기보다 크면 자식이 없는거니까 None 반환
            return None
            
        elif cur * 2 == self.__heapsize: 
        # 왼쪽 자식 노드가 힙 크기와 같으면 그게 마지막 노드니까 그거 반환
            return cur * 2
        else:
            if self.__container[cur * 2].key > self.__container[cur * 2 + 1].key: 
            #왼쪽이 오른쪽보다 크면 왼쪽 반환
                return cur * 2
            else:
                return cur * 2 + 1

    def pop(self): # 힙 데이터 삭제하는 메소드
        if self.is_empty():
            return

        ret = self.__container[1].key # 루트노드(인덱스 1)를 할당
        temp = self.__container[self.__heapsize] 
        # 가장 마지막 노드를 루트 노드로 옮기기 위해 temp에 담는다.
        
        cur_idx = 1
        bigger_child_idx = self.__get_bigger_child_idx(cur_idx) 
        # 루트 노드의 자식과 비교하기 위해 get~~child 메소드 사용

        while bigger_child_idx and temp.key < self.__container[bigger_child_idx].key: 
            # 자식노드가 존재하고, 자식노드의 값이 부모 노드의 값보다 커지거나 같아질 때까지 (최대 힙 조건 충족) 반복문 실행.
            self.__container[cur_idx] = self.__container[bigger_child_idx]
            cur_idx = bigger_child_idx
            bigger_child_idx = self.__get_bigger_child_idx(cur_idx)

        self.__container[cur_idx] = temp 
        #자식 노드에 원래 부모 노드 값을 넣어줌.
        
        self.__heapsize -= 1 # 값 제거로 인해 힙 사이즈 줄이기
        return ret # 처음에 루트노드에서 뺀 값 리턴

    def dump(self): #힙에 들어있는 데이터 출력
        if self.is_empty():
            print('힙이 비었습니다.')
        else:
            for i in range(1,self.__heapsize+1):
                print(self.__container[i].key, end=' ')
            print()

    def size(self): #힙의 데이터 사이즈 출력
        return self.__heapsize