import gymnasium as gym
import os
import gymnasium as gym

from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.vec_env import DummyVecEnv

environment_name = "CartPole-v0"

env = gym.make("CartPole-v1", render_mode="human")

env = DummyVecEnv([lambda: env]) 

PPO_path = os.path.join("training", "saved_models", "PPO_model_Cartpole")
model = PPO.load(PPO_path, env =env)

evaluate_policy(model, env, n_eval_episodes=10, render=True)
