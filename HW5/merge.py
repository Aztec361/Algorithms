class CountInversion:
    def __init__(self, strInput):
        self.listInput = [float(i) for i in strInput.strip().split(" ")]

    def mergeCount(self, l1, l2):
        mergeList = []
        idx1 = 0
        idx2 = 0
        count = 0
        while idx1 < len(l1) or idx2 < len(l2):
            if idx1 == len(l1):
                mergeList.append(l2[idx2])
                idx2 += 1
            elif idx2 == len(l2) or l1[idx1] <= l2[idx2]:
                mergeList.append(l1[idx1])
                idx1 += 1
            else:
                mergeList.append(l2[idx2])
                count += len(l1) - idx1
                idx2 += 1
        return mergeList, count

    def countSort(self, L):
        if len(L) <= 1:
            return L, 0
        mid = len(L) // 2
        l1, c1 = self.countSort(L[:mid])
        l2, c2 = self.countSort(L[mid:])
        sortL, c = self.mergeCount(l1, l2)
        return sortL, c1 + c2 + c

    def getCount(self):
        _, count = self.countSort(self.listInput)
        return count

def main():
    numInstance = int(input())
    insList = []
    for _ in range(numInstance):
        _ = int(input())
        insList.append(CountInversion(input()))
    for instance in insList:
        print(instance.getCount())

main()
