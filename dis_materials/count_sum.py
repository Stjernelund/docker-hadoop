from mrjob.job import MRJob

class MRCountSum(MRJob):

    def mapper(self, _, line):
        line = line.strip() # remove leading and trailing whitespace
        if line.find("From:") == 0 and line.find("@") != -1:
            end_index = -1
            email_domain = line[line.find("@")+1:end_index]
            for i,char in enumerate(email_domain):
                if char != '.' or char != '-' or !char.isnumeric() or !char.isalpha():
                    email_domain = email_domain[0:i]
            if len(email_domain) == 0:
                email_domain == "empty"
            yield email_domain, 1

    def combiner(self, key, values):
        yield key, sum(values)
        
    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    MRCountSum.run()
