import math
import types
import copy

import mindspore as ms
from mindspore.experimental.optim.lr_scheduler import StepLR as StepLR_MS
from mindspore.experimental.optim.lr_scheduler import MultiStepLR as MultiStepLR_MS
from mindspore.experimental.optim.lr_scheduler import ConstantLR as ConstantLR_MS
from mindspore.experimental.optim.lr_scheduler import LinearLR as LinearLR_MS
from mindspore.experimental.optim.lr_scheduler import ExponentialLR as ExponentialLR_MS
from mindspore.experimental.optim.lr_scheduler import PolynomialLR as PolynomialLR_MS
from mindspore.experimental.optim.lr_scheduler import CosineAnnealingLR as CosineAnnealingLR_MS
from mindspore.experimental.optim.lr_scheduler import MultiplicativeLR as MultiplicativeLR_MS
from mindspore.experimental.optim.lr_scheduler import LambdaLR as LambdaLR_MS
from mindspore.experimental.optim.lr_scheduler import SequentialLR as SequentialLR_MS
from mindspore.experimental.optim.lr_scheduler import ChainedScheduler as ChainedScheduler_MS
from mindspore.experimental.optim.lr_scheduler import ReduceLROnPlateau as ReduceLROnPlateau_MS
from mindspore.experimental.optim.lr_scheduler import CyclicLR as CyclicLR_MS
# from mindspore.experimental.optim.lr_scheduler import OneCycleLR as OneCycleLR_MS # not support yet
from mindspore.experimental.optim.lr_scheduler import CosineAnnealingWarmRestarts as CosineAnnealingWarmRestarts_MS

from mindtorch.torch.optim.optimizer import Optimizer
from mindtorch.torch.logging import warning
from mindtorch.utils import graph_mode_condition


__all__ = ['LambdaLR', 'MultiplicativeLR', 'StepLR', 'MultiStepLR', 'ConstantLR', 'LinearLR',
           'ExponentialLR', 'SequentialLR', 'CosineAnnealingLR', 'ChainedScheduler', 'ReduceLROnPlateau',
           'CyclicLR', 'CosineAnnealingWarmRestarts', 'PolynomialLR', 'LRScheduler']

EPOCH_DEPRECATION_WARNING = (
    "The epoch parameter in `scheduler.step()` was not necessary and is being " \
    "deprecated where possible. Please use `scheduler.step()` to step the " \
    "scheduler. During the deprecation, if epoch is different from None, the " \
    "closed form is used instead of the new chainable form, where available. "
)

class _LRScheduler_Common:
    def _process_state_dict(self, state_d):
        if 'base_lrs' in state_d:
            for i, base_lr in enumerate(state_d['base_lrs']):
                if isinstance(base_lr, ms.Tensor):
                    state_d['base_lrs'][i] = base_lr.asnumpy().tolist()
        if '_last_lr' in state_d:
            for i, base_lr in enumerate(state_d['_last_lr']):
                if isinstance(base_lr, ms.Tensor):
                    state_d['_last_lr'][i] = base_lr.asnumpy().tolist()
        return state_d

    def _process_state_dict_revert(self, state_d):
        if 'base_lrs' in state_d:
            if len(state_d['base_lrs']) != len(self.base_lrs):
                raise ValueError("In {} load_state_dict(), len of state_dict['base_lrs'] is not the same as `base_lrs`"
                                 .format(self.__class__.__name__))
            for i, base_lr in enumerate(self.base_lrs):
                _lr = self.base_lrs[i]
                if isinstance(_lr, ms.Tensor):
                    _lr.assign_value(ms.Tensor(base_lr).astype(_lr.dtype))
            state_d.pop('base_lrs')

        if '_last_lr' in state_d:
            if len(state_d['_last_lr']) != len(self._last_lr):
                raise ValueError("In {} load_state_dict(), len of state_dict['_last_lr'] is not the same as `_last_lr`"
                                 .format(self.__class__.__name__))
            for i, base_lr in enumerate(state_d['_last_lr']):
                _lr = self._last_lr
                if isinstance(_lr, ms.Parameter):
                    _lr.set_data(ms.Tensor(base_lr).astype(_lr.dtype))
            state_d.pop('_last_lr')
        return state_d

    def state_dict(self):
        ret = {key: value for key, value in self.__dict__.items() if key != 'optimizer'}
        ret = copy.deepcopy(ret)
        ret = self._process_state_dict(ret)
        return ret

    def load_state_dict(self, state_dict):
        state_dict = self._process_state_dict_revert(state_dict)
        self.__dict__.update(state_dict)

class LambdaLR(LambdaLR_MS, _LRScheduler_Common):
    def state_dict(self):
        state_dict = {key: value for key, value in self.__dict__.items() if key not in ('optimizer', 'lr_lambdas')}
        state_dict = copy.deepcopy(state_dict)
        state_dict['lr_lambdas'] = [None] * len(self.lr_lambdas)

        for idx, fn in enumerate(self.lr_lambdas):
            if not isinstance(fn, types.FunctionType):
                state_dict['lr_lambdas'][idx] = fn.__dict__.copy()

        state_dict = self._process_state_dict(state_dict)
        return state_dict

    def load_state_dict(self, state_dict):
        lr_lambdas = state_dict.pop('lr_lambdas')
        state_dict = self._process_state_dict_revert(state_dict)
        self.__dict__.update(state_dict)
        state_dict['lr_lambdas'] = lr_lambdas

        for idx, fn in enumerate(lr_lambdas):
            if fn is not None:
                self.lr_lambdas[idx].__dict__.update(fn)


class MultiplicativeLR(MultiplicativeLR_MS, _LRScheduler_Common):
    def state_dict(self):
        state_dict = {key: value for key, value in self.__dict__.items() if key not in ('optimizer', 'lr_lambdas')}
        state_dict = copy.deepcopy(state_dict)
        state_dict['lr_lambdas'] = [None] * len(self.lr_lambdas)

        for idx, fn in enumerate(self.lr_lambdas):
            if not isinstance(fn, types.FunctionType):
                state_dict['lr_lambdas'][idx] = fn.__dict__.copy()

        state_dict = self._process_state_dict(state_dict)
        return state_dict

    def load_state_dict(self, state_dict):
        lr_lambdas = state_dict.pop('lr_lambdas')
        state_dict = self._process_state_dict_revert(state_dict)
        self.__dict__.update(state_dict)
        state_dict['lr_lambdas'] = lr_lambdas

        for idx, fn in enumerate(lr_lambdas):
            if fn is not None:
                self.lr_lambdas[idx].__dict__.update(fn)


class StepLR(StepLR_MS, _LRScheduler_Common):
    pass


class MultiStepLR(MultiStepLR_MS, _LRScheduler_Common):
    pass


class ConstantLR(ConstantLR_MS, _LRScheduler_Common):
    pass


class LinearLR(LinearLR_MS, _LRScheduler_Common):
    pass


class ExponentialLR(ExponentialLR_MS, _LRScheduler_Common):
    pass


class PolynomialLR(PolynomialLR_MS, _LRScheduler_Common):
    pass


class CosineAnnealingLR(CosineAnnealingLR_MS, _LRScheduler_Common):
    pass


class ChainedScheduler(ChainedScheduler_MS, _LRScheduler_Common):
    def state_dict(self):
        state_dict = {key: value for key, value in self.__dict__.items() if key not in ('optimizer', '_schedulers')}
        state_dict = copy.deepcopy(state_dict)
        state_dict['_schedulers'] = [None] * len(self._schedulers)
        state_dict = self._process_state_dict(state_dict)

        for idx, s in enumerate(self._schedulers):
            state_dict['_schedulers'][idx] = s.state_dict()

        return state_dict

    def load_state_dict(self, state_dict):
        _schedulers = state_dict.pop('_schedulers')
        state_dict = self._process_state_dict_revert(state_dict)
        self.__dict__.update(state_dict)
        state_dict['_schedulers'] = _schedulers

        for idx, s in enumerate(_schedulers):
            self._schedulers[idx].load_state_dict(s)


class SequentialLR(SequentialLR_MS, _LRScheduler_Common):
    def state_dict(self):
        state_dict = {key: value for key, value in self.__dict__.items() if key not in ('optimizer', '_schedulers')}
        state_dict = copy.deepcopy(state_dict)
        state_dict['_schedulers'] = [None] * len(self._schedulers)

        for idx, s in enumerate(self._schedulers):
            state_dict['_schedulers'][idx] = self._process_state_dict(s.state_dict())

        return state_dict

    def load_state_dict(self, state_dict):
        _schedulers = state_dict.pop('_schedulers')
        self.__dict__.update(state_dict)
        state_dict['_schedulers'] = _schedulers

        for idx, s in enumerate(_schedulers):
            self._schedulers[idx].load_state_dict(s)


class ReduceLROnPlateau(ReduceLROnPlateau_MS, _LRScheduler_Common):
    def state_dict(self):
        state_d = {key: value for key, value in self.__dict__.items() if key != 'optimizer'}
        state_d = copy.deepcopy(state_d)
        if '_last_lr' in state_d:
            for i, base_lr in enumerate(state_d['_last_lr']):
                if isinstance(base_lr, ms.Tensor):
                    state_d['_last_lr'][i] = base_lr.asnumpy().tolist()
        return state_d

    def load_state_dict(self, state_dict):
        self.__dict__.update(state_dict)


class CyclicLR(CyclicLR_MS, _LRScheduler_Common):
    def state_dict(self):
        state = super().state_dict()
        state.pop("_scale_fn_ref")
        state = self._process_state_dict(state)
        return state

    def load_state_dict(self, state_dict):
        state_dict = self._process_state_dict_revert(state_dict)
        super().load_state_dict(state_dict)
        self._init_scale_fn()


class CosineAnnealingWarmRestarts(CosineAnnealingWarmRestarts_MS, _LRScheduler_Common):
    pass


class LRScheduler(_LRScheduler_Common):
    def __init__(self, optimizer, last_epoch=-1, verbose=False):
        if not isinstance(optimizer, Optimizer):
            raise TypeError('{} is not an Optimizer'.format(
                type(optimizer).__name__))
        self.optimizer = optimizer

        if last_epoch == -1:
            for group in optimizer.param_groups:
                if isinstance(group['lr'], ms.Parameter):
                    group.setdefault('initial_lr', group['lr'].value()) # Tensor
                else:
                    group.setdefault('initial_lr', group['lr'])
        else:
            for i, group in enumerate(optimizer.param_groups):
                if 'initial_lr' not in group:
                    raise KeyError("param 'initial_lr' is not specified "
                                   "in param_groups[{}] when resuming an optimizer".format(i))
        self.base_lrs = [group['initial_lr'] for group in optimizer.param_groups]
        self.last_epoch = last_epoch

        self.verbose = verbose

        self._initial_step()

    def _initial_step(self):
        self._step_count = 0
        self.step()

    def get_last_lr(self):
        for i, lr in enumerate(self._last_lr):
            if isinstance(lr, ms.Tensor):
                self._last_lr[i] = lr.asnumpy().tolist()
        return self._last_lr

    def get_lr(self):
        raise NotImplementedError

    def print_lr(self, is_verbose, group, lr, epoch=None):
        if isinstance(lr, ms.Tensor):
            lr = lr.asnumpy().tolist()

        if is_verbose:
            if epoch is None:
                print('Adjusting learning rate'
                      ' of group {} to {:.4e}.'.format(group, lr))
            else:
                epoch_str = ("%.2f" if isinstance(epoch, float) else
                             "%.5d") % epoch
                print('Epoch {}: adjusting learning rate'
                      ' of group {} to {:.4e}.'.format(epoch_str, group, lr))

    def step(self, epoch=None):
        self._step_count += 1

        if epoch is None:
            self.last_epoch += 1
            values = self.get_lr()
        else:
            warning(EPOCH_DEPRECATION_WARNING)
            self.last_epoch = epoch
            if hasattr(self, "_get_closed_form_lr"):
                values = self._get_closed_form_lr()
            else:
                values = self.get_lr()

        for i, data in enumerate(zip(self.optimizer.param_groups, values)):
            param_group, lr = data
            if isinstance(param_group['lr'], ms.Parameter):
                if not isinstance(lr, ms.Tensor):
                    lr = ms.ops.scalar_to_tensor(lr)
                lr = ms.ops.depend(lr, ms.ops.assign(param_group['lr'], lr))
            else:
                param_group['lr'] = lr
            self.print_lr(self.verbose, i, lr, epoch)

        self._last_lr = [group['lr'] for group in self.optimizer.param_groups]


class _LRScheduler(LRScheduler):
    pass

class OneCycleLR(LRScheduler):
    def __init__(self,
                 optimizer,
                 max_lr,
                 total_steps=None,
                 epochs=None,
                 steps_per_epoch=None,
                 pct_start=0.3,
                 anneal_strategy='cos',
                 cycle_momentum=True,
                 base_momentum=0.85,
                 max_momentum=0.95,
                 div_factor=25.,
                 final_div_factor=1e4,
                 three_phase=False,
                 last_epoch=-1,
                 verbose=False):

        if not isinstance(optimizer, Optimizer):
            raise TypeError('{} is not an Optimizer'.format(type(optimizer).__name__))
        self.optimizer = optimizer

        if total_steps is None and epochs is None and steps_per_epoch is None:
            raise ValueError("You must define either total_steps OR (epochs AND steps_per_epoch)")
        elif total_steps is not None:
            if total_steps <= 0 or not isinstance(total_steps, int):
                raise ValueError("Expected positive integer total_steps, but got {}".format(total_steps))
            self.total_steps = total_steps
        else:
            if epochs <= 0 or not isinstance(epochs, int):
                raise ValueError("Expected positive integer epochs, but got {}".format(epochs))
            if steps_per_epoch <= 0 or not isinstance(steps_per_epoch, int):
                raise ValueError("Expected positive integer steps_per_epoch, but got {}".format(steps_per_epoch))
            self.total_steps = epochs * steps_per_epoch

        if three_phase:
            self._schedule_phases = [
                {
                    'end_step': float(pct_start * self.total_steps) - 1,
                    'start_lr': 'initial_lr',
                    'end_lr': 'max_lr',
                    'start_momentum': 'max_momentum',
                    'end_momentum': 'base_momentum',
                },
                {
                    'end_step': float(2 * pct_start * self.total_steps) - 2,
                    'start_lr': 'max_lr',
                    'end_lr': 'initial_lr',
                    'start_momentum': 'base_momentum',
                    'end_momentum': 'max_momentum',
                },
                {
                    'end_step': self.total_steps - 1,
                    'start_lr': 'initial_lr',
                    'end_lr': 'min_lr',
                    'start_momentum': 'max_momentum',
                    'end_momentum': 'max_momentum',
                },
            ]
        else:
            self._schedule_phases = [
                {
                    'end_step': float(pct_start * self.total_steps) - 1,
                    'start_lr': 'initial_lr',
                    'end_lr': 'max_lr',
                    'start_momentum': 'max_momentum',
                    'end_momentum': 'base_momentum',
                },
                {
                    'end_step': self.total_steps - 1,
                    'start_lr': 'max_lr',
                    'end_lr': 'min_lr',
                    'start_momentum': 'base_momentum',
                    'end_momentum': 'max_momentum',
                },
            ]

        if pct_start < 0 or pct_start > 1 or not isinstance(pct_start, float):
            raise ValueError("Expected float between 0 and 1 pct_start, but got {}".format(pct_start))
        if anneal_strategy not in ['cos', 'linear']:
            raise ValueError("anneal_strategy must by one of 'cos' or 'linear', instead got {}".format(anneal_strategy))
        elif anneal_strategy == 'cos':
            self.anneal_func = self._annealing_cos
        elif anneal_strategy == 'linear':
            self.anneal_func = self._annealing_linear

        max_lrs = self._format_param('max_lr', self.optimizer, max_lr)
        if last_epoch == -1:
            for idx, group in enumerate(self.optimizer.param_groups):
                group['initial_lr'] = max_lrs[idx] / div_factor
                group['max_lr'] = max_lrs[idx]
                group['min_lr'] = group['initial_lr'] / final_div_factor

        self.cycle_momentum = cycle_momentum
        if self.cycle_momentum:
            if graph_mode_condition():
                raise RuntimeError('not support change momentum or betas under graph-mode')
            if 'momentum' not in self.optimizer.defaults and 'betas' not in self.optimizer.defaults:
                raise ValueError('optimizer must support momentum with `cycle_momentum` option enabled')
            self.use_beta1 = 'betas' in self.optimizer.defaults
            max_momentums = self._format_param('max_momentum', optimizer, max_momentum)
            base_momentums = self._format_param('base_momentum', optimizer, base_momentum)
            if last_epoch == -1:
                for m_momentum, b_momentum, group in zip(max_momentums, base_momentums, optimizer.param_groups):
                    if self.use_beta1:
                        group['betas'] = (m_momentum, *group['betas'][1:])
                    else:
                        group['momentum'] = m_momentum
                    group['max_momentum'] = m_momentum
                    group['base_momentum'] = b_momentum

        super().__init__(optimizer, last_epoch, verbose)

    def _format_param(self, name, optimizer, param):
        if isinstance(param, (list, tuple)):
            if len(param) != len(optimizer.param_groups):
                raise ValueError("expected {} values for {}, got {}".format(
                    len(optimizer.param_groups), name, len(param)))
            return param
        else:
            return [param] * len(optimizer.param_groups)

    def _annealing_cos(self, start, end, pct):
        cos_out = math.cos(math.pi * pct) + 1
        return end + (start - end) / 2.0 * cos_out

    def _annealing_linear(self, start, end, pct):
        return (end - start) * pct + start

    def get_lr(self):
        lrs = []
        _step_num = self.last_epoch

        if _step_num > self.total_steps:
            raise ValueError("Tried to step {} times. The specified number of total steps is {}"
                             .format(_step_num, self.total_steps))

        for group in self.optimizer.param_groups:
            start_step = 0
            for i, phase in enumerate(self._schedule_phases):
                end_step = phase['end_step']
                if _step_num <= end_step or i == len(self._schedule_phases) - 1:
                    pct = (_step_num - start_step) / (end_step - start_step)
                    _new_lr = self.anneal_func(group[phase['start_lr']], group[phase['end_lr']], pct)
                    if self.cycle_momentum:
                        __new_momentum = self.anneal_func(group[phase['start_momentum']],
                                                          group[phase['end_momentum']], pct)
                    break
                start_step = phase['end_step']

            lrs.append(_new_lr)
            if self.cycle_momentum:
                if self.use_beta1:
                    group['betas'] = (__new_momentum, *group['betas'][1:])
                else:
                    group['momentum'] = __new_momentum
        return lrs
