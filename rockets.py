import hashlib


def parsing_request(list_):
    start_ = []
    end_ = []
    for elem in list_:
        start_.append(elem[0])
        end_.append(elem[1])
    start_.sort()
    start_.pop(0)
    end_.sort()
    end_.pop(len(end_) - 1)
    return start_ == end_


if __name__ == '__main__':
    list_request = [[4, 5], [1, 2], [2, 4], [5, 7]]
    print(parsing_request(list_request))