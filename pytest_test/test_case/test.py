from time import sleep, ctime
import threading


def music(name):
    for i in range(2):
        print("I listen now", name, ctime())
        sleep(3)


def move(name):
    for i in range(2):
        print("I listen now", name, ctime())
        sleep(2)


threds = []
t1 = threading.Thread(target=music, args=("凤凰传奇",))
threds.append(t1)
t2 = threading.Thread(target=move, args=("阿凡达",))
threds.append(t2)

if __name__ == '__main__':
    print("The main process starts", ctime())
    for i in threds:
        i.setDaemon(True)
        i.start()
    i.join()
    print("The main process ends", ctime())
