#the following program was born out of the need to solve a picoCTF challenge
import sys
def main():
    try:
        # print(sys.argv[1])
        if sys.argv[1] == '-s':
            sys.stdout.write('space character detected, which isn"t currectly available')
        elif sys.argv[1] == '':
            sys.stdout.write('use <-h> for help')
        elif sys.argv[1] == '-l':    
            with open('file.txt', 'r') as f:
                car = [chr(int(b.strip())) for b in f.readlines()]

                sys.stdout.write(''.join(car))       
    except:
        return 'papi'
        # sys.stdout.write('no argument passed')
if __name__ =='__main__':
    main()