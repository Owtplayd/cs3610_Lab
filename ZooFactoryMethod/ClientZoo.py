from ZooFactoryMethod.TorontoZooClass import TorontoZoo
from ZooFactoryMethod.CalgaryZooClass import CalgaryZoo

def zooVisit():
    toronto = TorontoZoo()
    print("The Toronto Zoo visit is starting!")
    toronto.startVisit()

    calgary = CalgaryZoo()
    print("\nThe Calgary Zoo visit is starting!")
    calgary.startVisit()

if __name__ == "__main__":
    zooVisit()
