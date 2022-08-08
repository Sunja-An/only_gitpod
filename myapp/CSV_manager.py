
import csv

# Use Guide
# 1) sample data
# sample data contains train data, test data.
# sample 데이터는 writer 가 admin, datatime 은 00:00:00 으로 고정한다.

# 2) Data define
# 


f = open("sample_data.csv", "a", newline='\n', encoding="UTF-8")
# writer : 작가 , content : 내용 , TF_judge : 부조리 판단, datatime : 시간대
#columns = ["writer", "content", "tf_judge", "datetime"]
#f.write(columns[0] + ',' + columns[1] +',' + columns[2] + ',' + columns[3] + '\n')

class Sample:
    def __init__(self, writer, content, judge, datetime):
        self.writer = writer
        self.content = content
        self.tf_judge = judge
        self.datetime = datetime
    
    def insert(self):
        wr = csv.writer(f)
        line = list()
        line = [self.writer, self.content, self.tf_judge, self.datetime]
        wr.writerow(line)
        pass

    def delete(self):
        # Find the data that wanted delete and delete it.
        pass

    def modify(self):
        # modify the content or tf_judge, but not contain writer and datetime. They're core information.
        pass

    def show_data(self):
        return '%s %s %s %s' % (self.writer, self.content, self.tf_judge, self.datetime)

    def close(self):
        f.close()

    