class Jug():
    def __init__(self,water:int,maxWater:int):
        self.water=water
        self.maxWater=maxWater

    def __hash__(self):
        return hash((self.water,self.maxWater))

    def __eq__(self, other) -> bool:
        return(
            self.water==other.water and
            self.maxWater==other.maxWater
        )
    
    def __repr__(self) -> str:
        return(f"{self.water} {self.maxWater} ")
    

    
class Node():
    def __init__(self,state:list[Jug],parent:list[Jug]|None=None):
        """Creates a node with present state and parent state"""
        self.state=state
        self.parent=parent

    def __hash__(self) -> int:
        return hash((self.state,self.parent))
    
    def __eq__(self,other)-> bool:
        return(
            self.state == other.state and
            self.parent == other.parent
        )



def next_states(state:tuple[Jug]) -> list[tuple[Jug]]:
    """
    Takes input `state` and returns the list of all possible next states
    """
    j1,j2=state
    x=j1.water
    y=j2.water
    Mx=j1.maxWater
    My=j2.maxWater

    possible=set(
        ((Jug(x,Mx),Jug(0,My)),
        (Jug(0,Mx),Jug(y,My)),
        (Jug(Mx,Mx),Jug(y,My)),
        (Jug(x,Mx),Jug(My,My)))
    )
    
    if x+y>Mx:
        possible.add((Jug(Mx,Mx),Jug(x+y-Mx,My)))
    else:
        possible.add((Jug(x+y,Mx),Jug(0,My)))

    if x+y>My:
        possible.add((Jug(x+y-My,Mx),Jug(My,My)))
    else:
        possible.add((Jug(0,Mx),Jug(x+y,My)))

    possible.remove(state)
    return list(possible)


def path_find(state:tuple[Jug],goal:int) -> list[tuple[Jug]] | None:
    queue:list[Node]=[]
    firstnode=Node(state,None)
    queue.append(firstnode)
    explored=set()

    while True:
        if len(queue)==0:
            return None
        st=queue[0]
        queue=queue[1:]

        for pState in next_states(st.state):
            if pState not in explored and not any(pState== node.state for node in queue):
                child=(Node(pState,st))

                if child.state[0].water==goal or child.state[1].water==goal:
                    path=[]
                    while child.parent is not None:
                        path.append(child.state)
                        child=child.parent
                    path.reverse()
                    return path
                else:
                    queue.append(child)
        explored.add(st.state)


def main():
    mw1=int(input("enter the max water in smaller Jug: "))
    mw2=int(input("enter the max water in larger Jug: "))
    goal=int(input("enter your goal: "))


    jug1=Jug(0,min(mw1,mw2))
    jug2=Jug(0,max(mw1,mw2))
    state=(jug1,jug2)

    path=path_find(state,goal)

    if not path:
        print("NO Way of doing so.")
    else:
        print(f"Jug1(max:{jug1.maxWater})\tJug2(max:{jug2.maxWater})")
        print(f"0\t\t0")
        for st in path:
            print(f"{st[0].water}\t\t{st[1].water}")


if __name__=="__main__":
    main()