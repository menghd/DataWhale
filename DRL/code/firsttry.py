import gym
env = gym.make('CartPole-v0')
env.reset()
for _ in range (1000):
  env.render()
  action = env.action_space.sample() # 随机采样一个动作
  env.step(action) # 提交动作
env.close() # 直接关闭图形界面可能导致卡死