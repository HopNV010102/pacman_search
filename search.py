
import util

class SearchProblem:
  
    def getStartState(self):
      
        util.raiseNotDefined()

    def isGoalState(self, state):
        
        util.raiseNotDefined()

    def getSuccessors(self, state):
      
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
       
        util.raiseNotDefined()



def depthFirstSearch(problem):
    startingNode = problem.getStartState()
    if problem.isGoalState(startingNode):
        return []

    myQueue = util.Stack()
    visitedNodes = []
    # (node,actions)
    myQueue.push((startingNode, []))

    while not myQueue.isEmpty():
        currentNode, actions = myQueue.pop()
        if currentNode not in visitedNodes:
            visitedNodes.append(currentNode)

            if problem.isGoalState(currentNode):
                return actions

            for nextNode, action, cost in problem.getSuccessors(currentNode):
                newAction = actions + [action]
                myQueue.push((nextNode, newAction))


dfs = depthFirstSearch