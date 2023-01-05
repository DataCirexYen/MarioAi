import gym_super_mario_bros as GSM
from nes_py.wrappers import JoypadSpace
from gym_super_mario_bros.actions import SIMPLE_MOVEMENT
from gym.wrappers import GrayScaleObservation
from stable_baselines3.common.vec_env import VecFrameStack,DummyVecEnv
from matplotlib import pyplot as plt
print(SIMPLE_MOVEMENT)
env=GSM.make("SuperMarioBros-v0")  
env=JoypadSpace(env,SIMPLE_MOVEMENT) 
env=GrayScaleObservation(env,keep_dim=True)

env=DummyVecEnv([lambda:env])


env=VecFrameStack(env,4,channels_order="last")


done=True 

for step in range(100000):
    if done:
        env.reset() 
    state,reward,done,info=env.step(env.action_space.sample())

    env.render()
env.close()
