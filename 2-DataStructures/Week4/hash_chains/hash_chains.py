# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        self._hash_table_ = [[] for _ in range(bucket_count)]

    def _hash_func(self, s):
        ans = 0
        i = 0
        for c in s:
            #ans += (ans * self._multiplier + ord(c)) % self._prime
            ans += (ord(c) * self._multiplier ** i)
            i += 1
        return (ans % self._prime) % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # use reverse order, because we append strings to the end
            # self.write_chain(cur for cur in reversed(self.elems)
            #             if self._hash_func(cur) == query.ind)
            self.write_chain(reversed(self._hash_table_[query.ind]))
        elif query.type == 'find':
            h = self._hash_func(query.s)
            if query.s in self._hash_table_[h]:
                self.write_search_result(True)
            else:
                self.write_search_result(False)
        elif query.type == 'add':
            h = self._hash_func(query.s)
            if query.s not in self._hash_table_[h]:
                self._hash_table_[h].append(query.s)
        else:
            h = self._hash_func(query.s)
            if query.s in self._hash_table_[h]:
                self._hash_table_[h].remove(query.s)
            # elif query.type == 'add':
            #     if ind == -1:
            #         self.elems.append(query.s)
            # else:
            #     if ind != -1:
            #         self.elems.pop(ind)

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    #print('\n')
    proc.process_queries()
