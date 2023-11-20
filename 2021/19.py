import parse
import numpy as np


def Rx(th):
    th = np.deg2rad(th)
    c = np.cos(th)
    s = np.sin(th)
    R = np.array([
        [1, 0, 0],
        [0, c, -s],
        [0, s, c],
    ], dtype=int)
    return R

def Ry(th):
    th = np.deg2rad(th)
    c = np.cos(th)
    s = np.sin(th)
    R = np.array([
        [c, 0, s],
        [0, 1, 0],
        [-s, 0, c],
    ], dtype=int)
    return R

def Rz(th):
    th = np.deg2rad(th)
    c = np.cos(th)
    s = np.sin(th)
    R = np.array([
        [c, -s, 0],
        [s, c, 0],
        [0, 0, 1],
    ], dtype=int)
    return R


def solve(f):
    beacons = {}
    for i, coords in enumerate(open(f).read().split('\n\n')):
        arr = []
        for line in coords.splitlines()[1:]:
            x, y, z = parse.parse('{:d},{:d},{:d}', line.strip())
            arr.append([x,y,z])
        beacons[i] = np.array(arr)

    rotations = []
    for R1 in [Rz(0), Rz(90), Rz(180), Rz(270), Ry(90), Ry(270)]:
        for R2 in [Rx(0), Rx(90), Rx(180), Rx(270)]:
            rotations.append(R2 @ R1)

    while len(beacons) > 1:
        p0 = beacons[0] # (N,3)
        transforms = {}
        for i, p1 in beacons.items():
            for R in rotations:
                # R maps from scanner i -> scanner 0 coords
                p2 = p1 @ R
                p2 = np.tile(p2, (p0.shape[0], 1, 1))
                offset = (p0[:,np.newaxis,:] - p2).reshape((-1,3))
                mask = np.all(offset != np.array([[0,0,0]]), axis=-1)
                offset = offset[mask]
                unique, counts = np.unique(offset, return_counts=True, axis=0)
                overlap = unique[counts >= 12]
                if overlap.size > 0:
                    offset = overlap[:1]
                    transforms[i] = (offset, R)
                    break
            if i in transforms:
                break

        for k, (offset, R) in transforms.items():
            beacon_pts = beacons.pop(k) @ R + offset
            beacons[0] = np.unique(np.concatenate([beacons[0], beacon_pts], axis=0), axis=0)

    return len(beacons[0])


def solve2(f):
    beacons = {}
    for i, coords in enumerate(open(f).read().split('\n\n')):
        arr = []
        for line in coords.splitlines()[1:]:
            x, y, z = parse.parse('{:d},{:d},{:d}', line.strip())
            arr.append([x,y,z])
        beacons[i] = np.array(arr)

    rotations = []
    for R1 in [Rz(0), Rz(90), Rz(180), Rz(270), Ry(90), Ry(270)]:
        for R2 in [Rx(0), Rx(90), Rx(180), Rx(270)]:
            rotations.append(R2 @ R1)

    scanners = []
    while len(beacons) > 1:
        p0 = beacons[0] # (N,3)
        transforms = {}
        for i, p1 in beacons.items():
            for R in rotations:
                # R maps from scanner i -> scanner 0 coords
                p2 = p1 @ R
                p2 = np.tile(p2, (p0.shape[0], 1, 1))
                offset = (p0[:,np.newaxis,:] - p2).reshape((-1,3))
                mask = np.all(offset != np.array([[0,0,0]]), axis=-1)
                offset = offset[mask]
                unique, counts = np.unique(offset, return_counts=True, axis=0)
                overlap = unique[counts >= 12]
                if overlap.size > 0:
                    offset = overlap[:1]
                    transforms[i] = (offset, R)
                    break
            if i in transforms:
                break

        for k, (offset, R) in transforms.items():
            # print('MATCHED', k, offset)
            beacon_pts = beacons.pop(k) @ R + offset
            beacons[0] = np.unique(np.concatenate([beacons[0], beacon_pts], axis=0), axis=0)
            scanners.append(offset[0])
    
    scanners = np.stack(scanners, axis=0)

    max_d = 0
    s1 = scanners
    for i in range(1, s1.shape[0]):
        s2 = np.roll(s1, i, axis=0)
        l1 = np.abs(s1-s2).sum(axis=-1).max()
        max_d = max(l1, max_d)
    return max_d
    

if __name__ == '__main__':
    # print(solve('19_test.txt'))
    print(solve('19.txt'))
    # print(solve2('19_test.txt'))
    print(solve2('19.txt'))
