import tqdm

from . import DatasetAdapterProgressCallback


class DatasetAdapterTqdmProgressCallback(DatasetAdapterProgressCallback):
    def __init__(self, desc: str = None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.desc = desc
        self.tqdm_bar = None

    @property
    def desc(self) -> str:
        return self._desc

    @desc.setter
    def desc(self, desc: str):
        self._desc = desc or ""

    @property
    def tqdm_bar(self) -> tqdm.tqdm:
        return self._tqdm_bar

    @tqdm_bar.setter
    def tqdm_bar(self, tqdm_bar: tqdm.tqdm):
        self._tqdm_bar = tqdm_bar

    def on_loop_start(self, total_steps: int):
        self.tqdm_bar = tqdm.tqdm(total=total_steps, desc=self.desc)

    def on_loop_end(self):
        self.tqdm_bar.close()
        self.tqdm_bar = None

    def on_step_end(self, current_step: int = None):
        self.tqdm_bar.update(1 if current_step is None else current_step - self.tqdm_bar.n)
