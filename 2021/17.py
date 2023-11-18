import parse
from math import floor, ceil


def solve(f):
    line = open(f).read().strip()
    xm, xm, ym, yM = parse.parse("target area: x={:d}..{:d}, y={:d}..{:d}", line)
    return ym*(ym+1)//2

def solve2(f):
    line = open(f).read().strip()
    x1, x2, y1, y2 = parse.parse("target area: x={:d}..{:d}, y={:d}..{:d}", line)
    xm, xM = min(x1, x2), max(x1, x2)
    ym, yM = min(y1, y2), max(y1, y2)


    def init_vels(xf, yf, t):
        c = (t-1)/2
        return (xf/t + c, yf/t + c)

    def max_v(xf):
        # solution to xf = t*vx + t*(t-1)/2, where t = vx + 1 (zero velocity point)
        return ((8*xf+1)**0.5 - 1) / 2

    ### Trajectories that finish with vertical drop (vx = 0) ###
    vys = []
    t = 1
    for _ in range(10000):
        a, b = init_vels(ym, yM, t)
        if a <= ceil(a) <= b:
            for v in range(int(ceil(a)), int(floor(b))+1):
                vys.append(v)
        t += 1
    
    vxm = int(ceil(max_v(xm)))
    vxM = int(floor(max_v(xM)))

    vels = set()
    for vx in range(vxm, vxM+1):
        xf = vx*(vx+1)/2
        t = vx
        _, vym = init_vels(xf, yM, t)
        vym = int(ceil(vym))
        for vy in vys:
            if vy >= vym:
                vels.add((vx, vy))
    ####-----------------------------------------------------###

    #### Trajectories with no vertical drop using kinematics ###
    for xf in range(xm, xM+1):
        for yf in range(ym, yM+1):
            t = int(max_v(xf))
            while t > 0:
                vx, vy = init_vels(xf, yf, t)
                if vx.is_integer() and vy.is_integer():
                    vels.add((vx, vy))
                t -= 1
    ####----------------------------------------------------###
    
    return len(vels)

if __name__ == '__main__':
    # print(solve('17_test.txt'))
    print(solve('17.txt'))
    # print(solve2('17_test.txt'))
    print(solve2('17.txt'))
