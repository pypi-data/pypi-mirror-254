import datetime
import time

import torch
from matplotlib import pyplot as plt
from torch import jit
from torch import nn
from torch.backends import cuda, cudnn

import optim

torch._C._set_cublas_allow_tf32(True)
torch.use_deterministic_algorithms(False)
cudnn.enabled = True
cudnn.benchmark = True
cudnn.deterministic = False
cudnn.allow_tf32 = True
cuda.matmul.allow_tf32 = True
jit.optimized_execution(True)
jit.fuser("fuser2")

wds = [0.1 ** i for i in range(4)]
numbers = 1
features = 2 ** 8
depth = 1
input_scale = 1
lr = 1e-4
batch_size = 2 ** 7
iterations = 3 * 2 ** 25 // batch_size
noise_scale_range = (2 ** (2 * torch.arange(4).float() - 4)).cuda()
offset = 32 * 2048 * 15 // batch_size
printervall = 32 * 2048 * 16 // batch_size
names = ["L2", "L2 to Init", "L2 to EMA(1)",  "L2 to EMA(2)", "L2 to EMA(3)", "L2 to EMA(4)", "L2 to EMA(5)",
         "L2 to EMA(6)"]


def p(*shape):
    a = torch.randn(shape) / (1 if len(shape) == 1 else shape[0] ** 0.5)
    return [nn.Parameter(a.detach().clone().contiguous().requires_grad_(True)) for _ in
            range(len(names) * len(noise_scale_range) * len(wds))]


class MultiModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.p0 = p(numbers, features)
        self.p00 = p(features)
        self.p1 = p(features, features)
        self.p10 = p(features)
        self.p2 = p(features, numbers)
        self.p20 = p(features)
        for i, v in enumerate(self.p0 + self.p00 + self.p1 + self.p10 + self.p2 + self.p20):
            setattr(self, f"_param_for_model{i}", v)

    def forward(self, inp):
        out = torch.einsum("bgn,gnf->bgf", inp, torch.stack(self.p0)) + torch.stack(self.p00).unsqueeze(0)

        out = torch.nn.functional.leaky_relu(out, inplace=True)
        out = torch.einsum("bgn,gnf->bgf", out / out.norm(p=2, dim=-1, keepdim=True).clamp(min=1e-8),
                           torch.stack(self.p1)) + torch.stack(self.p10).unsqueeze(0)

        out = torch.nn.functional.leaky_relu(out, inplace=True)
        out = torch.einsum("bgn,gnf->bgf", out / out.norm(p=2, dim=-1, keepdim=True).clamp(min=1e-8),
                           torch.stack(self.p2)) + torch.stack(self.p20).unsqueeze(0)

        return out


class Ones(torch.optim.Optimizer):
    def step(self, closure=None):
        for g in self.param_groups:
            for p in g["params"]:
                p.add_(torch.ones_like(p), alpha=-1)


plt.yscale("log")
plt.xscale("log")
start_time = datetime.datetime.now()
colors = [lambda x: f"#{x:02x}0000", lambda x: f"#00{x:02x}00", lambda x: f"#0000{x:02x}",
          lambda x: f"#{x:02x}{x:02x}00", lambda x: f"#{x:02x}00{x:02x}", lambda x: f"#00{x:02x}{x:02x}"]

noise_scale = None


def get_noise():
    inp = torch.randn((batch_size, 1, numbers), device="cuda:0") * input_scale
    inp = inp.expand(-1, len(noise_scale_range), -1).contiguous()
    noise = torch.randn_like(inp) * inp.std() * noise_scale_range.view(1, -1, 1)
    return inp, noise


def noisy_square():
    inp, noise = get_noise()
    target = (noise + inp).square()
    ground_truth = inp.square()
    return inp, target, ground_truth


def rosenbrock(x, y):
    return (1 - x).square() + 100 * (y - x.square()).square()


def noisy_rosenbrock():
    inp, noise = get_noise()
    target = rosenbrock(*(inp + noise).chunk(2, -1))
    ground_truth = rosenbrock(*inp.chunk(2, -1))
    return inp, target, ground_truth


example = noisy_square

oo = []

loss_group = []

mod = MultiModel().cuda()
ps = list(zip(mod.p0, mod.p00, mod.p1, mod.p10, mod.p2, mod.p20))
oo = [o for w, p in [(0.1 ** (i // len(names)), ps[i:(i + len(names))]) for i in range(0, len(ps), len(names))] for o in
      [optim.Sign(p[0], torch.optim.Adam(p[0], lr=lr), weight_decay=w),
       optim.Sign(p[1], torch.optim.Adam(p[1], lr=lr), weight_decay=w,
                  weight_decay_cls=optim.WeightDecayChain(optim.WeightDecayToInit(), optim.L2WeightDecay())),
       optim.Sign(p[2], torch.optim.Adam(p[2], lr=lr), weight_decay=w,
                  weight_decay_cls=optim.WeightDecayChain(optim.WeightDecayToEMA(0.9), optim.L2WeightDecay())),
       optim.Sign(p[3], torch.optim.Adam(p[3], lr=lr), weight_decay=w,
                  weight_decay_cls=optim.WeightDecayChain(optim.WeightDecayToEMA(0.99), optim.L2WeightDecay())),
       optim.Sign(p[4], torch.optim.Adam(p[4], lr=lr), weight_decay=w,
                  weight_decay_cls=optim.WeightDecayChain(optim.WeightDecayToEMA(0.999), optim.L2WeightDecay())),
       optim.Sign(p[5], torch.optim.Adam(p[5], lr=lr), weight_decay=w,
                  weight_decay_cls=optim.WeightDecayChain(optim.WeightDecayToEMA(0.9999), optim.L2WeightDecay())),
       optim.Sign(p[6], torch.optim.Adam(p[6], lr=lr), weight_decay=w,
                  weight_decay_cls=optim.WeightDecayChain(optim.WeightDecayToEMA(0.99999), optim.L2WeightDecay())),
       optim.Sign(p[7], torch.optim.Adam(p[7], lr=lr), weight_decay=w,
                  weight_decay_cls=optim.WeightDecayChain(optim.WeightDecayToEMA(0.999999), optim.L2WeightDecay()))]]
all_losses = torch.zeros((iterations, len(oo)))

start_ts = time.time()

for i in range(iterations):
    inp, target, ground_truth = [x.unsqueeze(2).unsqueeze(1).expand(-1, len(wds), -1, len(names), -1
                                                                    ).reshape(x.size(0), -1, x.size(-1))
                                 for x in example()]
    if i == 0:
        mod = torch.jit.script(mod, inp)
    target = target.mean(-1, keepdim=True)
    ground_truth = ground_truth.mean(-1, keepdim=True)

    out = mod(inp)
    (out.size(1) * (out - target).abs()).mean().backward()
    for o in oo:
        o.step()
    mod.zero_grad()
    with torch.no_grad():
        loss_group.append((out - ground_truth).abs().mean((0, 2)).detach().to(device="cpu", non_blocking=True))
    if i % printervall == offset and i > printervall:
        all_losses[i - printervall - offset:i - offset] = torch.stack(loss_group[:printervall])
        loss_group = loss_group[printervall:]
        it = i / (time.time() - start_ts)
        eta = datetime.datetime.now() + datetime.timedelta(seconds=int((iterations - i) / it))
        all_local = all_losses[i - printervall - offset:i - offset].mean(0).numpy()
        print(f'{i:06d} || {datetime.datetime.now() - start_time} || {datetime.datetime.now()} || ETA: {eta} || {it:.1f} it/s || '
              f'{" | ".join(" - ".join(f"{o.item():9.7f}" for o in all_local[i:i+len(names)]) for i in range(0, len(oo), len(names)))}')
all_losses[-len(loss_group):] = torch.stack(loss_group).cpu()
all_losses = [[i.item() for i in losses] for losses in all_losses]
skipped = len(all_losses) // 32
all_losses = list(zip(*all_losses))
for i, ls in enumerate(all_losses):
    name = names[i % len(names)]
    color = colors[i](round(255 - 128 * (i // len(names)) / len(noise_scale_range)))
    plt.plot(list(range(skipped, len(ls))), [sum(ls[i:i + skipped]) / skipped for i in range(len(ls) - skipped)],
             color=color, label=f"{name} - noise=2**{(i // len(names)) % len(noise_scale_range)} - "
                                f"decay={0.1 ** (i // len(names) // len(noise_scale_range))}")
plt.legend()
plt.show()
