import numpy as np

cache = {}


def plane_best_filling(out_l, out_w, inner_l, inner_w, road=[]):
    if not ((out_l >= inner_l and out_w >= inner_w) or (out_l >= inner_w and out_w >= inner_l)):
        return 0, road.copy()

    if (out_l * out_w) // (inner_l * inner_w) == 1:
        tmp_road = road.copy()
        tmp_road.append(1)
        return 1, tmp_road

    key = '%s_%s_%s_%s' % (out_l, out_w, inner_l, inner_w)
    if key in cache:
        tmp_road = road.copy()
        tmp_road.extend(cache[key][1])
        return cache[key][0], tmp_road

    result = [0]
    result_road = [[]]

    def sol(out_x, out_y, inner_x, inner_y):
        if out_x >= inner_x and out_y >= inner_y:
            if out_x % inner_x == 0:
                tmp_road = road.copy()
                count = out_x // inner_x
                count_multiplier = out_y // inner_y
                tmp_road.append('(%s * %s) X (%s * %s)' % (inner_x, inner_y, count, count_multiplier))
                if count_multiplier == 2:
                    tmp = 1
                inner_count, inner_road = plane_best_filling(out_x, out_y % inner_y, inner_x, inner_y, tmp_road)
                result_road.append(inner_road)
                result.append(count * count_multiplier + inner_count)
            else:
                tmp_road = road.copy()
                count = out_x // inner_x
                tmp_road.append('(%s * %s) X (%s * %s)' % (inner_x, inner_y, count, 1))
                inner_count1, inner_road1 = plane_best_filling(out_x % inner_x, out_y, inner_x, inner_y, tmp_road)
                inner_count2, inner_road2 = plane_best_filling(out_x - (out_x % inner_x), out_y - inner_y, inner_x,
                                                               inner_y,
                                                               tmp_road)
                inner_count3, inner_road3 = plane_best_filling(out_x % inner_x, inner_y, inner_x, inner_y, tmp_road)
                inner_count4, inner_road4 = plane_best_filling(out_x, out_y - inner_y, inner_x, inner_y, tmp_road)
                inner_max = max(inner_count1 + inner_count2, inner_count3 + inner_count4)
                if inner_max == inner_count1 + inner_count2:
                    inner_road1.extend(inner_road2[len(tmp_road):])
                    result_road.append(inner_road1)
                else:
                    inner_road3.extend(inner_road4[len(tmp_road):])
                    result_road.append(inner_road3)
                result.append(count + inner_max)

    sol(out_l, out_w, inner_l, inner_w)
    sol(out_l, out_w, inner_w, inner_l)
    sol(out_w, out_l, inner_l, inner_w)
    sol(out_w, out_l, inner_w, inner_l)


    max_result = max(result)
    all_max_index = [i for i in range(len(result)) if result[i] == max_result]
    all_max_road = [result_road[i] for i in all_max_index]
    all_max_road_len = [len(item) for item in all_max_road]
    min_max_road = all_max_road[np.argmin(all_max_road_len)]

    cache[key] = (max_result, min_max_road[len(road):])

    return max_result, min_max_road


# print(plane_best_filling(60, 40, 13, 8))  # 23
# print(plane_best_filling(13, 7, 5, 3))  # 5
# print(plane_best_filling(53, 29, 13, 8))  # 14
# print(plane_best_filling(55, 55, 13, 8))  # 27
# print(plane_best_filling(55, 50, 13, 8))  # 25
# print(plane_best_filling(55, 50, 8, 9))  # 36

def compose(length, width, high, l, w, h):
    print()
    print(length, width, high, l, w, h)
    res = plane_best_filling(length, width, l, w)
    print(res, ' * ', high // h, ' = ', res[0] * (high // h), ' 单体：', length * width * high / (res[0] * (high // h)))
    res = plane_best_filling(length, width, h, l)
    print(res, ' * ', high // w, ' = ', res[0] * (high // w), ' 单体：', length * width * high / (res[0] * (high // w)))
    res = plane_best_filling(length, width, h, w)
    print(res, ' * ', high // l, ' = ', res[0] * (high // l), ' 单体：', length * width * high / (res[0] * (high // l)))
    print()


print(plane_best_filling(40, 50, 9.1, 13.2))
print(compose(40, 50, 60, 8.1, 9.1, 13.2))







