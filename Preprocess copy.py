import gym_super_mario_bros as GSM
from nes_py.wrappers import JoypadSpace
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
#Import frame stacker wrapper adn grayscaling Wrapper # grayscale es para convertirlo en gray
from gym.wrappers import GrayScaleObservation #Framestack es:Ai va a poder ver 4 frameshttps://youtu.be/dWmJ5CXSKdw?t=1508
#import vectorization wrappers  es paralelizar, literalmente hace eso dummyvec
from stable_baselines3.common.vec_env import VecFrameStack,DummyVecEnv #Darle varios layers a la imagen https://youtu.be/dWmJ5CXSKdw?t=1589
#Improt matplotlib
from matplotlib import pyplot as plt

#PREPORCESS
print(SIMPLE_MOVEMENT)
#SetupGame
env=GSM.make("SuperMarioBros-v0")  
env=JoypadSpace(env,SIMPLE_MOVEMENT) 
#GrayScale
env=GrayScaleObservation(env,keep_dim=True)
#Corremos varios marios/vectorizamos el entorno
env=DummyVecEnv([lambda:env])

#StackTheFrames que vaya obteniendo la info de a 4 frames asi sabemos para que lado van los enemigos, cuanto avanza mario etc
#https://www.youtube.com/watch?v=dWmJ5CXSKdw&t=2390s
env=VecFrameStack(env,4,channels_order="last")


done=True 

for step in range(100000): #Smth changes in your screen, you press a key. 100000 frames 
    if done:
        env.reset() 
    state,reward,done,info=env.step(env.action_space.sample())

    env.render()
env.close()
