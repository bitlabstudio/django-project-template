from rapid_prototyping.context.utils import append_overhead_costs, get_counter

MAIN_ID = 100
counter = [-1]
costs = [
    {
        'id': MAIN_ID + get_counter(counter)[0],
        'task': 'Create logo',
        'time': 240,
        'sprint': 1,
    },
    {
        'id': MAIN_ID + get_counter(counter)[0],
        'task': 'Create color scheme',
        'time': 120,
        'sprint': 1,
    },
    {
        'id': MAIN_ID + get_counter(counter)[0],
        'task': 'Create typography',
        'time': 120,
        'sprint': 2,
    }
]
costs = append_overhead_costs(costs, MAIN_ID + get_counter(counter)[0])
