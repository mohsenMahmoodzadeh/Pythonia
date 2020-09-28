# How to use from gym environment

## 1. Create virtual evnironemnt

## 2. Install prerequisities
1. numpy
2. tensorflow
3. Keras
4. keras-rl
5. gym

## 3. Design your RL model
I've used a simple DQN model on 'Mountain-Car v0' environment but you can create more better models and try to the mentioned environment.

## 4. Improve the reward
from your virtual environment directory, Enter to this path:
"ENV_NAME/Lib/site-packages/gym/envs/classic_control". open 'mountain_car.py' file an then in 'step' method in the class, change the definition of the 'reward' with respect to 'position' and 'velocity' attributes. 




