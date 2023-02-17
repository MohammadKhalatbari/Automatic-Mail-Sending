import pandas as pd
import csv

class SendAutomaticEmail():
    source_file = 'inputFile.csv'

    def reaad_CSV(self):
        persons = pd.read_csv(self.source_file,index_col='Name')
        print(str(persons))



class main():
    SendAutomaticEmail().reaad_CSV()