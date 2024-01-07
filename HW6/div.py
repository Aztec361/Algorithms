class CountInversion:
    def __init(self, List):
        self.listInput = List

    def mergeCount(self, l1, l2):
        mergeList = []
        idx1 = 0
        idx2 = 0
        count = 0

        while idx1 < len(l1) and idx2 < len(l2):
            if l1[idx1] <= l2[idx2]:
                mergeList.append(l1[idx1])
                idx1 += 1
            else:
                mergeList.append(l2[idx2])
                count += len(l1) - idx1
                idx2 += 1

        mergeList.extend(l1[idx1:])
        mergeList.extend(l2[idx2:])

        return mergeList, count

    def countSort(self, L):
        if len(L) <= 1:
            return L, 0
        mid = len(L) // 2
        l1, c1 = self.countSort(L[:mid])
        l2, c2 = self.countSort(L[mid:])
        sortedList, c = self.mergeCount(l1, l2)
        return sortedList, c1 + c2 + c

    def getCount(self):
        _, count = self.countSort(self.listInput)
        return count


def main():
    numInstances = int(input())
    countList = []
    for _ in range(numInstances):
        numNode = int(input())
        listInput1 = [int(input()) for _ in range(numNode)]
        count = CountInversion(listInput1).getCount()
        countList.append(count)

    for count in countList:
        print(count)


if __name__ == "__main__":
    main()
