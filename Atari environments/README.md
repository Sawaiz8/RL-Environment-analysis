# Atari Environment analysis
## Breakout
### What did I not understand?
#### How does stacking work and is the model trained?
Stacking multiple environment and training them simaltaneously is interesting but doesn't algorithms gets confused on how to update it's parameters. It's is like training the same neural network simaltaneously
VecFrame
Frame stack for CNN policy

### What did I learn new?
According to the other RL course video I saw, we have to stack frames and send it to CNN in games where we have motion. Because models do not have a sense of motion.

Some environment as easier to learn because of their reward function. Sparse reward functions give reward sparsely and dense reward functions give more proactively on every action. so I have to choose what kind of reward function I have.