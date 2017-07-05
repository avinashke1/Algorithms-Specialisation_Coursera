def greedy(jobs, greedy_criterion, ties_criterion):

    jobs.sort(key = ties_criterion)
    jobs.sort(key = greedy_criterion)
    
    timeline = 0
    sum = 0
    for w, l in jobs:
        timeline += l
        sum += w * timeline
        
    return sum
    
    
def main():
    
    f = open('jobs.txt')
    
    n = int(f.readline())
    
    jobs = []
    for line in f:
        w, l = [int(x) for x in line.split()]
        jobs.append((w, l))
        
    greedysummation = lambda (w, l): -(w - l)       
    ties = lambda (w, l): -w               
    
    print 'Answer: %i' % greedy(jobs, greedysummation, ties)     

if __name__ == '__main__':
  
  main()

