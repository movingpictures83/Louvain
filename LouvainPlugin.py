
#import sys
#import numpy
import pandas
import networkx
import community

def resize(v, newsize):
   while (len(v) < newsize):
      v.append([])

class LouvainPlugin:

    def input(self, filename):
        self.mydata = pandas.read_csv(filename, index_col=0)
        self.G = networkx.Graph(self.mydata.values)

    def run(self):
        self.partition = community.best_partition(self.G)
        self.clusters = []
        for key in self.partition.keys():
           cluster = self.partition[key]
           if (cluster >= len(self.clusters)):
              resize(self.clusters, cluster+1)
           self.clusters[cluster].append(self.mydata.keys()[int(key)])

    def output(self, filename):
        outfile = open(filename, 'w')
        for cluster in self.clusters:
           outfile.write("\"\",\"x\"\n")
           for i in range(1, len(cluster)+1):
              outfile.write("\""+str(i)+"\",\""+cluster[i-1]+"\"\n")
        #print self.partition
        #print dir(self.partition)
