import time
from dataclasses import asdict, dataclass

from ..adapter_callback import BaseDatasetAdapterCallback


@dataclass
class ProgressInfo:
    current_stage: str
    current_step: int
    total_steps: int
    start_time: float
    last_updated_time: float
    remaining_time: float

    def to_dict(self):
        return asdict(self)


class DatasetAdapterProgressCallback(BaseDatasetAdapterCallback):
    _current_stage = None
    _total_steps = None
    _current_step = None
    _last_updated_step = None
    _last_updated_time = None
    _start_time = None
    _started = False

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initialize()

    @property
    def current_stage(self) -> str:
        return DatasetAdapterProgressCallback._current_stage

    @current_stage.setter
    def current_stage(self, current_stage: str):
        DatasetAdapterProgressCallback._current_stage = current_stage

    @property
    def total_steps(self) -> int:
        return DatasetAdapterProgressCallback._total_steps

    @total_steps.setter
    def total_steps(self, total_steps: int):
        DatasetAdapterProgressCallback._total_steps = total_steps

    @property
    def current_step(self) -> int:
        return DatasetAdapterProgressCallback._current_step

    @current_step.setter
    def current_step(self, current_step: int):
        DatasetAdapterProgressCallback._current_step = current_step
        self.last_updated_step = current_step
        self.last_updated_time = time.time()

    @property
    def last_updated_step(self) -> int:
        return DatasetAdapterProgressCallback._last_updated_step

    @last_updated_step.setter
    def last_updated_step(self, last_updated_step: int):
        DatasetAdapterProgressCallback._last_updated_step = last_updated_step

    @property
    def last_updated_time(self) -> float:
        return DatasetAdapterProgressCallback._last_updated_time

    @last_updated_time.setter
    def last_updated_time(self, last_updated_time: float):
        DatasetAdapterProgressCallback._last_updated_time = last_updated_time

    @property
    def start_time(self) -> float:
        return DatasetAdapterProgressCallback._start_time

    @start_time.setter
    def start_time(self, start_time: float):
        DatasetAdapterProgressCallback._start_time = start_time

    @property
    def started(self) -> bool:
        return DatasetAdapterProgressCallback._started

    @started.setter
    def started(self, started: bool):
        DatasetAdapterProgressCallback._started = started

    def get_progress_info(self) -> ProgressInfo:
        return ProgressInfo(
            current_stage=self.current_stage,
            current_step=self.current_step,
            total_steps=self.total_steps,
            start_time=self.start_time,
            last_updated_time=self.last_updated_time,
            remaining_time=self.get_remaining_time(),
        )

    def get_remaining_time(self) -> float:
        if (
            self.start_time is None
            or self.current_step is None
            or self.current_step == 0
            or self.total_steps is None
        ):
            return float("inf")

        elapsed_time = self.last_updated_time - self.start_time
        return elapsed_time * (self.total_steps - self.current_step) / self.current_step

    def initialize(self):
        self.current_stage = None
        self.total_steps = None
        self.current_step = None
        self.last_updated_step = None
        self.last_updated_time = None
        self.start_time = None

        self.started = False

    def on_loop_start(self, total_steps: int):
        self.current_stage = "on_loop_start"
        if self.started:
            if self.total_steps != total_steps:
                raise ValueError("total_steps must be same with previous one")
            return
        self.started = True
        self.total_steps = total_steps
        self.current_step = 0
        self.start_time = time.time()

    def on_loop_end(self):
        self.current_stage = "on_loop_end"
        self.current_step = self.total_steps
        self.started = False

    def on_step_start(self):
        self.current_stage = "on_step_start"
        pass

    def on_step_end(self, current_step: int = None):
        if current_step is None:
            current_step = self.current_step + 1
        self.current_stage = "on_step_end"
        if current_step == self.last_updated_step:
            return
        if current_step > self.total_steps or current_step < self.current_step or current_step < 0:
            raise ValueError("current_step must be between 0 and total_steps")
        self.current_step = current_step
