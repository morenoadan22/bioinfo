import sys
sys.setrecursionlimit(3000)
import dna.utils as utils


def edit_distance(s, t, i, j, dp):
    if i < 0 and j < 0:
        return 0
    elif i < 0 or j < 0:
        if i < 0 and j >= 0:
            return j + 1
        else:
            return i + 1
    elif (i, j) in dp:
        return dp[(i, j)]
    else:
        if s[i] == t[j]:
            one = edit_distance(s, t, i - 1, j - 1, dp)
            two = 1 + edit_distance(s, t, i - 1, j, dp)
            three = 1 + edit_distance(s, t, i, j - 1, dp)
            dp[(i, j)] = min(one, two, three)
            return dp[(i, j)]
        else:
            one = 1 + edit_distance(s, t, i, j - 1, dp)
            two = 1 + edit_distance(s, t, i - 1, j, dp)
            three = 1 + edit_distance(s, t, i - 1, j - 1, dp)
            dp[(i, j)] = min(one, two, three)
            return dp[(i, j)]


def reconstruct(s, t, dp):
    s_star = []
    t_star = []
    m = len(s) - 1
    n = len(t) - 1
    options = [lambda x, y: (x - 1, y - 1), lambda x, y: (x - 1, y),
               lambda x, y: (x, y - 1)]
    while m >= 0 and n >= 0:
        diag = dp.get((m - 1, n - 1), float('inf'))
        left = dp.get((m - 1, n), float('inf'))
        up = dp.get((m, n - 1), float('inf'))
        candidates = [diag, left, up]
        answer = candidates.index(min(candidates))
        f = options[answer]
        if answer == 0:
            s_star.append(s[m])
            t_star.append(t[n])
        elif answer == 1:
            s_star.append(s[m])
            t_star.append("-")
        else:
            s_star.append("-")
            t_star.append(t[n])
        m, n = f(m, n)
    return "".join(s_star[::-1]), "".join(t_star[::-1])


if __name__ == '__main__':
    s = 'PRETTY'
    t = 'PRTTEIN'
    dp = {}
    if len(sys.argv) >= 2:
        s, t = utils.read_fasta(sys.argv[1])
    print(edit_distance(s, t, len(s) - 1, len(t) - 1, dp))
    s, t = reconstruct(s, t, dp)
    print(s)
    print(t)
