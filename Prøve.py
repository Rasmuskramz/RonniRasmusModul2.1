""" A simple base state for the state machine
"""
class BaseState:
    parent = None
    name = "state"
    isDone = False
    def __init__(self, name):
        self.name = name or self.name

    def enter(self):
        pass
    def update(self):
        pass
    def exit(self):
        pass


""" A simple State Machine
    Note that it is a sub-class of BaseState, this allows
    for nested complex states.

"""
class StateMachine(BaseState):
    def __init__(self, name):
        BaseState.__init__(self, name)
        self.stateDict = {}
        self.reset()

    def update(self):
        """ Update states
            note that it's sometimes beneficial to have an extra
            method on your state objects to allow them to forcibly
            seize control in certain scenarios, this simple model
            doesn't include such things
        """

        # no processing an empty stack often this will be used
        # to exit the menu or application (for example)
        if len(self.stateStack) <= 0:
            # here we're manually exiting the last state (if any)
            # since we are ensuring predictable behaviour by delaying
            # calls to enter() and exit() ie. not exiting a state
            # when it's done, but instead once we're ready for it to be
            self.exitState(self.lastState)
            self.isDone = True
            return

        currentState = self.stateStack[-1]

        if self.lastState != currentState:
            """ We've switched states, notify everyone involved """
            self.switchState( currentState )

        if currentState != None:
            currentState.update()            
            if currentState.isDone:
                self.popState()

    def reset(self):
        """ Reset the state machine, but leave its dictionary intact """
        self.stateStack = []        
        self.lastState = None
        self.isDone = False

    def switchState(self, newState):
        """ Handles exiting and entering states appropriately """
        self.exitState( self.lastState )
        self.enterState( newState )
        self.lastState = newState

    def enterState(self, stateObj):
        """ Helper function to safely enter the specified state object """
        if stateObj != None:
            stateObj.enter()

    def exitState(self, stateObj):
        """ Helper function to safely exit the specified state object """
        if stateObj != None:
            stateObj.exit()

    def addState(self, state):
        """ Add a state to the dictionary for later
            ! Doesn't push or enter !
        """
        state.parent = self
        self.stateDict[state.name] = state

    def pushState(self, stateName):
        """ Push a state onto the stack by name """
        if not self.stateDict.has_key(stateName):
            print ("here you whinge that state:%s doesn't exist.." % stateName)
            return        
        newState = self.stateDict[stateName]
        self.stateStack.append(newState)

        return newState

    def popState(self):
        currentState = self.stateStack.pop()


""" A little example state for demonstration
"""

class TestState(BaseState):
    def __init__(self, name):
        BaseState.__init__(self, name)

    def enter(self):
        print ("entered " + self.name)

    def update(self):
        print ("updated " + self.name)

        # just bail out of this state for testing
        self.isDone = True

    def exit(self):
        print ("exiting " + self.name)


if __name__ == '__main__':
    """ Test out the state machine """

    machine = StateMachine("Master Control Program")

    ## Ultra simple
    machine.addState( TestState("State-A") )
    machine.addState( TestState("State-B") )

    ## set up a simple stack
    machine.pushState("State-A")
    machine.pushState("State-B")

    ## test it out
    print("Running simple state machine...\n")
    while not machine.isDone:
        machine.update()



    ## Nested test
    machine.reset()

    nestedMachine = StateMachine("Nested-A")
    nestedMachine.addState( TestState("Sub-State-A") )
    nestedMachine.addState( TestState("Sub-State-B") )
    nestedMachine.addState( TestState("Sub-State-C") )

    ## Set up a simple nested stack
    nestedMachine.pushState("Sub-State-A");
    nestedMachine.pushState("Sub-State-B");
    nestedMachine.pushState("Sub-State-C");

    machine.addState( nestedMachine )

    ## set up another simple stack
    machine.pushState("State-A")
    machine.pushState("Nested-A")
    machine.pushState("State-B")

    print("Running simple nested state machine...\n")
    while not machine.isDone:
        machine.update()
