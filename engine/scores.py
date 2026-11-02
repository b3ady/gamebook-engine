"""Review-round score tracking and the stop rule.

Reads reviews/v<N>/R<k>.md (first line matching 'Verdict ... X/10'), prints the score table and
applies book.json "review_stop" (defaults below). Decisions:

  CONTINUE  - run another rewrite + review round
  AUDIT     - stop review rounds; go to the fine-tooth audit (stage 8)
  ESCALATE  - (printed alongside) problems the reviewers have raised in 3+ consecutive rounds are
              design questions for the human, not rewrite tasks (tracked by hand in reviews/OPEN.md)

Stop rule (defaults): stop when mean >= target_mean and no reviewer < floor; or when the mean has
gained less than min_gain for `patience` consecutive rounds (plateau); or after max_rounds.
"""
import glob, os, re

from .config import read_text

DEFAULT = dict(target_mean=8.5, floor=7.5, min_gain=0.1, patience=1, max_rounds=10)
VERDICT = re.compile(r'Verdict\D{0,12}(\d+(?:\.\d+)?)\s*/\s*10')


def table(cfg):
    rounds = []
    for d in sorted(glob.glob(cfg.path('reviews', 'v*')), key=lambda p: int(re.sub(r'\D', '', os.path.basename(p)) or 0)):
        row = {}
        for f in sorted(glob.glob(os.path.join(d, 'R*.md'))):
            m = VERDICT.search(read_text(f))
            if m:
                row[os.path.basename(f)[:-3]] = float(m.group(1))
        if row:
            rounds.append((os.path.basename(d), row))
    return rounds


def decide(rounds, rule):
    if not rounds:
        return 'CONTINUE', 'no reviews yet'
    means = [sum(r.values()) / len(r) for _, r in rounds]
    last = rounds[-1][1]
    if means[-1] >= rule['target_mean'] and min(last.values()) >= rule['floor']:
        return 'AUDIT', f"mean {means[-1]:.2f} >= {rule['target_mean']} and no reviewer below {rule['floor']}"
    gains = [b - a for a, b in zip(means, means[1:])]
    if len(gains) >= rule['patience'] and all(g < rule['min_gain'] for g in gains[-rule['patience']:]):
        return 'AUDIT', f"plateau: mean gain {gains[-1]:+.2f} < {rule['min_gain']} for {rule['patience']} round(s)"
    if len(rounds) >= rule['max_rounds']:
        return 'AUDIT', f"max_rounds {rule['max_rounds']} reached"
    return 'CONTINUE', f"mean {means[-1]:.2f}, last gain {gains[-1]:+.2f}" if gains else f"mean {means[-1]:.2f}"


def run(cfg):
    rule = dict(DEFAULT, **cfg.get('review_stop', {}))
    rounds = table(cfg)
    names = sorted({k for _, r in rounds for k in r})
    print('round  ' + '  '.join(f'{n:>4s}' for n in names) + '   mean   gain')
    prev = None
    for v, r in rounds:
        mean = sum(r.values()) / len(r)
        gain = '' if prev is None else f'{mean - prev:+.2f}'
        print(f'{v:6s} ' + '  '.join(f'{r.get(n, float("nan")):4.1f}' for n in names) + f'   {mean:4.2f}  {gain}')
        prev = mean
    d, why = decide(rounds, rule)
    print(f'\nDECISION: {d} ({why})')
    open_p = cfg.path('reviews', 'OPEN.md')
    if os.path.exists(open_p):
        esc = [l for l in read_text(open_p).splitlines() if re.search(r'\brounds?:\s*(\d+)', l) and int(re.search(r'\brounds?:\s*(\d+)', l).group(1)) >= 3]
        if esc:
            print('ESCALATE to the human (raised in 3+ rounds):\n  ' + '\n  '.join(esc))
    return d
