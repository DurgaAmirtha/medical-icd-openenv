from tasks import TASKS
from grader import Grader

class OpenEnv:
    def __init__(self, task_id=None):
        self.tasks = {t["id"]: t for t in TASKS}
        self.current_task = None
        self.steps_taken = 0
        self.grader = Grader()

        if task_id:
            self.set_task(task_id)

    def set_task(self, task_id):
        if task_id not in self.tasks:
            raise ValueError(f"Task {task_id} not found")

        self.current_task = self.tasks[task_id]
        self.reset()

    def reset(self):
        self.steps_taken = 0
        self.grader.reset()

        if not self.current_task:
            return "No task selected. Use set_task(id)."

        return {
            "description": self.current_task["description"],
            "steps": self.steps_taken
        }

    def step(self, action):
        if not self.current_task:
            raise Exception("No task active")

        self.steps_taken += 1
        target = self.current_task["target_code"]

        # Base reward from grader
        reward = self.grader.grade(action, target)

        # 🔥 Reward shaping + multi-step logic
        if action == target:
            if self.steps_taken == 1:
                reward = 0.5      # early correct → partial reward
                done = False      # force at least 2 steps
            else:
                reward = 1.0      # full reward
                done = True
        elif action and action[0] == target[0]:
            reward = max(reward, 0.3)
            done = False
        else:
            reward = max(reward, 0.1)
            done = False

        # 🔥 Force minimum 2 steps
        if self.steps_taken < 2:
            done = False

        # Stop if max steps reached
        if self.steps_taken >= self.current_task.get("max_steps", 3):
            done = True

        observation = {
            "description": self.current_task["description"],
            "steps": self.steps_taken
        }

        info = {
            "steps": self.steps_taken,
            "target": target
        }

        return observation, reward, done, info

    def state(self):
        return {
            "task_id": self.current_task["id"] if self.current_task else None,
            "steps": self.steps_taken
        }

def make(task_id=None):
    return OpenEnv(task_id)