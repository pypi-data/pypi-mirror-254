import crosspy as xp
from crosspy import cupy as cp  # CrossPy handles import errors

from timeit import timeit
import time

def quicksort(array, out=None):
    if len(array) <= 1:
        if out is not None:
            out[:] = array
        return
    
    if out is None:
        out = array

    # try:
    #     out.sort()
    # except AttributeError:
    # start = time.perf_counter()
    pivot = int(array[len(array) - 1])  # without type conversion it's a view, not copy
    left_mask = (array < pivot)
    right_mask = ~left_mask
    right_mask[len(array) - 1] = False
    left = array[left_mask]
    right = array[right_mask]
    # end = time.perf_counter()
    # print("body", end-start)
    # assert len(array) == len(left) + 1 + len(right)

    out[len(left)] = pivot
    if len(left):
        # xp.alltoall(out, slice(0, len(left)), left, None)
        out[0:len(left)] = left
        quicksort(out[0:len(left)])
    if len(right):
        # xp.alltoall(out, slice(len(left) + 1, len(array)), right, None)
        out[len(left) + 1:] = right
        quicksort(out[len(left) + 1:])


def main(args):
    # np.random.seed(10)
    # cp.random.seed(10)

    cupy_list_in = []
    cupy_list_out = []
    for i in range(args.n):
        with cp.cuda.Device(i):
            random_array = cp.random.randint(0, 100, size=args.m).astype(cp.int32)
            random_array = cp.asarray([59, 17, 76, 19,  6]).astype(cp.int32) if i == 0 else cp.asarray([69, 31, 89, 63, 89]).astype(cp.int32)
            cupy_list_in.append(random_array)
            cupy_list_out.append(cp.zeros_like(random_array))
    # print(timeit(lambda:
    #     cp.sort(cupy_list_in[0])
    # , number=3)/3)

    x_in = xp.array(cupy_list_in, axis=0)
    print("origin:", x_in)
    
    # x_out = xp.array(cupy_list_out, axis=0)
    # x_in = cupy_list_in[0]
    # x_out = cupy_list_out[0]
    x_out = None

    # print(timeit(lambda:
    quicksort(x_in, out=x_out)
    # , number=3)/3)

    # print("sorted:", x_out)
    print("sorted:", x_in)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", type=int, default=100, help="Size of array per GPU.")
    parser.add_argument("-n", type=int, default=2, help="Number of GPUs.")
    args = parser.parse_args()
    main(args)