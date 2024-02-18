def reset_data():
    from . import globals, consts
    from .utils.credits import credits
    from .utils.error_process import error_process
    from .utils.online_tracker import online_tracker

    credits.blue = 0
    credits.gold = 0
    credits.count_gold = 0
    globals.output_queue.put({"当前蓝币": 0, "当前金币": 0, "获得金币": 0})
    globals.FINISHED_COUNT = 0
    globals.output_queue.put({"完赛次数": globals.FINISHED_COUNT})
    globals.RACE_COUNT[consts.car_hunt_zh] = 0
    globals.RACE_COUNT[consts.legendary_hunt_zh] = 0
    globals.output_queue.put({"寻车次数": 0})
    error_process.count = 0
    globals.output_queue.put({"在线时长": 0})
    online_tracker.start_time = None
    online_tracker.total_online_time = 0
    globals.output_queue.put({"错误处理": 0})
