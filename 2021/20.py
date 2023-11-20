import numpy as np


def solve(f, N=2):
    algo, lines = open(f).read().split('\n\n')

    algo = [1 if c == '#' else 0 for c in algo.strip()]

    arr = []
    for line in lines.splitlines():
        arr.append([1 if c == '#' else 0 for c in line.strip()])
    arr = np.array(arr)

    pad_value = 0
    for _ in range(N):
        arr = np.pad(arr, ((2,2),(2,2)), mode='constant', constant_values=pad_value)
        H, W = arr.shape
        new_arr = arr.copy()
        for i, j in np.ndindex(H-2, W-2):
            w = arr[i:i+3,j:j+3]
            idx = int(''.join(str(x) for x in w.flatten()), base=2)
            new_arr[i+1,j+1] = algo[idx]
        pad_value = 1-pad_value if algo[0] else pad_value
        arr = new_arr[1:-1, 1:-1]

    return arr.sum()
    

def solve2(f):
    return solve(f, N=50)
    

if __name__ == '__main__':
    # print(solve('20_test.txt'))
    print(solve('20.txt'))
    # print(solve2('20_test.txt'))
    print(solve2('20.txt'))
