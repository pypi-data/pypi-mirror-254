import argparse
from enum import Enum

import torch

from rl.algorithm.dqn import DQNImpl
from rl.algorithm.ppo import PPOImpl
from rl.algorithm.rainbow import RainbowImpl


class Algorithm(Enum):
    DQN = DQNImpl
    PPO = PPOImpl
    RAINBOW = RainbowImpl


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='LevDoom runner')

    # Core
    parser.add_argument('--scenario_name', type=str, default=None, required=True,
                        choices=['defend_the_center', 'health_gathering', 'seek_and_slay', 'dodge_projectiles'])
    parser.add_argument('--algorithm', type=str, default=None, required=True, choices=['dqn', 'ppo', 'rainbow'])
    parser.add_argument('--seed', type=int, default=0)
    parser.add_argument('--logdir', type=str, default='log')
    parser.add_argument('--watch', default=False, action='store_true', help='watch the play of pre-trained policy')
    parser.add_argument('--resume-path', type=str, default=None)
    parser.add_argument('--save_interval', type=int, default=20)
    parser.add_argument("--hard_rewards", default=False, action='store_true')

    # DOOM
    parser.add_argument('--render', default=False, action='store_true')
    parser.add_argument('--render_sleep', type=float, default=0.02)
    parser.add_argument('--variable_queue_len', type=int, default=5)
    parser.add_argument('--normalize', type=bool, default=True)
    parser.add_argument('--frame-height', type=int, default=84)
    parser.add_argument('--frame-width', type=int, default=84)
    parser.add_argument('--frame-stack', type=int, default=4)
    parser.add_argument('--frame-skip', type=int, default=4)
    parser.add_argument('--resolution', type=str, default=None, choices=['800X600', '640X480', '320X240', '160X120'])

    # Training
    parser.add_argument('--train_levels', type=int, nargs='*', default=[0, 1], choices=[0, 1, 2, 3, 4])
    parser.add_argument('--device', type=str, default='cuda' if torch.cuda.is_available() else 'cpu')
    parser.add_argument('--envs', type=str, nargs='*', default=['default'])
    parser.add_argument('--epoch', type=int, default=300)
    parser.add_argument('--step-per-epoch', type=int, default=1e5)
    parser.add_argument('--step-per-collect', type=int, default=1000)
    parser.add_argument('--repeat-per-collect', type=int, default=4)
    parser.add_argument('--update-per-step', type=float, default=0.1)
    parser.add_argument('--batch-size', type=int, default=256)
    parser.add_argument('--hidden-size', type=int, default=512)
    parser.add_argument('--training-num', type=int, default=10)
    parser.add_argument('--buffer-size', type=int, default=1e5)
    parser.add_argument('--save-buffer-name', type=str, default=None)

    # Testing
    parser.add_argument('--test_levels', type=int, nargs='*', default=[2, 3, 4], choices=[0, 1, 2, 3, 4])
    parser.add_argument('--test_envs', type=str, nargs='*', default=['default'])
    parser.add_argument('--eps-test', type=float, default=0.005)
    parser.add_argument('--test-num', type=int, default=100)

    # RL
    parser.add_argument('--lr', type=float, default=2e-5)
    parser.add_argument('--lr-decay', type=int, default=True)
    parser.add_argument('--alpha', type=float, default=0.6)
    parser.add_argument('--beta', type=float, default=0.4)
    parser.add_argument('--gamma', type=float, default=0.99)
    parser.add_argument('--target-update-freq', type=int, default=500)
    parser.add_argument('--eps-train', type=float, default=1.)
    parser.add_argument('--eps-train-final', type=float, default=0.05)

    # Rainbow
    parser.add_argument('--num-atoms', type=int, default=51)
    parser.add_argument('--v-min', type=float, default=-10.)
    parser.add_argument('--v-max', type=float, default=10.)
    parser.add_argument('--n-step', type=int, default=3)

    # PPO
    parser.add_argument('--vf-coef', type=float, default=0.5)
    parser.add_argument('--ent-coef', type=float, default=0.01)
    parser.add_argument('--gae-lambda', type=float, default=0.95)
    parser.add_argument('--eps-clip', type=float, default=0.2)
    parser.add_argument('--dual-clip', type=float, default=None)
    parser.add_argument('--value-clip', type=int, default=0)
    parser.add_argument('--rew-norm', type=int, default=False)
    parser.add_argument('--max-grad-norm', type=float, default=0.5)
    parser.add_argument('--norm-adv', type=int, default=1)
    parser.add_argument('--recompute-adv', type=int, default=0)

    # WandB
    parser.add_argument('--with_wandb', default=False, action='store_true', help='Enables Weights and Biases')
    parser.add_argument('--wandb_user', default=None, type=str, help='WandB username (entity).')
    parser.add_argument('--wandb_project', default='LevDoom', type=str, help='WandB "Project"')
    parser.add_argument('--wandb_group', default=None, type=str, help='WandB "Group". Name of the env by default.')
    parser.add_argument('--wandb_job_type', default='default', type=str, help='WandB job type')
    parser.add_argument('--wandb_tags', default=[], type=str, nargs='*', help='Tags can help finding experiments')
    parser.add_argument('--wandb_key', default=None, type=str, help='API key for authorizing WandB')
    parser.add_argument('--wandb_dir', default=None, type=str, help='the place to save WandB files')

    # Scenario specific
    parser.add_argument('--reward_kill', default=1.0, type=float, help='For eliminating an enemy')
    parser.add_argument('--reward_health_kit', default=1.0, type=float, help='For picking up health kits')
    parser.add_argument('--penalty_health_loss', default=0.1, type=float, help='Negative reward for losing health')
    parser.add_argument('--penalty_ammo_used', default=0.1, type=float, help='Negative reward for using ammo')
    parser.add_argument('--traversal_reward_scaler', default=1e-3, type=float,
                        help='Reward scaler for traversing the map')
    return parser.parse_args()
