import json
import os
from pathlib import Path

from plover.machine.base import STATE_RUNNING
from plover.oslayer.config import CONFIG_DIR
from plover.registry import registry

_CONFIG_FILEPATH = Path(CONFIG_DIR) / "practice_plugin.json"

class PracticePlugin:
    def __init__(self, engine):
        self._engine = engine
        self._env_vars = {}

    def start(self):
        registry.register_plugin("meta", "get_env_var", self._get_env_var)
        self._engine.hook_connect(
            "machine_state_changed",
            self._machine_state_changed
        )
        self._env_vars = self._load_config()

    def stop(self):
        self._engine.hook_disconnect(
            "machine_state_changed",
            self._machine_state_changed
        )

    def _get_env_var(self, ctx, argument):
        try:
            env_var_value = self._env_vars[argument]
        except KeyError:
            env_var_value = self._expand(argument)
            self._env_vars[argument] = env_var_value
            self._save_config()

        action = ctx.new_action()
        action.text = env_var_value
        return action

    def _expand(self, argument):
        shell = os.getenv("SHELL", "bash").split("/")[-1]
        return os.popen(f"{shell} -ic 'echo {argument}'").read().strip()

    def _save_config(self):
        with _CONFIG_FILEPATH.open("w", encoding="utf-8") as file:
            data = {"env_var_names": sorted(self._env_vars.keys())}
            json.dump(data, file, indent=2)
            file.close()

    def _load_config(self):
        try:
            with _CONFIG_FILEPATH.open(encoding="utf-8") as file:
                data = json.load(file)
                file.close()
        except FileNotFoundError:
            data = {}

        env_var_names = data.get("env_var_names", [])
        env_var_values = self._expand(",".join(env_var_names))
        env_vars = dict(zip(env_var_names, env_var_values.split(",")))

        return env_vars

    def _machine_state_changed(self, _machine_type, machine_state):
        if machine_state == STATE_RUNNING:
            self._env_vars = self._load_config()
