import threading
from time import sleep, ctime
import logging


# logging.basicConfig(level=logging.INFO)
#
# loops = [2,4]
#
# def loop(nloop,nsec):
#     logging.info("start loop"+str(nloop)+ctime())
#     sleep(nsec)
#     logging.info("end loop"+str(nloop)+ctime())
#
# def main():
#     logging.info("start all at"+ctime())
#     thread = []
#     nloops = range(len(loops))
#     for i in nloops:
#         t = threading.Thread(target=loop,args=(i,loops[i]))
def work():
    print("I am working " + ctime())
    sleep(4)
    print("work over " + ctime())


def study():
    print("I am studying " + ctime())
    sleep(5)
    print("study over" + ctime())


func_list1 = [work, study]
threads = []
for i in range(2):
    t = threading.Thread(target=[work, study])
    threads.append(t)

if __name__ == '__main__':
    # threads = []
    # t1 = threading.Thread(target=work)
    # threads.append(t1)
    # t2 = threading.Thread(target=study)
    # threads.append(t2)
    print("The main process starts " + ctime())
    for i in threads:
        i.start()
        i.join()
    print("The main process ends ", ctime())
