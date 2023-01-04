import gym_super_mario_bros as GSM

from nes_py.wrappers import JoypadSpace

from gym_super_mario_bros.actions import SIMPLE_MOVEMENT

print(SIMPLE_MOVEMENT)
#SetupGame
env=GSM.make("SuperMarioBros-v0")  #Corre mario con las 256 conmbinacioens
env=JoypadSpace(env,SIMPLE_MOVEMENT) #Corre mario con movimiento simple, 7 combos
#print(env.action_space) any doubt print this btw
#print(env.observation_space.shape) Como se ve una screen del game


#Create a flag -- restart or not
done=True 

for step in range(100000): #Smth changes in your screen, you press a key. 100000 frames 
    if done:
        #start the game
        env.reset() 
    #Do random action
    state,reward,done,info=env.step(env.action_space.sample())#Step, metodo para hacer la accion. "env.action_space.sample()" accion rand
    #print(done) # Done se vuelve true cuando no hay ninguna accion imo
    #state.shape#Frame from the game 240 x 256 pxls 3 colores
    #env.step(1)[0] This is reward
    #Show the game
    env.render()
env.close()